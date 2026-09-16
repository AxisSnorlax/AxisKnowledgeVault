---
type: research
status: active
topic: professional-software-agent-surface
updated: 2026-09-16
tags:
  - agent
  - mcp
  - skills
  - desktop
  - industrial-software
  - automation
---

# Professional Software Agent Surface

## 结论

连续观察 `unity-mcp`、`Unity-Technologies/skills`、`t8y2/dbx`、`pascalorg/editor`、`HakanSeven12/OpenCADStudio` 与 `iOfficeAI/OfficeCLI` 后，一个模式已经足够稳定：

> **专业软件不应把 Agent 逻辑直接耦合进 UI；更合理的是保留权威 Domain Core，再对外提供确定性 Automation Contract、受控 MCP/Tool Surface 与 Domain Skills。**

推荐模型：

```text
Professional Application
│
├── Domain Core                # 权威状态、业务规则、事务/撤销/审计
│
├── Automation Contract        # 版本化、可测试、客户端无关
│   ├── Stable object identity / path
│   ├── Typed / structured schema
│   ├── Atomic mutation / rollback
│   └── Validation / verification
│
├── CLI / RPC / SDK            # 确定性自动化入口
│
├── MCP / Tool Surface         # Agent 可发现能力
│   ├── Read
│   ├── Safe Write
│   └── High-risk Write
│
├── Domain Skills              # 如何正确使用专业能力
│   ├── Workflow
│   ├── Preconditions
│   └── Verification
│
└── Permission / Approval      # Runtime 强制，不依赖 Prompt
```

这不是行业正式标准，而是当前开源生态中连续出现的工程模式。

## 证据

### Unity

`Unity-Technologies/skills` 将专业软件工作流包装为官方 Domain Skills；此前 `unity-mcp` 则验证了“专业软件能力 → MCP Surface”。二者组合说明：**Skill 描述专业工作流，MCP/Tool 承担真实操作能力**。

### dbx

`t8y2/dbx` 将数据库客户端与 MCP Server 分离，并区分 read-only / safe-write / high-risk-write。它证明 Agent Surface 可以拥有独立生命周期和更细的写权限，而不是一个笼统的 `CanWrite`。

### Pascal Editor

`pascalorg/editor` 是 local-first 3D building editor。其 CLI 可启动本地 editor 与经过认证的 MCP 服务；公共 Agent Skills 与本地/托管 MCP 连接分开管理。Skills 会先检查实际 MCP tool schema，再决定可用参数，而不是假设仓库最新版能力一定存在。

值得吸收的点：

- Local / Hosted Agent Surface 分离；
- MCP 生命周期由连接器/插件统一管理，避免重复连接；
- Skill 在调用前检查真实 capability schema；
- 高层工作流与底层 scene tools 分离；
- 本地项目默认不需要上传云端。

### Open CAD Studio

`HakanSeven12/OpenCADStudio` 将 DWG/DXF 编辑、2D/3D 渲染、插件和自动化分开。桌面端同时提供：

- 一次性 CLI 转换；
- 持久 headless automation server；
- 基于 stdin/stdout 或本地 TCP 的 line-based JSON 自动化合同；
- `--mcp` 暴露当前桌面编辑器能力；
- Native Plugins 使用独立进程并通过版本化 Plugin API 通信。

这个设计尤其适合工业和工程软件：**先有稳定 Automation Contract，再将同一能力映射给 MCP，而不是让 MCP 成为唯一业务接口。**

### OfficeCLI：Deterministic Structured Contract

2026-09-16 C# Trending 的 `iOfficeAI/OfficeCLI` 为这一模型增加了非常具体的工程证据。它将 Word / Excel / PowerPoint 暴露为结构化 Agent Surface，而不是让 Agent 操纵 Office UI。

最值得吸收的模式：

#### Stable Identity / Path

文档对象使用稳定结构路径，例如 slide / shape / paragraph / worksheet 等层级，而不是让模型依赖屏幕位置、自然语言名称或易漂移索引解释。

对 Axis：

- Station / Device / Channel / Task / Protocol Field / Calibration Step 都应拥有稳定 Domain ID；
- UI Row Index、Tab 序号、像素坐标不能成为 Agent 的业务身份系统。

#### Structured JSON Result

每个命令可返回结构化 JSON，避免 Agent 通过 regex 解析 CLI 人类文本。

对 Axis：Automation Contract 至少应有：

```text
Result
  ├── success / status
  ├── code
  ├── message
  ├── data
  ├── warnings[]
  ├── artifactIds[]
  ├── validation[]
  └── correlationId
```

人类可读文本可以存在，但不能替代机器合同。

#### Progressive Complexity

OfficeCLI 从普通 read/get/query，到结构化 document tree，再到 raw XML，形成逐层升级能力，而不是默认把最危险、最底层能力暴露给 Agent。

Axis 可采用类似层级：

```text
L1 Domain Read / Query
L2 Typed Domain Mutation
L3 Advanced / Expert Contract
L4 Raw / Escape Hatch           # 默认禁用或高风险权限
```

#### Atomic Mutation / Rollback

Batch 操作默认 atomic，任一失败可整体回滚；只有显式 best-effort 才允许部分成功。

工业/工程软件应优先采用同样原则：

- 多参数部署；
- 多字段协议变更；
- 配方/标定参数应用；
- 文档/配置批量修改；

不应在中途失败后留下无法解释的半完成状态。

#### Validate + Render / Observe

