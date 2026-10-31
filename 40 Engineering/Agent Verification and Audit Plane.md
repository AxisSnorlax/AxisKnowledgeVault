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

## 2026-10-09：Coverage 与 No-findings 边界

openai/codex-security 与 2026-10-08 的 Cloudflare security audit skill 形成连续证据：Verification Plane 不能只记录“发现了什么”，还必须记录**检查了什么、没有检查什么，以及证据覆盖范围**。

建议 Verification Result 继续增加：scope、coverage、coverageGaps、sourceRevision、findingStatus、severity、evidenceArtifacts、sarifArtifact、threatModelRef。

关键原则：**No findings ≠ Safe；No findings ≠ PASS。**

安全扫描无发现，只能说明在当前 scope、工具、模型与 coverage 下未发现问题。最终 PASS 仍需结合 Build/Test、静态分析、运行时验证、权限边界和必要的人工/独立检查。

参见：[[GitHub Trending — 2026-10-09]] · [[Deterministic Agent Runtime]]

## 2026-10-12：Verification Receipt 与语义真实性

近期 Memory/Agent 项目开始强调 signed receipt、independent judging 和可重算 Artifact。对 Verification Plane 的补充原则是：

- receipt 证明某次检查发生过、输入/输出未被篡改或某主体签署过；
- deterministic check 证明某个明确 invariant 是否满足；
- independent reviewer 降低单一执行者确认偏差；
- **以上任何一项单独存在，都不能自动证明复杂语义结论正确。**

高价值 PASS 应组合 Source Revision + Deterministic Check + Evidence Artifact + Coverage + Reviewer/Verifier，并保留 unresolved / conflict / needs-validation 状态。

参见：[[GitHub Trending — 2026-10-12]] · [[Agent Memory and Knowledge Lifecycle]]

## 2026-10-15：Judge Independence 与 Evidence Sufficiency

`ifixai-ai/iFixAi` 进一步确认：Verification 需要区分被测对象、Judge 与最终确定性门禁。

建议 Verification Result 增加：

- `fixtureRevision`
- `judgeProvider`
- `judgeModel`
- `judgeIndependence`
- `coverage` / `coverageGaps`
- `insufficientEvidence`
- `evidenceArtifacts[]`

关键原则：

- Self-judged 结果与 Independent Judge 结果必须显式区分；
- `insufficient_evidence` 应作为正式状态，不应强迫输出 PASS/FAIL；
- 模型评分只能作为证据的一部分，不能覆盖 Build/Test/E2E、静态分析、Runtime Sandbox、UIA/Hardware Gate 等确定性结果；
- Fixture、Source Revision、Judge 配置与原始 Evidence 必须可追溯，否则不同运行之间无法比较。

参见：[[GitHub Trending — 2026-10-15]] · [[Deterministic Agent Runtime]]

<!-- trend-watch:2026-10-22-graph-evidence:begin -->
## 2026-10-22：图关系来源与提取覆盖

[Graphify README](https://github.com/Graphify-Labs/graphify) 对显式提取与解析推断关系的区分，以及 [v0.9.93](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.93) 的提取器/缓存修复，为证据合同提供新样本。以下是 Axis 工作假设，本轮未运行该工具。

- 关系证据保留来源位置、源码版本、提取器/schema 版本及产生方式；静态解析和实际运行观测分别标记。
- `EXTRACTED` 不代表完整语义覆盖，`INFERRED` 不必然代表模型猜测；必须记录实际生成机制及未覆盖范围。
- 提取失败、文件只读了一部分、引用无法解析时保留缺口，不能把“未找到关系”直接解释成“关系不存在”。
- 验收仍回到源码、构建或运行证据，图是可重建的查询与追溯层。

参见：[[30 Intelligence/GitHub/Daily/2026-10-22|GitHub Trending — 2026-10-22]] · [[Agent Memory and Knowledge Lifecycle]] · [[AxisAgent]]
<!-- trend-watch:2026-10-22-graph-evidence:end -->

<!-- trend-watch:2026-10-31-browser-observation:begin -->
## 2026-10-31：浏览器观测后端与渲染证据

[Lightpanda 当前 README](https://github.com/lightpanda-io/browser) 区分无图形渲染引擎的自动化能力与文本型 PNG/PDF 输出；[1.0.2 发行说明](https://github.com/lightpanda-io/browser/releases/tag/1.0.2) 列出坐标、事件与协议行为修复。以下为 Axis 的设计推论，本轮未运行该浏览器。

- 验证记录包含观测引擎及版本、平台、渲染模式、目标页面/输入版本与已覆盖行为。
- DOM/文本内容正确不自动证明视觉布局正确；文本型图片不能当作完整图形渲染的截图。
- 协议连接成功与网页行为兼容分开；需要真实布局、输入命中或字体表现的检查，使用具备相应能力的后端并保留结果。
- 无法提供所需观测时记录 coverage gap 或 insufficient evidence，不能以替代格式生成成功给出视觉 PASS。

参见：[[30 Intelligence/GitHub/Daily/2026-10-31|GitHub Trending — 2026-10-31]] · [[AxisAgent]] · [[Deterministic Agent Runtime]]
<!-- trend-watch:2026-10-31-browser-observation:end -->
