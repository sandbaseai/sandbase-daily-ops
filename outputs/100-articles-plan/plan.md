# 100 篇双语博客规划（50 slug × EN + ZH = 100 文件）

> 创建日期：2026-07-31
> 仓库：sandbase-daily-ops / sandbase-blog
> 口径：100 个文件 = 50 个 slug，每个 slug 产出 EN + ZH-CN 双语原生重写
> 发布节奏：5 批 × 每批 10 slug（20 文件），批间隔 2 周，观察 GSC 收录曲线

---

## 总体分配

| 簇 | 主题 | slug 数 | category 分布 | 说明 |
|---|---|---:|---|---|
| 1 | 社媒数据 API（TikHub） | 12 | product-updates 2 / developer-tools 3 / tutorials 3 / best-of 2 / industry-insights 2 | 站内零覆盖，431 op，工程深度强 |
| 2 | LLM 新模型 | 10 | model-introduction 4 / model-comparison 4 / agent-best-picks 2 | Opus 5 / Sonnet 5 / Kimi K3 / GPT-5.6 |
| 3 | 视频生成 | 9 | model-introduction 3 / model-comparison 3 / best-of 2 / tutorials 1 | MiniMax H3 / Kling 3.0 / Gemini Omni Flash |
| 4 | 图像生成 | 7 | model-introduction 2 / model-comparison 2 / best-of 2 / developer-tools 1 | Seedream 5.0 Pro / Qwen-Image-3 / Nano Banana |
| 5 | 检索 & Embedding & RAG | 5 | developer-tools 2 / model-comparison 1 / best-of 1 / tutorials 1 | Cloudsway / text-embedding-v4 / RAG 栈 |
| 6 | 成本与定价 | 4 | pricing-guides 4 | 站内零覆盖分类 |
| 7 | 教程与集成 | 3 | tutorials 3 | 端到端 agent 搭建 |
| **合计** | | **50** | | |

### category 统计（含现有 52 篇后的预期）

| category | 现有 | 本批新增 | 合计 |
|---|---:|---:|---:|
| model-introduction | 6 | 9 | 15 |
| model-comparison | 9 | 10 | 19 |
| best-of | 6 | 7 | 13 |
| agent-best-picks | 0 | 2 | 2 |
| agent-use-cases | 10 | 0 | 10 |
| agent-daily-news | 16 | 0 | 16 |
| tutorials | 1 | 8 | 9 |
| product-updates | 3 | 2 | 5 |
| industry-insights | 0 | 2 | 2 |
| pricing-guides | 0 | 4 | 4 |
| developer-tools | 1 | 6 | 7 |

---

## 分批排期

| 批次 | slug 数 | 文件数 | 内容 | 门禁 |
|---|---:|---:|---|---|
| B1 | 10 | 20 | 簇 1 核心 6 + 簇 6 全部 4 | 发完观察 2 周 GSC；收录率 <70% 停诊断 |
| B2 | 10 | 20 | 簇 2 全部 10 (LLM) | 与旧模型文内链验证 |
| B3 | 10 | 20 | 簇 3 全部 9 + 簇 5 补 1 | DataForSEO 验证视频类关键词 |
| B4 | 10 | 20 | 簇 4 全部 7 + 簇 5 剩 3 | |
| B5 | 10 | 20 | 簇 1 剩 6 + 簇 7 全 3 + 簇 5 剩 1 | 全站内链审计 |

---

