# SEO 转化率优化计划

> 生成日期：2026-08-17
> 数据来源：Google Search Console (2026-08-01 ~ 2026-08-15)
> 当前状态：展示 21,330 / 点击 275 / CTR 1.3% / 平均排名 17.2

---

## 背景数据

- 展示量 30 天增长 10x（200/天 → 2,200/天），说明 Google 在大量展示页面
- 点击增长滞后（5/天 → 30/天），CTR 偏低
- 根因：大部分页面排在第 2 页（排名 10-22），用户看不到

---

## P0：优化高展现低点击页面的 Title/Description（30 分钟）

这些页面已有排名，只需改搜索展示文案就能提升 CTR。

### 修改方式

**模型/API 详情页的 title 和 description** 由后端数据库中的 `display_name` 和 `description` 字段决定。

生成逻辑在 `sandbase-fe/src/features/model-catalog/seo.ts` 的 `buildModelMetadata()` 函数：

```typescript
// 当前逻辑：
const title = `${model.display_name} by ${model.vendor}`
const description = model.description
  ? model.description.slice(0, 160)
  : `${model.display_name} - ${model.type.toUpperCase()} model by ${model.vendor}...`
```

**优化方案 A（推荐，改数据库）：** 在后台管理系统中修改模型的 `display_name` 和 `description` 字段，使其更适合搜索展示。

**优化方案 B（改代码，全局生效）：** 修改 `buildModelMetadata()` 函数的 title 模板，例如：

```typescript
// sandbase-fe/src/features/model-catalog/seo.ts 第 19 行附近
// 修改前：
const title = `${model.display_name} by ${model.vendor}`

// 修改后（加入 "Free API" 和 "SandBase" 品牌词）：
const title = `${model.display_name} — Free API | SandBase`
```

**博客文章的 title 和 description** 在 markdown frontmatter 中直接修改：

```yaml
# 文件：sandbase-blog/src/content/en/xxx.md
---
title: "新标题写在这里"
description: "新描述写在这里，控制在 150 字符内"
---
```

---

### 1. `/model/instagram/v1/media-id-to-shortcode`

- 当前数据：410 展示, 1.0% CTR, 排名 7.8
- **当前 Title**：`Instagram V1 Media Id To Shortcode by Instagram`（自动生成，缺乏吸引力）
- **建议 Title**：`Instagram Media ID to Shortcode Converter — Free Online API | SandBase`
- **建议 Description**：`Convert Instagram media IDs to shortcodes instantly. Free API, no rate limits. One request, structured response. Try it now.`
- **修改方式**：后台修改该模型的 `display_name` 为 `Instagram Media ID to Shortcode Converter`，或用方案 B 改代码模板
- [ ] 已完成

### 2. `/blog/glm-5-3-release-watch-2026`（博客文章）

- 当前数据：286 展示, 0.7% CTR, 排名 7.4
- **当前 Title**：`GLM-5.3 Launches: Frontier Coding and Emergent Cybersecurity`
- **建议 Title**：`GLM 5.3 Release Date: Everything We Know (Updated Aug 2026)`
- **建议 Description**：`When will GLM 5.3 launch? Latest leaks, benchmark predictions, and timeline analysis. Updated weekly.`
- **修改方式**：编辑 `sandbase-blog/src/content/en/glm-5-3-release-watch-2026.md` 的 frontmatter：
  ```yaml
  title: "GLM 5.3 Release Date: Everything We Know (Updated Aug 2026)"
  description: "When will GLM 5.3 launch? Latest leaks, benchmark predictions, and timeline analysis. Updated weekly."
  ```
  同步修改中文版 `sandbase-blog/src/content/zh-CN/glm-5-3-release-watch-2026.md`
- [ ] 已完成

### 3. `/model/instagram/v1/shortcode-to-media-id`

- 当前数据：216 展示, 2.3% CTR, 排名 9.1
- **建议 Title**：`Instagram Shortcode to Media ID — Free Converter API | SandBase`
- **建议 Description**：`Convert any Instagram shortcode to its numeric media ID. Free REST API with instant response. No authentication required.`
- **修改方式**：同 #1，后台修改 `display_name`
- [ ] 已完成

### 4. `/model/douyin/web/all-sec-user-id`

