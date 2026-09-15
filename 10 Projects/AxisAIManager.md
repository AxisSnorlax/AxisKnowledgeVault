---
type: project
project: AxisAIManager
status: active
platform: Windows
repository: AxisSnorlax/AxisAIManager
tags:
  - axis
  - local-ai
  - winforms
  - dotnet
---

# AxisAIManager

Axis.LocalAIManager 是本地 AI 基础设施控制面，基于 .NET 10、Windows Forms 与 AntdUI，管理 llama.cpp 推理/嵌入、ComfyUI、Docker Desktop、Qdrant 与模型配置。

> 项目仓库与正式文档仍是实现事实第一真源；本页只做聚合与研究候选记录。

## 与 AxisAgent 的边界

- Manager：模型配置、模型切换、进程所有权、健康检查、推理/嵌入/Qdrant 生命周期。
- [[AxisAgent]]：会话、Provider、RAG、MCP、插件与 Agent 工作流。
- Manager 不承载 Agent 会话和路由，不建设第二套 OpenAI Gateway。
- AxisAgent 通过本机控制接口发起模型切换，成功后直接调用 llama-server。

## 当前重要实现

- `POST http://127.0.0.1:8181/api/v1/models/switch`
- 控制接口仅监听回环地址。
- Windows Credential Manager 保存控制令牌。
- general / coder / vision 模型目录。
- Qdrant 非破坏性生命周期管理。
- ComfyUI 本地管理。
- Docker Engine 健康检查。
- 原子配置、运行缓存和脱敏日志。

## 研究候选（未实现事实）

### Hardware Fit / Measured Performance

2026-09-11 的 [[Local-AI]] 趋势中，`AlexsJones/llmfit` 提供了值得验证的模式；2026-09-12 其 Daily Trending 由知识库前一日记录的约 +247/day 上升到约 +482/day，并继续强化“真实 benchmark 覆盖 estimate”的闭环：

```text
Hardware Profile
  ↓
Model / Quantization / Context Fit
  ↓
Estimated TPS / Memory
  ↓
Real Benchmark
  ↓
Measured Result overrides / calibrates Estimate
```

如果未来进入实现，建议 AxisAIManager 只承担**本地硬件与 Runtime 能力诊断**，不扩张为 Agent Provider Gateway。候选字段包括：

- CPU / RAM / GPU / VRAM / backend；
- Model / Quantization / Context；
- Estimated memory / TPS；
- Measured TPS / TTFT；
- Measured peak RAM / VRAM；
- Runtime / driver / model hash；
- 数据来源与测量时间；
- Estimate / Measurement 明确状态。

测量结果必须保存 provenance。不同 Runtime、Driver、Context、Quantization 或模型文件哈希下的 benchmark 不能无条件横向比较。

### Memory Tier Diagnostics

`JustVugg/colibri` 的 VRAM / RAM / NVMe 分层权重与硬件规划属于实验性研究。2026-09-14 其 GitHub Trending 约 +960/day，相比知识库 2026-09-11 记录的约 +130/day 显著加速；2026-09-15 又升至约 **+2,233/day**，并进一步强化“所有优化都要用端到端 A/B 证明”的研究原则。

当前仍只值得吸收其 **Memory Tier、Storage Bandwidth、Residency、KV/Prefix Reuse 与实验验证方法**，不构成替换 llama.cpp 的理由。任何 Runtime Adapter 都必须在真实 Windows 目标硬件上通过可重复 benchmark 后再进入产品范围。

未来 Hardware Profile / Benchmark Provenance 候选可增加：

- Storage Tier / Device；
- Sequential / Random Read Bandwidth；
- Model Placement；
- Weight / Expert Residency Budget；
- Runtime Tune Profile；
- Runtime Commit / Version；
- Exact Launch Arguments；
- Cache State；
- Prompt / Workload Profile；
- Quality / Correctness Check；
- Raw Log / Artifact Reference；
- Baseline Run / Changed Variable；
- Tune / Benchmark Provenance。

这些字段应与静态硬件枚举分开，明确哪些是检测值、估算值和实测值。

建议长期遵守：

> **Microbenchmark 不能替代端到端资格；性能优化不能静默改变模型精度、路由语义或验证质量。**

### Multi-modal Engine / Capability Registry

2026-09-14 的 [[Local-AI]] 趋势中，`debpalash/VoiceStudio` 展示了一个值得研究的控制面模型：同一桌面产品管理多个 TTS / ASR Engine、Model Catalogue、GPU Backend、Remote Worker、Health/Diagnostics、OpenAI-compatible local API、MCP 与 Agent Skills。

这**不代表 AxisAIManager 当前已经支持这些能力，也不意味着下一版必须扩大产品范围**。它只提供一个未来边界参考：如果 Axis 需要把 ASR、TTS、VLM、图像生成等能力纳入本地控制面，应避免为每种模态重复建立一套互不兼容的生命周期管理代码。

候选抽象：

```text
Capability
  ├── chat
  ├── embedding
  ├── vision
  ├── tts
  ├── asr
  └── image
       ↓
Engine Adapter
       ↓
Model
       ↓
Device / Backend
       ↓
Health / Availability
       ↓
Route / Local Endpoint
```

候选数据至少应考虑：

- `CapabilityKind`
- `EngineId / EngineVersion`
- `ModelId / ModelHash`
- `Device / Backend`
- `Health / Availability`
- `LocalEndpoint`
- `RemoteWorker`（可选）
- `Source`
- `License`
- `Redistribution / CommercialUse` 元数据

尤其要把**应用许可证**与**模型权重许可证**分开记录，不能因为管理器或 Engine 开源就推断模型可自由分发或商用。

如果未来实现，对 [[AxisAgent]] 暴露的仍应是稳定的本地 Provider / Capability Contract，而不是让 Agent Runtime 直接依赖每个 ASR/TTS/VLM 厂商 SDK。

## 长期定位

它应该保持“Local AI Control Plane”而不是扩张成 Agent 平台。未来即使增加多模态 Engine，也应继续遵守：Manager 管基础设施、模型与运行时生命周期；[[AxisAgent]] 管会话、决策、工具、Memory、MCP 和 Agent Workflow。

关联：[[AxisAgent]] · [[Local-AI]] · [[WinForms]] · [[DotNet]] · [[GitHub Trending — 2026-09-11]] · [[GitHub Trending — 2026-09-12]] · [[GitHub Trending — 2026-09-14]] · [[GitHub Trending — 2026-09-15]]
