---
type: engineering-standard
status: working-thesis
date: 2026-10-08
topic: agent-verification-audit
tags:
  - agent
  - verification
  - audit
  - evidence
  - governance
---

# Agent Verification and Audit Plane

## 核心命题

Agent 的**安全执行**与**正确完成**是两个不同问题。

- Permission / Sandbox / Capability Policy 回答：这个动作能不能做。
- Verification / Audit 回答：这个动作是否真的完成、结果是否正确、证据是否充分。

因此 Verification 不应只是 Agent Runtime 的一个布尔字段，而应逐渐形成独立 Plane。

## 推荐模型

Task / Intent → Capability / Permission Policy → Execution → Candidate Result → Independent Verification Plane → Verified Result → PASS / REJECTED / NEEDS_VALIDATION

Independent Verification Plane 包括：Adversarial Reviewer、Deterministic Validator、Build/Test/Static Analysis、Runtime/UI/Hardware Check、Evidence Collection。

## 为什么要独立

“Agent 说完成了”不能成为完成真源。即使 Agent 没有越权，也可能漏掉范围、错误理解需求、产生表面通过但实际无效的修改、忽略失败日志、对自己的结论产生确认偏差，或在不同 Harness/Model 下表现不一致。

因此执行者与验证者最好在角色、上下文和工具权限上保持一定隔离。

## Independent Reviewer

独立 Reviewer 的目标不是重复执行，而是主动寻找反例：

- 是否存在遗漏路径？
- 是否有测试未覆盖？
- 是否有边界条件失败？
- 是否有证据与结论不一致？
- 是否有新的回归？
- 是否只修改了表面症状？

Reviewer 的输出应是候选意见，不直接等价于 PASS。

## Deterministic Verification

最终 PASS 应绑定可重复证据，例如 Build exit code、Unit/Integration/E2E、Static Analysis、Security Scan、Runtime Smoke、UIA/Visual Regression、Performance Benchmark、Protocol/Database/Hardware Validator、Hash/Signature/Artifact Integrity。

对工业系统，真实硬件门禁仍应独立保留。

## Evidence Contract

建议 Verification Result 至少包含 verificationId、runId、candidateRunId、producer、reviewer、verificationKind、sourceRevision、artifactIds、evidenceDigest、counterexamples、deterministicChecks、verdict、timestamp。

## 与 Deterministic Runtime 的关系

[[Deterministic Agent Runtime]] 定义不可越过的执行边界；本页定义结果如何被独立确认。

Deterministic Runtime 控制 what may happen；Verification Plane 证明 what actually happened and whether it is correct。二者都不应由 Prompt 替代。

## 对 AxisAgent 的映射

建议后续审计：

- Verification 是否与 Agent 文本总结解耦；
- Reviewer 是否能访问原始 Evidence 而不是只看摘要；
- PASS 是否必须依赖确定性门禁；
- Retry 是否关联原 Verification；
- Artifact / Log / Screenshot 是否可追溯；
- 高风险操作是否需要第二验证来源；
- UI / Browser / Computer Use 是否同时保留结构化状态和视觉证据。

## 当前来源

该长期判断由 [[Deterministic Agent Runtime]]、2026-09 的 Durable Run / Evidence Lineage 连续观察，以及 2026-10-08 的 cloudflare/security-audit-skill 信号共同支持。

关联：[[Agent]] · [[AxisAgent]] · [[GitHub Trending — 2026-10-08]]