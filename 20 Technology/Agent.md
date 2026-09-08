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

## 设计原则

1. Harness 统一调度，避免能力散落到多个互相交叉的 Manager。
2. Tool、MCP、Skill 都要有生命周期、权限、超时和失败恢复。
3. Context 是预算问题，不是简单把所有信息塞进 Prompt。
4. Streaming 面向事件而不是逐 token 直推 UI。
5. Agent 的完成标准是可验证的工作结果，而不是“生成了一段回答”。

关联：[[AxisAgent]] · [[Local-AI]] · [[GitHub Trending — 2026-09-09]]
