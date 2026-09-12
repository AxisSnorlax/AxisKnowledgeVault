---
type: technology-index
topic: desktop-ui
status: active
tags:
  - desktop
  - dotnet
  - windows
---

# Desktop UI

## 四条主要路线

### [[WinForms]]

- 优势：启动快、资源占用低、Designer 成熟、Win32 集成直接。
- 适合：工业采集、仪器控制、参数配置、传统业务桌面工具。
- 弱项：复杂视觉、动画、现代 Fluent 体验需要较多自定义工作。

### [[WPF]]

- 优势：成熟 XAML、Binding、Template、MVVM、复杂桌面生态。
- 适合：大型专业 Windows 桌面应用、复杂工作台、IDE 型应用。
- 特点：GPU 加速、成熟度高、设计工具完整。

### [[WinUI]]

- 优势：Windows App SDK、Fluent、Mica/Acrylic、Composition、现代 Windowing。
- 适合：Windows-only 现代桌面应用、Agent、消费者级桌面软件。
- 当前限制：传统 XAML Designer 仍弱于 WinForms/WPF。

### [[Avalonia]]

- 优势：跨平台、现代 XAML、Skia/GPU、WPF 思维迁移成本较低。
- 适合：Windows/Linux/macOS 共用桌面产品。
- 取舍：纯 Windows 项目需衡量平台抽象带来的额外复杂度。

## Axis 项目选择原则

- 工业/采集/配置工具：优先 [[WinForms]] 或 [[WPF]]。
- Windows-only 现代 Agent：优先评估 [[WinUI]]，但不得只凭框架宣传决定迁移。
- 明确跨平台：优先 [[Avalonia]]。
- IDE/复杂 Docking/专业工作台：重新评估 [[WPF]]。
- Rich Content / Markdown / Diff / Terminal 占比很高的 Agent 产品：允许把 Web/Hybrid 纳入同机 Benchmark，而不是预设“纯 XAML 一定更优”。

## 2026-09-12：Rust Native / GPUI 观察

Rust Weekly Trending 中 `longbridge/gpui-kit` 约 **+486 stars/week**。它提供 60+ 桌面组件，并明确分离 behavior/infrastructure 与 presentation/application；项目还强调 GPU UI、Markdown/HTML/syntax/chart 与扩展能力，并已用于商业产品。

这不是“Axis 应该从 C# 改成 Rust”的结论。它更适合作为 [[AxisAgent]] UI Framework Qualification 的**生态外基准样本**：

- 原生组件体系如何组织 Design System；
- 高密度桌面工作台如何减少模板/样式层级；
- Markdown / HTML / Syntax / Chart 如何进入原生 UI；
- GPU 渲染、滚动、动画、文本布局如何做真实 Benchmark；
- Behavior 与 Presentation 是否可以保持更清楚的边界。

项目自身的高帧率数字属于上游声明，不能直接作为框架性能结论。

同日两个 Agent/Knowledge Desktop 也提供了相反方向的现实样本：

- `vastsa/PI-Desktop`：React Renderer + Electron Main + Rust Privileged Host + Agent Sidecar；
- `nashsu/llm_wiki`：Tauri v2 Rust Backend + React/TypeScript/Vite，并将本地 Knowledge/MCP 能力置于后端。

这再次说明桌面框架选择应拆成两个问题：

```text
Product Runtime / Security Boundary
          ≠
UI Rendering / Styling Technology
```

对于 [[AxisAgent]]，无论 Avalonia、WinUI、WPF、WebView2/Hybrid 还是研究型 Rust UI，迁移决策都必须通过同一机器、同一页面、同一数据量的 Qualification：

- Cold / Warm Start
- Working Set / Private Bytes
- Idle CPU / GPU
- Streaming Update Cost
- 1000+ Message Scroll
- Rich Content / Diff / Terminal
- DPI / Windowing
- NativeAOT / Packaging（适用时）
- 达到同一设计稿的实现耗时与样式代码量

参见：[[GitHub Trending — 2026-09-12]]

关联：[[AxisAgent]] · [[AFSCADA]] · [[AxisAIManager]] · [[Avalonia]] · [[WinUI]]
