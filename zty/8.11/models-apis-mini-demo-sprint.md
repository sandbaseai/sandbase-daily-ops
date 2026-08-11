# SandBase Models + APIs 小 Demo 启动方案

> 建议周期：前 14 天  
> 发布平台：X 为主，LinkedIn 可使用稍长版本  
> 内容目标：先证明“能调用、结果清楚、上手简单”，再逐步引导到 Agent、Session、Sandbox 和 Trace 叙事  
> 核心页面：`https://www.sandbase.ai/models`、`https://www.sandbase.ai/apis`

## 1. 为什么先从 Models 和 APIs 开始

Models 和 APIs 比完整 Agent Runtime 更适合账号冷启动：

- 结果直观，一条帖子可以只讲一个能力。
- Demo 录制简单，通常只需要输入、运行和输出三个画面。
- 容易与新模型、AI 搜索、图片、视频和 SEO 热点结合。
- 可以直接链接具体模型或 API 页面，转化路径短。
- 后续能够自然升级为“Model + API + Agent + Runtime”的完整工作流。

当前公开目录显示：

- Models 页面显示 1,195 个模型、92 个提供商。
- APIs 页面显示 1,105 个 API、33 个提供商。

但 SandBase Docs 首页仍使用其他总量表述。正式发帖前，必须让产品或开发团队确认统一的公开数字；数字没有统一前，帖子只使用“one catalog / one API key / multiple providers”等非数量表达。

## 2. 小 Demo 的统一格式

每个 Demo 只回答四个问题：

1. 输入了什么？
2. 调用了哪个准确的 Model ID 或 API ID？
3. 返回了什么？
4. 开发者下一步去哪里试？

### 视频结构

| 时间 | 画面 | 字幕 |
|---|---|---|
| 0–3 秒 | 先展示最终结果 | `One call. This is the result.` |
| 3–8 秒 | 展示 SandBase 模型/API 页面 | 准确名称和 ID |
| 8–20 秒 | 输入参数并点击 Run | 突出核心输入 |
| 20–30 秒 | 展示返回结果 | 标记关键字段或输出 |
| 30–40 秒 | 展示 Docs 或具体页面 | 单一 CTA |

### 每条帖子的固定结构

```text
Hook：一句话说明结果或问题

What we ran：准确模型/API 名称
Input：一句话描述输入
Output：一句话说明结果

CTA：Try it / View the model / Read the API schema
```

不要在同一条 Demo 里同时介绍模型、沙箱、Agent、MCP、Session 和所有平台能力。

## 3. 第一批 14 天 Demo 顺序

### Day 1：GPT Image 2 文本生成图片

**为什么先发**：结果最直观，适合视频、GIF 和前后对比。

**准确页面**：`https://www.sandbase.ai/model/openai/gpt-image-2`

**演示任务**：生成一张包含英文和中文短文字的开发者活动海报，展示文本渲染能力。

**录屏画面**：

1. 先展示最终图片。
2. 展示 Prompt、Quality、Resolution、Aspect Ratio 和 Output Format。
3. 点击 Run。
4. 展示输出并放大海报中的文字。

**发帖前确认**：

- 当前模型 ID。
- 当前价格与质量档位。
- 输出格式和分辨率是否与公开页面一致。
- 生成图片可否公开用于社媒。

**X 帖子开头**：

> One prompt → a multilingual launch poster with readable text.

**CTA**：View GPT Image 2 on SandBase.

### Day 2：GPT Image 2 Edit 前后对比

**准确页面**：`https://www.sandbase.ai/model/openai/gpt-image-2/edit`

**演示任务**：将一张普通产品图更换背景、添加品牌色，同时保留主体。

**内容形式**：Before / After 滑动图或 20 秒录屏。

**核心价值**：让结果本身成为帖子，不写长说明。

**CTA**：Try an image edit.

### Day 3：Exa Search 自然语言网页搜索

**准确 ID**：`exa/search`

**准确页面**：`https://www.sandbase.ai/model/exa/search`

**演示任务**：

```text
Find recent technical articles explaining how production AI agents recover from failed tool calls.
```

**展示结果**：标题、URL、摘要和返回的结构化字段；不要只展示一段总结。

**X 帖子开头**：

> Give an agent a research question. Get structured sources back in one call.

**CTA**：Explore the Exa Search API schema.

### Day 4：Firecrawl Scrape 网页转 Markdown

**准确 ID**：`firecrawl/scrape`

**演示任务**：选择一个可公开访问的技术文档页面，将其转换为干净 Markdown。

**展示画面**：原网页 → API 输入 URL → Markdown 输出。

**注意**：确认目标页面允许公开演示，不抓取登录页、私人内容或付费内容。

**X 帖子开头**：

> A webpage in. Clean, agent-ready Markdown out.

### Day 5：DataForSEO 网页截图 API

**准确 ID**：`dataforseo/v3/on_page/page_screenshot`

**演示任务**：输入 SandBase 的公开模型页，返回桌面端或移动端整页截图。

**展示结果**：API 请求参数、返回的图片 URL 和最终截图。

**适用故事**：Agent 在分析网页前，先获取可审查的视觉证据。

**CTA**：View the screenshot API.

### Day 6：DeepSeek V4 Flash 小型代码任务

**准确 ID**：`deepseek/deepseek-v4-flash`

