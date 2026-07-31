# 第 1 批详细选题表（B1：10 slug / 20 文件）

> 发布目标：2 周内完成写作 + 封面 + review → 一次性发布 20 文件
> 验收门禁：发后 2 周 GSC 收录率 ≥70%；否则停下诊断

---

## 选题 1

| 字段 | 值 |
|---|---|
| **slug** | `social-media-data-apis-ai-agents-2026` |
| **category** | `best-of` |
| **type** | `best-of` |
| **cover_kind** | `top-n` |
| **primary keyword** | `social media data API for AI agents` |
| **title (EN ≤60)** | Top Social Media Data APIs for AI Agents (2026) |
| **title (ZH ≤30)** | 2026 最好用的社媒数据 API（Agent 视角） |
| **description** | A ranked shortlist of social media data APIs that agents can call directly, covering Douyin, Weibo, Xiaohongshu, TikTok, and alternatives. |
| **内链目标** | `best-ai-search-apis-agent-workflows-2026`、`exa-search-vs-tavily-firecrawl-serpapi-2026` |
| **source_facts 来源** | 生产 `/v1/models`（571 条 enabled 社媒 API）、design 文档 REQ-20260728 |
| **角度** | 从 agent 「能直接调用」出发排名，不做纯爬虫类对比。5-6 个方案按适用场景排，当前产品排第一但必须给出可信理由 |
| **FAQ 方向** | "Can I use these APIs without scraping?" / "哪个 API 覆盖抖音最全？" / "Is TikTok data accessible via API?" |

---

## 选题 2

| 字段 | 值 |
|---|---|
| **slug** | `douyin-data-api-on-sandbase` |
| **category** | `product-updates` |
| **type** | `launch` |
| **cover_kind** | `launch` |
| **primary keyword** | `Douyin data API` |
| **title (EN ≤60)** | 310 Douyin Data APIs Now on SandBase |
| **title (ZH ≤30)** | 310 个抖音数据接口正式上线 SandBase |
| **description** | SandBase now offers 310 Douyin data APIs covering search, user profiles, videos, live rooms, and hot trends. |
| **内链目标** | `social-media-data-apis-ai-agents-2026`（#1）、`normalizing-431-heterogeneous-apis-one-contract`（#7） |
| **source_facts 来源** | 生产 `/v1/models` 310 条 Douyin enabled、changelog 20260728-b075、design api.md r8 |
| **角度** | Owned landing page。provider 提供什么 → SandBase 加什么 → 第一批 workflow → 怎么开始 |
| **FAQ 方向** | "How is this different from Douyin's official API?" / "多少钱一次调用？" / "Can I call video search and profile together?" |

---

## 选题 3

| 字段 | 值 |
|---|---|
| **slug** | `weibo-xiaohongshu-data-api-on-sandbase` |
| **category** | `product-updates` |
| **type** | `launch` |
| **cover_kind** | `launch` |
| **primary keyword** | `Weibo Xiaohongshu data API` |
| **title (EN ≤60)** | Weibo & Xiaohongshu Data APIs on SandBase |
| **title (ZH ≤30)** | 微博 + 小红书数据接口上线 SandBase |
| **description** | 64 Weibo and 36 Xiaohongshu data operations are now available through SandBase, ready for agent workflows. |
| **内链目标** | `douyin-data-api-on-sandbase`（#2）、`social-media-data-apis-ai-agents-2026`（#1） |
| **source_facts 来源** | 生产 `/v1/models` Weibo 64 + Xiaohongshu 36 enabled、changelog 20260728-b075 |
| **角度** | 跨平台分析的第一步。微博=舆情、小红书=消费决策，两个平台、两种数据属性、同一套 agent 契约 |
| **FAQ 方向** | "Does it cover real-time Weibo hot search?" / "小红书笔记数据能拿到什么字段？" / "Is Xiaohongshu data available in English?" |

---

## 选题 4

| 字段 | 值 |
|---|---|
| **slug** | `douyin-data-api-competitor-monitor-agent` |
| **category** | `tutorials` |
| **type** | `how-to` |
| **cover_kind** | `launch` |
| **primary keyword** | `Douyin competitor monitoring agent` |
| **title (EN ≤60)** | Build a Douyin Competitor Monitor Agent |
| **title (ZH ≤30)** | 从零搭一个抖音竞品监控 Agent |
| **description** | Step-by-step tutorial: build an agent that tracks competitor Douyin accounts, detects new videos, and reports changes daily. |
| **内链目标** | `douyin-data-api-on-sandbase`（#2）、`cron-driven-agents-autonomous-workflows-2026` |
| **source_facts 来源** | 生产 API endpoint 可调用（user posts、video detail）、pricing 0-0.25/call |
| **角度** | 真能跑的代码。用 OpenAI SDK + SandBase `/v1/run` 调用 douyin user posts → LLM 分析 → cron 触发。全程按 blog-format.md 三种合法集成方式 |
| **FAQ 方向** | "How often can I poll without hitting rate limits?" / "一天监控 10 个账号花多少钱？" / "Can I add Weibo accounts to the same agent?" |

