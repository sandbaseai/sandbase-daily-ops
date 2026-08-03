# SandBase 运维会话总结（2026-08-02 ~ 08-03）

> 下次开新会话时提供此文件作为上下文。

---

## 项目结构

```
/root/kiro/
├── sandbase-blog/          ← 博客（Astro + Cloudflare Pages）
├── sandbase-daily-ops/     ← 运维规范、skills、脚本（唯一规则来源）
├── sandbase-monorepo/      ← 主产品（dashboard、apiserver、registry、docs）
└── review/                 ← 代码审查记录
```

---

## 已完成的工作

### 1. 规则统一化

- **所有写作规范、封面规则、分类 prompt** 从 `sandbase-blog` 迁移到 `sandbase-daily-ops/skills/api-launch-publish/`
- blog 的 `prompts/` 目录只剩一个 `README.md` 指针
- 规则文件索引：

| 文件 | 内容 |
|------|------|
| `references/writing-style.md` | 禁用词、真人感、多语言、代码、图片 |
| `references/seo-standards.md` | 标题、关键词、内链、meta、FAQ、GEO |
| `references/category-writing-guide.md` | 分类写作指南、结构、选题去重 |
| `references/visual-system.md` | 封面视觉系统 + 6类分类策略 + 完整生成工作流 |
| `references/quality-gates.md` | 质量门 checklist |
| `references/blog-format.md` | 博客格式、frontmatter、3篇文章策略 |
| `prompts/*.md` | 11个分类 prompt |

### 2. 封面图全量重做

- 模型：`openai/gpt-image-2`（从 nano-banana-pro 切换，文字渲染更可靠）
- 路径：`static.sandbase.ai/blog/covers-v2/{slug}.png`（换了路径绕过 CDN 缓存）
- 96 篇文章 + 3 篇新文章 = 99 张封面全部重新生成
- 工具：`regen-all-covers.ts` → `migrate_covers.py` → COS 上传

### 3. 新文章（3 篇）

| 文章 | 目标关键词 | 月搜索量 |
|------|-----------|---------|
| `image-to-video-api-product-demo-generator-python` | image to video AI | 40,500 |
| `anthropic-prompt-caching-agents-save-cost-2026` | anthropic prompt caching | 1,300 |
| `best-ai-coding-assistants-2026` | ai coding assistant | 22,200 |

每篇都有：SandBase 入口、Related Reading（6链接）、gpt-image-2 封面。

### 4. SEO 优化

| 项目 | 之前 | 之后 |
|------|------|------|
| 标题超60字符 | 12篇 | 0 |
| Description太短 | 8篇 | 0 |
| 孤儿页面（零内链） | 80篇 | 0 |
| 内链总数 | ~50条 | 612+条 |
| Related Reading | 无 | 全部102篇都有6个链接 |

### 5. 索引提交

- **Google Indexing API**：25 URL 已提交（含新文章、未索引文章、VS文章）
- **Yandex IndexNow**：正常，每次 202 Accepted
- **Bing IndexNow**：❌ 403 `UserForbiddedToAccessSite`——需要重新验证

### 6. Bing Webmaster

- DNS 验证于 8/2 完成，8/2 当天可用（提交了 50 URL）
- 8/3 变为 403——可能验证过期或权限问题
- key 文件已部署到 `blog.sandbase.ai` 和 `www.sandbase.ai`
- **ACTION NEEDED**：去 Bing Webmaster Tools 重新验证两个域名

---

## 当前状态

### SEO 数据（8/3）

| 指标 | 值 |
|------|---|
| 全站展示 | 2,434/周 |
| 博客展示 | 1,068/周 |
| 博客点击 | 9/周 |
| 有数据页面 | 301 |
| 新文章索引 | 0/10（正常等待 3-14 天） |
| Top 文章 | dify-explained（515展示, 排名11.3） |

### 封面

- 模型：`openai/gpt-image-2`
- 路径：`static.sandbase.ai/blog/covers-v2/{slug}.png`
- 配置：`config.yaml` 里 `coverImage.model: "openai/gpt-image-2"`
- 生成脚本：`regen-all-covers.ts`
- 上传脚本：`migrate_covers.py`
- CDN 缓存：`max-age=14400`（4h），换路径可绕过

### 凭证位置

```
~/.config/sandbase/.env:
  SANDBASE_API_KEY    ← 图片生成、模型调用
  COS_SECRET_ID      ← 腾讯云 COS（static.sandbase.ai）
  COS_SECRET_KEY
  COS_REGION=ap-singapore
  DATAFORSEO_LOGIN   ← DataForSEO 关键词数据
  DATAFORSEO_PASSWORD
  
~/.config/sandbase/google-service-account.json ← Google Indexing API + GSC
```

---

## 待办事项

### 紧急

- [ ] Bing Webmaster 重新验证 `www.sandbase.ai` 和 `blog.sandbase.ai`
- [ ] 验证后重跑 `python3 scripts/submit_indexnow.py --limit 50`

### 日常（每天跑一次）

```bash
cd /root/kiro/sandbase-daily-ops
export $(grep -v '^#' ~/.config/sandbase/.env | xargs)

# SEO 巡检
python3 skills/api-launch-publish/scripts/seo_daily_check.py

# Google Indexing API（提交新/更新的 URL）
python3 -c "..." # 见 playbooks/seo-geo-daily.md

# IndexNow（Bing 恢复后）
python3 scripts/submit_indexnow.py --limit 50
```

### 下一步项目

1. **Docs AI Agent 友好化**（设计文档已写好）
   - 文件：`sandbase-daily-ops/outputs/docs-agent-friendly-design.md`
   - 核心：部署 `llms.txt`、`openapi.yaml`、修复 SPA catch-all
   
2. **继续写高搜索量文章**（DataForSEO 数据）
   - "ai video generator" — 246,000/月
   - "mcp protocol" — 5,400/月
   - "langchain vs langgraph" — 2,900/月

3. **封面质量监控**
   - 部分 gpt-image-2 生成的封面可能仍有中文（概率低但存在）
   - 需要人工抽检或写 OCR 检测脚本

---

## 关键文件路径

```
# 博客内容
/root/kiro/sandbase-blog/src/content/en/*.md
/root/kiro/sandbase-blog/src/content/zh-CN/*.md

# 封面生成
/root/kiro/sandbase-blog/scripts/ai-content-generator/regen-all-covers.ts
/root/kiro/sandbase-blog/scripts/ai-content-generator/regen-one.ts
/root/kiro/sandbase-blog/scripts/ai-content-generator/cover-generator.ts
/root/kiro/sandbase-blog/scripts/migrate_covers.py

# 规范（唯一权威来源）
/root/kiro/sandbase-daily-ops/skills/api-launch-publish/references/
/root/kiro/sandbase-daily-ops/skills/api-launch-publish/prompts/

# SEO
/root/kiro/sandbase-daily-ops/playbooks/seo-geo-daily.md
/root/kiro/sandbase-daily-ops/scripts/submit_indexnow.py
/root/kiro/sandbase-daily-ops/skills/api-launch-publish/scripts/seo_daily_check.py
/root/kiro/sandbase-daily-ops/outputs/seo-daily-reports/

# 设计文档
/root/kiro/sandbase-daily-ops/outputs/docs-agent-friendly-design.md
```
