---
type: research
status: working-thesis
date: 2026-09-11
updated: 2026-09-12
topic: agent-memory-knowledge-lifecycle
tags:
  - agent
  - memory
  - context
  - knowledge
  - handoff
  - architecture
---

# Agent Memory and Knowledge Lifecycle

## 研究问题

Agent 的 `Context`、`Memory`、`Handoff`、`Knowledge Base` 应如何分层，避免最后全部退化成“往向量库里存东西”？

> 本文基于 2026-09-09 ～ 2026-09-12 连续观察到的 `context-mode`、`Tencent/teamai-cli`、`akitaonrails/ai-memory`、`nashsu/llm_wiki` 等项目形成，是 Axis 的工作模型，不是行业标准。

## 连续趋势证据

### mksglu/context-mode

重点解决当前会话中的 Context Budget、Tool Output 压缩和 Session Memory，说明 **Working Context 本身是受预算约束的运行时资源**。

### Tencent/teamai-cli

把“会话摩擦”作为知识 Capture 信号，并加入 Review、Recall、Promote、Maintenance / Prune，说明 **长期知识不应等价于自动保存所有会话**。

### akitaonrails/ai-memory

通过 MCP + Hooks 捕获 prompt、tool call 和 session boundary，并让下一会话获得 handoff；还允许同一 workstream 在不同 Harness（例如 Claude Code → Codex）之间继续，说明 **Session Continuity 可以独立于具体 Agent 客户端**。

### nashsu/llm_wiki

将文档增量编译为持久、互联的 Wiki；使用 SHA256 判断来源是否变化，未变化内容跳过重新处理。说明 **Promoted Knowledge 更像可维护的派生知识资产，而不是每次查询都从源文档重新生成答案**。

2026-09-12 该项目 Daily Trending 从前一日知识库记录的约 +94/day 上升到约 +640/day，同时其工程边界进一步值得吸收：

```text
Raw Sources
   │
   ├── immutable / traceable source material
   │
   ▼
Persistent Ingest Queue
   │
   ├── change detection / hash
   ├── normalize
   └── review candidate
   │
   ▼
Wiki / Promoted Knowledge
   │
   ├── index.md
   ├── wikilinks
   ├── YAML metadata
   └── derived explanations
   │
   ▼
Schema / Rules
   └── how knowledge should be organized and refreshed
```

它同时兼容 Obsidian 风格文件，并通过本机 API/MCP 暴露知识能力。这进一步强化了 Axis 的判断：**长期知识层应该是可维护、可链接、可刷新、可追溯的派生资产，而不是一个不可审计的 embedding 黑盒。**

## 建议分层

```text
Source of Truth
  │
  │  Files / Repos / Docs / Events / User Decisions
  │
  ▼
Capture Layer
  │
  │  Raw events / candidate facts / session signals
  │
  ├───────────────┐
  ▼               ▼
Working Context   Session / Handoff Memory
  │               │
  │               └── task state / decisions / pending work
  │
  └── current run budget / selected tool output
                  │
                  ▼
           Review / Promote
                  │
                  ▼
           Long-term Knowledge
                  │
                  ├── curated notes
                  ├── architecture decisions
                  ├── verified patterns
                  └── source traceability
                  │
                  ▼
             Recall / Retrieval
                  │
                  ▼
             Prune / Archive
```

## 三个必须分开的边界

### 1. Working Context

生命周期：单次 Run / Conversation Window。

包含：

- 当前用户请求；
- 当前计划；
- 经过裁剪的 Tool Result；
- 当前文件片段；
- 必要的近期消息。

原则：**越少越好，但必须足够完成当前任务。** 不应因为“可能有用”就全部塞入 Context Window。

### 2. Session / Handoff Memory

生命周期：跨 Run、跨会话，甚至跨 Harness。

包含：

- 当前任务进度；
- 已做决策；
- 已验证事实；
- 待完成事项；
- 当前工作区和关键 Artifact；
- 恢复执行所需的最小状态。

原则：**面向恢复和连续性，而不是百科全书。**

### 3. Promoted Knowledge

生命周期：长期。

包含：

- 已验证技术结论；
- ADR / 架构原则；
- 稳定项目事实摘要；
- 有来源的研究结论；
- 可复用工程规范。

原则：**需要来源、版本、Review 和维护。** `AxisKnowledgeVault` 属于这一层，而不是 Session Memory Store。

## Axis Knowledge Vault 生命周期

推荐：

