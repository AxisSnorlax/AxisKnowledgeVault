---
type: project
project: AxisAgent
status: active
platform: Windows
repository: AxisSnorlax/AxisAgent
tags:
  - axis
  - agent
  - windows
  - dotnet
---

# AxisAgent

AxisAgent 是 Windows 本地优先的通用 Agent 工作台。当前项目主循环围绕 Project/Conversation、显式 Permission/Model/Context、受控 Tool/Approval、Changes/Files/Terminal/Browser/Computer、Verification/Result/Artifact 与可恢复历史构建。

> 项目仓库与正式报告仍是实现事实第一真源；下述趋势映射只代表研究候选，不自动改变当前实现状态。

## 当前定位

- Windows 本地优先 Agent Desktop。
- Desktop 与 CLI 共享 Application 与 Agent Runtime 契约。
- Native Shell + Full Runtime 双运行时架构。
- 本地模型通过 [[AxisAIManager]] 控制切换；切换后 AxisAgent 直接访问 llama-server。
- Browser 以系统 Edge + WebView2 为主，不随应用分发 Chromium。

## 当前技术重点

- Agent Runtime
- Provider abstraction
- Tool / Approval / Permission
- Files / Git / Terminal / Browser / Computer
- Project / Conversation persistence
- Recovery / Verification / Artifact
- Native AOT 边界
- [[Local-AI]]

## 下一阶段值得重点研究

- [[Skills]] 作为一级能力模块。
- [[Context Engineering]] / Context Engine。
- [[Memory]] Engine。
- [[MCP]] Runtime 与插件体系。
- Streaming Event Pipeline。
- Browser / Computer / Terminal / Files / Git 独立能力域。
- Windows-only 桌面 UI 的框架资格验证，而不是仅凭趋势迁移。

## 2026-09-15 研究候选：Deterministic Runtime

连续几天的 Agent 工程趋势已经形成一条与 AxisAgent 当前架构高度兼容的长期路线：[[Deterministic Agent Runtime]]。

当前项目已经拥有显式 Permission / Approval、受控 Workspace、Tool、Verification、Artifact 与可恢复历史，因此后续更值得做的是**把这些边界继续工程化和可观测化**，而不是增加更多 Prompt Guardrail。

建议后续资格审计关注：

- Workspace Scope 是否始终由 Runtime 决定；
- Tool / MCP Server / Tool Name 是否都有稳定 Identity；
- Approval 是否绑定具体 Action / Resource / Run；
- Retry / Recovery 是否保存 Parent Run / Evidence lineage；
- Verification 是否独立于 Agent 文本判断；
- Credential 是否有最小 Scope / Lifetime，且不进入 Prompt、普通日志或持久 Git Config；
- Browser / Computer 高风险操作是否可追溯到真实用户授权；
- Run Store 是否可以在不依赖 Conversation 文本的情况下重建关键执行事实。

同时，`alibaba/open-code-review` 的 Deterministic Engineering × Agent 模式提供一个很适合 AxisAgent 的边界判断：

```text
不能出错的步骤
→ 代码 / 状态机 / Policy / Validator

需要探索的步骤
→ Agent Reasoning / Retrieval / Planning
```

这是研究候选，不表示上述字段当前已经全部实现。

## 架构原则

- UI 不拥有 Agent、Provider、MCP、Git、Process 等核心逻辑。
- Agent Core 与 Desktop UI 解耦。
- 真实运行结果、验证和失败恢复优先于视觉 Demo。
- 新实现优先收敛既有结构，不叠加兼容壳和临时补丁。
- 安全、权限、状态一致性和完成判定不能依赖 Prompt 自律。

## 关联

- [[Agent]]
- [[Agent Harness]]
- [[Skills]]
- [[Context Engineering]]
- [[Memory]]
- [[MCP]]
- [[Deterministic Agent Runtime]]
- [[Agent Skill Supply Chain]]
- [[WinUI]]
- [[Avalonia]]
- [[AxisAIManager]]
- [[GitHub Trending — 2026-09-15]]
