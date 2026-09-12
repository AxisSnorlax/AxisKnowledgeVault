---
type: intelligence-index
topic: local-ai
status: active
tags:
  - github
  - local-ai
  - inference
---

# Local AI 趋势索引

## 关注方向

- 本地 LLM / VLM
- llama.cpp / GGUF / CUDA
- 本地语音：ASR / TTS / Voice Clone
- 本地 Agent Runtime
- Embedding / Rerank
- 模型管理与 Provider 抽象
- GPU 资源调度

## 重点观察

- 本地模型是否开始更多采用 Agent/Tool Calling 原生能力
- Windows 下 CUDA / DirectML / ONNX Runtime / llama.cpp 的实际工程表现
- 语音、视觉和桌面 Computer Use 的本地化程度
- 模型管理工具对多 Provider、多模型与配置迁移的支持

## 2026-09-11 变化

### AlexsJones/llmfit

Rust Daily Trending 约 **+247 stars/day**。它把本地模型选择从“看参数量猜能不能跑”推进到硬件画像与可验证推荐：

- 检测 CPU、RAM、GPU/VRAM 与后端；
- 结合参数量、上下文、量化格式估算内存和 tokens/s；
- 按 memory fit、estimated speed、quality、context 评分；
- 提供 JSON / REST API；
- 可通过真实 benchmark 覆盖估算值。

对 [[AxisAIManager]]：值得研究 `Hardware Profile → Model Fit → Estimated Performance → Measured Performance` 数据模型。尤其要显式区分 Estimate 与 Measurement，避免 UI 给出伪精确的性能结论。

### JustVugg/colibri

GitHub Daily Trending 约 **+130 stars/day**，总星约 27k。其核心实验方向是将 VRAM、RAM、NVMe 作为统一的模型权重层级，按 MoE Expert 路由热度进行缓存、预取和分层驻留。

值得关注的不是“超大模型能启动”这一宣传点，而是这些工程问题：

- RAM / VRAM / Storage Budget 统一规划；
- Expert / Weight Residency；
- Storage Bandwidth 对 decode 的影响；
- Prefix/KV reuse；
- 真实吞吐、TTFT、内存、质量共同验证。

对 [[AxisAIManager]]：这属于实验性运行时研究，不应替换当前 llama.cpp 主路径。可以先吸收其硬件诊断与 Memory Tier 思路；只有在目标 Windows GPU 上真实 Benchmark 后才考虑额外 Runtime Adapter。

## 2026-09-12 变化

### AlexsJones/llmfit 加速

Rust Daily Trending 约 **+482 stars/day**，相比昨日知识库记录的 +247/day 明显加速。更重要的是其“真实测量覆盖估算”的闭环已经成为正式能力：

```text
Detect Hardware
  ↓
Estimate Fit / Speed / Memory
  ↓
Launch Benchmark
  ↓
Measure TPS / TTFT / Memory
  ↓
Replace or Calibrate Estimate
  ↓
Persist / Share Result
```

这进一步支持 [[AxisAIManager]] 不应只做静态 Model Catalog。建议未来的数据合同至少区分：

- `EstimatedMemoryBytes`
- `EstimatedTokensPerSecond`
- `MeasuredPeakVramBytes`
- `MeasuredPeakRamBytes`
- `MeasuredTokensPerSecond`
- `MeasuredTimeToFirstToken`
- `BenchmarkRuntime`
- `BenchmarkModelHash`
- `BenchmarkTimestamp`
- `HardwareProfileId`

并保留 benchmark provenance，避免不同 Runtime / Driver / Context / Quantization 的测量结果被误当成可直接比较。

今天没有发现足以替代 llama.cpp 主路径的新 Windows Local AI Runtime。`llmfit` 的价值仍然在 **Capacity Planning + Measurement Feedback**，不是成为推理网关。

## 当前结论

本地 AI 的管理层正在从“进程启动 + 模型列表”走向：

```text
Hardware Profile
  ↓
Fit / Capacity Planning
  ↓
Model + Quantization + Context Recommendation
  ↓
Runtime Launch
  ↓
Measured TPS / TTFT / VRAM / RAM
  ↓
Feedback to Recommendation
```

2026-09-12 的增长再次增强了这一判断。对 Axis 的价值高于继续增加更多静态模型白名单。

参见：[[GitHub Trending — 2026-09-11]] · [[GitHub Trending — 2026-09-12]]

关联：[[Agent]] · [[DotNet]] · [[AxisAgent]] · [[AxisAIManager]]