```text
Capture
  ↓
Deduplicate / Source Check
  ↓
Review
  ↓
Promote
  ↓
Link / Index
  ↓
Recall
  ↓
Refresh / Prune / Archive
```

### Capture

来源可以包括：

- GitHub Trending Daily；
- 项目仓库 README / 正式报告；
- 技术调研；
- 已验证的设计决策；
- Agent 会话中明确有长期价值的结论。

### Promote

只有满足以下条件之一才进入 `20 Technology/`、`40 Engineering/`、`50 Research/`、`60 Decisions/`：

- 同一趋势连续多次出现；
- 有权威来源或真实项目证据；
- 已通过原型/Benchmark；
- 对多个 Axis 项目可复用；
- 属于明确架构决策。

### Recall

Recall 不等于“向量相似度最高”。未来可以综合：

- Exact link / entity；
- Project / Technology scope；
- BM25 / FTS；
- Semantic retrieval；
- Recency；
- Source authority；
- Knowledge status（working-thesis / verified / deprecated）。

### Refresh / Prune

长期知识必须允许：

- 标记 outdated；
- 被新 ADR supersede；
- 来源失效时降级可信度；
- 重复页面合并；
- 低价值 Daily 长期归档。

## 2026-09-12：增量刷新与派生知识追踪

`llm_wiki` 的持续增长使以下能力从“可选优化”提升为值得 Axis Knowledge Vault 正式设计的候选：

- **Source Hash / Source Revision**：记录知识来自哪个文件、仓库、URL、commit 或版本。
- **Incremental Refresh**：来源未变化时不重复处理；来源变化时只刷新受影响派生知识。
- **Derivation Link**：长期结论应能追溯到来源和产生该结论的研究记录。
- **Review Queue**：自动生成的候选知识先进入待审，而不是直接污染长期页。
- **Knowledge Status**：`candidate / working-thesis / verified / deprecated / superseded`。
- **Deterministic Link**：Obsidian `[[wikilink]]` / stable id 优先于仅靠向量相似度维持关系。

这并不意味着 Axis 必须复制 `llm_wiki` 的实现。知识库当前仍以 Git/Markdown/Obsidian 为最简单可靠的事实载体；未来检索层可以叠加 FTS/Vector，但不应反向绑架知识存储格式。

## AxisAgent 建议接口边界

不要建立一个什么都做的 `MemoryService`。更合理的逻辑边界：

```text
Context Engine
  ├── Budget
  ├── Selection
  ├── Compaction
  └── Tool Output Reduction

Handoff Store
  ├── Run Summary
  ├── Decisions
  ├── Pending Work
  └── Resume State

Knowledge Gateway
  ├── Search
  ├── Read
  ├── Cite Source
  ├── Propose Capture
  └── Promote with Review
```

底层可以共享 SQLite、FTS、Vector DB 或文件存储，但**逻辑合同不能因为底层共用数据库而合并**。

未来 Knowledge Gateway 若支持写入，建议再增加：

```text
Knowledge Ingestion
  ├── Source Revision
  ├── Hash / Deduplicate
  ├── Candidate Extraction
  ├── Review Queue
  ├── Promote
  ├── Refresh Impact
  └── Supersede / Archive
```

## 安全与真实性

1. Agent 自动生成的总结不是事实真源，必须保存来源关联。
2. Session Memory 不能自动升级为长期 Knowledge。
3. 涉及项目状态时，项目仓库/正式报告优先于 Vault 摘要。
4. 自动 Capture 应可审计，自动 Promote 应更严格。
5. 删除、过期和 supersede 是 Memory 系统的正式能力，不是清理脚本。
6. 派生 Knowledge 必须保留 Source Revision；来源变化后应重新评估可信度，而不是继续显示为 verified。

## 当前结论

Axis 后续 Memory 架构建议采用：

**`Working Context ≠ Handoff Memory ≠ Long-term Knowledge`**。

2026-09-12 的 `llm_wiki` 加速进一步支持把长期 Knowledge 建模为 **source-traceable + incrementally refreshable + reviewable derived asset**。

这一分层目前已经得到连续多类开源项目的独立验证信号，值得作为 [[AxisAgent]] 与 [[Axis Knowledge Vault]] 的长期架构原则继续验证。

关联：[[Agent]] · [[Context Engineering]] · [[Memory]] · [[Agent Capability Packaging]] · [[GitHub Trending — 2026-09-11]] · [[GitHub Trending — 2026-09-12]]