- 当前数据：104 展示, 1.9% CTR, 排名 6.5
- **建议 Title**：`Douyin Sec User ID Lookup — Batch Resolve API | SandBase`
- **建议 Description**：`Resolve Douyin sec_user_id from share URLs or usernames in batch. Structured JSON response, ready for agent workflows.`
- **修改方式**：后台修改 `display_name`
- [ ] 已完成

### 5. `/model/instagram/v3/user-id-to-username`

- 当前数据：119 展示, 1.7% CTR, 排名 41.7
- 排名太靠后，暂不优先做 title 优化，先通过内链提升排名
- [ ] 跳过 / 已完成

### 6. 全局 Title 模板优化（方案 B，可选）

如果不想逐个改数据库，可以修改代码模板让所有模型页的 title 都更适合搜索：

**文件：** `sandbase-monorepo/sandbase-fe/src/features/model-catalog/seo.ts`

```typescript
// 修改前（第 19 行）：
const title = `${model.display_name} by ${model.vendor}`

// 修改后：
const title = `${model.display_name} — Free API | SandBase`
```

**注意：** 改模板会影响所有 5000+ 模型页的 title，部署前确认效果。

---

---

## P1：内链加强，推 Top 10 页面进 Top 5（2 小时）

排名 5-10 的页面进 top 5 后 CTR 会从 1-2% 跳到 5-15%。

### 修改方式

**博客文章加内链：** 在相关文章的正文或底部 "Related" 区块加入链接。

示例 — 在 `sandbase-blog/src/content/en/instagram-user-id-api-tutorial-2026.md` 正文中加入：
```markdown
To convert between media IDs and shortcodes, see our
[Media ID to Shortcode API](/model/instagram/v1/media-id-to-shortcode).
```

**模型页互链（需研发支持）：** 在模型详情页底部加一个 "Related APIs" 组件。

文件：`sandbase-fe/src/features/model-catalog/components/RelatedModels.tsx`（已存在）

如果需要跨 vendor 推荐，可在 `LLMDetailView.tsx` 底部加一段硬编码的快速链接，或者让后端返回 `related_models` 字段。

### 操作清单

- [ ] 在博客 `instagram-user-id-api-tutorial-2026` 文章正文中加内链到：
  - `/model/instagram/v1/media-id-to-shortcode`
  - `/model/instagram/v1/shortcode-to-media-id`
  - `/model/instagram/v3/user-id-to-username`
- [ ] 在博客 `best-open-source-ai-agent-frameworks-2026` 底部加内链到 `/agents`
- [ ] 在博客 `deepseek-harness-vs-openclaw-vs-hermes-2026` 加内链到：
  - `/model/deepseek/deepseek-v4-pro`
  - `/model/deepseek/deepseek-v4-flash`
- [ ] 在博客 `glm-5-3-release-watch-2026` 加内链到：
  - `/vendor/z-ai`
  - `/model/z-ai/glm-5.2`
- [ ] 首页 FAQ 区块或 footer "Learn" 栏考虑加一个 "Popular APIs" 链接（指向 `/apis`）
- [ ] （研发）模型详情页底部评估加 "Same Vendor" 推荐区块

---

## P2：为高展现 API 写教程博客（1 天）

围绕已有搜索需求写长尾内容，形成 topic cluster。

### 待写文章

- [ ] `instagram-media-id-shortcode-api-guide-2026` — "How to Convert Instagram Media ID to Shortcode in Python (2026)"
  - 内链目标：`/model/instagram/v1/media-id-to-shortcode`、`/model/instagram/v1/shortcode-to-media-id`
- [ ] `douyin-sec-user-id-batch-lookup-2026` — "Douyin Sec User ID: What It Is and How to Resolve It via API"
  - 内链目标：`/model/douyin/web/all-sec-user-id`、`/model/douyin/web/sec-user-id`
- [ ] `instagram-api-tools-compared-2026` — "Instagram API Tools Comparison: SandBase vs RapidAPI vs Direct"
  - 内链目标：所有 Instagram 相关模型页

---

## P3：模型页加 FAQ + Schema 增强（半天）

### 修改方式

**方案 A（快速，改模板）：** 在模型详情页组件中，根据模型类型自动生成 FAQ 区块。