OfficeCLI 将 schema validation、issues、HTML/PNG render 等作为修改后的检查路径。这说明专业 Agent Surface 的 Verification 不一定只有单元测试，还可以包括“重新读取 / 渲染 / 观察结果”。

对 Axis：

```text
Execute
  ↓
Read-back / Domain Validate
  ↓
Render / UIA / Screenshot / Telemetry Observe（适用时）
  ↓
Independent Verification
  ↓
Commit Result
```

这与 [[Deterministic Agent Runtime]] 的 Verification Gate 一致。

#### MCP Is Adapter, Not Core

同一文档能力同时可经 CLI、Resident Pipe SDK、Batch 与 MCP 使用，进一步证明：

> **Domain Contract 应独立于 MCP。MCP 是 Agent Transport / Discovery Adapter，不应成为业务逻辑唯一入口。**

## 对 Axis 系列项目的长期建议

### [[AxisAgent]]

AxisAgent 应做通用编排器、权限/审批器和 Runtime，而不是把所有专业领域逻辑复制进 Agent Core。

它应能够消费：

- Domain Skills；
- MCP/Tool capability schema；
- Stable Domain Identity；
- Structured Result Schema；
- Version / Compatibility；
- Permission class；
- Transaction / rollback metadata；
- Verification evidence。

### [[AFSCADA]]

建议未来 AI Surface 分层：

```text
Read Telemetry / Query History        -> Read
Analyze / Recommend Config            -> No direct write
Apply low-risk configuration          -> Safe Write + permission
Hardware command / calibration action -> High-risk + explicit approval + audit
Raw DB / protocol escape hatch        -> Disabled by default / admin gate
```

真实硬件动作仍受现有硬件门禁和业务状态机约束，Agent 不得绕过。

多站点或多参数写入应优先提供 transactional / compensating rollback 语义，而不是让 Agent 自己逐条调用并猜测失败恢复。

### [[AxisProtocolStudio]]

适合优先暴露：

- Protocol parse / validate；
- Replay / simulator；
- Frame encode/decode；
- Field / schema stable identity；
- Export / analysis；
- Controlled send。

真实 Serial/TCP/UDP 写入应与只读分析分级，并保留用户授权、目标端点和审计证据。

对协议定义的结构化修改可以采用：

```text
Read Current Schema
  ↓
Prepare Typed Patch
  ↓
Validate
  ↓
Atomic Apply
  ↓
Encode/Decode Regression
  ↓
Commit / Rollback
```

### 其他专业桌面工具

UI 页面不应成为 Agent API。Agent 调用应该进入 Domain/Application contract，由同一业务规则服务于 UI、CLI、MCP 和自动化测试。

## 设计约束

1. **Domain Core 是第一真源。** MCP、CLI、Skill 都只是适配层。
2. **Automation Contract 应先于 MCP 稳定。** 这样同一能力可服务脚本、测试、CLI 与 Agent。
3. **Domain Object 必须有稳定身份。** 不使用 UI Index / Pixel / 自然语言显示名充当业务主键。
4. **机器结果必须结构化。** JSON / typed DTO / schema 优先，stdout 文本仅用于人类展示。
5. **权限按风险分级。** 至少区分 Read / Safe Write / High-risk Write / Raw Escape Hatch。
6. **批量写入优先原子化。** 无法原子化时必须有明确 compensating rollback 与 partial-result contract。
7. **高风险操作必须 Runtime 强制审批。** Prompt 中写“请确认”不算安全边界。
8. **Capability 必须可发现且可版本化。** Skill 不能假设源仓库中存在的字段已经部署到用户机器。
9. **UI 与 Agent Surface 生命周期解耦。** 必要时 Agent Surface 可独立运行或 headless。
10. **插件/扩展尽量隔离。** 不可信或可选扩展优先独立进程/沙箱，而不是直接注入主进程。
11. **结果必须可验证。** 写操作返回结构化 Result / Artifact / Diff / Audit，而不是只返回自然语言“完成”。
12. **写后必须支持 Read-back / Validate。** 有视觉或实时状态的领域再增加 Render / Observe / Telemetry Verification。
13. **底层 Escape Hatch 默认受限。** Raw SQL、Raw XML、直接文件/设备写入等不应与普通 Domain Tool 同权限。

## 不建议

- 每个页面直接调用 LLM；
- 把 Prompt 当业务规则；
- 把所有写操作放到一个万能 MCP Tool；
- Agent 绕过 Domain 状态机直接改数据库；
- Agent 用 UI Row Index / Pixel Coordinate 代替真实 Domain Identity；
- 默认暴露 Raw SQL / Raw Protocol / Raw Device 命令；
- 多步修改没有事务或失败恢复语义；
- 为了“支持 AI”在每个专业软件里各自复制完整 Agent Runtime；
- 把 UI automation 当作已有稳定业务 API 的替代品。

## 观察状态

该模式已经由多个不同领域项目连续验证，可作为 Axis 工业/工程软件的长期架构原则继续使用。2026-09-16 的 OfficeCLI 进一步把模式收敛到 **Stable Identity + Structured Contract + Atomic Mutation + Validation/Observation**。具体协议、权限粒度、事务模型和进程边界仍需按项目真实风险验证。

关联：[[Agent]] · [[MCP]] · [[Skills]] · [[Desktop UI]] · [[AFSCADA]] · [[AxisProtocolStudio]] · [[AxisAgent]] · [[Deterministic Agent Runtime]] · [[GitHub Trending — 2026-09-13]] · [[GitHub Trending — 2026-09-16]]
