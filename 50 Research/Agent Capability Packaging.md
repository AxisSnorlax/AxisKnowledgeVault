---
type: research
status: working-thesis
date: 2026-09-10
updated: 2026-09-12
topic: agent-capability-packaging
tags:
  - agent
  - skills
  - plugins
  - harness
  - mcp
  - architecture
---

# Agent Capability Packaging

## 研究问题

Agent 生态中的 `Skill`、`Plugin`、`Harness`、`Team Harness` 应如何区分？它们在 [[AxisAgent]] 中应对应什么边界？

> 当前结论是基于 2026-09-09 ～ 2026-09-12 的开源项目连续观察形成的**工作假设**，不是行业正式标准。

## 观察证据

### openai/plugins

显示 Plugin 正在成为可安装的组合包，而不是单一代码扩展。一个 Plugin 可以同时携带：

- `.codex-plugin/plugin.json`
- `skills/`
- `.mcp.json`
- agents
- commands
- hooks
- assets

这说明 `Skill` 更适合作为 Plugin 内的一个能力单元，而 Plugin 承担分发、版本和组合边界。

### Tencent/teamai-cli

显示团队级 Harness 开始承担：

- Skills / Rules / Docs / Agents / Hooks / MCP 的 Git 分发
- Review / Merge / Pull
- 多 Agent 客户端适配
- 会话摩擦信号驱动的知识 Capture
- Recall
- Promote
- Maintenance / Prune

这比“共享 Prompt 仓库”更接近正式的软件资产治理。2026-09-11 其 Daily Trending 增速继续上升，增强了这一信号的持续性。

### vercel-labs/skills

2026-09-11 新增的重要证据。该工具已经把 Agent Skill 做成跨客户端的包管理生命周期：

- 支持 OpenCode、Claude Code、Codex、Cursor 等 75+ Agent；
- Source 可来自 GitHub、GitLab、任意 Git URL、本地路径和私有仓库；
- 支持 Project / Global Scope；
- 支持 `add / use / list / find / update / remove / init`；
- 可使用 canonical copy + symlink 让多个 Agent 共享单一 Skill 真源；
- 能读取部分 Plugin Manifest 中声明的 Skills。

这意味着 Skill Registry 不应只解决“如何找到 SKILL.md”，还应处理 Source、Version、Scope、Update、Removal、Compatibility、Integrity 与团队共享。

### affaan-m/ECC

显示 Skills 已成为 Agent Harness 中的重要工作流表面，同时安全扫描、Memory/Instinct、持续学习等能力仍由更高层 Harness 统一处理。

### microsoft/win-dev-skills

显示专业领域本身也可以被包装为 Agent Skills：WinUI scaffold、设计、Code Review、UI Testing、Packaging、Migration 等均可形成独立、可版本化工作流。

### vastsa/PI-Desktop

显示真正的 Agent Desktop 产品会进一步要求：

- Permission Boundary
- Filesystem / Secrets Ownership
- Plugin / Marketplace
- MCP / Skills / Subagents
- Context Checkpoint
- Session Recovery
- Plugin Sandboxing / Publisher Verification

2026-09-11 Daily Trending 增速较前一日继续上升，因此“Agent Desktop 是正式产品类别”的信号增强。

### obra/superpowers

2026-09-12 的新增证据。该项目将 brainstorming、writing plans、TDD、systematic debugging、parallel subagents、code review、git worktrees、verification-before-completion 等工程方法做成必须遵循的 Skills / Workflows。

这说明 Skill 的作用已经不只是：

```text
“告诉模型一些领域知识”
```

而开始变成：

```text
Precondition
  ↓
Required Workflow
  ↓
Allowed / Recommended Tools
  ↓
Required Verification
  ↓
Evidence
  ↓
Completion Gate
```

因此 Axis 的 Skill 模型需要区分：

- Knowledge Skill
- Workflow Skill
- Behavior / Policy Skill
- Verification Skill

但这些 Skill 都不能绕过 Runtime Permission。

### github/spec-kit

2026-09-12 的重要证据。它把 specification、planning、tasks、clarify、analyze、checklist 等 Agent 工程流程组织为可复用工作流，同时出现 Extensions、Presets、Bundles 与版本/安装策略。

这进一步表明：**工程流程本身正在成为可版本化、可组合的软件资产**。一个项目不一定需要把所有规则永久堆进 `AGENTS.md`；可以由 Project Profile 选择并固定特定 workflow bundle。

对 Axis 的启示：

```text
Project Profile
  ├── Required Skills
  ├── Required Plugins
  ├── Workflow Bundle
  ├── Verification Policy
  └── Version Pins
```

### Unity-Technologies/skills

Unity 官方开始把专业工作流发布为跨 Agent Skills。结合此前 `unity-mcp` 的持续增长，可以形成更完整的领域软件模型：

```text
Domain Knowledge / Workflow
      ↓
Domain Skills
      ↓
Controlled Tool / MCP Surface
      ↓
Professional Application
```

对 [[AFSCADA]]、[[AxisProtocolStudio]] 等产品尤其重要：AI 能力不应等价于把 Prompt 写进 ViewModel，而应通过正式 Domain Skill 和 Tool Contract 暴露。

### dotnet/skills

.NET 团队已经把 LSP、performance diagnostics、MSBuild、NuGet、upgrade、AI/RAG/MCP、testing、ASP.NET Core、Blazor 等组织为 curated plugins / skills。