文件：`sandbase-fe/src/features/model-catalog/components/LLMDetailView.tsx`

在页面底部渲染前，加入 FAQ section：

```tsx
{/* FAQ for SEO - 加在页面底部 return 之前 */}
<section className="mt-12 border-t pt-8">
  <h2 className="text-lg font-semibold mb-4">FAQ</h2>
  <details className="mb-3">
    <summary className="cursor-pointer font-medium">
      What is {model.display_name}?
    </summary>
    <p className="mt-2 text-sm text-muted-foreground">
      {model.description?.slice(0, 200)}
    </p>
  </details>
  <details className="mb-3">
    <summary className="cursor-pointer font-medium">
      How much does {model.display_name} cost?
    </summary>
    <p className="mt-2 text-sm text-muted-foreground">
      Input: ${model.model_card?.prompt_token_price}/M tokens,
      Output: ${model.model_card?.completion_token_price}/M tokens.
      See full pricing on this page.
    </p>
  </details>
  <details className="mb-3">
    <summary className="cursor-pointer font-medium">
      How do I call {model.display_name} via API?
    </summary>
    <p className="mt-2 text-sm text-muted-foreground">
      Use the SandBase unified API with your API key. See the Docs tab for request/response examples.
    </p>
  </details>
</section>
```

**方案 B（Schema 增强）：** 在 `sandbase-fe/src/features/model-catalog/json-ld.ts` 中的 `serializeJsonLd()` 增加 FAQPage schema：

