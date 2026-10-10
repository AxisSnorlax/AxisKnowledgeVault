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

## 2026-09-12 变化

今天最大的 .NET/C# 信号不是某个新 GUI 框架，而是 **官方领域 Skills 正式化**：

- `Unity-Technologies/skills` 位于 C# Daily Trending，约 **+45 stars/day**。Unity 官方开始将新建项目、CLI 等专业工作流包装为可复用 Agent Skills，并面向多种 Agent 客户端。
- `dotnet/skills` 位于 C# Daily Trending，约 **+13 stars/day**。绝对热度不高，但它由 .NET 团队维护，已经覆盖 LSP、performance diagnostics、MSBuild、NuGet、upgrade、AI/RAG/MCP、testing、ASP.NET Core、Blazor 等 Plugins/Skills。
- `dotnet/skills` 还提供 Skill Value dashboard，用 token use、elapsed time、activation、not-passed rate 等指标评估 Skill，这说明领域 Skill 正从“文档资产”走向可度量的工程资产。
- `CoplayDev/unity-mcp` 周榜仍约 **+227 stars/week**，`IvanMurzak/Unity-MCP` 约 **+138/week**。与 Unity 官方 Skills 一起看，专业软件的合理 AI Surface 越来越清楚：**Domain Skills + MCP/Tool Surface + Permission**。
- `luolangaga/tubatools` 周榜仍约 **+677 stars/week**；`files-community/Files` 今日约 +87/day。WinUI 真实应用仍有持续关注，但今天没有 WinUI 框架级新突破。
- Avalonia 本体今日约 +13/day，属于正常活跃度，不足以改变已有判断。

对 Axis：AFSCADA、Protocol Studio、工程工具等应优先建设可复用 Domain Skills 和受控 Tool/MCP Contract，而不是把 AI 逻辑写进 ViewModel/Page；同样应给 Skills 建立版本和效果回归指标。

参见：[[GitHub Trending — 2026-09-12]] · [[Agent]] · [[Agent Capability Packaging]]

## 2026-09-16 变化

今天 C#/.NET 最有价值的新信号是 `iOfficeAI/OfficeCLI`，C# Daily Trending 约 **+276 stars/day**。它验证了一个比“再造通用 Agent Framework”更适合 .NET 的方向：**把成熟专业数据/文档能力包装成确定性、结构化、可验证的 Agent Surface。**

值得吸收的工程模式：

- 命令返回稳定 Structured JSON，而不是要求 Agent 用正则解析 stdout；
- 文档元素拥有稳定 Path / Identity；
- Read / structured DOM-like access / raw XML 形成渐进复杂度；
- Batch 默认 atomic，任一失败可整体 rollback；
- `validate`、issues、HTML/PNG render 形成执行后的独立检查与视觉验证；
- CLI、SDK、MCP 共享同一 Domain Contract，MCP 不是业务核心本身。

这使此前的 .NET 长期判断进一步收敛：C#/.NET 的 AI 差异化应重点建设 **Professional Software Agent Surface + Domain Skills + Deterministic Contract + Native/Windows Integration**。

同日 `dotnet/skills` 约 **+53 stars/day**，相比 2026-09-12 记录的约 +13/day 明显增强，但仍属于既有 Domain Skills 趋势的延续；`CoplayDev/unity-mcp` 今日约 +29/day，也继续验证专业软件 MCP Surface。

今天没有足以改变 WinUI 3、WPF 或 Avalonia 技术判断的新框架级事件，因此不机械修改对应 UI 索引。

参见：[[GitHub Trending — 2026-09-16]] · [[Professional Software Agent Surface]] · [[Agent]]

关联：[[WinUI]] · [[Avalonia]] · [[Agent]] · [[Local-AI]]


## 2026-09-29 变化

今天 .NET/C# 的高价值信号集中在 **Windows Agent Runtime、桌面自动化和本地 AI Host**：

- `sbroenne/mcp-windows`：C# Windows UI Automation + MCP，强化 UIA-first Computer Use。
- `RedWoodOG/Hermes-Desktop`：.NET 10 + WinUI 3 + SQLite FTS5 + MCP + Skills + Provider switching，适合作为 Windows-native Agent Desktop 工程参考样本。
- `ramseur/sovrant`：Runtime 与 Desktop/Web/CLI Surface 分离，并将 Provider、Tool、Skill、Memory、Permission 单独建模。
- `Retro-Downfall/RetroDownfall.Arcanum`：.NET 10 + NativeAOT + Microsoft.Extensions.AI + SQLCipher + MCP，体现 long-lived local AI host + thin clients + OpenAI-compatible façade 的路线。
- Microsoft Foundry Local 已形成可直接从 C#/.NET 调用的 Windows 本地推理路线，值得纳入 [[AxisAIManager]] 的真实 Benchmark 候选。

长期判断进一步收敛：.NET 的差异化价值仍然是 **Windows Native + Professional/Industrial Software + Deterministic Tool Surface + Local AI + Agent Runtime**，而不是追求通用 Agent Framework 数量。

参见：[[GitHub Trending — 2026-09-29]] · [[Agent]] · [[Local-AI]]

## 2026-10-09 变化

今天 .NET/C# 最重要的新信号来自 Microsoft Execution Containers（MXC）：

- Microsoft 已提供 Windows 原生执行隔离与正式 .NET SDK；
- 对 [[AxisAgent]] 来说，Sandbox 不再只能作为自建权限层或外部 WSL2 实验方案研究；
- 推荐把 MXC 作为 Windows-native Execution Sandbox Adapter 的 P0 资格候选，并与现有 Permission / Approval / Audit / Verification 合同解耦；
- 资格测试必须覆盖目标 OS Build、补丁门槛、文件/网络/UI 拒绝行为、异常回收、并发、取消、x64/ARM64 与 NativeAOT 兼容性。

这进一步强化 .NET 的差异化方向：**Windows Native Runtime + Deterministic Agent Boundary + Professional Software Surface**。

参见：[[GitHub Trending — 2026-10-09]] · [[Agent Capability Policy Enforcement]] · [[Agent]]

## 2026-10-10 变化

`snownico0722/PaperTodo` 提供一个新的真实 WPF 参考样本：.NET 10、原生多窗口、贴边胶囊、Markdown、本地数据、插件目录，以及实验性的 MCP / PowerShell 能力。

对 [[AxisAgent]] 的价值主要在交互模型，而不是框架排名：

- Main Workspace + Mini Surface + Background Service 可以共存；
- 多显示器 DPI、焦点抢占、悬浮层状态恢复值得单独测试；
- MCP / Script Surface 必须与 UI 权限解耦，并纳入 [[Agent Capability Policy Enforcement]]；
- 作者的资源占用和流畅度声明需要同机 Benchmark，不能直接用于 WPF / WinUI / Avalonia 优劣判断。

今天没有足以改变 WinUI 3、WPF、Avalonia 技术路线的框架级证据。

参见：[[GitHub Trending — 2026-10-10]] · [[Desktop UI]] · [[Agent]]
