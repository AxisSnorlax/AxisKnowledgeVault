---
type: engineering-standard
status: working-thesis
date: 2026-09-15
topic: deterministic-agent-runtime
tags:
  - agent
  - runtime
  - governance
  - observability
  - security
  - engineering
---

# Deterministic Agent Runtime

## 核心命题

Agent 系统不应把“自然语言指令”当作安全、正确性或完整性的最终保证。

长期工程原则：

> **不能出错的步骤，用确定性代码、状态机、权限和验证器保证；允许探索和动态判断的步骤，再交给 Agent。**

该结论来自 2026-09-13 ～ 2026-09-15 对 Durable Run / Evidence Lineage、`alibaba/open-code-review` 与 GitHub `gh-aw` 官方工程实践的连续观察，并结合 [[AxisAgent]] 当前已有的 Permission / Approval / Tool / Verification / Artifact 边界形成。

## 为什么纯 Prompt 驱动不够

纯语言驱动 Agent 常见风险：

- 漏掉必须处理的文件、对象或步骤；
- 在长任务中自行缩减范围；
- 位置、路径、对象身份漂移；
- Prompt 微调导致结果不稳定；
- 把安全要求当成“建议”而不是不可越过的边界；
- 失败后无法准确恢复到确定状态；
- 无法证明某个结论来自哪次 Tool/MCP 调用和哪份输入。

这些问题不应该靠更长 System Prompt 解决。

## Runtime 分层

```text
Task / Request
  ↓
Deterministic Contract
  ├── Scope Resolution
  ├── Identity / Correlation
  ├── Permission / Approval
  ├── State Transition
  ├── Tool Capability Boundary
  ├── Integrity / Position Mapping
  ├── Verification Gate
  └── Evidence Recording
  ↓
Agent Decision Zone
  ├── Reasoning
  ├── Planning
  ├── Retrieval
  ├── Dynamic Context Selection
  └── Tool Choice within policy
  ↓
Deterministic Execution / Validation
  ↓
Durable Run Record
```

## Deterministic Contract 应负责什么

### Scope / Selection

由代码确定：

- 允许访问哪些 Workspace / Project / File；
- 哪些对象必须被处理；
- 哪些对象被明确过滤；
- 大任务如何切分成稳定 Work Unit。

Agent 可以建议 Scope，但不能静默扩大或缩小授权范围。

### Permission / Approval

Runtime 必须决定：

- read / safe-write / high-risk-write；
- Shell / Filesystem / Browser / Computer / Secrets；
- 是否需要人工批准；
- 批准作用于哪一个具体 Action / Resource / Run。

Prompt 中的“不要执行危险操作”不是权限系统。

### State Transition

Task / Run / Tool Call / Approval / Verification 应有合法状态转换。

例如：

```text
Planned
→ Ready
→ Running
→ WaitingApproval
→ Running
→ Verifying
→ Succeeded / Failed / Cancelled
```

非法跃迁必须由代码拒绝，而不是期待 Agent 自觉遵守。

### Identity / Position Mapping

任何需要精确引用的对象都应保留稳定身份：

- File / Commit / Blob；
- Tool / MCP Server / Tool Name；
- Diff Hunk / Line Mapping；
- Artifact / Verification Result；
- Run / Parent Run / Retry。

不要让模型凭自然语言自行维护精确位置和身份。

### Verification Gate

“Agent 说完成了”不能等于完成。

正式完成应来自可验证证据，例如：

- build / test exit code；
- CI status；
- static analysis；
- runtime smoke；
- hash / signature / integrity；
- UIA / screenshot / hardware gate；
- domain-specific validator。

验证失败必须保持失败，不允许由总结文本覆盖。

## Agent Decision Zone

Agent 最适合承担：

- 需求解释；
- 规划；
- 动态上下文检索；
- 候选方案比较；
- 在授权 Tool 集合中选择下一步；
- 失败原因分析；
- 生成可读解释。

Agent 不应成为：

- 权限判定器；
- Secret Store；
- 完成判定真源；
- Artifact 身份系统；
- 状态一致性机制；
- 安全边界。

## Runtime Observability

2026-09-14 GitHub Agentic Workflows 的官方更新开始在 JSON Logs 中显式记录每次 MCP 调用的 timestamp、server 和 tool，并持续强化 safe-output、threat detection 与 credential handling。

因此 Durable Run 至少建议记录：

- `runId`
- `parentRunId / retryOf`
- `correlationId`
- `timestamp`
- `actor / model / provider`
- `toolKind`
- `mcpServer`
- `toolName`
- `resourceScope`
- `permissionDecision`
- `approvalId`
- `inputDigest`
- `outputDigest`
- `safeOutputStatus`
- `threatCheckStatus`
- `verificationId`
- `artifactIds[]`
- `duration`
- `cost / token usage`（适用时）

日志重点不是“越多越好”，而是能回答：

1. 谁在什么时候做了什么？
2. 使用了哪个 Tool / MCP / Provider？
3. 为什么被允许？
4. 输入输出对应哪一个真实对象？
5. 最终结果由什么证据证明？

## Credential Blast Radius

敏感凭据建议遵守：

- 最小 Scope；
- 最短 Lifetime；
- 不进入 Prompt / Log / Screenshot；
- 不进入持久 Git Config；
- 需要时注入，用完撤销；
- 不因 Plugin/Skill 安装而自动获得；
- Credential Capability 与普通 Tool Capability 分离审计。

GitHub `gh-aw` 将 checkout 改为 `persist-credentials: false` 是一个直接工程信号：**Agent 自动化链路中的凭据暴露窗口本身必须被设计和验证。**

## Supply Chain

本页与 [[Agent Skill Supply Chain]] 互补：

- Supply Chain 解决“输入能力包来自哪里、是否被篡改、是否经过扫描”；
- Deterministic Runtime 解决“即使安装了这个能力，它运行时到底能做什么”。

所以：

> Integrity ≠ Runtime Permission。

## 对 AxisAgent 的映射

[[AxisAgent]] 当前已经具备显式 Permission / Approval、受控 Workspace、Tool、Verification、Artifact 与可恢复历史，这使其适合继续沿 Deterministic Runtime 路线收敛，而不是增加更多 Prompt-based guardrail。

建议后续逐项审计：

- Workspace Scope 是否完全由 Runtime 决定；
- Tool / MCP 调用是否都有稳定 identity；
- Approval 是否绑定具体 action/resource/run；
- Retry 是否保留 lineage；
- Verification 是否独立于 Agent 文本判断；
- Credential 是否有明确 scope/lifetime；
- Browser / Computer 高风险操作是否能追溯到用户授权；
- Run Store 是否能重建关键执行事实而不依赖聊天文本。

## 对专业软件的映射

结合 [[Professional Software Agent Surface]]：

```text
Domain Core
  ↓
Deterministic Automation Contract
  ↓
Permission / Validation
  ↓
MCP / Tool Surface
  ↓
Agent Decision
```

工业、CAD、数据库、SCADA 等软件尤其不应让 LLM 直接绕过 Domain Contract 操作底层状态或硬件。

## 当前结论

Agent 越强，Runtime 越需要弱化“信任模型自己守规则”的假设。

高质量 Agent 系统的方向不是：

```text
更长 Prompt
→ 更聪明模型
→ 希望它别犯错
```

而是：

```text
Deterministic Contract
+ Dynamic Agent Reasoning
+ Observable Execution
+ Independent Verification
```

关联：[[Agent]] · [[AxisAgent]] · [[Agent Skill Supply Chain]] · [[Professional Software Agent Surface]] · [[GitHub Trending — 2026-09-15]]
