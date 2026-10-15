"""Local-first GitHub Trend Watch. Python 3.10+, Git; standard library only."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import uuid
from contextlib import contextmanager

DEFAULT_REPO = r"D:\Projects\AxisKnowledgeVault"
REMOTE = "https://github.com/AxisSnorlax/AxisKnowledgeVault.git"
ALLOWED = ("30 Intelligence/GitHub/", "20 Technology/", "40 Engineering/", "50 Research/")


class Stop(RuntimeError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def decode(data):
    return data.decode("utf-8-sig").replace("\r\n", "\n")


def validate_markdown(path, data, date):
    text = decode(data)
    if not text.strip() or "\x00" in text:
        raise Stop(f"Empty/invalid Markdown: {path}")
    if re.search(r"(?m)^(?:<{7}|={7}|>{7})(?: |$)", text):
        raise Stop(f"Merge conflict markers: {path}")
    if re.search(r"\{\{[^}]+\}\}|(?im:^\s*(?:TODO|TBD|placeholder|待补充|待生成)\s*$)", text):
        raise Stop(f"Unfinished placeholder: {path}")
    comments = re.findall(r"<!--\s*(.*?)\s*-->", text, re.S)
    if len(comments) != len(set(comments)):
        raise Stop(f"Duplicate HTML markers: {path}")
    stack, seen = [], set()
    for key, edge in re.findall(r"<!-- trend-watch:([a-z0-9-]+):(begin|end) -->", text):
        if edge == "begin":
            if stack or key in seen:
                raise Stop(f"Duplicate/nested managed block: {path}: {key}")
            stack.append(key)
            seen.add(key)
        elif not stack or stack.pop() != key:
            raise Stop(f"Unbalanced managed block: {path}: {key}")
    if stack:
        raise Stop(f"Unclosed managed block: {path}")
    dated = re.findall(r"(?m)^##\s+(\d{4}-\d{2}-\d{2}[^\n]*)", text)
    if len(dated) != len(set(dated)):
        raise Stop(f"Duplicate dated sections: {path}")
    if path.startswith("30 Intelligence/GitHub/Daily/"):
        if path != f"30 Intelligence/GitHub/Daily/{date}.md":
            raise Stop("Daily path must match the run date.")
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not front or not re.search(r"(?m)^status:\s*reviewed\s*$", front[1]):
            raise Stop("Daily must have reviewed YAML frontmatter.")
        if not re.search(rf"(?m)^date:\s*{re.escape(date)}\s*$", front[1]):
            raise Stop("Daily frontmatter date mismatch.")
        for heading in ("今日结论", "长期判断", "来源"):
            match = re.search(rf"(?ms)^## {heading}\s*\n(.+?)(?=^## |\Z)", text)
            if not match or len(match[1].strip()) < 10:
                raise Stop(f"Daily lacks a complete {heading} section.")
        for pattern, label in ((r"https://github\.com/[\w.-]+/[\w.-]+", "project source"),
                               (r"增长|趋势信号", "growth signal"),
                               (r"Windows|\.NET", "Windows/.NET implications"),
                               (r"\[\[[^\]\n]+\]\]", "Obsidian links")):
            if not re.search(pattern, text):
                raise Stop(f"Daily missing {label}.")


class Workflow:
    def __init__(self, root, expected_remote=REMOTE):
        self.root = Path(root).resolve()
        self.expected_remote = expected_remote
        top = Path(self.git("rev-parse", "--show-toplevel").strip()).resolve()
        if top != self.root:
            raise Stop("Use the exact repository root.")
        self.meta = Path(self.git("rev-parse", "--absolute-git-dir").strip()) / "trend-watch"
        self.meta.mkdir(exist_ok=True)
        self.state_path = self.meta / "state.json"

    def git(self, *args, check=True, binary=False, input=None):
        # Keep TLS verification enabled; avoid the failing Windows Schannel backend.
        command = ["git", "-C", str(self.root), "-c", "http.sslVerify=true"]
        if os.name == "nt":
            command += ["-c", "http.sslBackend=openssl"]
        result = subprocess.run(command + list(args), input=input, capture_output=True,
                                timeout=120, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
        if check and result.returncode:
            raise Stop((result.stderr + result.stdout).decode("utf-8", errors="replace").strip()
                       or f"git {' '.join(args)} failed ({result.returncode})")
        if not check:
            return result
        return result.stdout if binary else result.stdout.decode("utf-8")

    @contextmanager
    def lock(self):
        path = self.meta / "run.lock"
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise Stop(f"Another command is running. Inspect stale lock before removal: {path}")
        try:
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            yield
        finally:
            path.unlink()

    def save(self, state):
        temp = self.state_path.with_suffix(".tmp")
        temp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(temp, self.state_path)

    def state(self):
        if not self.state_path.exists():
            raise Stop("Run prepare first.")
        return json.loads(self.state_path.read_text(encoding="utf-8"))

    def identity(self):
        urls = [self.git("remote", "get-url", "--all", "origin").strip(),
                self.git("remote", "get-url", "--push", "--all", "origin").strip()]
        allowed = {self.expected_remote}
        if self.expected_remote == REMOTE:
            allowed |= {REMOTE.removesuffix(".git"), "git@github.com:AxisSnorlax/AxisKnowledgeVault.git",
                        "ssh://git@github.com/AxisSnorlax/AxisKnowledgeVault.git"}
        if any(url not in allowed for url in urls):
            raise Stop("Unexpected origin fetch/push URL; refusing to publish.")
        if self.git("branch", "--show-current").strip() != "main":
            raise Stop("Expected main; do not switch a user's branch automatically.")
        if self.git("rev-parse", "--abbrev-ref", "@{upstream}").strip() != "origin/main":
            raise Stop("Expected upstream origin/main.")
        gitdir = self.meta.parent
        if any((gitdir / name).exists() for name in
               ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply")):
            raise Stop("An existing Git operation must be resolved first.")
        if self.git("ls-files", "-u").strip():
            raise Stop("Unmerged files exist.")

    def safe_path(self, name):
        if "\\" in name or ":" in name:
            raise Stop("Plan paths must be repository-relative POSIX paths.")
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or not name.startswith(ALLOWED) or path.suffix != ".md":
            raise Stop(f"Not an allowed knowledge page: {name}")
        full = self.root / name
        if not full.resolve().is_relative_to(self.root):
            raise Stop(f"Path escapes repository: {name}")
        for part in [full, *full.parents]:
            if part == self.root:
                break
            if part.is_symlink() or (hasattr(part, "is_junction") and part.is_junction()):
                raise Stop(f"Linked path is not supported: {name}")
        return full

    def head(self):
        return self.git("rev-parse", "HEAD").strip()

    def staged(self):
        return set(filter(None, self.git("diff", "--cached", "--name-only", "-z").split("\0")))

    def diff_check(self, *args):
        configured = self.git("config", "--get", "core.whitespace", check=False)
        rules = configured.stdout.decode().strip() or "blank-at-eol,blank-at-eof,space-before-tab"
        # CRLF is a valid newline even if this repository has autocrlf disabled.
        self.git("-c", "core.whitespace=" + rules + ",cr-at-eol", "diff", "--check", *args)

    def prepare(self, date, paths):
        self.identity()
        if self.state_path.exists() and self.state()["phase"] != "pushed":
            raise Stop("An unfinished run exists. Resume apply/check/sync; inspect state.json before abandoning.")
        if self.staged():
            raise Stop("Existing staged changes must be handled separately.")
        self.git("fetch", "origin")
        ahead, behind = map(int, self.git("rev-list", "--left-right", "--count", "HEAD...origin/main").split())
        if ahead:
            raise Stop("Unrelated/unresolved local commits exist; refusing to push them with the report.")
        if behind:
            # Git itself refuses overlaps with local edits. Never stash/reset/force automatically.
            self.git("merge", "--ff-only", "origin/main")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            raise Stop("Use an explicit Asia/Singapore date: YYYY-MM-DD.")
        from datetime import date as Date
        Date.fromisoformat(date)
        daily = f"30 Intelligence/GitHub/Daily/{date}.md"
        paths = list(dict.fromkeys([daily] + paths))
        records = {}
        run = self.meta / "runs" / uuid.uuid4().hex
        for name in paths:
            path = self.safe_path(name)
            if path.exists():
                tracked = self.git("ls-files", "--error-unmatch", "--", name, check=False)
                if tracked.returncode or self.git("diff", "--name-only", "--", name).strip():
                    raise Stop(f"Target contains pre-existing user changes: {name}")
                data = path.read_bytes()
                backup = run / "before" / name
                backup.parent.mkdir(parents=True, exist_ok=True)
                backup.write_bytes(data)
                records[name] = {"before": digest(data)}
            else:
                if self.git("ls-files", "--", name).strip():
                    raise Stop(f"Target was deleted locally: {name}")
                records[name] = {"before": None}
        state = {"phase": "prepared", "date": date, "base": self.head(),
                 "run": str(run), "files": records}
        self.save(state)
        return state

    def apply(self, plan_path):
        self.identity()
        state = self.state()
        if state["phase"] not in ("prepared", "applying", "applied"):
            raise Stop("This run has already been committed.")
        if self.head() != state["base"] or self.staged():
            raise Stop("HEAD/index changed after prepare.")
        plan_bytes = Path(plan_path).read_bytes()
        if state["phase"] == "prepared":
            plan = json.loads(plan_bytes.decode("utf-8-sig"))
            entries = plan["files"]
            if len(entries) != len(state["files"]) or {e["path"] for e in entries} != set(state["files"]):
                raise Stop("Plan must contain each prepared file exactly once.")
            for entry in entries:
                name = entry["path"]
                path = self.safe_path(name)
                record = state["files"][name]
                old = path.read_bytes() if path.exists() else None
                if (digest(old) if old is not None else None) != record["before"]:
                    raise Stop(f"File changed since prepare: {name}")
                if entry.get("base_sha256") != record["before"]:
                    raise Stop(f"Plan was not based on the recorded file: {name}")
                if old is None:
                    text = entry.get("create", "")
                    if entry.get("edits") or entry.get("append_blocks"):
                        raise Stop("New pages require a complete create body.")
                else:
                    if "create" in entry:
                        raise Stop("Never replace an existing page with create; use exact edits.")
                    text = decode(old)
                    for edit in entry.get("edits", []):
                        before, after = edit["before"], edit["after"]
                        if not before or text.count(before) != 1:
                            raise Stop(f"Edit anchor must match exactly once: {name}")
                        text = text.replace(before, after, 1)
                    for block in entry.get("append_blocks", []):
                        key = block["key"]
                        if not re.fullmatch(r"[a-z0-9-]+", key):
                            raise Stop("Block key must use lowercase letters, digits and hyphens.")
                        begin, end = f"<!-- trend-watch:{key}:begin -->", f"<!-- trend-watch:{key}:end -->"
                        body = begin + "\n" + block["content"].strip() + "\n" + end
                        if begin in text or end in text:
                            if text.count(body) != 1:
                                raise Stop(f"Existing block differs; read and edit it incrementally: {key}")
                        else:
                            text = text.rstrip("\n") + "\n\n" + body + "\n"
                # Preserve existing newline convention and BOM, including no-op bytes.
                newline = "\r\n" if old is not None and b"\r\n" in old else "\n"
                data = text.replace("\r\n", "\n").replace("\n", newline).encode("utf-8")
                if old is not None and old.startswith(b"\xef\xbb\xbf"):
                    data = b"\xef\xbb\xbf" + data
                if old is not None and text == decode(old):
                    data = old
                validate_markdown(name, data, state["date"])
                after = Path(state["run"]) / "after" / name
                after.parent.mkdir(parents=True, exist_ok=True)
                after.write_bytes(data)
                record["after"] = digest(data)
            state.update(phase="applying", plan_sha256=digest(plan_bytes))
            self.save(state)
        elif digest(plan_bytes) != state["plan_sha256"]:
            raise Stop("Use the same plan to resume this run.")
        # All candidates are complete and validated before the first write. Serial file updates.
        for name, record in state["files"].items():
            path = self.safe_path(name)
            current = digest(path.read_bytes()) if path.exists() else None
            if current == record["after"]:
                continue
            if current != record["before"]:
                raise Stop(f"Concurrent user edit preserved; stopping: {name}")
            data = (Path(state["run"]) / "after" / name).read_bytes()
            if digest(data) != record["after"]:
                raise Stop("Saved candidate changed.")
            path.parent.mkdir(parents=True, exist_ok=True)
            # Write through a same-directory temporary file, then atomic replace.
            temp = path.with_name(path.name + ".trend-watch-" + uuid.uuid4().hex + ".tmp")
            try:
                temp.write_bytes(data)
                if (digest(path.read_bytes()) if path.exists() else None) != record["before"]:
                    raise Stop(f"Concurrent user edit preserved: {name}")
                os.replace(temp, path)
            finally:
                if temp.exists():
                    temp.unlink()
        state["phase"] = "applied"
        self.save(state)
        return state

    def check(self):
        self.identity()
        state = self.state()
        if state["phase"] not in ("applied", "committing", "committed", "pushed"):
            raise Stop("Finish applying the complete plan first.")
        for name, record in state["files"].items():
            data = self.safe_path(name).read_bytes()
            if digest(data) != record["after"]:
                raise Stop(f"File changed after apply; preserve and reconcile it: {name}")
            validate_markdown(name, data, state["date"])
        paths = list(state["files"])
        self.diff_check("--", *paths)
        if not self.staged().issubset(set(paths)):
            raise Stop("Unrelated staged changes detected.")
        self.diff_check("--cached", "--", *paths)
        return state

    def verify_commit(self, commit, state, changed):
        if self.git("rev-parse", commit + "^").strip() != state["base"]:
            raise Stop("Commit does not directly follow the prepared base.")
        actual = set(filter(None, self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "-z", commit).split("\0")))
        if actual != set(changed):
            raise Stop("Commit includes missing or unrelated paths.")
        for name in changed:
            candidate = (Path(state["run"]) / "after" / name).read_bytes()
            if digest(candidate) != state["files"][name]["after"]:
                raise Stop("Saved candidate changed.")
            expected = self.git("hash-object", "--path=" + name, "--stdin",
                                input=candidate).strip()
            if self.git("rev-parse", commit + ":" + name).strip() != expected:
                raise Stop(f"Commit content differs from reviewed local content: {name}")

    def sync(self):
        state = self.check()
        if state["phase"] == "pushed":
            return state
        paths = list(state["files"])
        if state["phase"] in ("applied", "committing"):
            if self.head() != state["base"]:
                if state["phase"] != "committing":
                    raise Stop("HEAD changed since prepare.")
                self.verify_commit(self.head(), state, state["changed"])
                state.update(phase="committed", commit=self.head())
                self.save(state)
            else:
                if state["phase"] == "applied" and self.staged():
                    raise Stop("Index changed after apply.")
                self.git("fetch", "origin")
                if self.git("rev-parse", "origin/main").strip() != state["base"]:
                    raise Stop("Remote advanced; keep local files and reconcile before committing.")
                changed = [p for p in paths if self.git("diff", "--name-only", "HEAD", "--", p).strip()
                           or not self.git("ls-files", "--", p).strip()]
                if not changed:
                    state.update(phase="pushed", commit=state["base"], no_changes=True)
                    self.save(state)
                    return state
                state.update(phase="committing", changed=changed)
                self.save(state)
                self.git("add", "--", *changed)
                if self.staged() != set(changed):
                    raise Stop("Staged paths differ from the explicit change list.")
                for name in changed:
                    candidate = (Path(state["run"]) / "after" / name).read_bytes()
                    expected = self.git("hash-object", "--path=" + name, "--stdin", input=candidate).strip()
                    if self.git("rev-parse", ":" + name).strip() != expected:
                        raise Stop(f"Staged content changed before commit: {name}")
                self.diff_check("--cached")
                self.git("commit", "-m", f"Update GitHub Trend Watch for {state['date']} (local first)")
                self.verify_commit(self.head(), state, changed)
                state.update(phase="committed", commit=self.head())
                self.save(state)
        if self.head() != state["commit"]:
            raise Stop("HEAD changed after the report commit; reconcile before pushing.")
        if self.staged():
            raise Stop("Index changed after the report commit.")
        self.git("fetch", "origin")
        remote = self.git("rev-parse", "origin/main").strip()
        if self.git("merge-base", "--is-ancestor", state["commit"], "origin/main", check=False).returncode:
            if remote != state["base"]:
                raise Stop("Remote advanced; local commit retained. Never force-push.")
            self.git("push", "origin", "HEAD:refs/heads/main")
            self.git("fetch", "origin")
            self.git("merge-base", "--is-ancestor", state["commit"], "origin/main")
        state["phase"] = "pushed"
        self.save(state)
        return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=DEFAULT_REPO)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare = sub.add_parser("prepare")
    prepare.add_argument("--date", required=True)
    prepare.add_argument("--paths", nargs="*", default=[])
    apply = sub.add_parser("apply")
    apply.add_argument("--plan", required=True)
    for name in ("check", "sync", "status"):
        sub.add_parser(name)
    args = parser.parse_args()
    try:
        flow = Workflow(args.repo)
        with flow.lock():
            if args.command == "prepare":
                result = flow.prepare(args.date, args.paths)
            elif args.command == "apply":
                result = flow.apply(args.plan)
            elif args.command == "status":
                flow.identity()
                result = {"head": flow.head(), "status": flow.git("status", "--short", "--branch"),
                          "run": flow.state() if flow.state_path.exists() else None}
            else:
                result = getattr(flow, args.command)()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (Stop, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