更值得注意的是它提供 Skill Value dashboard，观察：

- token use
- elapsed time
- activation
- not-passed rate
- executor model
- judge model

这说明 Skill 也需要正式质量度量，而不是“能安装就算完成”。Axis 可借鉴的指标包括：

- Activation Precision / Recall
- Success / Not-Passed Rate
- Median / P95 Duration
- Token Cost
- Tool Error Rate
- Verification Pass Rate
- Version Regression

## 建议分层

```text
Team Harness
   │
   ├── Distribution / Review
   ├── Shared Knowledge
   ├── Recall / Promote / Prune
   │
   ▼
Harness / Runtime
   │
   ├── Permission / Approval
   ├── Context / Memory
   ├── Tool / MCP Lifecycle
   ├── Recovery / Verification
   │
   ▼
Plugin
   │
   ├── Skills
   ├── Tools / MCP
   ├── Agents
   ├── Hooks
   ├── Assets
   └── Metadata / Permissions
   │
   ▼
Skill
   └── Focused Workflow / Behavior / Verification Policy
```

**Skill Distribution / Package Management 是横切层，不应被误建模为另一种 Skill。** 它负责 Source、Install、Scope、Version、Update、Integrity 和兼容性，并同时服务 Project、User 和 Team Harness。

## AxisAgent 建议模型

### Skill Manifest

建议最少包含：

- `id`
- `version`
- `name`
- `description`
- `entry/workflow`
- `source`
- `scope`
- `kind`（knowledge / workflow / behavior / verification）
- `requiredCapabilities`
- `recommendedTools`
- `preconditions`
- `requiredChecks`
- `completionEvidence`
- `compatibility`
- `integrity`（远程分发时）

Skill 默认不直接表达任意本机代码执行权限。

### Skill 生命周期

```text
Discover Source
  ↓
Inspect Metadata
  ↓
Resolve Compatibility
  ↓
Verify Integrity / Trust
  ↓
Install to Project or User Scope
  ↓
Enable under Harness Governance
  ↓
Observe Quality Metrics
  ↓
Check / Update
  ↓
Disable / Remove
```

### Plugin Manifest

建议最少包含：

- `id`
- `version`
- `publisher`
- `displayName`
- `skills[]`
- `tools[]` / `mcpServers[]`
- `agents[]`
- `hooks[]`
- `assets[]`
- `permissions[]`
- `compatibility`
- `uiMetadata`（可选）
- `signature/publisherVerification`（未来正式分发）

### Plugin 生命周期

```text
Discover
  ↓
Inspect Manifest
  ↓
Verify Publisher / Integrity
  ↓
Resolve Compatibility
  ↓
Show Permissions
  ↓
Install
  ↓
Enable
  ↓
Run under Harness Governance
  ↓
Measure / Verify
  ↓
Upgrade / Disable / Remove
```

## 安全原则

1. Plugin 的权限来自 Manifest + Runtime Enforcement，不来自 Prompt 自律。
2. 本机代码、Shell、Filesystem、Browser/Computer、Secrets 属于不同权限域，应可分别批准。
3. MCP Server 连接同样需要来源、能力发现、命名冲突、超时和断线恢复治理。
4. Plugin UI 扩展不应默认与 Runtime 共享完整进程权限。
5. Publisher Verification、Sandbox、Version Compatibility、Session Recovery 应成为正式产品门禁，而不是后补功能。
6. 来自 Git/URL/私有仓库的 Skill 也属于供应链输入，应保留 Source、版本/提交、完整性与更新记录。
7. Skill 声明的 workflow/check 不是安全边界；Runtime 仍必须独立执行权限和危险操作确认。
8. Skill 的“效果”必须可回归，不能仅靠 README 或模型主观判断。

## 与 Axis Knowledge Vault 的关系

知识库不应无差别保存所有 Agent 会话。建议采用：

```text
Capture → Review → Promote → Recall → Prune / Archive
```

可将 Daily Intelligence 视为 Capture；`20 Technology/` 与 `40 Engineering/` 是 Promote 后的长期知识；项目仓库和正式报告仍是事实第一真源。

Memory 与 Knowledge 的更细分边界见 [[Agent Memory and Knowledge Lifecycle]]。

## 当前建议

对 [[AxisAgent]]：

- 明确 `Skill / Plugin / Harness` 三层模型。
- 给 Skill 增加正式的 Source / Scope / Version / Update 生命周期，而不是只扫描目录。
- 把 Skill 从“静态说明文件”升级为可声明 workflow、precondition、required checks、completion evidence 的能力单元。
- 给 Skill/Plugin 增加 activation、success、duration、token、verification 和版本回归指标。
- Plugin 不与 .NET Assembly 画等号，优先 Manifest-driven。
- 支持声明式 Skill/MCP/Agent/Hook/Asset 组合。
- Runtime 统一执行权限、隔离、生命周期和恢复。
- 等插件机制真正进入产品实现时，再根据真实需求决定是否允许托管 .NET Plugin Assembly。

关联：[[Agent]] · [[Skills]] · [[MCP]] · [[Context Engineering]] · [[Memory]] · [[WinUI]] · [[GitHub Trending — 2026-09-11]] · [[GitHub Trending — 2026-09-12]]
