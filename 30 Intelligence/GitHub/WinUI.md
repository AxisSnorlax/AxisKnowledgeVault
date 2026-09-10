---
type: intelligence-index
topic: winui
status: active
tags:
  - github
  - winui
  - windows-app-sdk
  - desktop
---

# WinUI 3 趋势索引

## 关注方向

- Windows App SDK
- WinUI 3 框架与控件
- XAML tooling / designer / preview
- Fluent / Mica / Acrylic / Composition
- Windowing / App Lifecycle / Notifications
- .NET 10 Desktop
- WinUI + Agent Desktop

## 对 AxisAgent 的关注点

- 高性能 Streaming UI
- ItemsRepeater / 虚拟化
- Markdown / CodeBlock / ToolCall 组件化
- 多 Pane 与 NavigationView
- Composition 动画
- Window / AppWindow 管理
- 与 Windows 原生能力集成

## 2026-09-10 变化

`microsoft/win-dev-skills` 值得提升为 WinUI Agent 开发的一线参考源。它由 Microsoft 官方维护，以 Agent Plugins 1.0 形式面向 GitHub Copilot、Claude Code 与 OpenAI Codex 提供 WinUI 3 / Windows App SDK 专用能力，覆盖：

- WinUI 开发工作流
- Fluent / Mica 设计
- Code Review
- UI 自动化测试
- Packaging
- WPF → WinUI Migration
- Session Report
- 开发环境 Setup

同时配套 WinApp CLI、Roslyn Analyzer 与 WinRT/.NET Metadata 工具。其价值不在“替代 Visual Studio”，而在于让 Agent 能获得更可靠、可版本化的 WinUI 专用规则和工具链，而不是从通用 WPF/UWP/XAML 知识中猜实现。

对 [[AxisAgent]]：若未来桌面端采用 WinUI 3，应把 `microsoft/win-dev-skills + WinApp CLI + 自有项目规则/Analyzer` 作为 Agent 编程基线候选，并继续保留真实 Build/Test/UIA/Packaging 门禁。

参见：[[GitHub Trending — 2026-09-10]]

关联：[[Agent]] · [[DotNet]] · [[AxisAgent]]
