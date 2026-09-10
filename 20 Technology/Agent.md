---
type: technology-index
topic: agent
status: active
tags:
  - ai
  - agent
  - runtime
---

# Agent

## 核心组成

- [[Agent Harness]]
- [[Skills]]
- [[Context Engineering]]
- [[Memory]]
- [[MCP]]
- Tool Registry
- Permission / Approval
- Browser / Computer / Terminal / Files / Git
- Checkpoint / Recovery
- Verification / Result / Artifact
- Streaming Event Pipeline

## 推荐架构

```text
UI / CLI
   ↓
Application
   ↓
Agent Runtime
   ├── Skills
   ├── Context
   ├── Memory
   ├── Tools
   ├── MCP
   ├── Approval
   ├── Browser/Computer
   └── Recovery
   ↓
Provider / Local Model / External Services
```

## 能力包装层级

截至 2026-09-10 的开源生态信号，建议把以下概念区分开，不把它们都叫“插件”或“工具”：

### Skill

聚焦、可复用的工作流或行为单元。它可以描述“怎么完成某类任务”，也可以描述“回答与推进任务时应采用什么行为策略”。Skill 本身不应默认获得高权限。

### Plugin

可安装、可版本化的能力包。一个 Plugin 可以组合：

- Skills
- Tools / MCP Servers
- Specialized Agents
- Commands
- Hooks
- Assets
- Permission Manifest
- Compatibility Metadata

Plugin 是分发和治理边界，不等同于 DLL，也不要求所有插件都执行本机代码。

### Harness

运行、组合和治理能力的基础设施层，负责：

- Capability Discovery / Registry
- Context / Memory
- Permission / Approval
- Tool / MCP Lifecycle
- Checkpoint / Recovery
- Verification
- Event Streaming
- Plugin Compatibility / Isolation

### Team Harness

在 Harness 之上增加团队级版本化、Review、共享知识、经验沉淀、Recall 与 Prune。它解决的是“能力和知识如何跨用户、跨 Agent、跨项目长期治理”，而不是单次 Agent Loop。

这一层级是当前观察得到的工程模型，并非行业正式标准。详细研究见 [[Agent Capability Packaging]]。

## 知识生命周期

长期 Memory/Knowledge 不应等价于“自动保存所有对话”。更合理的流程是：

```text
Capture
  ↓
Review
  ↓
Promote
  ↓
Recall
  ↓
Prune / Archive
```

只有经过筛选、可复用且有事实依据的内容才进入长期知识层。这同样适用于 [[Axis Knowledge Vault]]。

## 设计原则

1. Harness 统一调度，避免能力散落到多个互相交叉的 Manager。
2. Tool、MCP、Skill、Plugin 都要有生命周期、权限、超时和失败恢复。
3. Context 是预算问题，不是简单把所有信息塞进 Prompt。
4. Streaming 面向事件而不是逐 token 直推 UI。
5. Agent 的完成标准是可验证的工作结果，而不是“生成了一段回答”。
6. Plugin 必须有来源、版本、兼容性和权限声明；高权限能力不能仅靠 Prompt 约束。

关联：[[AxisAgent]] · [[Local-AI]] · [[GitHub Trending — 2026-09-09]] · [[GitHub Trending — 2026-09-10]]