```typescript
// 在现有 JSON-LD 的 @graph 数组中追加：
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": `What is ${model.display_name}?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": model.description?.slice(0, 200) || ""
      }
    },
    {
      "@type": "Question",
      "name": `How much does ${model.display_name} cost?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `Input: $${model.model_card?.prompt_token_price}/M tokens, Output: $${model.model_card?.completion_token_price}/M tokens.`
      }
    }
  ]
}
```

**方案 C（SoftwareApplication schema，针对免费 API 工具页）：**

在 `json-ld.ts` 中，对 type 为 `connector` 或非 LLM 类型的模型加入：

```typescript
{
  "@type": "SoftwareApplication",
  "name": model.display_name,
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }
}
```

这可能在搜索结果中触发 "Free" 价格标注，提升 CTR。

### 操作清单

- [ ] Instagram 相关模型页加 FAQ（优先 media-id-to-shortcode、shortcode-to-media-id）
- [ ] Douyin 相关模型页加 FAQ（优先 all-sec-user-id、user-search）
- [ ] 评估是否全局为 model 详情页模板加 FAQ 组件
- [ ] 评估 SoftwareApplication schema 对 API 工具页的效果

---

## P4：乘胜追击 DeepSeek Harness 系列（2-3 天）

"deepseek harness vs hermes" 已获得 17.6% CTR + 排名 2.9，是已验证的高价值主题。

### 待写文章

- [ ] `deepseek-harness-quickstart-tutorial-2026` — "DeepSeek Harness Tutorial: Build Your First Agent in 10 Minutes"
- [ ] `deepseek-harness-vs-langchain-crewai-2026` — "DeepSeek Harness vs LangChain vs CrewAI: Which Agent Framework?"
- [ ] `deepseek-harness-architecture-internals-2026` — "DeepSeek Harness Architecture: How the Agent Loop Works"

每篇互相内链 + 链回已有的 `deepseek-harness-vs-openclaw-vs-hermes-2026`。

---

## P5：技术优化（按开发排期）

| 项目 | 说明 | 优先级 |
|------|------|--------|
| 模型页 SSR | `/models` 列表页是 CSR，初始 HTML 只有 "Loading..."。改 SSR 可加速收录 | 中 |
| PageSpeed | 用 PageSpeed Insights 测 `/models` 和模型详情页，优化 LCP | 中 |
| 模型页互链 | 详情页底部加 "Similar Models"、"Same Vendor" 推荐 | 低 |
| OG Image | 制作 1200x630 品牌 OG 图，放 `sandbase-fe/public/og-image.png` | 低 |

---

## P5：全量 Model/API 详情页丰富化（统一改一遍）

### 目标

当前 5000+ 模型/API 详情页内容相对单薄（只有 playground + readme），需要统一丰富，让每个页面都对搜索引擎和用户有足够的信息密度。

### 当前页面结构

```
sandbase-fe/src/app/model/[vendor]/[...slug]/page.tsx
├── <JsonLd />                        ← JSON-LD 结构化数据
├── <main>
│   ├── <LLMDetailView />             ← 主要内容
│   │   ├── <ModelBuilderIntro />     ← 标题、vendor、actions
│   │   ├── <ModelDetailTabs />       ← Playground / History 切换
│   │   ├── <LLMChatPlayground />     ← 可交互的 playground
│   │   └── <ModelReadmeBlock />      ← readme markdown 渲染
│   └── <RelatedModels />             ← 相关模型推荐（已有）
└──
```

### 需要增加的区块（按位置排列）

#### 1. Quick Info 摘要卡片（加在 ModelBuilderIntro 下方）

**文件：** `sandbase-fe/src/features/model-catalog/components/LLMDetailView.tsx`

**加在** `<ModelBuilderIntro />` 和 `<section>` (tabs) 之间：

```tsx
{/* Quick Info Card */}
<div className="grid grid-cols-2 gap-3 sm:grid-cols-4 rounded-xl border p-4"
     style={{ borderColor: 'var(--border-primary)', backgroundColor: 'var(--bg-card)' }}>
  <div>
    <span className="text-[11px] uppercase font-semibold" style={{ color: 'var(--text-muted)' }}>Provider</span>
    <p className="mt-1 text-[14px] font-medium" style={{ color: 'var(--text-primary)' }}>
      <a href={vendorPath(model.vendor_slug)}>{model.vendor}</a>
    </p>
  </div>
  <div>
    <span className="text-[11px] uppercase font-semibold" style={{ color: 'var(--text-muted)' }}>Context</span>
    <p className="mt-1 text-[14px] font-medium" style={{ color: 'var(--text-primary)' }}>
      {(model.context_length / 1000).toFixed(0)}K tokens
    </p>
  </div>
  <div>
    <span className="text-[11px] uppercase font-semibold" style={{ color: 'var(--text-muted)' }}>Input Price</span>
    <p className="mt-1 text-[14px] font-medium" style={{ color: 'var(--text-primary)' }}>
      ${model.model_card?.prompt_token_price}/M
    </p>
  </div>
  <div>
    <span className="text-[11px] uppercase font-semibold" style={{ color: 'var(--text-muted)' }}>Output Price</span>
    <p className="mt-1 text-[14px] font-medium" style={{ color: 'var(--text-primary)' }}>
      ${model.model_card?.completion_token_price}/M
    </p>
  </div>
</div>
```

#### 2. 能力标签展示（加在 Quick Info 下方）

```tsx
{/* Capability Tags */}
{model.capability_tags?.length > 0 && (
  <div className="flex flex-wrap gap-2">
    {model.capability_tags.map(tag => (
      <span key={tag} className="rounded-full border px-3 py-1 text-[12px] font-medium"
            style={{ borderColor: 'var(--border-primary)', color: 'var(--text-secondary)' }}>
        {tag.replace('_', ' ')}
      </span>
    ))}
  </div>
)}
```

#### 3. Quick Start 代码片段（加在 Playground 区块下方）

**文件：** `sandbase-fe/src/features/model-catalog/components/LLMDetailView.tsx`

**加在** `</section>` (tabs section 结束) 之后，`<ModelReadmeBlock />` 之前：

```tsx
{/* Quick Start Code Example */}
<section className="rounded-xl border p-5" style={{ borderColor: 'var(--border-primary)' }}>
  <h2 className="text-[16px] font-semibold mb-3" style={{ color: 'var(--text-primary)' }}>
    Quick Start
  </h2>
  <div className="rounded-lg p-4 overflow-x-auto" style={{ backgroundColor: 'var(--bg-secondary)' }}>
    <pre className="text-[13px] font-mono leading-6" style={{ color: 'var(--text-primary)' }}>
{`curl -X POST https://api.sandbase.ai/v1/chat/completions \\
  -H "Authorization: Bearer $SANDBASE_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "${model.name}",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 256
  }'`}
    </pre>
  </div>
  <p className="mt-3 text-[12px]" style={{ color: 'var(--text-muted)' }}>
    Get your API key from <a href="/console" className="underline">Console</a>.
    See <a href={`/model/${model.vendor_slug}/${model.model_slug}/docs`} className="underline">full API docs</a> for all parameters.
  </p>
