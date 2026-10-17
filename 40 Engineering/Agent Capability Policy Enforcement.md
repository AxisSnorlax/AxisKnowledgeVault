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

## 2026-10-09：Windows-native Execution Sandbox 候选

2026-10-07 Microsoft Execution Containers（MXC）GA，并提供正式 .NET SDK。这个信号更新了本页此前“Windows 原生 Runtime 主要需要 AxisAgent 自行实现”的判断。

新的推荐分层：

Capability / Approval Policy → Execution Sandbox Adapter → OS-native containment backend → Tool / Process execution → Evidence / Audit

其中：

- Capability / Approval 决定**允许什么**；
- Sandbox Adapter 负责**在运行时真正限制什么**；
- Verification Plane 负责**证明实际发生了什么以及结果是否正确**。

### MXC 资格边界

MXC 只能先作为候选，不直接视为已通过：

- 目标 Windows Build / patch 必须真实探测；
- backend capability 必须按机器检测；
- 文件系统、网络、GUI/Clipboard 等拒绝策略必须在目标机实测；
- backend 不可用或失败时必须验证 fail-closed，不允许静默扩大权限；
- 需要覆盖 cancellation、timeout、crash cleanup、persistent lifecycle、并发与 x64/ARM64；
- NativeAOT/自包含发布也必须单独验证。

长期原则更新为：Agent Policy 不应自己承担 OS Sandbox 的全部职责；当平台已有可验证的原生隔离能力时，应通过 Adapter 接入，同时保留 AxisAgent 自身 Permission / Approval / Audit Contract。

参见：[[GitHub Trending — 2026-10-09]] · [[DotNet]] · [[Agent Verification and Audit Plane]]

## 2026-10-12：Hook / Proxy Coverage 不是 Sandbox

`hashgraph-online/hol-guard` 进一步强调：Agent Hook、MCP Proxy 或 Tool Allowlist 可以成为 Runtime Policy 的执行点，但它们的安全强度取决于实际覆盖范围。

因此 AxisAgent 的 Policy Engine 应记录：

- enforcement point；
- covered harness / transport / tool kind；
- uncovered paths / bypass risk；
- approval mode；
- sandbox backend；
- audit receipt / evidence id。

原则：**Hook / Proxy / Tool Filtering ≠ OS Sandbox。** 当某类 Tool 无可靠拦截点时，应 fail-closed 或降级为只读/人工批准，而不是默认放行。

参见：[[GitHub Trending — 2026-10-12]] · [[Agent Skill Supply Chain]]

<!-- trend-watch:2026-10-17-launch-policy:begin -->
## 2026-10-17：应用负责的参数与实际启动配置

[Llama-Windows v0.12.0 发布说明](https://github.com/ggml-org/Llama-Windows/releases/tag/v0.12.0) 提供了一个具体案例：自定义启动参数可能改变应用已经决定的网络与凭据设置。这里提炼为 Axis 的设计建议，尚未进行独立实测。

- 将用户可调性能选项与 Policy 管理的安全选项分开；后者不接受自由文本覆盖。
- 配置保存与进程启动都检查最终有效配置，记录经过脱敏的执行证据。
- 绑定地址失效、身份不匹配或更新完整性不可验证时，保留可诊断的拒绝/回退结果，不静默扩大权限。
- 明确这些检查只覆盖启动与配置路径，不能替代 OS Sandbox 或运行中的资源权限验证。

参见：[[30 Intelligence/GitHub/Daily/2026-10-17|GitHub Trending — 2026-10-17]] · [[30 Intelligence/GitHub/Local-AI|Local-AI 趋势索引]] · [[Agent Verification and Audit Plane]]
<!-- trend-watch:2026-10-17-launch-policy:end -->
