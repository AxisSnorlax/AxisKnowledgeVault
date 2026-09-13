---
type: research
status: active
topic: professional-software-agent-surface
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

连续观察 `unity-mcp`、`Unity-Technologies/skills`、`t8y2/dbx`、`pascalorg/editor` 与 `HakanSeven12/OpenCADStudio` 后，一个模式已经足够稳定：

> **专业软件不应把 Agent 逻辑直接耦合进 UI；更合理的是保留权威 Domain Core，再对外提供受控 Automation Contract、MCP/Tool Surface 与 Domain Skills。**

推荐模型：

```text
Professional Application
│
├── Domain Core                # 权威状态、业务规则、事务/撤销/审计
│
├── Automation Contract        # 版本化、可测试、客户端无关
│   ├── CLI / JSON / RPC
│   └── Typed capability schema
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

## 对 Axis 系列项目的长期建议

### [[AxisAgent]]

AxisAgent 应做通用编排器、权限/审批器和 Runtime，而不是把所有专业领域逻辑复制进 Agent Core。

它应能够消费：

- Domain Skills；
- MCP/Tool capability schema；
- Version / Compatibility；
- Permission class；
- Verification evidence。

### [[AFSCADA]]

建议未来 AI Surface 分层：

```text
Read Telemetry / Query History        -> Read
Analyze / Recommend Config            -> No direct write
Apply low-risk configuration          -> Safe Write + permission
Hardware command / calibration action -> High-risk + explicit approval + audit
```

真实硬件动作仍受现有硬件门禁和业务状态机约束，Agent 不得绕过。

### [[AxisProtocolStudio]]

适合优先暴露：

- Protocol parse / validate；
- Replay / simulator；
- Frame encode/decode；
- Export / analysis；
- Controlled send。

真实 Serial/TCP/UDP 写入应与只读分析分级，并保留用户授权、目标端点和审计证据。

### 其他专业桌面工具

UI 页面不应成为 Agent API。Agent 调用应该进入 Domain/Application contract，由同一业务规则服务于 UI、CLI、MCP 和自动化测试。

## 设计约束

1. **Domain Core 是第一真源。** MCP、CLI、Skill 都只是适配层。
2. **Automation Contract 应先于 MCP 稳定。** 这样同一能力可服务脚本、测试、CLI 与 Agent。
3. **权限按风险分级。** 至少区分 Read / Safe Write / High-risk Write。
4. **高风险操作必须 Runtime 强制审批。** Prompt 中写“请确认”不算安全边界。
5. **Capability 必须可发现且可版本化。** Skill 不能假设源仓库中存在的字段已经部署到用户机器。
6. **UI 与 Agent Surface 生命周期解耦。** 必要时 Agent Surface 可独立运行或 headless。
7. **插件/扩展尽量隔离。** 不可信或可选扩展优先独立进程/沙箱，而不是直接注入主进程。
8. **结果必须可验证。** 写操作返回结构化 Result / Artifact / Diff / Audit，而不是只返回自然语言“完成”。

## 不建议

- 每个页面直接调用 LLM；
- 把 Prompt 当业务规则；
- 把所有写操作放到一个万能 MCP Tool；
- Agent 绕过 Domain 状态机直接改数据库；
- 为了“支持 AI”在每个专业软件里各自复制完整 Agent Runtime；
- 把 UI automation 当作已有稳定业务 API 的替代品。

## 观察状态

该模式已经由多个不同领域项目连续验证，可作为 Axis 工业/工程软件的长期架构原则继续使用；具体协议、权限粒度和进程边界仍需按项目真实风险验证。

关联：[[Agent]] · [[MCP]] · [[Skills]] · [[Desktop UI]] · [[AFSCADA]] · [[AxisProtocolStudio]] · [[AxisAgent]] · [[GitHub Trending — 2026-09-13]]