</section>
```

#### 4. FAQ 区块（加在 ReadmeBlock 之后，RelatedModels 之前）

**文件：** `sandbase-fe/src/app/model/[vendor]/[...slug]/page.tsx` 第 117 行附近

在 `<LLMDetailView />` 和 `<RelatedModels />` 之间插入新组件：

```tsx
{/* FAQ Section */}
<ModelFAQ model={model} />
```

新建文件 `sandbase-fe/src/features/model-catalog/components/ModelFAQ.tsx`：

```tsx
import type { Model } from '@/features/model-catalog/server/models';

export function ModelFAQ({ model }: { model: Model }) {
  const faqs = buildFAQs(model);
  if (faqs.length === 0) return null;

  return (
    <section className="mt-8 border-t pt-8" style={{ borderColor: 'var(--border-primary)' }}>
      <h2 className="text-[18px] font-semibold mb-4" style={{ color: 'var(--text-primary)' }}>
        Frequently Asked Questions
      </h2>
      <div className="space-y-3">
        {faqs.map((faq, i) => (
          <details key={i} className="group rounded-lg border px-4 py-3"
                   style={{ borderColor: 'var(--border-primary)' }}>
            <summary className="cursor-pointer text-[14px] font-medium list-none flex justify-between items-center"
                     style={{ color: 'var(--text-primary)' }}>
              {faq.question}
              <span className="text-[16px] transition-transform group-open:rotate-45">+</span>
            </summary>
            <p className="mt-3 text-[13px] leading-6" style={{ color: 'var(--text-muted)' }}>
              {faq.answer}
            </p>
          </details>
        ))}
      </div>
    </section>
  );
}

function buildFAQs(model: Model) {
  const faqs = [];

  faqs.push({
    question: `What is ${model.display_name}?`,
    answer: model.description?.slice(0, 300) ||
      `${model.display_name} is a ${model.type} model by ${model.vendor}, available through the SandBase unified API.`,
  });

  if (model.model_card?.prompt_token_price) {
    faqs.push({
      question: `How much does ${model.display_name} cost?`,
      answer: `Input: $${model.model_card.prompt_token_price}/M tokens. Output: $${model.model_card.completion_token_price}/M tokens. ` +
        `Cache reads: ${Number(model.model_card.cache_read_multiplier || 1) * 100}% of input price. No minimum commitment, pay as you go.`,
    });
  }

  if (model.context_length) {
    faqs.push({
      question: `What is the context window of ${model.display_name}?`,
      answer: `${model.display_name} supports a context window of ${(model.context_length / 1000).toFixed(0)}K tokens (approximately ${Math.round(model.context_length * 0.75 / 1000)}K words).`,
    });
  }

  faqs.push({
    question: `How do I call ${model.display_name} via API?`,
    answer: `Use the SandBase unified API at api.sandbase.ai/v1/chat/completions with model="${model.name}". ` +
      `Works with any OpenAI-compatible SDK. Get an API key from the Console to start.`,
  });

  if (model.capability_tags?.includes('function_calling')) {
    faqs.push({
      question: `Does ${model.display_name} support function calling?`,
      answer: `Yes. ${model.display_name} supports function calling (tool use), structured output, and can be used in agent workflows with tool definitions.`,
    });
  }

  return faqs;
}
```

#### 5. JSON-LD Schema 增强

**文件：** `sandbase-fe/src/features/model-catalog/components/JsonLd.tsx` 或 `json-ld.ts`

在现有的 JSON-LD 基础上追加 FAQPage schema（让 FAQ 有机会在搜索结果中展示为 Rich Result）：

```typescript
// 在 serializeJsonLd 或 JsonLd 组件中，追加到 @graph：
{
  "@type": "FAQPage",
  "mainEntity": buildFAQs(model).map(faq => ({
    "@type": "Question",
    "name": faq.question,
    "acceptedAnswer": {
      "@type": "Answer",
      "text": faq.answer
    }
  }))
}
```

#### 6. SEO Title 模板优化

**文件：** `sandbase-fe/src/features/model-catalog/seo.ts` 第 19 行

```typescript
// 修改前：
const title = `${model.display_name} by ${model.vendor}`

