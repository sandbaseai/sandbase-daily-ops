# SandBase Docs — 左侧 Sidebar 统一重构 + Agent-Friendly API 新区

> 目标：去掉顶部多 tab 导航的分区逻辑，统一为左侧单一 sidebar 树；新增 Agent-Friendly API 区让 AI agent 能直接发现和使用 SandBase API。

---

## 一、当前问题

| 问题 | 影响 |
|------|------|
| 顶部 5 个 tab（Start/Store/Setup/Build Agent/API Reference）+ 左侧 sidebar 双导航 | 用户认知负担大 |
| 每个 tab 切换完全不同的 sidebar | 同一内容多处出现 |
| 27 个页面没有在任何 sidebar 中露出 | 内容不可发现 |
| Sandbox/MCP 作为独立顶级概念 | 产品已不单独暴露，它们是 Agent 内部实现 |
| 没有 Agent-Friendly 入口 | AI agent 无法一次性获取 API 全貌 |

---

## 二、设计原则

1. **单一导航入口** — 所有内容通过左侧 sidebar 可达，顶部 nav 只保留 logo + 搜索 + 外部链接
2. **Sandbox/MCP/Runtime/Environments CRUD 不再暴露** — 产品已去掉这些独立概念
3. **Agent-Friendly API 作为独立区** — 面向 AI agent 的一页式参考
4. **Runs 是查看结果** — 创建 Run 通过 Published Agent 的调用入口（REST/MCP），Runs 区只做查询观测
5. **去掉 SDKs** — 暂不暴露

---

## 三、最终 Sidebar 结构

```
📖 SandBase Docs
│
├── Getting Started
│   ├── Overview
│   ├── Quickstart
│   ├── First API Call
│   └── API Keys
│
├── Agent-Friendly API              ← 新增
│   ├── Overview                    (= llms.txt HTML 版)
│   ├── Complete API Reference      (= llms-full.txt HTML 版)
│   ├── Models & Pricing            (一页汇总表)
│   ├── Error Codes                 (完整错误码表)
│   └── OpenAPI Spec                (外链 api.sandbase.ai/openapi.yaml)
│
├── Store
│   ├── Overview
│   ├── Models
│   ├── APIs
│   ├── Agents
│   ├── Skills
│   ├── Supported Models
│   └── Capability Matrix
│
├── Setup
│   ├── Overview
│   ├── Setup Groups
│   └── Installed Tools
│
├── Agents
│   ├── Overview
│   ├── Define an Agent
│   ├── Add APIs and Tools
│   ├── Runs
│   ├── Published Agents
│   ├── Scheduled Agents
│   ├── Environments
│   └── Webhooks
│
├── Guides
│   ├── Overview
│   ├── Model Routing
│   ├── Streaming
│   ├── Error Handling
│   ├── Rate Limiting
│   ├── Billing & Pricing
│   └── Site Agent Integration
│
├── Use Cases
│   ├── Overview
│   └── Site Agent Copilot
│
├── API Reference
│   ├── Overview
│   ├── Authentication
│   ├── Errors
│   │
│   ├── Models
│   │   ├── Chat Completions
│   │   ├── Anthropic Messages
│   │   ├── Image Generation
│   │   ├── Video Generation
│   │   ├── Audio
│   │   ├── Vision
│   │   ├── Embeddings
│   │   ├── Assets
│   │   ├── List Models
│   │   └── Get Model
│   │
│   ├── Tasks
│   │   └── Get Task Cost
│   │
│   ├── MCP (APIs & Connectors)
│   │   ├── Overview
│   │   ├── List Servers
│   │   ├── List Tools
│   │   ├── SSE Proxy
│   │   └── Client Configuration
│   │
│   ├── Agents
│   │   ├── Create Agent
│   │   ├── List Agents
│   │   ├── Get Agent
│   │   ├── Update Agent
│   │   ├── Archive Agent
│   │   └── List Versions
│   │
│   ├── Published Agents
│   │   ├── Publish and Invoke     (包含 Run 调用方式：REST + MCP)
│   │   └── Quickstart
│   │
│   ├── Schedules
│   │   ├── Create Schedule
│   │   └── Manage Runs
│   │
│   ├── Runs
│   │   ├── List Runs
│   │   ├── Get Run
│   │   ├── Stream Events
│   │   └── List Events
│   │
│   └── Skills & Webhooks
│       ├── Skills API
│       └── Webhooks
│
├── Workspace
│   ├── API Keys
│   ├── Organizations
│   ├── Billing
│   └── Rate Limits
│
├── FAQ
└── Changelog
```

