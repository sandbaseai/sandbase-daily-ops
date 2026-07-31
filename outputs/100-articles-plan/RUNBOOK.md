# 100 篇博客项目 — 执行手册

> 仓库：sandbase-daily-ops (规划/脚本/发布包) + sandbase-blog (文章源文件)
> 创建日期：2026-07-31
> 最新更新：2026-07-31

本文档是完整执行手册，所有步骤、依赖、检查点在此归档。丢 session 后读此文即可继续。

---

## 0. 环境状态快照

| 项 | 路径/值 |
|---|---|
| daily-ops 仓库 | `/root/kiro/sandbase-daily-ops` |
| blog 仓库 | `/root/kiro/sandbase-blog` |
| monorepo（只读参考） | `/root/kiro/sandbase-monorepo` |
| daily-ops 分支 | `fix/cross-platform-cover-render`（未提交） |
| blog 分支 | `main`（干净） |
| Python | 3.10.12 |
| Pillow | 12.3.0 |
| 字体 Latin | Inter (`/usr/share/fonts/opentype/inter/Inter-*.otf`) |
| 字体 CJK | Noto Sans CJK SC (`/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc#2`) |
| API Key 位置 | `~/.config/sandbase/.env`（chmod 600，用户待放入） |
| DataForSEO 凭据 | 同上文件，`DATAFORSEO_LOGIN` + `DATAFORSEO_PASSWORD` |

---

## 1. 待提交的 daily-ops 修复（分支 fix/cross-platform-cover-render）

### 变更清单

| 文件 | 改动 |
|---|---|
| `.gitignore` | 新增 `.env*` / `*.pem` / `*.key` / `credentials.json` 忽略 |
| `README.md` | 默认渠道加 Medium + Zhihu；产出流程更新 |
| `SKILL.md` | 默认渠道 + macOS 路径 → 相对路径 + 产出结构更新 |
| `references/blog-format.md` | source of truth 改为仓库相对路径 |
| `references/channel-copy-template.md` | Medium/Zhihu 标签去 (optional) |
| `scripts/render_launch_cover.py` | 跨平台字体解析、CJK 行高、contains_cjk 修正 |
| `scripts/generate_api_launch_images.py` | 使用 `sandbase_env.py`、--env-file 参数 |
| `scripts/generate_blog_cover_url.py` | 使用 `sandbase_env.py`、移除冗余 load_env_file |
| `scripts/dataforseo_seo_review.py` | `datetime.UTC` → `timezone.utc`（py3.10 兼容） |
| `scripts/sandbase_env.py` | **新增** — 统一凭据加载模块 |
| `outputs/100-articles-plan/plan.md` | **新增** — 100 篇分配表 |
| `outputs/100-articles-plan/batch-1-detailed.md` | **新增** — B1 详细选题 |

### 提交命令（用户确认后执行）

```bash
cd /root/kiro/sandbase-daily-ops
git add -A
git commit -m "feat: cross-platform cover render, unified credentials, medium/zhihu channels, 100-article plan

- render_launch_cover.py: cross-platform font resolution (Inter + Noto CJK SC), CJK line height fix, contains_cjk Unicode-range fix
- sandbase_env.py: shared credential loader with permission warning
- dataforseo_seo_review.py: Python 3.10 compat (timezone.utc)
- generate_api_launch_images.py/generate_blog_cover_url.py: use shared loader
- .gitignore: block credential files from being tracked
- SKILL.md + README.md: promote Medium + Zhihu to default channels
- Remove all macOS absolute paths (/Users/liyb/...)
- outputs/100-articles-plan/: full 50-slug allocation + B1 detailed topics"
git push -u origin fix/cross-platform-cover-render
```

---

## 2. 凭据设置（用户操作）

```bash
mkdir -p ~/.config/sandbase
# 用编辑器写入，不要 echo（避免 shell history 泄漏）
nano ~/.config/sandbase/.env
# 内容：
# SANDBASE_API_KEY=sk-...
# DATAFORSEO_LOGIN=...
# DATAFORSEO_PASSWORD=...
chmod 600 ~/.config/sandbase/.env
```

验证：

```bash
cd /root/kiro/sandbase-daily-ops/skills/api-launch-publish/scripts
python3 -c "from sandbase_env import load_credentials, require; load_credentials([]); print('OK:', len(require('SANDBASE_API_KEY')), 'chars')"
```

---

## 3. 第 1 批（B1）执行步骤

### 3.1 DataForSEO 关键词验证