**演示任务**：给一段简短但有错误的 Python 函数，让模型解释问题并返回修复版本。

**展示重点**：输入、模型 ID、结构清楚的输出；不要自行发布速度或质量对比结论。

**禁止表述**：没有正式 benchmark 时，不写“比某模型更快/更强”。

### Day 7：第一周合集 Thread

**主题**：`6 small things you can run through SandBase Models + APIs`

**内容**：每个 Demo 使用一张结果图、一句话能力和具体页面链接。

**目标**：把零散帖子变成一篇可收藏的索引。

## 第 2 周

### Day 8：Scholar Search 学术搜索

**准确 ID**：`scholar/search-scholar` 或开发确认后的正式 ID。

**演示任务**：查找 AI Agent tool-use reliability 相关论文。

**展示重点**：论文标题、作者、摘要和引用信息。

**发帖前确认**：具体搜索来源、返回字段和当前价格。

### Day 9：DataForSEO 关键词搜索量

**准确 ID**：`dataforseo/v3/keywords_data/google_ads/search_volume/live`

**演示任务**：比较 3–5 个公开 AI Agent 关键词，不展示内部商业关键词。

**展示重点**：输入关键词、搜索量和竞争字段。

**注意**：标明国家、语言、设备和数据时间；不脱离条件引用数字。

### Day 10：Nano Banana 2 图片生成或编辑

**候选 ID**：

- `google/nano-banana-2`
- `google/nano-banana-2/edit`

**演示任务**：与 GPT Image 2 使用不同场景，不做未经验证的优劣对比。

**建议场景**：将一个简单线框图转成有品牌风格的产品概念图。

### Day 11：Kling Video V3 Pro 图生视频

**准确 ID**：`kwaivgi/kling-video/v3/pro/image-to-video`

**演示任务**：使用 Day 1 或 Day 10 生成的静态视觉，转换成 5–8 秒动态片段。

**内容价值**：把两个独立 Model Demo 串成一个小工作流。

**发帖前确认**：输入规格、时长、分辨率、生成时间和价格。

### Day 12：Tavily Search 搜索与页面内容

**准确 ID**：`tavily/search`

**演示任务**：查询一个当日开发者热点，展示 ranked results 和返回内容。

**注意**：不要与 Exa 做“谁更好”的结论；可以说明不同参数或返回结构。

### Day 13：API Chain——Search → Scrape → Model Summary

**目的**：从单个能力自然升级到工作流。

**步骤**：

1. Exa 或 Tavily 找到相关页面。
2. Firecrawl 或 Context.dev 抓取 Markdown。
3. 选择一个 LLM 生成带来源的简短摘要。

**视频长度**：控制在 40–60 秒。

**传播重点**：多个能力通过 SandBase 组成可复现的研究流程。

### Day 14：第二周复盘与投票

**发布内容**：

- 最受欢迎的 Models Demo。
- 最受欢迎的 APIs Demo。
- 下一周希望看到的方向：Image、Video、Search、SEO 或 Social Data。

**数据记录**：曝光、视频观看、资料页访问、模型/API 页面点击和有效问题。

## 4. 推荐的第一条 Demo

第一条建议选择 **GPT Image 2 文本生成图片**，原因：

- 页面已有完整 Playground 和公开说明。
- 结果适合 X 的视觉信息流。
- 可以同时展示英文和中文文字生成。
- Demo 只需要 Prompt、Run、Result 三步。

### 第一条帖子草稿

```text
One prompt → a multilingual launch poster with readable text.

We generated this with GPT Image 2 through SandBase:
• English + Chinese text
• 16:9 output
• One model page, one run

Here’s the full prompt and result ↓

[model page URL]
```

正式发布前，将 `16:9`、价格、质量档位和模型 ID 与实际运行结果逐项确认。

## 5. 每个 Demo 需要保存什么

在 `zty/<date>/` 或统一内容资产目录中保存：

```text
demo-name/
├── source-facts.md
├── prompt-or-request.json
├── raw-result.json
├── screenshot-before.png
├── screenshot-after.png
├── demo.mp4 或 demo.gif
├── x-copy.md
└── published-url.md
```

其中 `source-facts.md` 至少记录：

- 正式模型/API 名称和 ID。
- 官方页面和 Docs URL。
- 截止当天的价格与日期。
- 输入和输出规格。
- 实际调用是否成功。
- 哪些表述已由开发确认。

## 6. 发布前检查

- [ ] 实际运行成功，不用页面示例冒充自己的测试结果。
- [ ] 模型/API 名称和 ID 与官网一致。
- [ ] 价格在发布当天重新确认。
- [ ] 没有暴露 API Key、账号、内部 URL 和客户数据。
- [ ] Demo 开头先展示结果。
- [ ] 一个 Demo 只讲一个主要能力。
- [ ] CTA 链接到具体模型/API 页面，而不是一律链接首页。
- [ ] 发布后保存 URL、时间和基础数据。

## 7. 后续升级路径

两周小 Demo 完成后，内容按以下顺序升级：

```text
单个 Model / API
→ Model + API 组合
→ 可复现工作流
→ Agent + Tool
→ Session + Sandbox + Trace
→ 生产 Runtime 故障、权限和成本控制
```

这样既能用 Models 和 APIs 快速开始，又不会把 SandBase 长期定位限制成简单的模型或 API 聚合目录。