---

## 选题 5

| 字段 | 值 |
|---|---|
| **slug** | `xiaohongshu-kol-screening-agent-tutorial` |
| **category** | `tutorials` |
| **type** | `how-to` |
| **cover_kind** | `launch` |
| **primary keyword** | `Xiaohongshu KOL screening AI agent` |
| **title (EN ≤60)** | Xiaohongshu KOL Screening Agent (Tutorial) |
| **title (ZH ≤30)** | 用 Agent 自动筛小红书 KOL |
| **description** | Build an agent that scores Xiaohongshu influencers by engagement, content fit, and audience quality using SandBase data APIs. |
| **内链目标** | `weibo-xiaohongshu-data-api-on-sandbase`（#3）、`best-ai-search-apis-agent-workflows-2026` |
| **source_facts 来源** | 生产 API endpoint（xiaohongshu hot-list、user posts）、pricing |
| **角度** | DTC 品牌投放场景。Anthropic SDK + `/v1/run` 拿数据 → Claude 打分 → 输出 CSV。包含成本估算 |
| **FAQ 方向** | "What data points can I get per KOL?" / "能看到笔记互动率吗？" / "How does this compare to manual research?" |

---

## 选题 6

| 字段 | 值 |
|---|---|
| **slug** | `social-listening-agent-weibo-douyin-2026` |
| **category** | `tutorials` |
| **type** | `how-to` |
| **cover_kind** | `launch` |
| **primary keyword** | `social listening AI agent Weibo Douyin` |
| **title (EN ≤60)** | Build a Social Listening Agent: Weibo + Douyin |
| **title (ZH ≤30)** | 搭个舆情监控 Agent：微博 + 抖音 |
| **description** | Tutorial: an agent that monitors Weibo hot search and Douyin trending, flags brand mentions, and sends alerts via webhook. |
| **内链目标** | `douyin-data-api-on-sandbase`（#2）、`weibo-xiaohongshu-data-api-on-sandbase`（#3）、`multi-channel-ai-agents-slack-discord-whatsapp-2026` |
| **source_facts 来源** | 生产 API（weibo hot-search、douyin hot-search-list）、pricing |
| **角度** | 跨平台 agent。两个数据源、一个 LLM 判断层、一个 webhook 输出。含成本估算：每天 N 次 poll × 单价 |
| **FAQ 方向** | "How fast does it pick up trending topics?" / "能按关键词过滤吗？" / "What's the daily cost for hourly monitoring?" |

---

## 选题 7

| 字段 | 值 |
|---|---|
| **slug** | `normalizing-431-heterogeneous-apis-one-contract` |
| **category** | `developer-tools` |
| **type** | `architecture` |
| **cover_kind** | `comparison` |
| **primary keyword** | `normalize heterogeneous APIs agent contract` |
| **title (EN ≤60)** | Normalizing 431 APIs into One Agent Contract |
| **title (ZH ≤30)** | 431 个异构接口怎么归一成 Agent 契约 |
| **description** | Engineering deep-dive: how SandBase turned 571 heterogeneous social media operations into a uniform /v1/run contract with naming rules, body wrapping, and fail-closed validation. |
| **内链目标** | `douyin-data-api-on-sandbase`（#2）、`mcp-vs-function-calling-ai-agent-tool-integration`、`production-ai-agents-need-a-runtime-layer` |
| **source_facts 来源** | design.md（命名规则、root body 包装、313/310/3 对账、object/array 映射）、changelog QA 证据 |
| **角度** | 工程叙事：为什么 `fetch_multi_video` 的 root array 需要包成 `body` 字段；为什么名称归一要剥 `fetch`/`get`/`handler`；为什么 313 减 3 不能用位置推断。有判断有取舍。不是产品介绍 |
| **FAQ 方向** | "Why not just use the original OpenAPI spec?" / "为什么不直接转发原始参数？" / "How do you handle breaking changes upstream?" |

---

## 选题 8

