# Axis Knowledge Vault

Axis 系列项目、技术决策、工程规范、开源趋势与研究资料的长期知识库，面向 Obsidian、ChatGPT 自动化与 AxisAgent 共同使用。

主入口：`Home.md`

## 信息架构

- `00 Inbox/`：临时收集、待归档内容。
- `10 Projects/`：Axis 系列项目档案、状态、边界与关键决策。
- `20 Technology/`：C#、.NET、WinForms、WPF、WinUI、Avalonia、Agent、MCP、Local AI 等长期技术主题。
- `30 Intelligence/`：GitHub Trending、生态变化、工具、开源项目与外部技术情报。
- `40 Engineering/`：架构、代码质量、重构原则、测试与交付标准。
- `50 Research/`：专题调研、技术比较、源码研究和实验结论。
- `60 Decisions/`：跨项目或长期有效的 ADR/技术决策。
- `80 Templates/`：Obsidian 笔记、项目档案、ADR、趋势日报等模板。
- `90 Archive/`：失效或历史资料。

## 当前核心入口

- `Home.md`
- `10 Projects/AxisAgent.md`
- `10 Projects/AxisAIManager.md`
- `20 Technology/Desktop UI.md`
- `20 Technology/Agent.md`
- `20 Technology/WinUI.md`
- `40 Engineering/Refactoring Principles.md`

## GitHub Trending 自动化

每日趋势写入：

`30 Intelligence/GitHub/Daily/YYYY-MM-DD.md`

长期主题索引：

- `30 Intelligence/GitHub/Agent.md`
- `30 Intelligence/GitHub/DotNet.md`
- `30 Intelligence/GitHub/WinUI.md`
- `30 Intelligence/GitHub/Avalonia.md`
- `30 Intelligence/GitHub/Local-AI.md`

自动化原则：

1. 不机械收录榜单，只保留有技术价值或趋势意义的项目。
2. Daily 保存时间敏感证据；稳定结论继续沉淀到 `20 Technology`、`40 Engineering` 或项目页。
3. 使用 YAML frontmatter 和 `[[双向链接]]`。
4. 项目仓库与正式报告仍是事实第一真源；Vault 负责聚合、解释、关联和长期决策。
5. 自动化不得覆盖人工内容，不重复制造相同知识节点。

## 本地使用

将本仓库 clone 到本机后，可直接用 Obsidian 的 **Open folder as vault** 打开仓库根目录。
