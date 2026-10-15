"""Integration tests: real local Git repos, no production credentials or network."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from trend_watch import Workflow, Stop, digest, validate_markdown

DATE = "2026-10-15"
DAILY = f"30 Intelligence/GitHub/Daily/{DATE}.md"
INDEX = "30 Intelligence/GitHub/Local-AI.md"
REPORT = """---
type: github-trending-daily
date: 2026-10-15
status: reviewed
---

# GitHub Trending — 2026-10-15

## 今日结论

本测试验证本地写入、内容保留、明确路径提交和远端同步。

## 重点项目

- 项目：https://github.com/AxisSnorlax/AxisKnowledgeVault
- 增长信号：测试样本没有采集真实增长数据。
- Windows/.NET 借鉴：用明确的文件清单与完整性检查同步知识。[[Local-AI]]

## 长期判断

知识正文保留在本地，远端保存经过检查后的提交历史。

## 来源

- https://github.com/AxisSnorlax/AxisKnowledgeVault
"""


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, check=True)
    return result.stdout.decode("utf-8").strip()


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="trend-watch-test-")
        self.base = Path(self.tmp.name)
        self.remote = self.base / "remote.git"
        self.remote.mkdir()
        git(self.remote, "init", "--bare", "--initial-branch=main")
        self.root = self.base / "vault"
        self.root.mkdir()
        git(self.root, "init", "--initial-branch=main")
        git(self.root, "config", "user.name", "Trend Watch Test")
        git(self.root, "config", "user.email", "test@example.invalid")
        git(self.root, "config", "core.autocrlf", "false")
        git(self.root, "config", "core.hooksPath", str(self.base / "empty-hooks"))
        (self.root / "human.md").write_text("Original human note.\n", encoding="utf-8")
        p = self.root / INDEX
        p.parent.mkdir(parents=True)
        p.write_bytes(b"# Local AI\r\n\r\nHuman paragraph: preserve exactly.\r\n")
        git(self.root, "add", "--", "human.md", INDEX)
        git(self.root, "commit", "-m", "Initial")
        git(self.root, "remote", "add", "origin", str(self.remote))
        git(self.root, "push", "-u", "origin", "main")
        self.flow = Workflow(self.root, str(self.remote))
        self.plan_path = self.base / "plan.json"

    def tearDown(self):
        self.tmp.cleanup()

    def prepare_plan(self, include_index=True):
        s = self.flow.prepare(DATE, [INDEX] if include_index else [])
        entries = [{"path": DAILY, "base_sha256": s["files"][DAILY]["before"]}]
        if s["files"][DAILY]["before"] is None:
            entries[0]["create"] = REPORT
        else:
            entries[0]["edits"] = []
        if include_index:
            entries.append({"path": INDEX, "base_sha256": s["files"][INDEX]["before"],
                            "append_blocks": [{"key": "2026-10-15-local-first",
                            "content": "## 2026-10-15 本地同步\n\n保留人工段落并逐文件同步。[[Agent]]"}]})
        self.plan_path.write_text(json.dumps({"files": entries}, ensure_ascii=False), encoding="utf-8")
        return entries

    def test_end_to_end_idempotence_and_human_changes(self):
        human = self.root / "human.md"
        human.write_text("Uncommitted human edit.\n", encoding="utf-8")
        extra = self.root / ".vs"
        extra.mkdir()
        (extra / "scratch.txt").write_text("Do not stage", encoding="utf-8")
        original = (self.root / INDEX).read_bytes()
        self.prepare_plan()
        self.flow.apply(self.plan_path)
        first = (self.root / INDEX).read_bytes()
        self.assertTrue(first.startswith(original.rstrip(b"\r\n")))
        self.assertNotIn(b"\n", first.replace(b"\r\n", b""))
        self.flow.apply(self.plan_path)
        self.assertEqual(first, (self.root / INDEX).read_bytes())
        self.flow.check()
        s = self.flow.sync()
        self.assertEqual(s["phase"], "pushed")
        self.assertEqual(git(self.remote, "rev-parse", "main"), s["commit"])
        self.assertEqual(git(self.root, "show", "HEAD:human.md"), "Original human note.")
        self.assertEqual(human.read_text(), "Uncommitted human edit.\n")
        self.assertEqual(set(git(self.root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines()), {DAILY, INDEX})
        self.assertEqual(self.flow.sync()["commit"], s["commit"])
        self.prepare_plan()
        self.flow.apply(self.plan_path)
        s2 = self.flow.sync()
        self.assertTrue(s2["no_changes"])
        self.assertEqual(s["commit"], s2["commit"])
        self.assertEqual(first, (self.root / INDEX).read_bytes())

    def test_dirty_target_and_staged_changes_rejected(self):
        (self.root / INDEX).write_text("Human edit", encoding="utf-8")
        with self.assertRaisesRegex(Stop, "pre-existing"):
            self.flow.prepare(DATE, [INDEX])
        git(self.root, "add", "--", INDEX)
        with self.assertRaisesRegex(Stop, "staged"):
            self.flow.prepare(DATE, [])

    def test_concurrent_edit_blocks_all_initial_writes(self):
        self.prepare_plan()
        (self.root / INDEX).write_text("New human paragraph", encoding="utf-8")
        with self.assertRaisesRegex(Stop, "changed since prepare"):
            self.flow.apply(self.plan_path)
        self.assertFalse((self.root / DAILY).exists())
        self.assertEqual((self.root / INDEX).read_text(), "New human paragraph")

    def test_placeholder_blocks_all_writes(self):
        entries = self.prepare_plan()
        entries[0]["create"] = "TODO\n"
        self.plan_path.write_text(json.dumps({"files": entries}), encoding="utf-8")
        with self.assertRaisesRegex(Stop, "placeholder"):
            self.flow.apply(self.plan_path)
        self.assertFalse((self.root / DAILY).exists())

    def test_existing_daily_incremental_edit_preserves_human_text(self):
        self.prepare_plan(False)
        self.flow.apply(self.plan_path)
        self.flow.sync()
        p = self.root / DAILY
        p.write_text(REPORT + "\n人工补充：保留此段。\n", encoding="utf-8")
        git(self.root, "add", "--", DAILY)
        git(self.root, "commit", "-m", "Human annotation")
        git(self.root, "push", "origin", "main")
        entries = self.prepare_plan(False)
        entries[0]["edits"] = [{"before": "本测试验证本地写入、内容保留、明确路径提交和远端同步。",
                                "after": "本测试进一步验证已有日报的增量更新和人工内容保留。"}]
        self.plan_path.write_text(json.dumps({"files": entries}, ensure_ascii=False), encoding="utf-8")
        self.flow.apply(self.plan_path)
        self.flow.sync()
        self.assertIn("人工补充：保留此段。", p.read_text(encoding="utf-8"))
        self.assertIn("进一步验证", p.read_text(encoding="utf-8"))

    def test_existing_file_full_replacement_rejected(self):
        entries = self.prepare_plan()
        entries[1]["create"] = "# Replacement"
        self.plan_path.write_text(json.dumps({"files": entries}), encoding="utf-8")
        with self.assertRaisesRegex(Stop, "Never replace"):
            self.flow.apply(self.plan_path)
        self.assertFalse((self.root / DAILY).exists())

    def test_ambiguous_anchor_rejected(self):
        entries = self.prepare_plan()
        entries[1]["edits"] = [{"before": "missing anchor", "after": "replacement"}]
        self.plan_path.write_text(json.dumps({"files": entries}), encoding="utf-8")
        with self.assertRaisesRegex(Stop, "exactly once"):
            self.flow.apply(self.plan_path)
        self.assertFalse((self.root / DAILY).exists())

    def test_user_edit_after_apply_is_not_committed(self):
        self.prepare_plan()
        self.flow.apply(self.plan_path)
        original_head = self.flow.head()
        p = self.root / DAILY
        p.write_text(REPORT + "\nFresh human annotation.\n", encoding="utf-8")
        with self.assertRaisesRegex(Stop, "changed after apply"):
            self.flow.sync()
        self.assertEqual(original_head, self.flow.head())
        self.assertIn("Fresh human", p.read_text(encoding="utf-8"))

    def test_interrupted_commit_is_recovered_without_duplicate(self):
        self.prepare_plan(False)
        self.flow.apply(self.plan_path)
        original_save = self.flow.save
        def interrupted(state):
            if state["phase"] == "committed":
                raise OSError("Simulated interruption after commit")
            original_save(state)
        with patch.object(self.flow, "save", side_effect=interrupted):
            with self.assertRaisesRegex(OSError, "interruption"):
                self.flow.sync()
        commit = self.flow.head()
        self.assertEqual(self.flow.state()["phase"], "committing")
        recovered = self.flow.sync()
        self.assertEqual(commit, recovered["commit"])
        self.assertEqual(git(self.remote, "rev-parse", "main"), commit)

    def test_duplicate_and_unbalanced_markers_rejected(self):
        for content in ("<!-- marker -->\n<!-- marker -->", "<!-- trend-watch:one:begin -->",
                        "## 2026-10-15 update\na\n## 2026-10-15 update\nb"):
            with self.assertRaises(Stop):
                validate_markdown(INDEX, content.encode(), DATE)

    def test_push_failure_reuses_local_commit(self):
        self.prepare_plan()
        self.flow.apply(self.plan_path)
        original_git = self.flow.git
        def fail_push(*args, **kwargs):
            if args[0] == "push":
                raise Stop("Simulated network failure")
            return original_git(*args, **kwargs)
        with patch.object(self.flow, "git", side_effect=fail_push):
            with self.assertRaisesRegex(Stop, "network failure"):
                self.flow.sync()
        pending = self.flow.state()
        self.assertEqual(pending["phase"], "committed")
        self.assertTrue((self.root / DAILY).exists())
        recovered = self.flow.sync()
        self.assertEqual(pending["commit"], recovered["commit"])
        self.assertEqual(git(self.remote, "rev-parse", "main"), recovered["commit"])

    def test_remote_race_preserves_local_commit(self):
        self.prepare_plan(False)
        self.flow.apply(self.plan_path)
        original_git = self.flow.git
        def fail_push(*args, **kwargs):
            if args[0] == "push":
                raise Stop("Simulated network failure")
            return original_git(*args, **kwargs)
        with patch.object(self.flow, "git", side_effect=fail_push):
            with self.assertRaises(Stop):
                self.flow.sync()
        pending = self.flow.state()["commit"]
        peer = self.base / "peer"
        git(self.base, "clone", str(self.remote), str(peer))
        git(peer, "config", "user.name", "Peer")
        git(peer, "config", "user.email", "peer@example.invalid")
        (peer / "peer.md").write_text("Remote advanced.\n")
        git(peer, "add", "peer.md")
        git(peer, "commit", "-m", "Concurrent update")
        git(peer, "push", "origin", "main")
        with self.assertRaisesRegex(Stop, "Remote advanced"):
            self.flow.sync()
        self.assertEqual(self.flow.head(), pending)
        self.assertTrue((self.root / DAILY).exists())
        self.assertEqual(git(self.remote, "rev-parse", "main"), git(peer, "rev-parse", "HEAD"))

    def test_wrong_remote_branch_and_path_rejected(self):
        with self.assertRaisesRegex(Stop, "Unexpected origin"):
            Workflow(self.root).identity()
        for path in ("../escape.md", "30 Intelligence/GitHub/../../escape.md", ".obsidian/workspace.json"):
            with self.assertRaises(Stop):
                self.flow.safe_path(path)
        git(self.root, "switch", "-c", "human-work")
        with self.assertRaisesRegex(Stop, "Expected main"):
            self.flow.identity()


if __name__ == "__main__":
    unittest.main(verbosity=2)