```bash
cd /root/kiro/sandbase-daily-ops/skills/api-launch-publish/scripts

# 先 dry-run 确认请求计划
python3 dataforseo_seo_review.py \
  --input ../../../outputs/100-articles-plan/b1-seo-input.json \
  --package ../../../outputs/100-articles-plan/b1-seo \
  --env-file ~/.config/sandbase/.env \
  --dry-run

# 用户确认后加 --allow-billable-requests 执行
python3 dataforseo_seo_review.py \
  --input ../../../outputs/100-articles-plan/b1-seo-input.json \
  --package ../../../outputs/100-articles-plan/b1-seo \
  --env-file ~/.config/sandbase/.env \
  --allow-billable-requests
```

### 3.2 确认生产 source_facts

```bash
# 拿到线上社媒数据模型数量作为 source_fact
# ⚠️ 写作约束：不提 TikHub。只说 SandBase 自身能力，不暴露上游供应商名称。
curl -s -H "Authorization: Bearer $SANDBASE_API_KEY" \
  "https://api.sandbase.ai/v1/models?vendor=Douyin&pageSize=1" | python3 -c "
import json,sys; d=json.load(sys.stdin); print('Douyin enabled:', d.get('total',d.get('pagination',{}).get('total_items','?')))"

curl -s -H "Authorization: Bearer $SANDBASE_API_KEY" \
  "https://api.sandbase.ai/v1/models?vendor=Weibo&pageSize=1" | python3 -c "
import json,sys; d=json.load(sys.stdin); print('Weibo enabled:', d.get('total',d.get('pagination',{}).get('total_items','?')))"

curl -s -H "Authorization: Bearer $SANDBASE_API_KEY" \
  "https://api.sandbase.ai/v1/models?vendor=Xiaohongshu&pageSize=1" | python3 -c "
import json,sys; d=json.load(sys.stdin); print('Xiaohongshu enabled:', d.get('total',d.get('pagination',{}).get('total_items','?')))"
```

将真实数字更新到 `batch-1-detailed.md` 的 source_facts。

### 3.3 写文章（按 slug 顺序）

对每个 slug：

1. **在 blog 仓库开 feature 分支**：`git checkout -b content/b1-<slug> main`
2. **去重检查**：读 `scripts/ai-content-generator/content-index.md`
3. **写 EN**：`src/content/en/<slug>.md`
4. **写 ZH**：`src/content/zh-CN/<slug>.md`（原生重写，不是翻译）
5. **SEO 自查**：标题 ≤60 / 关键词位置 / description / 表格 / FAQ / 内外链
6. **frontmatter schema 验证**：`npm run check` (需 `npm ci` 先装依赖)
7. **追加 content-index.md**：EN + ZH 各一行
8. **提交**：`git add src/content/ scripts/ai-content-generator/content-index.md && git commit`

### 3.4 生成封面

```bash
cd /root/kiro/sandbase-blog/scripts/ai-content-generator
npx --yes tsx batch-covers.ts --dry-run    # 预览缺封面的文章
npx --yes tsx batch-covers.ts              # 生成（需要 SANDBASE_API_KEY）
```

或用 daily-ops 的脚本对完整发布包（#1、#2、#10 走三篇制）：

```bash
cd /root/kiro/sandbase-daily-ops/skills/api-launch-publish/scripts
python3 generate_blog_cover_url.py \
  --title "<标题>" \
  --description "<描述>" \
  --category <category> \
  --article-type <launch|comparison|top-n> \
  --out-json ../../outputs/<slug>-launch/cover-url.json \
  --update-markdown /root/kiro/sandbase-blog/src/content/en/<slug>.md \
  --update-markdown /root/kiro/sandbase-blog/src/content/zh-CN/<slug>.md
```

### 3.5 渲染验证

```bash
cd /root/kiro/sandbase-blog
npm ci          # 首次需要
npm run build   # 完整构建验证
npm run dev &   # 可选：本地预览
# 检查每个 slug 的 EN/ZH 页面是否 200
```

### 3.6 独立 Review

对完整发布包（#1+#2+#10 组合、#7 单篇）走 `references/reviewer-role.md`：

- 读 input.json + source_facts
- 逐条核对事实声明
- 检查封面可读性（肉眼看 PNG）
- 写 `review-report.md`
- 返回 APPROVED 或 REVISE

单篇走简化清单（SEO 9 项 + GEO 5 项 + 封面可读性），记录在 `outputs/100-articles-plan/b1-review-log.md`。

### 3.7 发布

