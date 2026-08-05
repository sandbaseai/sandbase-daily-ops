# 博客文章发布流程（Daily Ops）

> 从热点监控到文章上线的标准化流程。每天跑一次热点检测，有选题就走这个流程。

---

## 一、热点检测（每日 1 次，1 分钟）

```bash
cd /root/kiro/sandbase-daily-ops
python3 scripts/daily_hot_topics.py
```

输出：Top 10 热点 + 搜索量建议 + 选题机会。

### 选题决策标准

| 优先级 | 条件 | 行动 |
|--------|------|------|
| 🔴 高 | 月搜索量 > 50K 且未覆盖 | 当天写 |
| 🔴 高 | 当天/昨天发布的热门模型 | 当天写 |
| 🟡 中 | 已有文章但需更新 | 安排本周更新 |
| 🟢 低 | 新框架/工具，热度未确认 | 观察 2-3 天再决定 |

---

## 二、写作（10-30 分钟/篇）

### 前置检查

```bash
# 检查 content-index.md 避免重复
cat /root/kiro/sandbase-blog/scripts/ai-content-generator/content-index.md | grep -i "<关键词>"
```

### 文章规格

| 维度 | 要求 |
|------|------|
| 字数 | EN 1500-2500 词，ZH 2000-3500 字 |
| 结构 | TL;DR + 经验发现式开头 + 对比表格 + FAQ |
| SEO | EN title ≤60 字符，ZH title ≤30 字符 |
| 内链 | 至少 2 条指向站内文章 |
| 封面 | 信息不要太密：标题 ≤8 词，底部标签 ≤4 个，留白 ≥25% |
| 禁用 | 无 "seamlessly"、"game-changer"、"let's dive in" 等 AI 味句式 |

### 写入路径

```
sandbase-blog/src/content/en/<slug>.md
sandbase-blog/src/content/zh-CN/<slug>.md
```

### Category 选择

| 文章类型 | category |
|----------|----------|
| 模型介绍 | model-introduction |
| 模型对比 | model-comparison |
| Top N 推荐 | best-of |
| 开发者工具 | developer-tools |
| Agent 场景 | agent-use-cases |
| 教程 | tutorials |

---

## 三、生成封面（2 分钟）

```bash
cd /root/kiro/sandbase-daily-ops/skills/api-launch-publish/scripts

python3 generate_blog_cover_url.py \
  --title "<英文短标题，6-8词>" \
  --description "<一句话描述>" \
  --category <category> \
  --article-type <deep-dive|model-intro|comparison|tutorial> \
  --image-alt "<封面 alt text>" \
  --out-json /tmp/<slug>-cover.json \
  --update-markdown /root/kiro/sandbase-blog/src/content/en/<slug>.md \
  --update-markdown /root/kiro/sandbase-blog/src/content/zh-CN/<slug>.md
```

### 封面信息密度控制（重要）

生成封面时注意：
- **标题**：最多 6-8 个英文单词
- **副标题**：最多 1 行 10 个词
- **评估维度**：最多 4 项
- **底部标签**：最多 4 个
- **留白**：整体至少 25% 空间
- **禁止**：中文文字、暗色背景、真人照片

---

## 四、上传到永久存储（1 分钟）

```bash
cd /root/kiro/sandbase-blog/scripts

# EN 文章
python3 migrate_covers.py --locale en

# ZH 文章
python3 migrate_covers.py --locale zh-CN
```

验证 frontmatter 中 URL 格式：
```
image: https://static.sandbase.ai/blog/covers/<slug>.jpg  ✅
image: https://media.sandbase.ai/files/...                 ❌ 临时URL，不可用
```

---

## 五、构建验证（1 分钟）

```bash
cd /root/kiro/sandbase-blog
npm run build
```

确认：
- [ ] 构建无报错
- [ ] 新文章的 HTML 在 `dist/<slug>/index.html` 和 `dist/zh-CN/<slug>/index.html`

---

## 六、更新 Content Index

```bash
# 在 content-index.md 中追加行
# 格式：| date | title | slug | type | category | tags | description | locale | words | cover |
# 封面已上传则标 ✅，否则 ❌
```

---

## 七、部署 + 提交索引

```bash
# 部署
cd /root/kiro/sandbase-blog
git add .
git commit -m "publish: <slug> (EN+ZH)"
git push origin main

# 提交 IndexNow（可选，加速 Bing 收录）
cd /root/kiro/sandbase-daily-ops
python3 scripts/submit_indexnow.py --urls \
  "https://blog.sandbase.ai/<slug>" \
  "https://blog.sandbase.ai/zh-CN/<slug>"
```

---

## 八、快速参考命令

### 完整发布流程（复制粘贴版）

```bash
# 1. 生成封面
cd /root/kiro/sandbase-daily-ops/skills/api-launch-publish/scripts
python3 generate_blog_cover_url.py \
  --title "TITLE" --description "DESC" \
  --category CATEGORY --article-type TYPE \
  --update-markdown /root/kiro/sandbase-blog/src/content/en/SLUG.md \
  --update-markdown /root/kiro/sandbase-blog/src/content/zh-CN/SLUG.md

# 2. 上传到 CDN
cd /root/kiro/sandbase-blog/scripts
python3 migrate_covers.py --locale en
python3 migrate_covers.py --locale zh-CN

# 3. 构建验证
cd /root/kiro/sandbase-blog
npm run build

# 4. 部署
git add . && git commit -m "publish: SLUG" && git push origin main
```

---

## 关联文件

- 热点监控脚本：`/root/kiro/sandbase-daily-ops/scripts/daily_hot_topics.py`
- 封面生成脚本：`skills/api-launch-publish/scripts/generate_blog_cover_url.py`
- 封面上传脚本：`/root/kiro/sandbase-blog/scripts/migrate_covers.py`
- 内容索引：`/root/kiro/sandbase-blog/scripts/ai-content-generator/content-index.md`
- 视觉规范：`skills/api-launch-publish/references/visual-system.md`
- 写作规范：`skills/api-launch-publish/references/writing-style.md`
- SEO 规范：`skills/api-launch-publish/references/seo-standards.md`
- 质量门检：`skills/api-launch-publish/references/quality-gates.md`
