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
- `github/spec-kit` — Spec-driven Agent Workflow；规格、计划、任务、检查清单与 Extensions/Presets/Bundles 形成可组合工程流程。
- `Unity-Technologies/skills` — Unity 官方 Domain Skills，强化“专业工作流 → Skills”路线。
- `dotnet/skills` — .NET 团队维护的 Plugins/Skills 集合，并开始度量 Skill Value。
- `superplanehq/superplane` — Durable Work Order / Run / Artifact / Retry 模型，面向验证后可审查的工程自动化。
- `alphaXiv/OpenResearch` — Local-first Research Agent Workspace；使用独立 Git Worktree、实验树与不可变 Run Snapshot 保存证据链。
- `pascalorg/editor` — 3D 专业编辑器同时提供 Local/Hosted MCP、Domain Skills 与能力发现。
- `HakanSeven12/OpenCADStudio` — CAD 专业软件提供版本化 Automation API、Headless Server、MCP 与进程隔离 Plugin。
- `Tencent/WeKnora` — RAG + Agent + Auto-Wiki；强调 Wiki Revision / Diff / Rollback 与 Cross-session Memory。
- `tech-leads-club/agent-skills` — Secure Skill Registry；把静态扫描、内容哈希、Lockfile、路径隔离、审计与回滚带入 Skill 分发链。
- `alibaba/open-code-review` — Deterministic Engineering × Agent；关键步骤由确定性工程保证，Agent 专注动态判断与检索。
- `github/gh-aw` — Agentic Workflows；持续强化 Run/MCP 可观测性、Safe Output、Threat Detection 与 Credential Blast Radius。
- `Panniantong/Agent-Reach` — Internet Capability Layer；按真实 Health Probe 在多个 Backend Adapter 之间选择与回退。

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

## 2026-09-12 变化

今天出现三个值得提升为长期模型的信号：

1. **Skill → Executable Governance**：`obra/superpowers` 将 brainstorming、计划、TDD、systematic debugging、code review 与完成前验证做成强制 Skill workflow；Skill 不再只是知识提示，而开始表达工程行为与验证门禁。
2. **Workflow → Versioned Composition**：`github/spec-kit` 的 Extensions / Presets / Bundles 与版本/安装策略说明，项目工程流程也正在获得可组合、可版本化的分发层。
3. **Vendor Domain Skills**：Unity 官方 `Unity-Technologies/skills` 与 .NET 官方 `dotnet/skills` 同时活跃，说明专业软件/平台厂商正在直接发布领域 Skills。此前“Professional App → MCP Surface”的判断应扩展为 **Professional App → Domain Skills + Controlled MCP/Tool Surface**。

`nashsu/llm_wiki` 从昨日约 +94/day 上升到约 +640/day，也显著增强了“Promoted Knowledge 应作为持久、可维护派生资产”的信号，详见 [[Agent Memory and Knowledge Lifecycle]]。

参见：[[GitHub Trending — 2026-09-12]] · [[Agent Capability Packaging]] · [[Agent Memory and Knowledge Lifecycle]]

## 2026-09-13 变化

今天新增两个达到架构级价值的信号：

1. **Conversation → Durable Work Record**：`superplanehq/superplane` 将 Work Order、Automation、Run、Retry、Cost、Artifact 和 Event History 作为持久执行记录；`alphaXiv/OpenResearch` 则使用独立 Git Worktree、Experiment Tree 与不可变 Commit Archive 保存每次实验证据。长期来看，Agent Runtime 的 Task/Run Store 应独立于聊天记录，支持恢复、比较、审计和验证。
2. **Professional App → Stable Agent Surface**：`pascalorg/editor` 与 `OpenCADStudio` 同日出现，和此前 `dbx`、Unity Skills/MCP 形成连续证据。长期模型正式沉淀为 [[Professional Software Agent Surface]]：Domain Core → Automation Contract → MCP/Tool Surface → Domain Skills → Permission / Approval。

Knowledge 方向也得到进一步确认：`Tencent/WeKnora` 把 Auto-Wiki 与 revision history、line diff、rollback、人工编辑结合起来，说明 Promoted Knowledge 除来源和增量刷新外，还需要可逆的版本治理。

