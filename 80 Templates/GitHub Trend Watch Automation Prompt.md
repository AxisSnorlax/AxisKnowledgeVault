# GitHub Trend Watch 自动化提示词

以下正文用于现有 GitHub Trend Watch 任务。保持现有调度时间和 Asia/Singapore 时区，将执行环境改为可访问 `D:\Projects\AxisKnowledgeVault` 的用户 Windows 本机。停用旧的 connector-first 写入规则，避免两套任务并行写入。

---

每次运行时，研究 GitHub Trending 与近期高增长开源项目，重点关注 Agent、AI Coding、MCP、C#/.NET、WinUI 3、WPF、Avalonia、本地 AI 和对 Windows 工程的实际借鉴。核查项目官方仓库、发布记录和可靠的增长窗口；区分项目自报数据与独立验证，不编造数据，不为凑日报制造框架变化。

必须在用户 Windows 本机 `D:\Projects\AxisKnowledgeVault` 先更新本地知识库，再通过本机 Git 同步 `AxisSnorlax/AxisKnowledgeVault` 的 main。运行前读取根目录 AGENTS.md 和 `80 Templates/GitHub Trend Watch Local First.md`，使用 `tools/trend_watch.py` 执行 prepare → apply → check → sync。不要通过 GitHub connector create_file/update_file 直接写正文。Public/Private 不作为阻断条件。

日期按 Asia/Singapore 确定。当天路径为 `30 Intelligence/GitHub/Daily/YYYY-MM-DD.md`。若日报已存在，先完整读取，保留人工修订与原有有效内容，进行完整的增量更新。日报必须包含今日结论、重点项目、增长信号及时间窗口、Windows/.NET 借鉴、长期判断、来源和 Obsidian 双向链接；只写完整 reviewed 正文，禁止 placeholder。

根据实际新增证据选择必要的长期索引或研究页，如 `30 Intelligence/GitHub/Agent.md`、DotNet.md、WinUI.md、Avalonia.md、Local-AI.md、`40 Engineering/`、`50 Research/`。逐文件串行读取和更新，复用已有日期段落与 marker，避免重复内容。没有新证据的主题不机械更新。所有原有人工文本，包括 marker 内的人工补充，都必须保留。

prepare 核对路径、分支、fetch/push remote、工作树、暂存区和远端变化，记录原始哈希。为每个文件生成精确增量计划；apply 校验完整内容后写入本地。审查 git diff、来源、双向链接、重复 marker 和日期段落，check 通过后 sync 只 add 本轮明确文件，再 commit/push/fetch 验证。禁止 git add .、自动 stash、reset --hard、force push 或夹带无关人工改动。发现用户的新编辑、分叉或并发远端提交时保留全部本地成果并报告具体冲突。

失败时说明停在哪一步、哪些本地文件已完整保存、是否已有 commit，以及恢复所需的具体条件。push 失败不重复生成日报、不重建已有提交；解决后重跑 sync。只有 fetch 验证本次提交已在 origin/main 上，才报告同步成功。

汇报当天关键发现、实际更新文件、commit SHA、远端核验结果以及需用户处理的问题。若运行环境无法访问本机目录，明确报告执行环境需要迁移，不退回远端优先写入，也不声称本地已更新。
