# SEO & GEO 每日运维清单

> 每天花 10-15 分钟执行，持续提升搜索可见性和索引覆盖率。

---

## 一、Search Console 检查（5 分钟）

### 1. 索引覆盖率
- 打开 [Search Console > Pages](https://search.google.com/search-console/index)
- 记录：已编入 ___，未编入 ___
- 查看 "Why pages aren't indexed" 前 3 个原因
- 如果有新的 "Crawled - not indexed" 页面，检查内容是否太薄

### 2. 手动提交索引（每天 10-20 个）
- 进入 URL Inspection
- 提交未编入的高价值页面：
  - 优先：热门模型（GPT-5.x、Claude、Gemini、DeepSeek）
  - 其次：新上线的 /vendor/{slug} 页面
  - 再次：/apis 列表页分页
- 提交格式：`https://www.sandbase.ai/model/{vendor}/{slug}`

### 3. 检查错误
- 是否有新的 404 / 5xx 错误
- 是否有新的 "Excluded by noindex" 页面
- 是否有 canonical 异常

---

## 二、内容优化（5 分钟）

### 4. 检查高展现低点击页面
- Search Console > Performance > Pages，按展现排序
- 找 CTR < 2% 且展现 > 50 的页面
- 优化这些页面的 title 和 meta description：
  - Title 包含目标关键词 + 吸引点击的修饰词（"2026"、"Guide"、"vs"、"Best"）
  - Description 在 150 字符内，包含行动号召或价值主张

### 5. 检查排名 5-20 的页面（有机会进首页）
- Search Console > Performance > Queries，按排名筛选 5-20
- 这些页面只需要小幅提升就能进 top 5
- 操作：从其他页面给它们加内链、更新内容丰富度

---

## 三、GEO（Generative Engine Optimization）

### 6. 结构化数据检查
- 用 [Rich Results Test](https://search.google.com/test/rich-results) 抽查 2-3 个模型页
- 确认 JSON-LD 无错误
- 确认 BreadcrumbList、SoftwareApplication schema 正确

### 7. AI 搜索引擎可见性
- 在 ChatGPT/Perplexity/Google AI Overview 中搜索核心关键词：
  - "best ai model api"
  - "sandbase ai"
  - "{vendor} model pricing"
- 确认 sandbase.ai 是否被引用
- 如果没有，考虑在内容中增加直接回答问题的段落（FAQ 格式）

---

## 四、每周任务（每周一做一次）

### 8. Sitemap 状态
- 检查 https://www.sandbase.ai/sitemap-index.xml 是否正常
- 确认 sitemap-models.xml 数量与实际模型数一致
- 确认 sitemap-vendors.xml 包含所有厂商

### 9. 新内容覆盖
- 本周新增了哪些模型？确认它们出现在 sitemap 中
- 新模型的详情页内容是否足够丰富（>200 字描述）
- 薄页面列表（description 为空的模型）：考虑补充内容

### 10. 外链和社交
- 在 Reddit (r/LocalLLaMA, r/MachineLearning)、HN、Discord 分享有价值的对比文章
- 检查 Ahrefs/Semrush 的新增反向链接
- 对比类文章（X vs Y）是最容易获得自然外链的

---

## 五、关键指标追踪

每天记录：

| 日期 | 已编入页数 | 总展现 | 总点击 | 平均排名 | 备注 |
|------|-----------|--------|--------|---------|------|
| 8/2  | 514       | 5867   | 148    | 17.9    | 部署 v2.83.0 |

---

## 六、当前待处理事项

- [ ] 等 v2.83.0 部署完成后，验证 /models、/apis、/vendor 页面正常
- [ ] 在 Search Console 对 /apis 做 Request Indexing（之前是 404）
- [ ] 提交 /vendor/openai、/vendor/google 等高价值厂商页
- [ ] canonical 修复已部署，对 /pricing、/agents 做 Request Indexing
- [ ] 博客标题优化已推送，等博客 CI 重建后检查效果
- [ ] 检查 Dify 文章排名变化（当前 1048 展现，目标进 top 10）
- [ ] 117 个 vendor 页面分批提交索引（每天 10-20 个）

---

## 参考资源

- Search Console: https://search.google.com/search-console
- Rich Results Test: https://search.google.com/test/rich-results
- URL Architecture 文档: `sandbase-monorepo/docs/design/url-architecture.md`
- Google 服务账号: `/root/.config/sandbase/google-service-account.json`
  - 可通过 API 批量查询索引状态（脚本已验证可用）
- SEO Daily Check 脚本: `skills/api-launch-publish/scripts/seo_daily_check.py`
