# 模型详情页 SEO 优化方案

> 创建日期：2026-08-01
> 问题：262 个模型详情页有 2163 次展示、仅 17 次点击（CTR 0.79%）
> 目标：CTR 提升到 3-5%（行业标准），即从 17 到 65-108 点击/30天

---

## 1. 问题诊断总结

### 1.1 根本原因：Prerender 失效

| 事实 | 证据 |
|---|---|
| Googlebot 收到的 title | "SandBase - Agent-native Platform for AI Agents"（所有 262 页一样） |
| Googlebot 收到的 description | 通用平台描述 |
| HTML 大小（Googlebot UA） | 25167 字节 = index.html shell |
| HTML 大小（普通 UA） | 25167 字节 = 同样的 shell |
| 已 prerender 列表中的 `/models` | 同样返回 shell |

**结论**：nginx 的 prerender 逻辑有效（配置正确），但 `dist/prerender/` 目录中没有生成文件。prerender.ts 要么没有在 CI/CD 中运行，要么运行失败了。

### 1.2 次要问题：Title/Description 模板弱

即使 prerender 修复后（或 Google JS renderer 采用了 JS 生成的 title），当前模板也有问题：

| 问题 | 影响 | 数据 |
|---|---|---|
| Vendor 名在 title 中重复 | 浪费 title 空间，看起来冗余 | 45% 的页面（127/280） |
| 缺少意图关键词 | 不匹配搜索意图 | "pricing"、"free"、"alternative" 等完全缺失 |
| Description 无差异化 | 262 页几乎相同的 snippet | 通用模板 |
| 无定价/规格信息 | 不如竞品吸引点击 | 用户搜"gpt-5.6 sol pro"想看定价 |

### 1.3 其他问题

- Cloudflare HTTP→HTTPS 用的是 **302**（应为 301），不传递 link equity
- prerender 列表完全没有 `/model/` 动态路由

---

## 2. 优化方案（按优先级排序）

### P0: 修复 prerender 或实现服务端 meta injection

**方案 A（推荐）：API Server 端 Meta Injection**

在 nginx 配置中，当请求路径匹配 `/model/*` 且 UA 是爬虫时，将请求转发到 apiserver 的一个新端点 `GET /seo/render?path=...`，apiserver 返回注入了正确 meta 的完整 HTML。

优势：
- 不依赖 Puppeteer/prerender 的维护
- 实时反映模型数据变化（价格更新、新模型上线）
- 不需要每次部署跑 prerender
- 可复用 sitemap 中已有的模型查询逻辑

实现：
```go
// GET /seo/render?path=/model/openai/gpt-5.6-sol-pro
// 返回注入了正确 <title>、<meta description>、JSON-LD 的 index.html
func (h *SEOHandler) RenderMeta(c *gin.Context) {
    path := c.Query("path")
    // 解析 /model/{vendor_slug}/{model_slug}
    // 查询模型数据
    // 用 template 注入 meta 到 index.html
    // 返回完整 HTML
}
```

nginx 配置修改：
```nginx
location / {
    if ($prerender = 1) {
        # 模型详情页 → API server 动态渲染
        rewrite ^/model/(.+)$ /seo/render?path=/model/$1 last;
        # 静态页 → prerender 文件
        rewrite ^/$ /prerender/index.html last;
        rewrite ^/(.+?)/?$ /prerender/$1.html last;
    }
    try_files $uri $uri/ /index.html;
}

location /seo/render {
    internal;
    proxy_pass http://sandbase-apiserver.${NGINX_NAMESPACE}.svc.cluster.local:8080;
    proxy_set_header Host $host;
}
```

**方案 B（备选）：修复现有 prerender + 动态路由**

修复 CI/CD 中 prerender 步骤，并在 prerender.ts 中加入动态模型路由：

```typescript
// 从 API 获取所有模型 slug，加入 ROUTES
const modelsResp = await fetch('https://api.sandbase.ai/v1/models?pageSize=500&page=1');
const models = (await modelsResp.json()).data;
for (const m of models) {
  ROUTES.push(`/model/${m.vendor_slug}/${m.model_slug}`);
}
```

缺点：
- 每次部署需要跑 prerender（增加 CI 时间）
- 新模型上线到被 prerender 有延迟
- 2000+ 页面的 Puppeteer 渲染可能很慢/不稳定

### P1: 改进 Title 模板

**当前**：`{display_name} - {vendor} API | SandBase`
**问题**：Vendor 重复 + 无意图词

**新模板**：

```typescript
function generateModelTitle(model: ModelDetail): string {
  const displayName = model.display_name || model.name;
  const vendor = model.vendor || '';
  
  // 去除 display_name 中的 vendor 前缀（如 "DeepSeek: DeepSeek V4 Flash" → "DeepSeek V4 Flash"）
  let cleanName = displayName;
  if (cleanName.toLowerCase().startsWith(vendor.toLowerCase() + ':')) {
    cleanName = cleanName.slice(vendor.length + 1).trim();
  }
  
  // 根据模型类型选择意图词
  const intentWord = getIntentWord(model.type);
  
  // 新格式："{Clean Name} API - {Intent} | SandBase"
  // 例: "GPT-5.6 Sol Pro API - Pricing & Docs | SandBase"
  // 例: "LTX-2.3 22B Video API - Free Trial | SandBase"
  return `${cleanName} API - ${intentWord} | SandBase`;
}

function getIntentWord(type: string): string {
  switch (type) {
    case 'llm': return 'Pricing & Docs';
    case 'image': return 'Image Generation API';
    case 'video': return 'Video Generation API';
    case 'audio': return 'Audio API';
    case 'embedding': return 'Embedding API';
    default: return 'API Documentation';
  }
}
```

