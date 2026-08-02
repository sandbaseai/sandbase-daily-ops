# SandBase Docs — AI Agent 友好化设计方案

> 目标：让 AI agent（ChatGPT、Claude、Cursor、Copilot、自研 agent）能直接发现、理解并调用 SandBase API，无需人类中间翻译。

---

## 一、当前问题

| 问题 | 影响 |
|------|------|
| `llms.txt` 返回 SPA HTML（被 React SPA catch-all 拦截） | AI agent 无法发现 SandBase 是什么、提供什么 API |
| 没有 OpenAPI spec（`api.sandbase.ai/openapi.json` 返回 404） | Agent 无法自动生成调用代码、无法做 schema 校验 |
| `ai-plugin.json` 返回 SPA HTML | ChatGPT Plugin / Copilot Extension 无法识别 |
| Docs 是人类导航结构（菜单+分页） | Agent 需要一次性获取"全部 API"而不是点击 10 个页面 |
| 缺少模型能力矩阵的机器可读版本 | Agent 不知道该调哪个模型 |
| 定价公式分散在各模型详情页 | Agent 无法预估成本 |

---

## 二、目标架构

```
www.sandbase.ai/
├── llms.txt                    ← AI agent 发现入口（精简版）
├── llms-full.txt               ← AI agent 完整参考（所有 API + 示例）
├── .well-known/
│   └── ai-plugin.json          ← ChatGPT/Copilot plugin 标准
│
api.sandbase.ai/
├── openapi.yaml                ← OpenAPI 3.1 完整规范
├── openapi.json                ← 同上 JSON 格式
│
www.sandbase.ai/docs/
├── agent-api-reference/        ← 新增：一页式 API 快速参考
│   ├── index.md                ← 全部端点汇总表
│   ├── models.md               ← 模型列表+定价+能力矩阵
│   ├── calling.md              ← 调用方式（chat/run/generations）
│   ├── billing.md              ← 费用查询+计算逻辑
│   └── errors.md               ← 完整错误码表
```

---

## 三、各文件详细设计

### 3.1 `llms.txt`（精简版 — AI agent 第一次接触）

标准参考：https://llmstxt.org/

```markdown
# SandBase

> AI agent infrastructure platform. One API key to call 400+ models (LLM, image, video, audio, embedding), MCP servers, sandboxes, and agent workflows.

## API Base URL

https://api.sandbase.ai/v1

## Authentication

Bearer token: `Authorization: Bearer sk-sb-YOUR_KEY`

## Core Endpoints

- POST /v1/chat/completions — OpenAI-compatible chat (LLM)
- POST /v1/run — Unified generation (image, video, audio, any async task)
- GET /v1/models — List all available models
- GET /v1/models/{name} — Get model details + pricing
- GET /v1/tasks/{id}/cost — Get task cost and usage

## Pricing

Pay-per-use. Each model has a `price_formula` field:
- LLM: `$input_tokens * X + $output_tokens * Y`
- Image/Video: flat `base_price` per generation

## Docs

- Full API reference: https://www.sandbase.ai/docs/api-reference/
- OpenAPI spec: https://api.sandbase.ai/openapi.yaml
- Complete LLM reference: https://www.sandbase.ai/llms-full.txt

## Models

400+ models from OpenAI, Anthropic, Google, DeepSeek, Meta, Mistral, ByteDance, Alibaba, MiniMax, and more.

Browse: https://www.sandbase.ai/models
```

### 3.2 `llms-full.txt`（完整版 — agent 深度参考）

结构：

```markdown
# SandBase — Complete API Reference for AI Agents

## Authentication
...

## Endpoints

### POST /v1/chat/completions
OpenAI-compatible. Supports streaming, function calling, vision, JSON mode.

Request:
{json example}

Response:
{json example}

### POST /v1/run
Unified async generation. Use for image, video, audio, embedding.

Request:
{json example}

Response (sync):
{json example}

Response (async — poll):
GET /v1/run/{id}
{json example}

### GET /v1/models
...

### GET /v1/models/{name}
...

### GET /v1/tasks/{id}/cost
...

## Model Categories

### LLM Models
| Name | Vendor | Context | Input Price ($/M) | Output Price ($/M) | Capabilities |
|------|--------|---------|-------|--------|---|
| openai/gpt-4o | OpenAI | 128K | $2.50 | $10.00 | chat, vision, tools, json_mode |
| anthropic/claude-sonnet-5 | Anthropic | 200K | $3.00 | $15.00 | chat, vision, tools, cache |
| deepseek/deepseek-v4 | DeepSeek | 1M | $0.50 | $2.00 | chat, tools |
...（从 registry 自动生成）

### Image Models
| Name | Vendor | Base Price | Resolution | Speed |
...

### Video Models
| Name | Vendor | Base Price | Duration | Resolution |
...

## Error Codes
| Code | HTTP Status | Description | Fix |
|------|-------------|-------------|-----|
| invalid_api_key | 401 | API key is invalid or revoked | Check /console/keys |
| rate_limited | 429 | Too many requests | Wait and retry with backoff |
| model_not_found | 404 | Model doesn't exist or is disabled | Check /v1/models |
| insufficient_balance | 402 | Account balance too low | Top up at /console/billing |
...

## Billing & Cost

### How costs are calculated
- LLM: input_tokens × prompt_price + output_tokens × completion_price
- Cached tokens: input_tokens × prompt_price × cache_read_multiplier
- Image/Video: flat base_price per generation
- Check cost after generation: GET /v1/tasks/{id}/cost

### Budget control
- Set spend alerts in /console/billing
- Monitor usage: /console/usage
```

### 3.3 `openapi.yaml`（OpenAPI 3.1 规范）

