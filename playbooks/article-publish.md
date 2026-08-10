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
| 截图 | **每篇不少于 3 张**（见下方截图规范）|
| 作者 | 从 `src/data/authors.ts` 中选择合适的人 |
| 封面 | gpt-image-2 信息密集型，白底三栏 |
| 禁用 | 无 "seamlessly"、"game-changer"、"let's dive in" 等 AI 味句式 |

### 截图规范（每篇必须 ≥3 张）

> 截图是文章真实感和视觉丰富度的关键。没有截图的文章看起来像 AI 水文。

**数量要求：每篇文章至少 3 张截图**，推荐 3-5 张。分布在文章不同段落中。

**截图类型建议：**

| 类型 | 适用场景 | 推荐来源 |
|------|---------|---------|
| 产品首页/官网 | 介绍新工具/平台 | 该产品官网 |
| 控制台/Dashboard | 展示使用体验 | 产品后台截图 |
| 代码编辑器 | 展示 IDE 集成 | VS Code / Cursor 截图 |
| 排行榜/Benchmark | 模型对比文章 | artificialanalysis.ai, lmarena.ai |
| API 文档页 | 开发者工具文章 | 官方 docs 页面 |
| GitHub 仓库 | 开源项目介绍 | github.com/{org}/{repo} |
| 定价页面 | 成本对比文章 | 产品 pricing page |

**截图命令：**

```bash
export SANDBASE_API_KEY=$(grep SANDBASE_API_KEY ~/.config/sandbase/.env | tail -1 | cut -d= -f2)

curl -s -X POST https://api.sandbase.ai/v1/run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -d '{
    "model": "dataforseo/v3/on_page/page_screenshot",
    "url": "https://目标URL",
    "browser_preset": "desktop",
    "full_page_screenshot": false,
    "disable_cookie_popup": true,
    "accept_language": "en"
  }'
```

**截图处理流程：**

1. 调用 API 截图 → 获取 DataForSEO CDN URL
2. 下载到 `/tmp/` 验证（无弹窗/骨架屏）
3. 上传到 COS → `static.sandbase.ai/blog/screenshots/{slug}-{描述}.png`
4. 在 EN 和 ZH 文章中用 Markdown 图片语法嵌入：

```markdown
![Alt description in English](https://static.sandbase.ai/blog/screenshots/{slug}-{name}.png)
*Caption explaining what the screenshot shows and its source.*
```

**截图分布原则：**
- 第 1 张：紧跟文章开头或 TL;DR 之后（引起兴趣）
- 第 2 张：在核心对比/分析段落中（佐证观点）
- 第 3 张：在实操/架构部分（增加可信度）
- EN 和 ZH 共用同一张截图，但 alt 和 caption 分别用英文/中文

**禁止：**
- ❌ 文章里没有任何截图
- ❌ 截图全部堆在文章开头或结尾
- ❌ 截图是骨架屏/加载中/被弹窗遮挡
- ❌ 使用临时 URL（media.sandbase.ai 或 api.dataforseo.com）

### 作者选择

| 作者 | 擅长领域 |
|------|---------|
| Marcus Chen | 基础设施、Agent runtime、部署 |
| Evelyn Park | ML 模型、LLM、多模态 |
| Daniel Russo | 开发工具、全栈、DX |
| Sophie Lin | 创意 API、视频/图像生成 |
| SandBase Team | 产品更新、通用 |

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

## 三、生成封面（3 分钟）

> ⚠️ 使用 `gpt-image-2` 一次性生成信息密集型封面（含完整文字和布局）。
> 不再使用旧的"背景+叠字"模式。

### Step 1：用 regen-one.ts 生成完整封面

```bash
cd /root/kiro/sandbase-blog/scripts/ai-content-generator

export SANDBASE_API_KEY=<your-key>
export COVER_MODEL=openai/gpt-image-2

npx tsx regen-one.ts <slug1> [slug2] ...
```

脚本会：
1. 读取文章的 title、description、category
2. 构建信息密集型 prompt（三栏布局、产品卡片、架构图、底部标签）
3. 调用 gpt-image-2 生成 16:9 PNG
4. 自动将临时 URL 写入 EN 和 ZH 的 frontmatter

### Step 2：迁移到永久 CDN

```bash
cd /root/kiro/sandbase-blog/scripts

python3 migrate_covers.py               # EN
python3 migrate_covers.py --locale zh-CN # ZH
```

这会把 `media.sandbase.ai/files/` 临时 URL 下载并上传到 `static.sandbase.ai/blog/covers/`。

### 封面风格（由 cover-generator.ts 中的 prompt 控制）

| 属性 | 要求 |
|------|------|
| 背景 | 白色/浅灰 #F8F8F6，**禁止暗色** |
| 布局 | 三栏：左标题+维度，中产品卡片，右架构图，底部标签栏 |
| 颜色 | 黑色文字 + SandBase Green #20B987 唯一强调色 |
| 文字 | 全英文，清晰可读，无中文 |
| 信息密度 | 标题 + 副标题 + 维度列表 + 产品卡片 + 架构图 + 底部栏 |
| 禁止 | 中文、暗色、渐变、真人、设备、霓虹 |

### 验收标准

- [ ] 封面是信息密集的白色背景信息图（不是纯抽象背景）
- [ ] 有清晰可读的英文标题
- [ ] URL 以 `https://static.sandbase.ai/blog/covers/` 开头
- [ ] 小缩略图（200×112px）下标题仍可辨认
- [ ] EN 和 ZH 共用同一张封面

---

## 四、更新 Frontmatter（1 分钟）

封面上传后，确认 frontmatter 中的 image URL 正确：

```bash
# 检查所有文章 image 字段
grep "^image:" /root/kiro/sandbase-blog/src/content/en/<slug>.md
grep "^image:" /root/kiro/sandbase-blog/src/content/zh-CN/<slug>.md
```

如果没有自动更新，手动写入：

```yaml
image: https://static.sandbase.ai/blog/covers/<slug>.jpg
```

验证 frontmatter 中 URL 格式：
```
image: https://static.sandbase.ai/blog/covers/<slug>.jpg  ✅
image: https://media.sandbase.ai/files/...                 ❌ 临时URL，不可用
image:                                                     ❌ 空，没封面
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
SLUG="your-article-slug"

# 1. 生成封面 (gpt-image-2 一次性信息密集型)
cd /root/kiro/sandbase-blog/scripts/ai-content-generator
export SANDBASE_API_KEY=$(grep SANDBASE_API_KEY ~/.config/sandbase/.env | tail -1 | cut -d= -f2)
export COVER_MODEL=openai/gpt-image-2
npx tsx regen-one.ts ${SLUG}

# 2. 迁移封面到永久 CDN
cd /root/kiro/sandbase-blog/scripts
python3 migrate_covers.py
python3 migrate_covers.py --locale zh-CN

# 3. 构建验证
cd /root/kiro/sandbase-blog
npm run build

# 4. 部署
git add . && git commit -m "publish: ${SLUG} (EN+ZH)" && git push origin main

# 5. 提交索引
cd /root/kiro/sandbase-daily-ops
python3 scripts/submit_indexing.py --limit 10
python3 scripts/submit_indexnow.py --limit 10
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