// 修改后（增加品牌词和吸引力）：
const title = `${model.display_name} — API & Pricing | SandBase`
```

**Description 模板也优化：**

```typescript
// 修改前（第 20-22 行）：
const description = model.description
  ? model.description.slice(0, 160)
  : `${model.display_name} - ${model.type.toUpperCase()} model by ${model.vendor}. Available on Sandbase unified AI API.`

// 修改后（加入结构化信息）：
const description = model.description
  ? model.description.slice(0, 130) + ` Context: ${(model.context_length/1000).toFixed(0)}K. Input: $${model.model_card?.prompt_token_price || '?'}/M.`
  : `${model.display_name} by ${model.vendor}. ${(model.context_length/1000).toFixed(0)}K context, $${model.model_card?.prompt_token_price || '?'}/M input. Try free on SandBase.`
```

---

### 实施顺序

| 步骤 | 改动 | 文件 | 影响范围 |
|------|------|------|----------|
| 1 | Title/Desc 模板优化 | `seo.ts` | 全部 5000+ 页面 |
| 2 | Quick Info 卡片 | `LLMDetailView.tsx` | 全部详情页 |
| 3 | 能力标签展示 | `LLMDetailView.tsx` | 全部详情页 |
| 4 | Quick Start 代码 | `LLMDetailView.tsx` | 全部详情页 |
| 5 | FAQ 组件 | 新建 `ModelFAQ.tsx` + `page.tsx` 引用 | 全部详情页 |
| 6 | FAQ JSON-LD | `JsonLd.tsx` | 全部详情页 |
| 7 | RelatedModels 已有 | — | ✅ 已有 |

全部是前端模板改动，改一次全站 5000+ 页面自动生效，不需要逐个改数据库。

---

## P6：技术优化（按开发排期）

| 项目 | 说明 | 优先级 |
|------|------|--------|
| 模型页 SSR | `/models` 列表页是 CSR，初始 HTML 只有 "Loading..."。改 SSR 可加速收录 | 中 |
| PageSpeed | 用 PageSpeed Insights 测 `/models` 和模型详情页，优化 LCP | 中 |
| OG Image | 制作 1200x630 品牌 OG 图，放 `sandbase-fe/public/og-image.png` | 低 |

---

## P7：Model/API Readme 丰富化模板规范

### 目标

给每个模型/API 的 `readme` 字段写入丰富的 markdown 内容，让详情页有足够的**差异化、非结构化内容**（Google 更喜欢有深度的页面）。

### 分工

| 内容类型 | 放哪里 | 谁负责 |
|----------|--------|--------|
| 价格、context、tags、curl | 前端模板自动生成（P5） | 研发改一次模板 |
| 模型特点、场景、对比、建议 | `model_card.readme` 字段 | 运营/AI 批量生成 |

### Readme 标准模板

每个模型的 readme 应包含以下区块（按顺序）：

```markdown
## Overview

<!-- 1-2 段，说清楚这个模型/API 是什么、核心优势是什么 -->
<!-- 字数要求：100-200 词，避免空洞 -->

{model.display_name} is {one sentence positioning}.
It excels at {key strength 1}, {key strength 2}, and {key strength 3}.
{One sentence on architecture or differentiator, e.g., "Built on a 284B MoE architecture with 13B active parameters"}.

## Best For

<!-- 用 bullet list 列出 3-5 个最佳使用场景 -->

- **Agent workflows** — long-running, multi-step tasks with tool use
- **Code generation** — project-level refactors and debugging
- **Structured extraction** — parsing documents into JSON schemas
- **RAG pipelines** — grounding answers with retrieved context
- **Cost-sensitive workloads** — high throughput at low per-token cost

## When to Choose This vs Alternatives

<!-- 对比同类模型，帮用户做决策 -->

