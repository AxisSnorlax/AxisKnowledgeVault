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
   ├── Handoff Memory
   ├── Tools
   ├── MCP
   ├── Provider Routing
   ├── Approval
   ├── Browser/Computer
   └── Recovery
   ↓
Provider / Local Model / External Services
```

长期知识通过独立 `Knowledge Gateway` 接入 Runtime，不应和当前 Context 或 Session Handoff 混为同一合同。

## 能力包装层级

截至 2026-09-11 的连续开源生态信号，建议把以下概念区分开，不把它们都叫“插件”或“工具”：

### Skill

聚焦、可复用的工作流或行为单元。它可以描述“怎么完成某类任务”，也可以描述“回答与推进任务时应采用什么行为策略”。Skill 本身不应默认获得高权限。

同时，Skill 已经出现明确的分发生命周期需求：Source、Version、Project/User Scope、Compatibility、Install、Update、Remove、Integrity。详见 [[Agent Capability Packaging]]。

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

## Memory 与 Knowledge 分层

连续观察 `context-mode`、`teamai-cli`、`ai-memory`、`llm_wiki` 后，长期架构原则升级为：

**`Working Context ≠ Session/Handoff Memory ≠ Long-term Knowledge`**。

### Working Context

面向当前 Run，受 Token/Latency Budget 约束。只装入完成当前任务所需的信息。

### Session / Handoff Memory

面向恢复和连续性，记录任务进度、已验证事实、关键决策、待完成事项和 Resume State；可以跨会话，未来也可以跨 Harness。

### Long-term Knowledge

面向长期复用，需要来源、Review、状态、Refresh 和 Prune。[[Axis Knowledge Vault]] 属于这一层，不能直接等价于 Agent Session Store。

详细研究见 [[Agent Memory and Knowledge Lifecycle]]。

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

## Provider Routing

2026-09-11 出现新的明显信号：Provider Registry 之上开始形成独立 Routing Plane，用健康、能力、成本、延迟、配额、上下文和本地/云偏好决定真实请求去向。

当前对 [[AxisAgent]] 的建议是**预留 Routing Policy，而不是立即实现复杂 Gateway**。第一阶段只需要可解释的少量信号：

- Capability / Model Role
- Health
- Cost
- Latency
- Local vs Cloud preference

任何自动 fallback 都必须保留用户约束、权限和可审计记录。

## 设计原则

1. Harness 统一调度，避免能力散落到多个互相交叉的 Manager。
2. Tool、MCP、Skill、Plugin 都要有生命周期、权限、超时和失败恢复。
3. Context 是预算问题，不是简单把所有信息塞进 Prompt。
4. Working Context、Handoff Memory、Long-term Knowledge 必须保持逻辑合同分离，即使底层共用存储。
5. Streaming 面向事件而不是逐 token 直推 UI。
6. Agent 的完成标准是可验证的工作结果，而不是“生成了一段回答”。
7. Plugin/Skill 必须有来源、版本、兼容性和权限声明；高权限能力不能仅靠 Prompt 约束。
8. Provider Routing 必须可解释、可审计，并尊重用户对本地/云、成本和隐私的明确约束。

关联：[[AxisAgent]] · [[Local-AI]] · [[GitHub Trending — 2026-09-09]] · [[GitHub Trending — 2026-09-10]] · [[GitHub Trending — 2026-09-11]]
