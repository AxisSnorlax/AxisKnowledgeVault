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

## Agent-native WinUI 开发

截至 2026-09-10，Microsoft 已维护 `microsoft/win-dev-skills`，把 WinUI 3 / Windows App SDK 的开发流程包装为可被 GitHub Copilot、Claude Code 与 OpenAI Codex 使用的 Agent Plugin/Skills。当前仍属于 Preview，应作为**高价值参考基线**，而不是未经验证的项目真源。

值得吸收的工程方式：

1. 把 WinUI 专用开发规则做成可版本化 Skill，而不是只依赖通用 System Prompt。
2. 将 scaffold、design、build、review、UI testing、packaging、migration 拆成独立工作流。
3. 使用 WinApp CLI 让 Agent 能在不依赖 IDE GUI 操作的情况下执行可重复的 Windows 应用工程流程。
4. 使用 Roslyn Analyzer / Metadata 工具把一部分“提示词规则”下沉为机器可验证的门禁。
5. Visual Studio 仍适合 XAML Hot Reload、Live Visual Tree、深层诊断；CLI/Agent 工作流与 VS 不冲突。

### Axis 建议基线

```text
Codex / Agent
     ↓
WinUI Skills + Axis Project Rules
     ↓
WinApp CLI / dotnet / Analyzer
     ↓
Build / Test / UIA / Package
     ↓
真实验收 Gate
```

这比“让 Agent 自由生成 XAML，然后人工看起来差不多”更适合正式项目。

## AxisAgent UI 关注点

- Streaming Event Pipeline 与 UI batching。
- ItemsRepeater / 虚拟化。
- Markdown、CodeBlock、ToolCall、Approval 等消息块组件化。
- 多 Pane 与响应式布局。
- Theme / Fluent / Composition。
- UI 与 Agent Runtime 严格解耦。

关联：[[Desktop UI]] · [[AxisAgent]] · [[WPF]] · [[WinForms]] · [[Avalonia]] · [[Agent Capability Packaging]]
