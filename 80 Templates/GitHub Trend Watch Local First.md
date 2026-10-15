# GitHub Trend Watch：本地优先同步

工作目录：`D:\Projects\AxisKnowledgeVault`。远端：`AxisSnorlax/AxisKnowledgeVault`，分支：`main`。日期使用 Asia/Singapore。

## 执行流程

1. 阅读现有日报及相关长期页，完成来源研究，确定本轮真正需要改动的文件。保留原有人工内容、frontmatter、引用和双向链接。
2. `prepare` 检查仓库、fetch/push URL、main/upstream、暂存区和未完成 Git 操作；fetch 后仅允许 fast-forward。无关未暂存修改可以保留；目标文件有人工修改、暂存区非空、存在未归属本任务的本地提交或分叉时停止并报告。不要自动 stash/reset。
3. `prepare` 为每个目标文件记录原始字节 SHA-256，并在 `.git/trend-watch/runs/` 保存修改前副本。先完成远端更新，再按本地现有内容编写增量计划。
4. 所有候选文件必须完整、通过结构检查后，`apply` 才开始写本地文件。日报先写，长期页按照指定顺序逐文件串行处理；不会并行覆盖。
5. 阅读 `git diff`，核对新增来源、链接和人工内容。执行 `check`，再执行 `sync`：明确路径的 add → commit → 普通 push → fetch 验证提交在 origin/main 历史中。
6. 任何网络、权限或冲突失败均保留本地正文与提交，报告具体错误。禁止 fallback 到 connector 写正文，禁止 placeholder，禁止 force push。Public/Private 不作为阻断条件。

## Windows 命令

需要 Python 3.10+ 和 Git，凭据由本机 Git credential helper 提供。脚本在 Windows 的每条 Git 命令中使用 OpenSSL，仍然启用证书验证；不改全局 Git 配置。

```powershell
Set-Location -LiteralPath 'D:\Projects\AxisKnowledgeVault'
python tools/trend_watch.py prepare --date 2026-10-15 --paths '30 Intelligence/GitHub/Local-AI.md' '40 Engineering/Agent Verification and Audit Plane.md'
# 阅读 prepare 返回的哈希及文件完整内容，在任务工作目录编写 plan.json。
python tools/trend_watch.py apply --plan 'C:\path-to-task\work\plan.json'
git diff -- '30 Intelligence/GitHub/Daily/2026-10-15.md' '30 Intelligence/GitHub/Local-AI.md' '40 Engineering/Agent Verification and Audit Plane.md'
python tools/trend_watch.py check
python tools/trend_watch.py sync
python tools/trend_watch.py status
```

日期按运行当天修改；`prepare` 自动把当天日报放在文件列表首位。没有必要更新的长期页不要传入。若只需核验已完整的日报，计划可仅包含日报及空 edits，不产生空提交。

## 增量计划协议

JSON 顶层为 `files` 数组，每项含 `path` 与 `base_sha256`，必须覆盖 prepare 的每个文件且恰好一次。

- 已存在文件：`base_sha256` 使用 prepare 输出值；`edits` 是 `{ "before": "原有精确片段", "after": "修改后片段" }` 数组。每个 before 必须恰好出现一次。使用最小必要片段，不把整个人工页面当成可重写模板。没有变更时用空数组。
- 新文件：`base_sha256` 为 null，`create` 为完整 Markdown 正文。禁止先创建占位再填充。已存在文件禁止使用 create。
- 新增长期段落：可使用 `append_blocks`，每项包含唯一 `key`（小写英文字母、数字、连字符）和完整 `content`。脚本添加成对的 `<!-- trend-watch:key:begin -->` / `end` 标记。相同 key 与内容重跑为 no-op；相同 key 内容不同则必须先读旧内容，用精确 edits 更新。
- 旧页面已有当天段落时直接增量修改旧段落，不再添加同一天的重复 marker。人工补充即使在 managed block 内也必须保留；marker 不赋予删除人工内容的权限。
- 文本片段使用 LF 换行；脚本保留原文件的换行约定及 UTF-8 BOM。原始 SHA-256 防止在研究期间覆盖用户的新编辑。

日报必须有 `status: reviewed`、与路径一致的日期、非空的“今日结论 / 长期判断 / 来源”、项目来源、增长或趋势信号、Windows/.NET 借鉴与 Obsidian 链接。增长数据无法可靠取得时，明确写“未取得可靠增长数据”并解释观察信号，不造数。结构校验不能替代来源核验与人工内容审查。

## 重试与恢复

- 同一计划重复 apply 不追加重复内容。中断时可以使用完全相同的计划再次 apply，已写入且哈希一致的文件跳过。
- push 失败后，先解决真实的网络/凭据错误，再重跑 sync；复用已有提交，不重复提交。远端并发前进则保留本地提交并停止，检查和合并后重新审核；不盲目 rebase/覆盖人工内容。
- 状态位于 `.git/trend-watch/state.json`，完整 before/after 在 runs 子目录。不要把状态、计划、凭据、`.obsidian`、`.vs` 或临时资产加入提交。
- 如果必须放弃一次运行，先检查 state、diff 和备份，明确处理本轮修改后，将 state.json 归档到对应 run 目录。脚本不提供破坏性自动回滚。
- 锁只在命令执行期间占用；崩溃遗留 run.lock 时先确认记录的进程已结束，再删除该单个锁文件。

## 自动任务配置

使用 `80 Templates/GitHub Trend Watch Automation Prompt.md` 替换旧任务的写入规则。任务必须具有本机执行环境和此目录访问权限；保持原定时间与时区，不创建与旧任务同时写同一日报的第二个任务。

先完成配置迁移和旧任务替换，再声称“今后自动生效”。仅保存脚本、AGENTS.md 或提示词文件不等于已修改托管任务。
