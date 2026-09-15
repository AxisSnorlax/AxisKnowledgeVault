---
type: research
status: working-thesis
date: 2026-09-14
topic: agent-skill-supply-chain
tags:
  - agent
  - skills
  - security
  - supply-chain
  - mcp
  - architecture
---

# Agent Skill Supply Chain

## 研究问题

当 Skill 从本地 `SKILL.md` 演化成可发现、可安装、可更新、跨 Agent 分发的软件资产后，应该如何治理来源、完整性、安全扫描、审计与回滚？

> 当前结论来自 2026-09-09 ～ 2026-09-15 对 `openai/skills`、`vercel-labs/skills`、`Tencent/teamai-cli`、`dotnet/skills`、`Unity-Technologies/skills`、`obra/superpowers`、`github/spec-kit` 与 `tech-leads-club/agent-skills` 的连续观察。它是 Axis 的工作假设，不是行业正式标准。

## 为什么需要独立 Supply-chain 层

Skill 早期可以只是：

```text
Project/.skills/foo/SKILL.md
```

但当前生态已经出现：

```text
Remote Source
  ↓
Discover / Search
  ↓
Resolve Version / Compatibility
  ↓
Verify Source / Integrity / Trust
  ↓
Scan Content
  ↓
Install / Link / Cache
  ↓
Enable under Runtime Governance
  ↓
Audit / Measure
  ↓
Update / Rollback / Remove
```

因此 `Skill Registry` 不应只是目录扫描器，也不应假定“文本文件 = 无安全风险”。Skill 可以影响工具选择、Shell/Browser/Computer 操作、代码修改、依赖安装和完成判定，本质上属于 Agent 的软件供应链输入。

## 关键证据

### vercel-labs/skills

把 Skill 做成跨多种 Agent 客户端的 package lifecycle，支持 Git/GitHub/GitLab/本地/私有来源、Project/Global Scope、install/update/remove，并允许多个 Agent 共享 canonical source。

长期启示：`source / version / scope / compatibility / update` 已经是 Skill 的正式元数据。

### dotnet/skills

除了 curated Skills，还开始观察 activation、not-passed rate、elapsed、token、executor/judge model 等 Skill Value 指标。

长期启示：Skill 不只需要安全治理，还必须可回归、可测量。

### obra/superpowers / github/spec-kit

Skill/Workflow 已经能够强制表达 planning、TDD、debugging、review、verification、completion gate，以及可组合的 workflow bundle。

长期启示：被污染或被错误升级的 Skill 不只是“给错建议”，还可能改变 Agent 的完整执行流程，因此版本锁定与回滚十分重要。

### tech-leads-club/agent-skills

2026-09-14 GitHub Trending 约 +215/day；2026-09-15 上升到约 **+506/day**，继续明显加速。其显式 Supply-chain 设计包括：

- source-only distribution；
- CI static analysis；
- immutable integrity via lockfile/content hashing；
- sanitization；
- path isolation；
- symlink guards；
- atomic lockfile；
- audit trail；
- 发布前 Agent Skill security scan；
- MCP progressive disclosure：先 search/list，再 read/fetch references。

这个项目的重要性不在“它的 Catalog 比别人多”，而在于它把 **Trust / Integrity / Audit** 变成 Skill 分发的一等问题；连续两日加速则说明这一问题正在从小众安全议题进入更广泛的 Agent 工程实践。

## AxisAgent 建议模型

### Skill Source Record

建议至少包含：

- `sourceType` — builtin / git / registry / local / plugin
- `sourceUri`
- `publisher`
- `repository`
- `commitOrVersion`
- `resolvedAt`
- `contentDigest`
- `license`
- `provenance`

### Security / Trust Record

建议至少包含：

- `trustLevel`
- `scanStatus`
- `scanEngine`
- `scanTimestamp`
- `integrityVerified`
- `signatureOrPublisherVerification`（未来）
- `declaredCapabilities`
- `requestedPermissions`
- `riskFlags[]`

