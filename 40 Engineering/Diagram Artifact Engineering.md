---
type: engineering-standard
status: working-thesis
date: 2026-10-10
topic: diagram-artifact-engineering
tags:
  - diagram
  - documentation
  - design-system
  - verification
  - engineering
---

# Diagram Artifact Engineering

## 核心命题

工程图表不应把最终 PNG/SVG 当作唯一真源。长期可维护的图表需要同时保留结构事实、可编辑定义、样式系统、渲染产物和验证证据。

推荐模型：

Domain Facts → Editable Structured Source → Design Tokens / Style Contract → Rendered SVG/PNG/HTML → Semantic / Visual / Accessibility Checks → Versioned Evidence

## 为什么需要这样做

仅保存最终图片会导致：

- 无法可靠修改节点、边和约束；
- 难以判断图表是否仍与正式架构、协议、状态机一致；
- 视觉更新容易破坏语义；
- Agent 修改时只能依赖截图猜测；
- 无法稳定复现同一版本的渲染结果。

## 结构真源

根据图表类型，结构真源可以是 Mermaid、Graphviz、PlantUML、JSON/YAML DSL、HTML/SVG 生成源码或项目自定义 Schema。

关键要求不是具体格式，而是：

- 能表达节点、边、方向、状态、约束和分组；
- 能被版本控制；
- 能被程序化检查；
- 渲染结果可以从源码重新生成。

## Design Contract

建议集中管理：

- typography；
- spacing；
- hierarchy；
- stroke / border；
- semantic color token；
- label 规则；
- icon 规则；
- dark/light mode；
- accessibility / contrast。

Design Contract 与 Domain Facts 分离，避免视觉改动篡改结构事实。

## Verification

对高价值工程图，至少检查：

- 节点集合是否与正式源一致；
- 边方向和依赖关系是否正确；
- 状态机是否遗漏合法/非法转换；
- 协议流程是否与实现一致；
- 标签是否截断、重叠或不可读；
- 对比度和缩放是否可接受；
- 渲染工具和版本是否可追溯。

如果图表用于正式验收或架构决策，应保留 source revision、render tool/version、artifact digest 和 verification result。

## 对 Axis 的应用

- [[AFSCADA]]：系统拓扑、Station/Command/Telemetry、状态机、数据流；
- [[AxisProtocolStudio]]：协议帧、解析状态机、设备通信流程；
- [[AxisAgent]]：Runtime、Permission、Verification、Memory、Plugin/Skill 架构；
- [[Axis Knowledge Vault]]：长期技术知识图和研究关系图。

## 当前证据

2026-10-08 ～ 2026-10-10 对 `cathrynlavery/diagram-design` 的连续观察增强了这一方向：图表 Skill 开始将语义图表类型、Style Guide、可复用 Profile 和可重复导出组织为正式资产。

该项目的热度本身不是标准依据；真正长期有效的是“结构真源 + 设计合同 + 可复现渲染 + 验证”这一工程原则。

参见：[[GitHub Trending — 2026-10-08]] · [[GitHub Trending — 2026-10-10]]

关联：[[Agent]] · [[AxisAgent]] · [[Axis Knowledge Vault]]