从现有 docs 中的 API reference 页面自动生成，包含：

- 所有端点的 path + method
- Request/response JSON Schema
- Authentication 定义
- 错误码枚举
- 示例值

生成方式：写一个脚本扫描 `sandbase-docs/api-reference/` 的所有 `.md` 文件，提取 endpoint、参数、响应格式，输出 OpenAPI spec。

### 3.4 `.well-known/ai-plugin.json`

```json
{
  "schema_version": "v1",
  "name_for_human": "SandBase",
  "name_for_model": "sandbase",
  "description_for_human": "Call 400+ AI models (LLM, image, video) with one API key.",
  "description_for_model": "SandBase API provides access to 400+ AI models. Use POST /v1/chat/completions for LLM chat (OpenAI-compatible), POST /v1/run for image/video/audio generation, GET /v1/models to list models, GET /v1/models/{name} for pricing. Auth: Bearer sk-sb-KEY. Base: https://api.sandbase.ai/v1",
  "auth": {
    "type": "user_http",
    "authorization_type": "bearer"
  },
  "api": {
    "type": "openapi",
    "url": "https://api.sandbase.ai/openapi.yaml"
  },
  "logo_url": "https://www.sandbase.ai/logo.svg",
  "contact_email": "support@sandbase.ai",
  "legal_info_url": "https://www.sandbase.ai/terms"
}
```

### 3.5 Docs 新增页面：`agent-api-reference/`

一页式快速参考，面向 agent 和高级开发者：

- **不用菜单导航**，一个长页面自上而下
- 所有端点 + 请求/响应 + 一个 curl 示例
- 模型能力矩阵表
- 定价公式汇总表
- 错误码完整表

---

## 四、实现步骤

### Phase 1：静态文件路由（1 天）

解决 SPA catch-all 拦截问题：

1. 在 Cloudflare 或 Nginx 层为 `llms.txt`、`llms-full.txt`、`.well-known/ai-plugin.json`、`openapi.yaml` 配置静态文件路由，绕过 SPA
2. 或者把这些文件放到 `public/` 目录让构建系统直接输出

### Phase 2：内容生成（2-3 天）

1. **`llms.txt`** — 手写精简版（~50 行）
2. **`llms-full.txt`** — 从 registry + docs 自动生成
   - 脚本从 `sandbase-registry/data/` 读取所有模型的 pricing、capabilities
   - 脚本从 `sandbase-docs/api-reference/` 读取所有 endpoint schema
   - 输出一个纯文本的完整 API 参考
3. **`openapi.yaml`** — 从 docs 的 API reference 页面提取
4. **`ai-plugin.json`** — 手写（很短）

### Phase 3：自动化维护（1 天）

1. CI 脚本：每次 model registry 更新时重新生成 `llms-full.txt`
2. CI 脚本：每次 docs 更新时重新生成 `openapi.yaml`
3. 版本号：`llms-full.txt` 顶部加日期标记，agent 可以判断是否是最新版

### Phase 4：Docs 重构（可选，3-5 天）

1. 新增 `agent-api-reference/` 一页式参考
2. 整理现有 docs 结构，确保每个 endpoint 页面有一致的格式
3. 补充缺失内容（billing API、usage API、webhook 事件列表）

---

## 五、文件位置规划

| 文件 | 仓库 | 路径 | 部署到 |
|------|------|------|--------|
| `llms.txt` | sandbase-monorepo | `sandbase-dashboard/public/llms.txt` | `www.sandbase.ai/llms.txt` |
| `llms-full.txt` | sandbase-monorepo | `sandbase-dashboard/public/llms-full.txt` | `www.sandbase.ai/llms-full.txt` |
| `ai-plugin.json` | sandbase-monorepo | `sandbase-dashboard/public/.well-known/ai-plugin.json` | `www.sandbase.ai/.well-known/ai-plugin.json` |
| `openapi.yaml` | sandbase-monorepo | `sandbase-apiserver/public/openapi.yaml` | `api.sandbase.ai/openapi.yaml` |
| 生成脚本 | sandbase-daily-ops | `scripts/generate-llms-txt.py` | CI |
| Agent API 页面 | sandbase-docs | `agent-api-reference/*.md` | `www.sandbase.ai/docs/agent-api-reference/` |

---

## 六、优先级

| 优先级 | 任务 | 影响 | 耗时 |
|--------|------|------|------|
| P0 | `llms.txt` 静态路由 + 内容 | AI 搜索引擎（Perplexity/ChatGPT）能发现 SandBase | 2h |
| P0 | `openapi.yaml` 生成 | Agent 能自动生成调用代码 | 4h |
| P1 | `llms-full.txt` 自动生成 | Agent 能一次性获取全部 API + 定价 | 4h |
| P1 | `ai-plugin.json` 路由修复 | ChatGPT Plugin 标准兼容 | 1h |
| P2 | Docs 一页式 agent 参考 | 开发者快速查阅 | 1d |
| P3 | CI 自动化维护 | 保持内容同步 | 4h |

---

## 七、验收标准

- [ ] `curl https://www.sandbase.ai/llms.txt` 返回纯文本（不是 HTML）
- [ ] `curl https://api.sandbase.ai/openapi.yaml` 返回有效 OpenAPI 3.1
- [ ] `curl https://www.sandbase.ai/.well-known/ai-plugin.json` 返回有效 JSON
- [ ] `llms-full.txt` 包含全部模型的名称、定价、能力标签
- [ ] 在 ChatGPT 中问 "What is SandBase API?" 能从 llms.txt 获取信息
- [ ] Cursor/Cline 能通过 openapi.yaml 自动补全 SandBase API 调用
- [ ] Agent 能通过一次 GET 请求获取完整的 API 使用指南
