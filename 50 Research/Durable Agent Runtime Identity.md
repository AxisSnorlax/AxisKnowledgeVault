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

<!-- trend-watch:2026-11-09-execution-environment-identity:begin -->
## 2026-11-09：控制端、Runtime 宿主与工作区目标

[OpenBitFun README](https://github.com/GCWing/OpenBitFun) 与[远程工作区文档](https://github.com/GCWing/OpenBitFun/blob/main/docs/features/remote-workspaces.md) 提供了新的身份分层样本：远程命令／文件面向目标环境，Runtime 与会话记录仍归宿主机；远程会话 fork 共用工作树，产物读取不能退回控制端同名路径。以下是 Axis 设计推论，未独立实测上游实现。

- 为回执区分 `controllerId`、`runtimeHostId`、`executionTarget`、`workspaceBinding` 与 `artifactOrigin`；目标可进一步带 SSH／容器／WSL 身份和路径命名空间。
- Task／Run 身份稳定不意味着执行位置不变。重新连接或切换目标时核对完整绑定及授权范围，不能仅比较相同路径文字。
- 控制端失联、工作区不可达和任务结束分别表示；只有来自对应执行环境的当前回执可以推进状态。
- 会话历史复制、工作树隔离和快照覆盖分别声明。可显示某次 diff 不保证完整回滚；恢复前核对来源主机、版本和可访问范围，不从当前文件伪造历史基线。

这扩展了现有 `restoreMode / processGeneration`：恢复不仅需要知道“是哪一代进程”，也需要知道“在哪个环境读取哪份状态”。

参见：[[30 Intelligence/GitHub/Daily/2026-11-09|GitHub Trending — 2026-11-09]] · [[AxisAgent]] · [[Agent Memory and Knowledge Lifecycle]] · [[Agent Verification and Audit Plane]]
<!-- trend-watch:2026-11-09-execution-environment-identity:end -->