```bash
cd /root/kiro/sandbase-blog
# 合并所有 B1 feature 分支到一个发布分支
git checkout -b release/b1 main
git merge content/b1-social-media-data-apis-ai-agents-2026
git merge content/b1-douyin-data-api-on-sandbase
# ... 依次合并所有 10 个
git push -u origin release/b1
# 创建 PR → 用户 review → merge → 打 tag 触发部署
```

### 3.8 发布后观察

- GSC 提交 sitemap-index.xml
- 每天检查收录状态（目标 2 周内 ≥70% 的新 URL 被索引）
- 记录结果到 `outputs/100-articles-plan/b1-post-launch.md`
- 收录率达标 → 启动 B2；不达标 → 诊断并调整策略

---

## 4. 后续批次（B2-B5）

每批启动前：

1. 读本文档 + `plan.md` + 上一批的 `post-launch.md`
2. 确认上批收录门禁通过
3. 为当批建 `batch-N-detailed.md`（同 B1 格式）
4. 可选跑 DataForSEO 验证当批关键词
5. 按 3.3-3.8 执行

---

## 5. 关键规范引用（丢 session 后看这里）

| 文档 | 路径 | 用途 |
|---|---|---|
| 写作规范 | `sandbase-blog/scripts/ai-content-generator/prompts/_base-skill.md` | 风格、禁用词、SEO、代码规则 |
| 写作方法 | `sandbase-blog/scripts/ai-content-generator/WRITING-METHOD.md` | 10 步流程、中文硬要求 |
| 发布 SOP | `sandbase-daily-ops/skills/api-launch-publish/SKILL.md` | 三篇制、reviewer、封面 |
| blog 格式 | `sandbase-daily-ops/skills/api-launch-publish/references/blog-format.md` | frontmatter、category、cover |
| 质量门禁 | `sandbase-daily-ops/skills/api-launch-publish/references/quality-gates.md` | 发布前清单 |
| reviewer | `sandbase-daily-ops/skills/api-launch-publish/references/reviewer-role.md` | 独立审核角色 |
| 视觉系统 | `sandbase-daily-ops/skills/api-launch-publish/references/visual-system.md` | 封面品牌规范 |
| 去重索引 | `sandbase-blog/scripts/ai-content-generator/content-index.md` | 选题前必查 |
| 合法 category | `sandbase-blog/src/utils/categories.ts` | 11 个枚举值 |
| content schema | `sandbase-blog/src/content.config.ts` | zod frontmatter 校验 |

---

## 6. 已知问题与待办

- [ ] 用户放入 `~/.config/sandbase/.env`（SANDBASE_API_KEY + DataForSEO 凭据）
- [ ] 提交并推送 daily-ops 分支（用户确认后执行）
- [ ] 确认生产 `/v1/models` 的社媒 API 数量（作为 source_fact）
- [ ] B1 的 DataForSEO 验证（需 `--allow-billable-requests` 授权）

## 8. 写作硬约束（全局）

| 约束 | 说明 |
|---|---|
| **不提 TikHub** | 所有文章只说 SandBase 自身能力。不暴露上游供应商名称。用户 2026-07-31 明确要求。 |
| **差异化 = Agent Runtime 编排** | SandBase 的卖点是 runtime 编排（统一契约、session context、工具编排、skill 复用、沙盒、可观测、智能路由），不是"便宜的 API 聚合"。竞品写中立具体，给真实适用场景。详见 `references/differentiation-positioning.md`。 |
| 不编造数字 | 所有数据必须来自生产 API 响应或官方文档，无来源不写 |
| 中文原生重写 | 不是翻译。写完大声读，拗口就重写 |
| 禁用词零容忍 | 见 `_base-skill.md` 禁用词表 |
| SEO 9/10 | 每篇必达标后才提交 |
- [ ] `sandbase-blog` 安装依赖（`npm ci`）并验证 `npm run build` 通过
- [ ] 补全 `public/og-default.png`（1200x630 兜底 OG 图，目前未创建）
- [ ] 补录 content-index.md 缺失的 2 篇（`30-days-ai-infrastructure-startup-discoverable` + `sandbase-agent-infrastructure-product-update-july-2026`）

---

## 7. 进度追踪

| 批次 | 状态 | slug 完成数 | 文件完成数 | 发布日期 | 收录率 |
|---|---|---:|---:|---|---|
| B1 | 📋 规划完成 | 0/10 | 0/20 | — | — |
| B2 | ⬚ 待启动 | 0/10 | 0/20 | — | — |
| B3 | ⬚ 待启动 | 0/10 | 0/20 | — | — |
| B4 | ⬚ 待启动 | 0/10 | 0/20 | — | — |
| B5 | ⬚ 待启动 | 0/10 | 0/20 | — | — |
