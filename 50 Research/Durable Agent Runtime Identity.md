# Durable Agent Runtime Identity

工作假设（2026-10-14）：Agent 的 Task、Run 与 Session 应保留稳定身份，执行 Worker 可以暂停、恢复或被替换。运行状态恢复后仍应保持原授权及验证证据。

依据：`agent-substrate/substrate` 的 Actor/Worker 设计与此前的 Durable Run 研究。其 Kubernetes 实现尚处于 pre-1.0，不应直接移植到 [[AxisAgent]]。

来源：https://github.com/agent-substrate/substrate

关联：[[GitHub Trending — 2026-10-14]] · [[Deterministic Agent Runtime]] · [[Agent]]

<!-- trend-watch:2026-10-25-restore-modes:begin -->
## 2026-10-25：恢复方式与进程代次

[Herdr 会话文档](https://herdr.dev/docs/session-state/) 区分原进程持续运行、布局恢复和原生会话恢复；[Windows 支持页](https://herdr.dev/docs/windows-beta/) 明确不支持 live handoff。文档是当前产品说明，不等于所有平台或已发布版本均通过本机验证。

对 [[AxisAgent]] 的新增工作假设：恢复回执记录 `restoreMode`、`processGeneration`、`nativeSessionReference` 与当前活性证据；任务身份稳定不意味着进程身份不变。恢复目录不可用应显示具体失败，保留原位置与会话引用。重新建立工具连接后，以当前执行结果判断完成，不以历史画面或旧状态替代。

本轮未运行 Herdr，也未调整现有授权模型。参见：[[30 Intelligence/GitHub/Daily/2026-10-25|GitHub Trending — 2026-10-25]] · [[Deterministic Agent Runtime]]
<!-- trend-watch:2026-10-25-restore-modes:end -->
