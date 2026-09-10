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
- `openai/plugins` — Codex 可分发插件包；可组合 Skills、MCP、Agents、Commands、Hooks 与 Assets。
- `Tencent/teamai-cli` — 团队级 Harness 分发、Context/Knowledge Recall 与持续改进。
- `vastsa/PI-Desktop` — Local-first 独立 Agent Desktop，分离 UI、特权 Host 与 Agent Sidecar。
- `rtk-ai/rtk` — 面向 Agent 的 Tool Output / Token 压缩层。

## 2026-09-10 变化

今天出现三个值得长期跟踪的层级信号：

1. **Skill → Plugin**：Skill 更像单一工作流/行为能力；Plugin 开始成为 Skills + MCP + Agent + Hook + Asset 的分发容器。
2. **Plugin → Team Harness**：团队开始需要版本化、审查、分发、Recall、Prune 和跨 Agent 兼容，而不是每个人维护自己的 Prompt/Skill 目录。
3. **Harness → Desktop Product**：Agent Desktop 不再只是聊天壳，开始正式承载 Permission、Workspace、Secrets、Plugin、MCP、Subagent、Checkpoint 与 Recovery。

参见：[[GitHub Trending — 2026-09-10]] · [[Agent Capability Packaging]]

## 对 AxisAgent 的长期启示

建议将以下能力提升为一级架构组件，而不是零散 Service：

- Skill Registry
- Plugin Registry / Manifest / Compatibility
- Context Engine
- Memory Engine
- Tool Registry
- MCP Runtime
- Browser/Computer Runtime
- Approval & Permission
- Checkpoint / Recovery
- Streaming Event Pipeline
- Knowledge Capture / Review / Promote / Recall / Prune

关联：[[AxisAgent]]
