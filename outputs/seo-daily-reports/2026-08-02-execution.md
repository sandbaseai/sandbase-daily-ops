# SEO 执行报告 - 2026-08-02

## 当日指标

| 指标 | 数值 |
|------|------|
| 已编入页数 | 514 |
| 未编入页数 | 2405 |
| 28 天总展现 | 5,867 |
| 28 天总点击 | 148 |
| 平均 CTR | 2.5% |
| 平均排名 | 17.9 |

## 执行内容

### 1. 技术修复（sandbase-monorepo v2.82.0 + v2.83.0）

| 改动 | PR | 状态 |
|------|-----|------|
| /models SSR 分页列表（排除 type=api） | #417 | ✅ 已合并 |
| /apis SSR 分页列表（type=api，979个） | #417 | ✅ 已合并 |
| /vendor/{slug} 厂商集合页（117个） | #417 | ✅ 已合并 |
| /vendor 索引页 | #417 | ✅ 已合并 |
| 模型详情页相关模型互链 | #416 | ✅ 已合并 |
| Sitemap priority 分层 | #416 | ✅ 已合并 |
| sitemap-vendors.xml（117 URLs） | #417 | ✅ 已合并 |
| Ingress: /models, /apis, /vendor, /collection, /solutions → model-pages | #417 | ✅ 已合并 |
| Dashboard 页码分页（50/页） | #416 | ✅ 已合并 |
| Dashboard 卡片简化（2列、价格、去标签） | #416 | ✅ 已合并 |
| 修复 canonical 硬编码为 / 的 bug | #418 | ✅ 已合并 |
| 修复 routes.go 引用不存在 handler | #418 | ✅ 已合并 |

### 2. 博客 Title/Description 优化（sandbase-blog）

| 文章 | 展现 | 优化点 |
|------|------|--------|
| Dify AI Platform Explained | 1,048 | 加入 "2026 Guide"、提及竞品对比 |
| LiteLLM vs OpenRouter | 125 | 强调 "Self-Hosted vs Managed" |
| Dify vs LangGraph | 144 | 问句标题引导点击 |
| LiteLLM Model Gateway | 196 | 强调 "100+ LLM"、"unified API" |
| Best AI Sandboxes | 136 | 列出所有品牌名 |
| LangChain/LangGraph | 106 | 加入 "Guide & Comparison" |
| Warp Terminal | 103 | 突出 "AI-Native IDE" |

### 3. 发现的问题

| 问题 | 严重性 | 状态 |
|------|--------|------|
| /apis 在 Google 中是 404 状态 | 🔴 高 | 修复已部署，需 Request Indexing |
| 所有 dashboard 页面 canonical 指向 / | 🔴 高 | #418 已修复 |
| /models 页面之前不存在（404） | 🔴 高 | #417 已修复 |
| 模型页只有 254/2173 有展现 | 🟡 中 | 等内链+分页生效后改善 |
| Dify 文章 1048 展现仅 1 点击 | 🟡 中 | Title 已优化 |

### 4. URL 架构规划

创建了 `docs/design/url-architecture.md`，规划：
- `/vendor/{slug}` — 厂商集合页（已实现）
- `/collection/{slug}` — 策展集合页（待实现）
- `/solutions/{slug}` — 解决方案页（待实现）

## Search Console 关键数据

### 按页面类型
| 类型 | 页面数 | 点击 | 展现 |
|------|--------|------|------|
| /model/ | 254 | 17 | 2,120 |
| /blog/ | 85 | 43 | 3,086 |
| /docs/ | 50 | 0 | 442 |
| 其他 | 53 | 90 | 1,414 |

### 按地区
| 地区 | 点击 | 展现 |
|------|------|------|
| 中国 | 39 | 219 |
| 美国 | 21 | 2,078 |
| 新加坡 | 19 | 146 |
| 日本 | 10 | 216 |
| 印度 | 8 | 218 |

### 接近首页的页面（排名 5-15）
| 页面 | 排名 | 展现 |
|------|------|------|
| /blog/dify-vs-langgraph-2026/ | 6.9 | 144 |
| /blog/30-days-ai-infrastructure-startup-discoverable/ | 6.2 | 95 |
| /agents | 7.5 | 85 |
| /blog/glm-5-1-open-weight-swe-bench-pro-2026/ | 9.2 | 71 |

## 明日待做

- [ ] 验证 v2.83.0 部署后 /models, /apis, /vendor 正常
- [ ] Search Console: Request Indexing /apis
- [ ] Search Console: 提交 10 个 /vendor/ 页面
- [ ] Search Console: 提交 10 个高价值未索引模型页
- [ ] 检查博客标题优化后的 CTR 变化
