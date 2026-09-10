---
type: research
status: working-thesis
date: 2026-09-10
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

> 当前结论是基于 2026-09-09 ～ 2026-09-10 的开源项目观察形成的**工作假设**，不是行业正式标准。

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

这比“共享 Prompt 仓库”更接近正式的软件资产治理。

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

因此插件系统不能只停留在“加载 DLL”。

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
   └── Focused Workflow / Behavior Policy
```

## AxisAgent 建议模型

### Skill Manifest

建议最少包含：

- `id`
- `version`
- `name`
- `description`
- `entry/workflow`
- `requiredCapabilities`
- `recommendedTools`
- `compatibility`

Skill 默认不直接表达任意本机代码执行权限。

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
Upgrade / Disable / Remove
```

## 安全原则

1. Plugin 的权限来自 Manifest + Runtime Enforcement，不来自 Prompt 自律。
2. 本机代码、Shell、Filesystem、Browser/Computer、Secrets 属于不同权限域，应可分别批准。
3. MCP Server 连接同样需要来源、能力发现、命名冲突、超时和断线恢复治理。
4. Plugin UI 扩展不应默认与 Runtime 共享完整进程权限。
5. Publisher Verification、Sandbox、Version Compatibility、Session Recovery 应成为正式产品门禁，而不是后补功能。

## 与 Axis Knowledge Vault 的关系

知识库不应无差别保存所有 Agent 会话。建议采用：

```text
Capture → Review → Promote → Recall → Prune / Archive
```

可将 Daily Intelligence 视为 Capture；`20 Technology/` 与 `40 Engineering/` 是 Promote 后的长期知识；项目仓库和正式报告仍是事实第一真源。

## 当前建议

对 [[AxisAgent]]：

- 明确 `Skill / Plugin / Harness` 三层模型。
- Plugin 不与 .NET Assembly 画等号，优先 Manifest-driven。
- 支持声明式 Skill/MCP/Agent/Hook/Asset 组合。
- Runtime 统一执行权限、隔离、生命周期和恢复。
- 等插件机制真正进入产品实现时，再根据真实需求决定是否允许托管 .NET Plugin Assembly。

关联：[[Agent]] · [[Skills]] · [[MCP]] · [[Context Engineering]] · [[Memory]] · [[WinUI]]
