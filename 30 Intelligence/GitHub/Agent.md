---
type: intelligence-index
topic: agent
status: active
tags:
  - github
  - agent
  - ai-coding
---

# Agent 趋势索引

## 当前主线

Agent 开源生态正在从“模型 + Prompt + Tool”转向更完整的工程化体系：

- [[Skills]]
- [[Context Engineering]]
- [[Memory]]
- [[MCP]]
- [[Browser Agent]]
- [[Computer Use]]
- [[Agent Harness]]
- [[Multi-Agent Runtime]]

## 重点项目

- `openai/skills` — Agent Skills 规范与可复用能力层。
- `mksglu/context-mode` — Context 压缩、工具输出治理、Session Memory。
- `browser-use/browser-use` — Browser Agent。
- `ChromeDevTools/chrome-devtools-mcp` — Browser/MCP 工具链。
- `NousResearch/hermes-agent` — Agent Runtime。
- `affaan-m/ECC` — Agent Harness 优化。
- `ruvnet/ruflo` — Multi-Agent / Harness / Memory / RAG。
- `obra/superpowers` — Skills 工作流。

## 对 AxisAgent 的长期启示

建议将以下能力提升为一级架构组件，而不是零散 Service：

- Skill Registry
- Context Engine
- Memory Engine
- Tool Registry
- MCP Runtime
- Browser/Computer Runtime
- Approval & Permission
- Checkpoint / Recovery
- Streaming Event Pipeline

关联：[[AxisAgent]]