参见：[[GitHub Trending — 2026-09-13]] · [[Professional Software Agent Surface]] · [[Agent Memory and Knowledge Lifecycle]]

## 2026-09-14 变化

今天新增一个足以独立沉淀的长期信号，并确认一个昨日结论继续加速：

1. **Skill Package → Skill Supply Chain**：`tech-leads-club/agent-skills` 将 static scan、content hash、lockfile、path/symlink guard、audit trail 与发布前安全扫描加入 Skill Catalog。至此 Skill Registry 不能只处理 Source / Version / Scope / Install / Update，还必须处理 Trust / Integrity / Scan / Audit / Rollback。详见 [[Agent Skill Supply Chain]]。
2. **Progressive Disclosure → Skill/MCP Catalog 基线**：该项目的 MCP Surface 采用 `search/list metadata → read primary skill → fetch required references`，进一步支持 Context Engine 不应一次性注入完整 Catalog。
3. **Durable Run / Evidence Lineage 继续增强但不重复建模**：`alphaXiv/OpenResearch` 从昨日约 +120/day 加速至今日约 +304/day，继续验证独立 Worktree、不可变 Run Snapshot 与 Artifact lineage 的价值，但沿用 2026-09-13 已沉淀模型。

参见：[[GitHub Trending — 2026-09-14]] · [[Agent Skill Supply Chain]] · [[Agent Capability Packaging]]

## 2026-09-15 变化

今天出现两个新的工程级信号，并确认两个既有方向继续加速：

1. **Prompt Guardrail → Deterministic Runtime Contract**：`alibaba/open-code-review` 今日约 +1,796/day。其核心设计把文件选择、Work Unit 分组、规则匹配、定位与反射等关键步骤放到确定性工程层，Agent 只处理动态决策和上下文检索。长期原则正式沉淀为 [[Deterministic Agent Runtime]]：不能出错的步骤用代码/状态机/验证器保证，Agent 只进入允许探索的决策区。
2. **Durable Run → Observable / Security-aware Run**：GitHub `gh-aw` 2026-09-14 官方周报显示 MCP Tool Call 已进入结构化日志，且持续强化 Threat Detection、Safe Output、凭据不持久化与 Action SHA Pinning。这让 Durable Run / Evidence Lineage 从“留痕”进一步升级为 Runtime Governance。
3. **Skill Supply Chain 继续加速**：`tech-leads-club/agent-skills` 从知识库昨日记录的约 +215/day 上升到今日约 +506/day，说明 Source / Digest / Scan / Lock / Audit / Rollback 不是单日噪声。
4. **Capability → Adapter Router**：`Panniantong/Agent-Reach` 今日约 +640/day。其 `Capability → ordered backends → real probe → selected backend → fallback/doctor` 模式值得 Browser/Search Runtime 借鉴，但登录态/Cookie 类非官方接入路径存在账号与凭据风险，不能直接复制。

参见：[[GitHub Trending — 2026-09-15]] · [[Deterministic Agent Runtime]] · [[Agent Skill Supply Chain]]

## 对 AxisAgent 的长期启示

建议将以下能力提升为一级架构组件，而不是零散 Service：

- Skill Registry（Source / Version / Scope / Update / Compatibility）
- Skill Workflow / Verification Metadata
- Skill Supply-chain Trust / Integrity / Scan / Audit / Rollback
- Plugin Registry / Manifest / Compatibility
- Context Engine
- Session / Handoff Memory
- Promoted Knowledge Boundary
- Tool Registry
- MCP Runtime
- Provider Routing Policy
- Capability Adapter Routing / Health Probe / Fallback
- Browser/Computer Runtime
- Approval & Permission
- Checkpoint / Recovery
- Durable Run Record / Evidence Lineage
- Deterministic Runtime Contract
- Runtime Observability / Credential Scope / Threat & Safe-output Evidence
- Streaming Event Pipeline
- Knowledge Capture / Review / Promote / Recall / Prune
- Skill Quality Metrics（activation / success / elapsed / token / regression）

关联：[[AxisAgent]] · [[Deterministic Agent Runtime]]
