---
type: technology
topic: winui
status: active
tags:
  - winui
  - windows-app-sdk
  - xaml
  - desktop
---

# WinUI

## 定位

WinUI 3 是当前现代 Windows 桌面 UI 的主要原生路线之一，适合 Windows-only、Fluent、动画、Composition、高 DPI 与现代 Windowing 场景。

## 适合 Axis 的场景

- [[AxisAgent]] 这类现代 Windows Agent Desktop。
- 需要 Mica/Acrylic、NavigationView、AppWindow、现代 TitleBar 的应用。
- 对 Browser/Computer/Files/Terminal 等动态工作流进行现代化呈现。

## 不应误解

- WinUI 并不意味着所有场景都比 [[WinForms]] 更快。
- 简单表单、资源占用与 Designer 效率方面，WinForms 仍然很强。
- 复杂专业工作台如果高度依赖成熟 Docking/Template/生态，需要与 [[WPF]] 重新比较。

## 学习主线

XAML → Grid/Layout → Controls → Resources/Styles → Binding/x:Bind → MVVM → Navigation → Windowing → Composition。

## AxisAgent UI 关注点

- Streaming Event Pipeline 与 UI batching。
- ItemsRepeater / 虚拟化。
- Markdown、CodeBlock、ToolCall、Approval 等消息块组件化。
- 多 Pane 与响应式布局。
- Theme / Fluent / Composition。
- UI 与 Agent Runtime 严格解耦。

关联：[[Desktop UI]] · [[AxisAgent]] · [[WPF]] · [[WinForms]] · [[Avalonia]]
