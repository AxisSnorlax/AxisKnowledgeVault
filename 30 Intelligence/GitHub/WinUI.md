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

<!-- trend-watch:2026-11-11-reactor-maturity:begin -->
## 2026-11-11：Reactor 的编写层与工具成熟度

[Microsoft.UI.Reactor README](https://github.com/microsoft/microsoft-ui-reactor) 描述真实 WinUI 控件之上的声明式 C# 编写方式，并给核心、DevTools、数据及异步能力分别标记成熟度。[0.1.0-preview.17](https://github.com/microsoft/microsoft-ui-reactor/releases/tag/v0.1.0-preview.17) 仍为预发布，框架、可选扩展、诊断包、Skill Kit 与 Visual Studio 内嵌预览分开交付。

对 [[AxisAgent]] 的研究建议：

- 将编写方式与底层 WinUI 平台分开，保留现有 XAML／MVVM 互操作及技术选择。
- 按所需功能核对成熟度、实际包版本和工具依赖；核心可用不证明预览工具、可访问性或 AOT 路径全部通过。
- 评价增量协调与控件复用时同时核对状态、焦点、DPI 和诊断输出；调试工具可用不等于可默认随正式产品开放。

本轮未安装框架、CLI 或 VSIX，也未开展代码迁移；此项为候选观察，不构成项目切换依据。

参见：[[30 Intelligence/GitHub/Daily/2026-11-11|GitHub Trending — 2026-11-11]] · [[DotNet]] · [[Agent Verification and Audit Plane]]
<!-- trend-watch:2026-11-11-reactor-maturity:end -->

<!-- trend-watch:2026-11-13-release-mode-qualification:begin -->
## 2026-11-13：发布通道、合成模式与动态数据验证

[WinUI / WinAppSDK 2.6.5](https://github.com/microsoft/microsoft-ui-xaml/releases/tag/winui3%2Frelease%2F2.6.5) 修复多显卡／显示器渲染及合成接口缺失问题，并明确 System Composition Engine 模式下 content islands 与 XAML windows 的系统背景限制。[2.6.6-experimental 发布记录](https://github.com/microsoft/microsoft-ui-xaml/releases) 则新增 TableView 层级／实时整形、Chart UIA 与可选的滚动视口外绘制；两者页面均显示 11 月 11 日，但发布通道不同。

对 [[AxisAgent]] 的设计推论：

- UI 资格记录绑定包版本、稳定／实验通道、系统版本和实际合成模式；不从更高版本号推导全部能力可用。
- 多显卡、多显示器与背景材质分别验证，保留回退模式及不支持原因。
- 动态排序、分组和层级变动后重新核对对象身份、可见内容与自动化树；增加 UIA 接口不自动证明定位始终稳定。
- 视口外绘制是独立选项；启用后另验视觉、命中测试和裁剪行为，不凭可见结果猜测输入区域。

这是待验证的研究候选，本轮未升级框架或修改 XAML，不改变现有 UI 技术路线。

参见：[[30 Intelligence/GitHub/Daily/2026-11-13|GitHub Trending — 2026-11-13]] · [[DotNet]] · [[Agent Verification and Audit Plane]]
<!-- trend-watch:2026-11-13-release-mode-qualification:end -->
