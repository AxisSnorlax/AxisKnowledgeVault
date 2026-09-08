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
- Windows-only 桌面 UI 是否迁移到 [[WinUI]]。

## 架构原则

- UI 不拥有 Agent、Provider、MCP、Git、Process 等核心逻辑。
- Agent Core 与 Desktop UI 解耦。
- 真实运行结果、验证和失败恢复优先于视觉 Demo。
- 新实现优先收敛既有结构，不叠加兼容壳和临时补丁。

## 关联

- [[Agent]]
- [[Agent Harness]]
- [[Skills]]
- [[Context Engineering]]
- [[Memory]]
- [[MCP]]
- [[WinUI]]
- [[Avalonia]]
- [[AxisAIManager]]
