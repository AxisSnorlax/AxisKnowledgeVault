# Durable Agent Runtime Identity

工作假设（2026-10-14）：Agent 的 Task、Run 与 Session 应保留稳定身份，执行 Worker 可以暂停、恢复或被替换。运行状态恢复后仍应保持原授权及验证证据。

依据：`agent-substrate/substrate` 的 Actor/Worker 设计与此前的 Durable Run 研究。其 Kubernetes 实现尚处于 pre-1.0，不应直接移植到 [[AxisAgent]]。

来源：https://github.com/agent-substrate/substrate

关联：[[GitHub Trending — 2026-10-14]] · [[Deterministic Agent Runtime]] · [[Agent]]