**效果对比**：

| 当前 | 优化后 |
|---|---|
| DeepSeek: DeepSeek V4 Flash - DeepSeek API \| SandBase | DeepSeek V4 Flash API - Pricing & Docs \| SandBase |
| Anthropic: Claude Opus 4.1 - Anthropic API \| SandBase | Claude Opus 4.1 API - Pricing & Docs \| SandBase |
| LTX-2.3 22B Distilled - Lightricks API \| SandBase | LTX-2.3 22B Distilled - Video Generation API \| SandBase |
| MiniMax Voice Cloning - MiniMax API \| SandBase | MiniMax Voice Cloning - Audio API \| SandBase |

### P2: 改进 Description 模板

**当前**：`Use {name} by {vendor} through SandBase API. Compare pricing, capabilities, and start building.`

**新模板**：

```typescript
function generateModelDescription(model: ModelDetail): string {
  // 优先使用模型自带的 description（前 120 字符）
  if (model.description) {
    const baseDesc = model.description.slice(0, 120).replace(/\[.*?\]\(.*?\)/g, '').trim();
    // 追加 CTA 和关键规格
    const specs = getKeySpecs(model);
    return `${baseDesc}. ${specs} Try free on SandBase.`;
  }
  
  // Fallback: 包含具体规格
  const specs = getKeySpecs(model);
  return `${model.display_name} by ${model.vendor}. ${specs} Available via OpenAI-compatible API on SandBase. Start free.`;
}

function getKeySpecs(model: ModelDetail): string {
  const parts: string[] = [];
  if (model.context_length) parts.push(`${(model.context_length/1000).toFixed(0)}K context`);
  if (model.pricing?.prompt_token_price) parts.push(`from $${model.pricing.prompt_token_price}/M tokens`);
  if (model.capability_tags?.length) parts.push(model.capability_tags.slice(0, 2).join(', '));
  return parts.join('. ') + (parts.length ? '.' : '');
}
```

**效果示例**：

| 页面 | 新 Description |
|---|---|
| text-embedding-v4 | "Alibaba Cloud Model Studio text-embedding-v4 is a Qwen3-Embedding series text embedding model for semantic search. 1048K context. Try free on SandBase." |
| gpt-5.6-sol-pro | "GPT-5.6 Sol Pro is the same underlying model as GPT-5.6 Sol, served with reasoning. 1048K context. from $2.00/M tokens. Try free on SandBase." |
| claude-opus-4.1 | "Claude Opus 4.1 is an updated version of Anthropic's flagship model, offering improved performance in coding, reasoning. Try free on SandBase." |

### P3: Cloudflare 302 → 301

在 Cloudflare Dashboard → Rules → Redirect Rules 中添加：

```
When: Host = www.sandbase.ai AND Scheme = http
Then: 301 redirect to https://www.sandbase.ai/{path}
```

或者关闭 "Always Use HTTPS"，改用 Page Rule：
```
URL: http://*sandbase.ai/*
Setting: Forwarding URL (301)
Destination: https://www.sandbase.ai/$2
```

---

## 3. 实施顺序

| 步骤 | 优先级 | 预期影响 | 工时 |
|---|---|---|---|
| 1. 实现 API Server Meta Injection | P0 | 最大：Google 能看到正确 title | 4-6h |
| 2. 改进 title 模板（ModelDetail.tsx + API render） | P1 | 提升 CTR | 1-2h |
| 3. 改进 description 模板 | P2 | 提升 CTR | 1-2h |
| 4. Cloudflare 302→301 | P3 | 传递 link equity | 10min |
| 5. 验证：用 GSC URL Inspection 确认新 meta | — | 确认修复 | 30min |

---

## 4. 成功指标

| 指标 | 当前 | 目标（4 周后） |
|---|---|---|
| 模型页 CTR | 0.79% (17/2163) | ≥3% |
| 0 点击页面数 | 246/259 | ≤100 |
| 平均排名 | 18.0 | ≤15（排名应自然提升因为 CTR 信号改善） |
| 展示量 | 2163 | ≥3000（更好的 title 匹配更多查询） |

---

## 5. 验证清单

- [ ] Googlebot UA 请求 `/model/openai/gpt-5.6-sol-pro` 返回正确 title
- [ ] `curl -H "User-Agent: Googlebot" https://www.sandbase.ai/model/openai/gpt-5.6-sol-pro | grep '<title>'` 显示模型名
- [ ] GSC URL Inspection 显示 rendered title 正确
- [ ] Google cache 页面显示正确标题（可能需要 1-2 周）
- [ ] HTTP→HTTPS 返回 301
