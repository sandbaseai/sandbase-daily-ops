# 博客运营最佳实践（经验总结）

> 从实际操作中积累的坑和解决方案。每次踩新坑时更新此文件。

---

## 一、文章开头：经验发现式 vs 概述式

### 问题

AI 生成的文章开头通常是概述式——"X is a Y that does Z, launched on date D"。这种开头：
- 读起来像产品说明书
- 没有人味
- 读者第一段就判断"又是 AI 水文"，跳出

### 解决方案：经验发现式开头

用一个具体场景、数字、或亲身踩坑体验开头。让读者在第一段就感受到"写这篇的人真的用过"。

#### 好的模式

```markdown
## EN 示例
I was running a 140-iteration refactoring agent on Claude Opus 4.7. 
The invoice was $47. Swapped to Qwen 3.7 Max — same task, same result. 
Invoice: $2.80. That's not a typo.
```

```markdown
## ZH 示例
上周跑一个 140 轮重构 Agent，用 Opus 4.7，账单 $47。
换成 Qwen 3.7 Max，同任务同结果，$2.80。不是打错了。
```

#### 坏的模式（禁止）

```markdown
❌ Qwen 3.7 Max is Alibaba's flagship model launched on May 20, 2026.
   It features a 1M context window and...

❌ In today's rapidly evolving AI landscape, a new model has emerged...

❌ Alibaba has released their latest generation model, which represents
   a significant advancement in...
```

### 规则

1. **第一段必须有具体数字或场景**（价格、时间、轮数、错误信息）
2. **第一人称 "I" / "我"**——署名是 SandBase Team 但正文像高级工程师在写
3. **前 3 段内暴露一个判断或观点**——不要两边讨好
4. **限定性声明建立信任**——"我没测完"、"benchmark 数据不全"、"这块不确定"
5. **TL;DR 放最前面**——但 TL;DR 用数据说话，不用形容词

---

## 二、封面设计：呼吸感

### 问题

gpt-image-2 生成的封面默认信息过密——文字堆满、元素挤在一起、没有喘气空间。在博客列表页缩略图下看起来像一团噪音。

### 解决方案

1. **标题最多 6-8 个英文单词**
2. **副标题最多 10 个词，1 行**
3. **画面至少 25% 留白**
4. **底部标签最多 4 个**
5. **架构图节点最多 5 个**

### Prompt 追加指令

每次生成封面时，在 prompt 末尾加：
```
IMPORTANT: Leave generous whitespace between all elements.
The cover must feel spacious, not cramped.
At least 25% of the canvas should be empty white space.
Limit text to headline (max 8 words) + subtitle (max 10 words).
Do not fill every corner. Breathing room is critical.
```

### 验收标准

- 缩小到 200×112px 缩略图后，标题仍可辨认
- 元素之间有明显间距（不紧贴）
- 整体感觉是"清爽的技术杂志封面"而非"挤满信息的 infographic"

---

## 三、截图配图：选源和质量控制

### 问题

很多网站截图会遇到：
- Cookie 弹窗遮挡
- SPA 骨架屏（JS 未执行完）
- robots.txt 拦截
- 内容需要登录

### 可靠截图源（按成功率排序）

| 网站 | 成功率 | 适合 |
|------|--------|------|
| together.ai/models/{model} | ⭐⭐⭐ | 模型规格、benchmark |
| openrouter.ai/{vendor}/{model} | ⭐⭐⭐ | 定价对比 |
| artificialanalysis.ai/leaderboards | ⭐⭐⭐ | 排行榜 |
| huggingface.co/{org} | ⭐⭐⭐ | 开源社区数据 |
| chat.qwen.ai | ⭐⭐⭐ | 模型上线证据 |
| alibabacloud.com/.../qwen | ⭐⭐ | 平台全貌 |
| qwen.ai/blog?id={post} | ⭐⭐ | 官方发布（有时骨架屏） |
| lmarena.ai | ⭐ | 经常被 cookie 弹窗挡 |
| cryptobriefing.com | ⭐ | GDPR 弹窗 |
| medium.com | ❌ | 登录墙 |

### 流程

1. 调用 `dataforseo/v3/on_page/page_screenshot`
2. 下载到 `/tmp/` 检查（用 Image 工具看内容）
3. 确认无弹窗/骨架屏后上传到 COS
4. 插入文章，写好 alt text 和 caption

### 每篇文章截图配额

- 最少 3 张，理想 4-6 张
- 每 300-500 词之间放一张图
- 不要连续两个 H2 之间没有图

---

## 四、部署与索引：完整清单

### 部署前

- [ ] `npm run check` — 0 errors
- [ ] `npm run build` — page count 正确
- [ ] 截图全部验证通过（无弹窗/骨架屏）
- [ ] 中英文版 image URL 统一（指向 COS 永久地址）

### 部署

```bash
cd /root/kiro/sandbase-blog
git add -A
git commit -m "feat(blog): ..."
git push origin main
```

### 部署后（1-2 分钟等 Cloudflare 构建）

- [ ] 访问 `https://blog.sandbase.ai/blog/{slug}/` 确认页面正常
- [ ] Google Indexing API 提交新/更新的 URL
- [ ] IndexNow 提交（Yandex 正常，Bing 待验证）
- [ ] 检查 OG 图片是否正确显示（分享到社交媒体预览）

---

## 五、SEO 优化：从 GSC 数据驱动

### 每周做一次

1. **拉 GSC 28 天数据**（按 page 维度，blog 目录过滤）
2. **找 3 类机会**：
   - 🔴 高曝光低 CTR（title/desc 需改）
   - 🟡 pos<10 零点击（snippet 不吸引人）
   - 🟠 pos 10-20（冲首页，加内链/更新内容）
3. **用 DataForSEO 验证关键词搜索量**
4. **改 title + description + updatedDate**
5. **部署 + 提交索引**

### Title 优化规则

- 精确匹配搜索词（"LangChain vs LangGraph" 而不是 "LangGraph vs LangChain"）
- 加 "(2026)" 提升时效性点击
- 加问句式或结论式吸引点击（"Which Should You Pick?"）
- 控制 60 字符以内

### Description 优化规则

- 第一句给结论（snippet 抓第一句）
- 包含具体数字或对比结论
- 120-155 字符
- 包含 CTA 暗示（"Full comparison inside"、"Ranked with pros and cons"）

---

## 六、常见错误检查清单

| 错误 | 后果 | 预防 |
|------|------|------|
| 中文版 image URL 没更新 | 指向临时 media URL | 封面上传后检查所有 4 个文件 |
| description 超 160 字符 | SERP 截断 | 写完数字符 |
| 忘了加 updatedDate | Google 不知道内容更新了 | 每次改 title/desc 都加 |
| 截图是骨架屏 | 读者看到空白图失去信任 | 每张截图先下载 Image 检查 |
| 内链用了绝对 URL | 跨环境出问题 | 一律用 `/blog/{slug}` 相对路径 |
| TL;DR 用形容词 | 没有信息量 | 用数字和具体对比 |