## 簇 1：社媒数据 API（12 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 1 | social-media-data-apis-ai-agents-2026 | best-of | best-of | Top Social Media Data APIs for AI Agents (2026) |
| 2 | tikhub-douyin-data-api-on-sandbase | launch | product-updates | 310 Douyin Data APIs on SandBase |
| 3 | tikhub-weibo-xiaohongshu-data-on-sandbase | launch | product-updates | Weibo & Xiaohongshu Data Available Through SandBase |
| 4 | douyin-data-api-competitor-monitor-agent | how-to | tutorials | Build a Douyin Competitor Monitor Agent |
| 5 | xiaohongshu-kol-screening-agent-tutorial | how-to | tutorials | Xiaohongshu KOL Screening Agent from Scratch |
| 6 | social-listening-agent-weibo-douyin-2026 | how-to | tutorials | Build a Social Listening Agent for Weibo & Douyin |
| 7 | normalizing-431-heterogeneous-apis-one-contract | architecture | developer-tools | How We Normalized 431 APIs into One Agent Contract |
| 8 | per-call-pricing-vs-token-pricing-api-agents | analysis | pricing-guides | Per-Call vs Token Pricing: When Each Model Works |
| 9 | sync-only-api-design-ai-agents | architecture | developer-tools | Why Sync-Only is the Right Default for Data APIs |
| 10 | social-data-api-vs-web-scraping-agents-2026 | comparison | developer-tools | Social Data API vs Web Scraping for Agents (2026) |
| 11 | best-douyin-data-api-services-2026 | best-of | best-of | Best Douyin Data API Services in 2026 |
| 12 | china-social-commerce-data-ai-agents-2026 | analysis | industry-insights | China Social Commerce Data: The Agent Opportunity |

B1 取 #1~#6 + #7~#10（已含簇 6），B5 取 #11~#12 + 簇 1 剩余场景扩展。

---

## 簇 2：LLM 新模型（10 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 13 | claude-opus-5-deep-dive-2026 | model | model-introduction | Claude Opus 5: 1M Context and What It Changes |
| 14 | claude-sonnet-5-agents-coding-2026 | model | model-introduction | Claude Sonnet 5 for Agents and Coding (2026) |
| 15 | kimi-k3-moonshot-1m-context-2026 | model | model-introduction | Kimi K3: Moonshot's 1M-Context Leap |
| 16 | gpt-5-6-luna-sol-terra-explained | model | model-introduction | GPT-5.6 Luna, Sol, Terra: What Each Variant Does |
| 17 | claude-opus-5-vs-sonnet-5-which-to-pick | comparison | model-comparison | Opus 5 vs Sonnet 5: Architecture, Cost, Speed |
| 18 | kimi-k3-vs-claude-opus-5-2026 | comparison | model-comparison | Kimi K3 vs Claude Opus 5: 1M Context Showdown |
| 19 | gpt-5-6-vs-claude-5-agents-2026 | comparison | model-comparison | GPT-5.6 vs Claude 5 for Agent Workloads |
| 20 | best-1m-context-models-agents-2026 | best-of | agent-best-picks | Best 1M-Context Models for Agents in 2026 |
| 21 | anthropic-cache-pricing-5m-1h-explained | analysis | model-comparison | Anthropic's Split Cache Pricing: 5min vs 1hr |
| 22 | best-models-autonomous-agents-2026 | best-of | agent-best-picks | Best Models for Autonomous Agents (2026 Update) |

---

## 簇 3：视频生成（9 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 23 | minimax-h3-video-2k-stereo-2026 | model | model-introduction | MiniMax H3: Native 2K Stereo Video Generation |
| 24 | kling-video-3-unified-generation-2026 | model | model-introduction | Kling Video 3.0: Unified Multi-Shot Generation |
| 25 | gemini-omni-flash-video-2026 | model | model-introduction | Gemini Omni Flash: Google's Fast Video Model |
| 26 | minimax-h3-vs-kling-3-vs-gemini-omni | comparison | model-comparison | H3 vs Kling 3.0 vs Gemini Omni Flash |
| 27 | text-to-video-vs-image-to-video-2026 | comparison | model-comparison | T2V vs I2V vs Reference-to-Video: When to Use Each |
| 28 | kling-turbo-vs-omni-pro-standard-2026 | comparison | model-comparison | Kling Turbo vs Omni/Pro vs Standard Tiers |
| 29 | best-ai-video-generation-apis-2026 | best-of | best-of | Best AI Video Generation APIs in 2026 |
| 30 | best-image-to-video-models-agents-2026 | best-of | best-of | Best Image-to-Video Models for Agent Workflows |
| 31 | video-generation-agent-ad-creative-tutorial | how-to | tutorials | Build an Ad-Creative Video Agent (Tutorial) |

---

