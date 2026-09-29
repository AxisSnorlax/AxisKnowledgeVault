---
type: intelligence-index
topic: avalonia
status: active
tags:
  - github
  - avalonia
  - desktop
  - cross-platform
---

# Avalonia 趋势索引

## 关注方向

- Avalonia 12+
- XAML / AXAML tooling
- Desktop / Mobile / Browser
- NativeAOT
- Skia / Composition
- 高性能数据展示
- Agent Desktop 跨平台实现

## 评估重点

- Windows 下与 WPF/WinUI 的性能差异
- Designer / Preview / Hot Reload 工具链
- NativeAOT 与发布体积
- 高 DPI、多窗口、复杂 XAML、虚拟化
- 与 MCP、Local AI、系统级工具集成的成本

关联：[[DotNet]] · [[Agent]] · [[WinUI]]


## 2026-09-29 变化

`wieslawsoltes/CDP` 值得作为 Avalonia 新的工程化观察点：它为 Avalonia 应用提供 CDP 风格 inspection/automation surface，并结合 Playwright、MCP、截图、输入和 headless E2E。

这带来一个新的 UI Framework Qualification 维度：**Agent 可操作性 / 可验证性**。

除了启动速度、RAM、GPU、Streaming、视觉还原和开发效率，未来还应比较：

- Visual Tree 是否可以结构化读取；
- UI Automation / Accessibility 暴露是否稳定；
- 是否支持 headless / automated E2E；
- Agent 能否可靠定位控件而非依赖坐标；
- 修改后是否可以通过结构化状态和视觉证据双重验证。

这不构成继续或放弃 Avalonia 的单独理由，但它直接关系到 Agent 辅助 UI 开发、自动验收和 Computer Use 的可靠性。

参见：[[GitHub Trending — 2026-09-29]] · [[Agent]] · [[DotNet]]