| 字段 | 值 |
|---|---|
| **slug** | `llm-api-pricing-guide-2026` |
| **category** | `pricing-guides` |
| **type** | `analysis` |
| **cover_kind** | `top-n` |
| **primary keyword** | `LLM API pricing 2026` |
| **title (EN ≤60)** | LLM API Pricing in 2026: The Complete Guide |
| **title (ZH ≤30)** | 2026 LLM API 定价全指南 |
| **description** | A practical pricing reference for GPT-5.6, Claude 5, Kimi K3, and 10+ models: input/output rates, cache tiers, and real cost examples. |
| **内链目标** | `claude-opus-5-deep-dive-2026`（#13）、`kimi-k3-moonshot-1m-context-2026`（#15）、`best-1m-context-models-agents-2026`（#20） |
| **source_facts 来源** | 生产 `/v1/models` 价格字段、OpenAI/Anthropic/Moonshot 官方定价页 |
| **角度** | 不做广告，给可操作的对比表。1K/10K/100K token 三档真实费用；cache hit 的实际节省；pro vs non-pro 的边际收益。明确说不含 SandBase markup 除非有事实 |
| **FAQ 方向** | "Which model is cheapest per million tokens?" / "1M context 一次对话花多少？" / "Does caching really save money?" |

---

## 选题 9

| 字段 | 值 |
|---|---|
| **slug** | `video-generation-cost-model-explained` |
| **category** | `pricing-guides` |
| **type** | `analysis` |
| **cover_kind** | `comparison` |
| **primary keyword** | `video generation API cost` |
| **title (EN ≤60)** | Video Generation Costs: Per-Second vs Per-Call |
| **title (ZH ≤30)** | AI 视频生成的钱怎么算 |
| **description** | Break down video generation pricing across MiniMax H3, Kling 3.0, and Gemini Omni Flash: per-second, per-call, resolution tiers, and real budget examples. |
| **内链目标** | `minimax-h3-video-2k-stereo-2026`（#23）、`best-ai-video-generation-apis-2026`（#29） |
| **source_facts 来源** | 生产 `/v1/models` 价格、各厂商官方定价页 |
| **角度** | 三种计费模型的真实费用对比：固定/call（社媒数据 API 类）、按秒×分辨率（Kling/H3）、按 token 估算（Gemini）。含 10/100/1000 条视频的预算模板 |
| **FAQ 方向** | "How much does a 10-second video cost?" / "4K 比 1080p 贵多少？" / "Is turbo tier worth the quality trade-off?" |

---

## 选题 10

| 字段 | 值 |
|---|---|
| **slug** | `per-call-pricing-vs-token-pricing-api-agents` |
| **category** | `pricing-guides` |
| **type** | `analysis` |
| **cover_kind** | `comparison` |
| **primary keyword** | `per-call pricing vs token pricing AI agents` |
| **title (EN ≤60)** | Per-Call vs Token Pricing: Which Works for Agents |
| **title (ZH ≤30)** | 按次 vs 按 Token：Agent 怎么选 |
| **description** | Two pricing models dominate AI APIs. This guide explains when per-call billing (data APIs) beats token billing (LLMs) and how to mix them in one agent budget. |
| **内链目标** | `llm-api-pricing-guide-2026`（#8）、`normalizing-431-heterogeneous-apis-one-contract`（#7）、`production-ai-agents-need-a-runtime-layer` |
| **source_facts 来源** | SandBase 社媒 API 0-0.25 USD/call、LLM 定价数据、design api.md base_price 定义 |
| **角度** | Agent 视角的成本决策框架：什么时候一次 0.001 USD 的数据 API 调用比让 LLM 自己搜便宜 10 倍？含决策树和计算模板 |
| **FAQ 方向** | "When is per-call cheaper than letting the LLM browse?" / "怎么控制 agent 一天的总花销？" / "Can I set a budget cap per agent session?" |

---

## 交叉内链拓扑（B1 内部）

```
#1 (Top N) ←──→ #2 (Douyin launch) ←──→ #3 (Weibo/XHS launch)
      ↕                    ↕                        ↕
#4 (教程 Douyin)    #5 (教程 XHS)         #6 (教程 Weibo+Douyin)
      ↕                                           ↕
#7 (工程架构) ←──────────────────────────────────→ #10 (per-call vs token)
      ↕
#8 (LLM pricing) ←──→ #9 (video pricing) ←──→ #10 (per-call vs token)
```

每篇至少 2 条内链（1 条 B1 内部 + 1 条指向现有 52 篇）。

---

## DataForSEO 验证建议

对 B1 建议跑两组验证：

1. **社媒数据 API 组**：primary query "social media data API for AI agents"，seed keywords ["douyin data API", "xiaohongshu API", "weibo API agent", "TikTok data API alternative"]，market US (2840) + CN (2156)
2. **定价组**：primary query "LLM API pricing 2026"，seed keywords ["video generation API cost", "per-call vs token pricing", "AI API budget control"]，market US (2840)

需要你授权 `--allow-billable-requests` 后执行。
