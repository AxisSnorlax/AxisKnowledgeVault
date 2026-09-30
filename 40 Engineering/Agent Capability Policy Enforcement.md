---
type: engineering-standard
status: working-thesis
date: 2026-09-30
topic: agent-capability-policy-enforcement
tags:
  - agent
  - runtime
  - permission
  - sandbox
  - security
---

# Agent Capability Policy Enforcement

## 定位

本页是 [[Deterministic Agent Runtime]] 的运行时权限子主题，聚焦一个问题：

> **Agent 的权限必须由可执行 Runtime Policy 强制，而不是由 Prompt、Skill 或 UI checkbox 自律。**

2026-09-30 的 `NVIDIA/OpenShell` 趋势进一步验证了这个方向。它把文件、系统调用、网络与凭据访问放入 Runtime Policy，并对高风险 Policy 变化提供 Review/验证路径。

参见：[[GitHub Trending — 2026-09-30]]

## 建议模型

```text
User / Project Policy
  ↓
Capability Resolution
  ↓
Action + Target / Resource
  ↓
Process / Filesystem / Network / Credential Scope
  ↓
Runtime Enforcement
  ↓
Evidence / Audit
```

## 对 [[AxisAgent]] 的约束

Tool Registry 建议逐步拥有：

- `CapabilityId`
- `ActionKind`
- `TargetType / TargetId`
- `WorkspaceScope`
- `ProcessScope`
- `FilesystemScope`
- `NetworkScope`
- `CredentialScope`
- `ApprovalPolicy`
- `PolicyDecision`
- `Evidence / AuditId`

### Credential 单独建模

Credential 不应因为某个 Tool 获准调用就自动可见。更合理的是：

```text
Tool Allowed
  ≠
Credential Visible
```

需要凭据的调用应由 Runtime 在明确 endpoint / action / lifetime 下临时注入，并避免进入普通 Prompt、日志和截图。

## 与已有原则的关系

- [[Deterministic Agent Runtime]]：负责整体确定性合同、状态、验证与审计。
- [[Agent Skill Supply Chain]]：负责 Skill 来源、完整性、扫描、版本与供应链信任。
- 本页：负责“能力已安装之后，运行时到底允许做什么”。

因此：

> **Integrity ≠ Runtime Permission；Skill Instruction ≠ Runtime Enforcement。**

## Windows 边界

OpenShell 当前 Windows 路线以 WSL2 为实验路径，因此它更适合作为 Runtime Policy 的架构证据，而不是直接成为 [[AxisAgent]] Windows 原生 Runtime 的依赖。

AxisAgent 应优先在自身 Windows Runtime / Tool Host 中实现等价的可执行 Scope、Approval、Evidence 与 Credential Boundary。

关联：[[Agent]] · [[AxisAgent]] · [[Deterministic Agent Runtime]] · [[Agent Skill Supply Chain]] · [[GitHub Trending — 2026-09-30]]
