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
- Windows-only 现代 Agent：优先评估 [[WinUI]]。
- 明确跨平台：优先 [[Avalonia]]。
- IDE/复杂 Docking/专业工作台：重新评估 [[WPF]]。

关联：[[AxisAgent]] · [[AFSCADA]] · [[AxisAIManager]]