### Installation Record

建议至少包含：

- `scope` — project / user / team
- `installMethod` — copy / managed-cache / link
- `installedVersion`
- `lockDigest`
- `installedAt`
- `updatedAt`
- `previousVersion`
- `rollbackAvailable`

### Audit Record

关键事件至少保留：

- discover
- inspect
- scan
- install
- enable
- disable
- update
- rollback
- remove
- integrity-failure
- compatibility-failure

## Progressive Disclosure

Skill Registry 不应把完整 Catalog 和 reference materials 一次性注入 Context。

建议：

```text
Intent
  ↓
Search metadata
  ↓
Select candidate
  ↓
Read primary Skill
  ↓
Fetch only required references/templates
  ↓
Execute under Runtime Permission
```

这同时降低 Token 占用和恶意/无关内容进入 Working Context 的面积。

## 重要安全边界

1. **Integrity ≠ Safety。** Hash 只能证明内容没变，不能证明内容本身安全。
2. **Static Scan ≠ Runtime Permission。** Skill 即使通过扫描，也不能直接获得 Shell、Filesystem、Browser/Computer 或 Secrets 权限。
3. **Prompt Instruction ≠ Security Boundary。** “不要做危险操作”不能替代 Runtime Enforcement。
4. **Publisher Trust ≠ Permanent Trust。** 更新后必须重新解析、扫描和验证完整性。
5. **Project Skill ≠ User Skill。** Project Scope 的供应链风险应被限制在项目边界，不能静默晋升到 Global Scope。
6. **Remote Reference 也是输入。** Skill 引用的模板、脚本、文档和 MCP endpoint 同样需要来源和版本治理。
7. **Rollback 是正式能力。** Workflow Skill 可以改变工程行为，升级失败时必须能回到上一个已验证版本。

## 与 Plugin 的关系

```text
Plugin
  ├── Manifest
  ├── Skills
  ├── Tools / MCP
  ├── Agents
  ├── Hooks
  └── Assets
```

Plugin Supply Chain 是更高一级问题；Skill Supply Chain 可以先独立落地，并共享 Source / Publisher / Integrity / Compatibility / Audit 数据结构。

## 2026-09-15 复验

`tech-leads-club/agent-skills` 从 2026-09-14 记录的约 +215/day 上升到约 +506/day。新增判断不是“Star 更高”，而是以下模型已连续得到验证：

- 安装来源、版本与内容摘要需要被锁定；
- 静态扫描和 Runtime Permission 必须分层；
- 更新后需要重新验证完整性与兼容性；
- Skill Catalog 应使用 progressive disclosure，避免一次性扩大 Context 和攻击面；
- Rollback / Audit 不是附加功能，而是 Workflow Skill 进入正式工程环境后的基本治理能力。

因此本页仍保持 `working-thesis`，但已经不再把 Skill Supply Chain 视为单项目特例。

## 对 Axis 的当前建议

- [[AxisAgent]]：Skill Registry 不再只扫描目录；正式预留 Source/Version/Digest/Trust/Scan/Lock/Audit/Rollback。
- [[Agent Capability Packaging]]：继续负责 Skill / Plugin / Harness 分层，本页只负责 Supply-chain Trust。
- Team/Project Profile：固定 required skill versions 或 commit，避免无人知情的自动漂移。
- 自动更新默认不直接 Enable；先经过 compatibility + integrity + scan，再进入 staged activation。
- 高风险 Skill 应允许组织策略禁止安装，即使来源可验证。
- Skill Quality Metrics 与 Security Metrics 分开：安全不代表有效，有效也不代表安全。

关联：[[Agent Capability Packaging]] · [[Skills]] · [[MCP]] · [[Agent]] · [[AxisAgent]] · [[GitHub Trending — 2026-09-14]] · [[GitHub Trending — 2026-09-15]]
