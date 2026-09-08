---
type: project
project: AxisAIManager
status: active
platform: Windows
repository: AxisSnorlax/AxisAIManager
tags:
  - axis
  - local-ai
  - winforms
  - dotnet
---

# AxisAIManager

Axis.LocalAIManager 是本地 AI 基础设施控制面，基于 .NET 10、Windows Forms 与 AntdUI，管理 llama.cpp 推理/嵌入、ComfyUI、Docker Desktop、Qdrant 与模型配置。

## 与 AxisAgent 的边界

- Manager：模型配置、模型切换、进程所有权、健康检查、推理/嵌入/Qdrant 生命周期。
- [[AxisAgent]]：会话、Provider、RAG、MCP、插件与 Agent 工作流。
- Manager 不承载 Agent 会话和路由，不建设第二套 OpenAI Gateway。
- AxisAgent 通过本机控制接口发起模型切换，成功后直接调用 llama-server。

## 当前重要实现

- `POST http://127.0.0.1:8181/api/v1/models/switch`
- 控制接口仅监听回环地址。
- Windows Credential Manager 保存控制令牌。
- general / coder / vision 模型目录。
- Qdrant 非破坏性生命周期管理。
- ComfyUI 本地管理。
- Docker Engine 健康检查。
- 原子配置、运行缓存和脱敏日志。

## 长期定位

它应该保持“Local AI Control Plane”而不是扩张成 Agent 平台。

关联：[[AxisAgent]] · [[Local-AI]] · [[WinForms]] · [[DotNet]]
