---
type: engineering-standard
topic: refactoring
status: active
tags:
  - engineering
  - refactoring
  - quality
---

# Refactoring Principles

## 核心原则

1. 追求正确、简单、可维护的整体结构，不以最小 diff 为目标。
2. 优先修正已有实现、调整既有参数或删除不再需要的流程；避免通过新增兼容壳、补丁分支、包装层和重复抽象来掩盖问题。
3. 删除失效、重复、废弃、不可达、无真实用途的文件与代码。
4. 不保留“以后可能有用”的死代码；需要时应从版本历史恢复，而不是长期留在生产树中。
5. 公共抽象必须由真实复用需求驱动，不为了模式而模式。
6. 模块边界应让依赖方向清晰、职责单一、失败模式可验证。
7. 重构完成必须通过构建、测试、静态检查、关键 Smoke 与必要的真实运行验证。
8. 外部条件无法验证时必须明确记录 Gate，不用 Mock 结果冒充真实通过。

## 代码质量目标

- 明确命名，减少 Manager/Helper/Util 泛化类型。
- 小而清晰的接口，避免巨型 Service。
- 无重复流程与影子实现。
- 无无效兼容逻辑和历史残骸。
- 异步链路可取消、可超时、可恢复。
- 日志有结构、无敏感信息泄露。
- 性能优化基于真实热点，不用复杂度换取假想收益。

## 项目结构目标

```text
Presentation
    ↓
Application
    ↓
Domain / Core contracts
    ↓
Infrastructure adapters
```

具体项目可调整，但依赖方向必须可解释且可测试。

## 验收

- Debug/Release 构建通过。
- 自动化测试全部通过或明确说明真实 External Gate。
- 无新增高危漏洞。
- 关键用户路径 Smoke 通过。
- 文件数、代码量、依赖关系相较重构前应更合理，而不是仅仅“代码能跑”。

关联：[[Engineering Standards]] · [[Architecture]] · [[AxisAgent]]