---

## 四、顶部 Nav 改造

### Before
```
Start | Store | Setup | Build Agent | API Reference
```

### After
```
[Logo] ──────── [Search] ──── Console | GitHub
```

不再用顶部 nav 做内容分区切换。

---

## 五、Agent-Friendly API 区详细设计

### 5.1 Overview (= llms.txt)

- SandBase 是什么（一句话）
- Base URL: https://api.sandbase.ai/v1
- Auth: Bearer sk-sb-YOUR_KEY
- 核心 endpoint 列表
- 定价模型概述
- 链接到 Full Reference / OpenAPI

### 5.2 Complete API Reference (= llms-full.txt)

- 所有 endpoint 完整 request/response schema
- 每个 endpoint 一个 curl 示例
- 模型分类表 + 定价
- 错误码完整表
- 计费逻辑
- 一页到底，不分页

### 5.3 Models & Pricing

从 registry 自动生成的表：

| Name | Type | Vendor | Context | Input $/M | Output $/M | Capabilities |

### 5.4 Error Codes

| Code | HTTP | Description | Fix |

### 5.5 静态文件（同源双输出）

| 文件 | 部署到 | 放置位置 |
|------|--------|----------|
| llms.txt | www.sandbase.ai/llms.txt | sandbase-dashboard/public/llms.txt |
| llms-full.txt | www.sandbase.ai/llms-full.txt | sandbase-dashboard/public/llms-full.txt |
| openapi.yaml | www.sandbase.ai/docs/openapi.yaml | sandbase-docs/public/openapi.yaml (已存在) |

---

## 六、去掉的内容

| 去掉什么 | 原因 |
|----------|------|
| Sandbox API（19 页） | 产品已不单独暴露 sandbox |
| Runtime 区（7 页） | sandbox-lifecycle/persistence/events 等已移除 |
| Environments CRUD（6 页） | 环境统一为 1 个，实际是密钥管理 |
| SDKs（3 页） | 暂不暴露 |
| Runs 的 Create/Update/Archive/Delete/Send Events | Run 由 Published Agent 调用产生，不直接创建 |

---

## 七、实现步骤

### Phase 1: Sidebar 重构（1 天）
1. 重写 `sandbase-docs/.vitepress/sidebar.ts`
2. 修改 `sandbase-docs/.vitepress/config.ts` — 去掉顶部 tabs
3. 删除或隐藏已去掉的页面路由

### Phase 2: Agent-Friendly API 页面（2 天）
1. 创建 `sandbase-docs/for-agents/` 目录 + 4 个 md
2. 手写 index.md + full.md + errors.md
3. 脚本生成 models.md

### Phase 3: 静态文件（半天）
1. 创建 llms.txt + llms-full.txt 放到 dashboard public/
2. 验证 curl 返回纯文本

### Phase 4: CI 自动化（半天）
1. registry 更新时重新生成 models.md + llms-full.txt

---

## 八、验收标准

- [ ] 左侧 sidebar 统一，无顶部 tab 切换
- [ ] Agent-Friendly API 区完整可用
- [ ] curl https://www.sandbase.ai/llms.txt 返回纯文本
- [ ] 去掉的页面不再出现在导航中
- [ ] Published Agent 入口明确包含 Run 调用方式

---

## 九、关联文档

- `outputs/docs-agent-friendly-design.md` — Agent 友好化内容设计（llms.txt/OpenAPI 内容细节）
- 本文档 — 整体导航结构 + 菜单定义
