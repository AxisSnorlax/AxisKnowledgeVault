---
type: intelligence-index
topic: dotnet
status: active
tags:
  - github
  - dotnet
  - csharp
---

# .NET / C# 趋势索引

## 关注方向

- .NET Desktop
- WinUI 3 / Windows App SDK
- WPF
- Avalonia
- NativeAOT
- MCP / Agent SDK
- 本地 AI 集成
- 高性能工具链

## 当前观察

GitHub Trending 的 AI 热度主要集中在 Python 和 TypeScript，但 C#/.NET 的价值更集中在 Windows、企业软件、专业桌面工具和 AI 与传统软件的集成层。

值得持续观察：

- MCP 与专业桌面软件集成
- C# Agent Runtime / Tooling
- Windows 原生 Agent Desktop
- NativeAOT 与本地模型/推理工具集成
- 高性能图表、数据采集和实时 UI

## 2026-09-10 变化

- `microsoft/win-dev-skills` 把 WinUI 3 / Windows App SDK 的 scaffold、设计、构建、UI 测试、Code Review、打包和 WPF→WinUI 迁移正式包装成 Agent Skills，并同时兼容 Copilot、Claude Code 与 Codex。这说明 .NET/Windows 开发正在出现“Agent-native engineering workflow”，不仅是给 IDE 增加聊天助手。
- `CoplayDev/unity-mcp` 在 C# Trending 继续增长（约 +31 today），再次印证 C# 的 AI 差异化更适合落在专业软件、桌面工具、工程环境与 MCP 集成层。
- 今日没有新的 C# 通用 Agent Framework 爆发。对 Axis 而言，没有必要追 Python/TS 的框架数量；应继续强化 Windows Native、工业/专业软件和 Agent Tooling 的结合。

参见：[[GitHub Trending — 2026-09-10]] · [[WinUI]] · [[Agent]]

## 2026-09-11 变化

- `files-community/Files` 位于 C# Daily Trending，约 **+208 stars/day**。它的仓库标签包含 .NET、Fluent、WinAppSDK、WinUI、XAML，说明成熟 Windows 原生 GUI 应用仍有很强关注度。
- `luolangaga/tubatools` 位于 C# Weekly Trending，约 **+686 stars/week**；其 README 明确为 **WinUI 3 + .NET 10** 的复杂 Windows 工具工作台，并包含 AI 助手、硬件监控和 Fluent 工具体系。它比单页 Sample 更适合作为真实 WinUI 工程参考。
- `CoplayDev/unity-mcp` 本周约 **+239 stars**，继续确认 C# AI 的强项是把 Unity、工业/工程软件等现有专业能力安全地暴露给 Agent。
- `microsoft/mcp` 仍在 C# Daily Trending，继续提供官方 Microsoft MCP Server Catalog 的生态信号。

结论没有改变：Axis 的差异化重点应放在 **Windows / Industrial / Professional Software + MCP/Computer Use + Local AI**，而不是追逐通用 Agent Framework 数量。

参见：[[GitHub Trending — 2026-09-11]] · [[WinUI]] · [[Agent]]

关联：[[WinUI]] · [[Avalonia]] · [[Agent]] · [[Local-AI]]
