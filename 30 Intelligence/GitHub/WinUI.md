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

## 2026-09-11 变化

今天没有新的 WinUI 框架级突破，但出现两个值得加入 **UI Framework Qualification** 的真实应用样本：

### files-community/Files

- C# Daily Trending 约 **+208 stars/day**。
- 仓库标签包含 `.NET / Fluent / WinAppSDK / WinUI / XAML`。
- 适合作为现代 Windows 原生桌面 UI 的参考：Navigation、文件列表、窗口行为、上下文菜单、主题和 Shell 集成。

### luolangaga/tubatools

- C# Weekly Trending 约 **+686 stars/week**。
- README 明确为 **WinUI 3 + .NET 10** 社区重构版。
- 功能密度较高，包含大量工具卡片、硬件监控、AI 助手、亮暗主题和“快速模式”（可关闭界面动画）。
- 对 [[AxisAgent]] 的价值在于：它比 Gallery/Sample 更接近复杂 Windows 工具工作台，可用于评估实际布局、样式组织、动画成本和高密度页面表现。

这两者只能作为工程/视觉参考，不能凭 Star 或截图推导 WinUI 性能优于 Avalonia/WPF；框架迁移仍应通过同一页面、同一数据量、同一机器的真实 Benchmark 决定。

另外，本轮发现 `asklar/lvt` 这一低星但高相关工具：它可统一读取 WinUI 3、WPF、WinForms、Avalonia、Chromium 等 UI Tree，并通过 MCP/UIA 驱动 Windows 应用。虽然当前仅约 24 stars，不属于趋势爆点，但其“framework-native visual tree + UIA + MCP”思路值得 [[AxisAgent]] 的 Computer Use / UI Verification 原型验证。

参见：[[GitHub Trending — 2026-09-11]]

关联：[[Agent]] · [[DotNet]] · [[AxisAgent]]

<!-- trend-watch:2026-10-24-recovery-snapshots:begin -->
## 2026-10-24：恢复决策期间保护已有快照

[DeskBox v1.5.9](https://github.com/Tianyu199509/DeskBox/releases/tag/v1.5.9)（10 月 23 日）记录了配置缺失时的恢复选择，并在决定前暂停定时快照；更新器另有失败退避与计费网络处理。这为 WinUI 桌面应用的数据生命周期提供了具体样本。

对 [[AxisAgent]] 的设计推论：启动检测、快照资格校验、用户恢复选择及后台保存需要共享明确状态；不能在恢复决定前让默认状态覆盖仅存证据。可把“配置缺失但备份存在”列为恢复验收场景，分别核对恢复和重新开始后的数据归属。

这是发布说明支持的研究候选。本轮未安装或独立复验项目的测试、签名与 Native AOT 发布结果，不能据此宣称 WinUI 性能或部署资格通过。

参见：[[30 Intelligence/GitHub/Daily/2026-10-24|GitHub Trending — 2026-10-24]]
<!-- trend-watch:2026-10-24-recovery-snapshots:end -->