## 簇 4：图像生成（7 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 32 | seedream-5-pro-bytedance-image-2026 | model | model-introduction | Seedream 5.0 Pro: ByteDance's Image Generator |
| 33 | qwen-image-3-alibaba-generation-edit | model | model-introduction | Qwen-Image-3: Generation + Edit in One Model |
| 34 | seedream-vs-qwen-image-vs-nano-banana-2026 | comparison | model-comparison | Seedream vs Qwen-Image-3 vs Nano Banana |
| 35 | seedream-fast-vs-pro-quality-cost-2026 | comparison | model-comparison | Seedream Fast vs Pro: Quality-Cost Tradeoff |
| 36 | best-ai-image-generation-apis-2026 | best-of | best-of | Best AI Image Generation APIs in 2026 |
| 37 | best-ai-image-editing-apis-2026 | best-of | best-of | Best AI Image Editing APIs for Agents (2026) |
| 38 | batch-image-generation-agent-tutorial | how-to | developer-tools | Batch Image Generation Pipeline for Agents |

---

## 簇 5：检索 & Embedding & RAG（5 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 39 | text-embedding-v4-alibaba-deep-dive | deep-dive | developer-tools | Alibaba text-embedding-v4: What's New |
| 40 | cloudsway-search-api-explained-2026 | deep-dive | developer-tools | Cloudsway Search API: Ranked Results + Summaries |
| 41 | cloudsway-vs-exa-search-agents-2026 | comparison | model-comparison | Cloudsway vs Exa: Which Search API Fits Your Agent |
| 42 | best-embedding-models-rag-agents-2026 | best-of | best-of | Best Embedding Models for RAG Agents (2026) |
| 43 | rag-cost-structure-embedding-search-2026 | analysis | tutorials | RAG Cost Structure: Embedding + Search + LLM |

---

## 簇 6：成本与定价（4 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 44 | llm-api-pricing-guide-2026 | analysis | pricing-guides | LLM API Pricing in 2026: The Complete Guide |
| 45 | video-generation-cost-model-explained | analysis | pricing-guides | Video Generation Costs: Per-Second vs Per-Call |
| 46 | multimodal-agent-cost-breakdown-2026 | analysis | pricing-guides | Multimodal Agent Costs: A Real Breakdown |
| 47 | ai-api-budget-control-agents-2026 | how-to | pricing-guides | Budget Control for AI API Agents (Practical Guide) |

---

## 簇 7：教程与集成（3 slug）

| # | slug | type | category | 标题方向 |
|---|---|---|---|---|
| 48 | build-social-monitor-agent-openai-sdk | how-to | tutorials | Build a Social Monitor Agent (OpenAI SDK) |
| 49 | multimodal-agent-artifacts-e2b-sandbox | how-to | tutorials | Multimodal Agent with Artifacts (E2B Sandbox) |
| 50 | cost-dashboard-agent-anthropic-sdk | how-to | tutorials | Cost Dashboard Agent (Anthropic SDK Tutorial) |

---

## 完整发布包（走 api-launch-publish 三篇制）

以下 5 个主题走完整 SOP（owned + comparison + Top N = 3 slug 对应 6 文件），已计入上表：

| 主题 | owned slug | comparison slug | Top N slug |
|---|---|---|---|
| TikHub Douyin | #2 | #10 | #1 |
| Kimi K3 | #15 | #18 | #20 |
| MiniMax H3 | #23 | #26 | #29 |
| Seedream 5.0 Pro | #32 | #34 | #36 |
| Cloudsway Search | #40 | #41 | #42 |

---

## 风险与门禁

| 风险 | 缓解 |
|---|---|
| 批量上线触发 Google scaled content abuse | 5 批 × 2 周间隔，每批后 GSC 验收 |
| TikHub 可用性声明 | 需要生产 `/v1/models` 响应做 source_fact |
| 新模型缺 benchmark/pricing | 只写 registry 里有的字段，查不到的不编造 |
| 中文翻译腔 | 每篇按 `WRITING-METHOD.md` 第 5 节自查后才提交 |
| 封面产能 | 每批 10 张，render_launch_cover.py 本地完成 |
| reviewer 工作量 | 5 个完整发布包走 reviewer-role；单篇走简化 SEO/GEO 清单 |
| 内链稀疏 | 每篇至少 1 个站内链接，B5 做全站内链审计补漏 |

---

## 第 1 批详细选题表

见下一节（独立表格，含 primary keyword / 内链目标 / cover_kind / source_facts 来源）。
