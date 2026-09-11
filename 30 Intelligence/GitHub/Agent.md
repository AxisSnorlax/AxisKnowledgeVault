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
- `vercel-labs/skills` — 跨 75+ Agent 的 Skill 安装、发现、更新与分发 CLI。
- `akitaonrails/ai-memory` — 面向 Coding Agent 的跨 Harness 长期 Memory 与 Session Handoff。
- `nashsu/llm_wiki` — 增量构建和维护持久知识 Wiki，而不是每次从原始来源重新 RAG。
- `diegosouzapw/OmniRoute` — 多 Provider Gateway 与可组合 Routing Policy；关注路由层而非其 Provider 数量宣传。
- `t8y2/dbx` — 专业桌面数据库工具将 MCP 独立分发并进行读/写/高风险写权限分层。

## 2026-09-10 变化

今天出现三个值得长期跟踪的层级信号：

1. **Skill → Plugin**：Skill 更像单一工作流/行为能力；Plugin 开始成为 Skills + MCP + Agent + Hook + Asset 的分发容器。
2. **Plugin → Team Harness**：团队开始需要版本化、审查、分发、Recall、Prune 和跨 Agent 兼容，而不是每个人维护自己的 Prompt/Skill 目录。
3. **Harness → Desktop Product**：Agent Desktop 不再只是聊天壳，开始正式承载 Permission、Workspace、Secrets、Plugin、MCP、Subagent、Checkpoint 与 Recovery。

参见：[[GitHub Trending — 2026-09-10]] · [[Agent Capability Packaging]]

## 2026-09-11 变化

今日进一步确认四个方向：

1. **Skill → Package Lifecycle**：`vercel-labs/skills` 把 Skill 的 Discovery、Install、Project/User Scope、Private Source、Update、Remove 和多 Agent Compatibility 做成统一 CLI。Skill Registry 不能只等价于目录扫描。
2. **Memory → Cross-Harness Continuity**：`ai-memory`、`llm_wiki` 与此前 `context-mode`、`teamai-cli` 共同说明 Working Context、Session/Handoff Memory、Promoted Knowledge 应分层治理。详见 [[Agent Memory and Knowledge Lifecycle]]。
3. **Provider Registry → Routing Plane**：`OmniRoute` 将 quota、health、cost、latency、context、cache、fallback 等组合为路由策略。对 [[AxisAgent]] 的合理动作是预留 Routing Policy，而不是立即复制完整 Gateway。
4. **Professional App → MCP Surface**：`dbx`、`unity-mcp` 以及 Rust 生态中的 KiCAD 工具继续说明，专业软件越来越倾向把受控能力暴露成 MCP/Tool Surface，而不是把 Agent 逻辑耦合进 UI。

此外，`Tencent/teamai-cli` 从昨日记录的 +563/day 上升至 +837/day，`vastsa/PI-Desktop` 从 +393/day 上升至 +636/day，说明 Team Harness 与 Agent Desktop 暂时不是单日噪声。

参见：[[GitHub Trending — 2026-09-11]] · [[Agent Capability Packaging]] · [[Agent Memory and Knowledge Lifecycle]]

## 对 AxisAgent 的长期启示

建议将以下能力提升为一级架构组件，而不是零散 Service：

- Skill Registry（Source / Version / Scope / Update / Compatibility）
- Plugin Registry / Manifest / Compatibility
- Context Engine
- Session / Handoff Memory
- Promoted Knowledge Boundary
- Tool Registry
- MCP Runtime
- Provider Routing Policy
- Browser/Computer Runtime
- Approval & Permission
- Checkpoint / Recovery
- Streaming Event Pipeline
- Knowledge Capture / Review / Promote / Recall / Prune

关联：[[AxisAgent]]