| Scenario | Choose this model | Consider instead |
|----------|------------------|-----------------|
| Budget agent tasks | ✅ $0.14/M input | GPT-4o-mini ($0.15/M) |
| Maximum reasoning | Consider DeepSeek V4 Pro | ✅ Claude Opus 4.8 |
| Vision + code | Consider Gemini 3.5 Flash | ✅ This model (text only) |

## Capabilities

<!-- 简短描述支持的能力 -->

- ✅ Chat / Multi-turn conversation
- ✅ Reasoning (configurable depth)
- ✅ Function calling / Tool use
- ✅ Structured output (JSON mode)
- ❌ Vision (text-only)
- ❌ Audio input

## Pricing

<!-- 定价表 -->

| Tier | Price |
|------|-------|
| Input | ${prompt_token_price}/M tokens |
| Output | ${completion_token_price}/M tokens |
| Cache read | {cache_read_multiplier × 100}% of input |
| Cache write | {cache_write_multiplier × 100}% of input |

**Real-world cost example:** An agent making 50 calls/day × 4K tokens/call ≈ ${monthly_estimate}/month.

## Quick Start

```bash
curl -X POST https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model.name}",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 256
  }'
```

## Python Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.sandbase.ai/v1",
    api_key="your-sandbase-key",
)

response = client.chat.completions.create(
    model="{model.name}",
    messages=[{"role": "user", "content": "Explain quantum computing in 3 sentences."}],
    max_tokens=256,
)
print(response.choices[0].message.content)
```

## FAQ

**Q: What is the context window?**
A: {context_length/1000}K tokens (approximately {context_length * 0.75 / 1000}K words).

**Q: Does it support streaming?**
A: Yes. Add `"stream": true` to the request body.

**Q: Can I use it with the OpenAI SDK?**
A: Yes. Point `base_url` to `https://api.sandbase.ai/v1` and use your SandBase API key.

**Q: Is there a free tier?**
A: New accounts get free credits. After that, pay-as-you-go with no minimum.

## Related

- [{similar_model_1}](/model/{vendor}/{slug})
- [{similar_model_2}](/model/{vendor}/{slug})
- [{comparison_blog}](/blog/{slug})
```

### 按模型类型的变体

**LLM 模型：** 用上面的完整模板。

**Image/Video 生成 API：** 替换 Quick Start 为对应的请求格式，FAQ 调整为：
- Q: What resolutions are supported?
- Q: How long does generation take?
- Q: What is the cost per image/video?

**Data API（Instagram, Douyin 等）：** 替换为：
- Overview 说明数据源和更新频率
- Best For 说明典型用途（竞品监控、KOL 筛选等）
- 加入 Response Example（JSON 片段）
- FAQ 调整为：
  - Q: How fresh is the data?
  - Q: What rate limits apply?
  - Q: Do I need the target platform's credentials?

### 批量生成方式

可以用 AI 批量生成 readme：

1. 从数据库导出所有模型的 `name`, `display_name`, `vendor`, `type`, `description`, `capability_tags`, `model_card` 字段
2. 用 prompt 模板 + LLM 为每个模型生成符合上述规范的 readme
3. 批量写回数据库的 `model_card.readme` 字段
4. 人工抽查 10-20 个确认质量后全量更新

建议优先处理高展现页面（按 GSC 展示量排序前 100 个模型），再批量处理剩余。

### 内容质量底线

- 每个 readme 至少 300 词（Google 倾向于收录有深度的页面）
- 避免纯复制 model description（会被判定为 thin content）
- 必须包含至少 1 个代码示例
- 必须包含至少 3 个 FAQ
- Related 区块至少链接 2 个相关页面（内链价值）

---

## 验收标准

完成上述优化后，预期 2-4 周内观察到：

- [ ] 整体 CTR 从 1.3% 提升到 2.5%+
- [ ] Top 3 高展现页面 CTR 各提升 3-5 个百分点
- [ ] 排名 5-10 的页面中至少 3 个进入 Top 5
- [ ] DeepSeek Harness 系列关键词占据 Top 3

---

## 参考

- SEO 巡检 playbook：`sandbase-daily-ops/playbooks/seo-geo-daily.md`
- 每日自动报告：`sandbase-daily-ops/outputs/seo-daily-reports/`
- Google 服务账号（GSC API）：`/root/.config/sandbase/google-service-account.json`
