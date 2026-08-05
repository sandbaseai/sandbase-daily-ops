# SandBase Blog Cover Visual System

## 基准参考

以下两张封面是全站封面的质量标准和风格基准：

- `https://blog.sandbase.ai/images/growth/best-ai-sandboxes-2026-comparison.png`
- `https://blog.sandbase.ai/images/growth/best-mcp-servers-2026-comparison.png`

**所有新生成的封面必须达到这两张的信息密度、布局质量和视觉风格。**

---

## 封面风格规范

### 整体风格

- **白色/浅灰背景**（#F8F8F6 或纯白），不使用暗色/黑色/渐变背景
- **全英文**，无论文章是 EN 还是 ZH 版本，封面一律英文
- **信息密集但清晰**：一张封面要传递"这篇文章讲什么、比了谁、从哪些维度评估"
- **16:9 比例**，目标 1600×900px
- **扁平/轻 3D 风格**，不使用照片、真人、设备、霓虹、赛博朋克

### 颜色系统

| Token | 值 | 用途 |
|---|---|---|
| Background | `#FFFFFF` 或 `#F8F8F6` | 画布 |
| Ink | `#101311` 或 `#1A1A1A` | 标题和加粗文字 |
| Subtitle | `#6B7280` 或 `#737A78` | 副标题和说明文字 |
| SandBase Green | `#20B987` 或 `#10B981` | 强调色：标签、图标、连线、立方体 |
| Light Green BG | `#ECFDF5` / `#D1FAE5` | 浅绿色区块背景 |
| Border/Grid | `#E5E7EB` / `#D9DEDB` | 卡片边框、网格线 |
| Icon fill | `#20B987`（绿）、`#374151`（黑） | 功能图标 |

### 布局结构（三栏）

```
┌─────────────────────────────────────────────────────────────────────┐
│ [标签] 2026 COMPARISON                                               │
│                                                                       │
│ ┌─── 左侧 35% ───┐  ┌─── 中间 30% ───┐  ┌─── 右侧 35% ───┐      │
│ │                  │  │                  │  │                  │      │
│ │ 大标题（2-3行）   │  │ 产品卡片列表      │  │ 架构/流程图      │      │
│ │                  │  │ Logo+名称+定位    │  │ 概念关系图       │      │
│ │ 副标题           │  │ 3D 图标          │  │ Agent Loop 等    │      │
│ │                  │  │ 虚线连接          │  │                  │      │
│ │ 评估维度列表      │  │                  │  │                  │      │
│ │ ✓ Dimension 1   │  │                  │  │                  │      │
│ │ ✓ Dimension 2   │  │                  │  │                  │      │
│ │ ✓ Dimension 3   │  │                  │  │                  │      │
│ │ ✓ Dimension 4   │  │                  │  │                  │      │
│ └──────────────────┘  └──────────────────┘  └──────────────────┘      │
│                                                                       │
│ ┌─── 底部能力栏（横向 4-6 个标签） ─────────────────────────────────┐ │
│ │ 🔒 Label 1  │  ⚡ Label 2  │  ☁️ Label 3  │  📊 Label 4  │ ... │ │
│ └───────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 左侧区域（35%）

1. **标签**：左上角，绿色圆角矩形内白字 "2026 COMPARISON" / "2026 TOP PICKS" / "TUTORIAL" / "DEEP DIVE"
2. **大标题**：黑色加粗，2-3 行，字号最大（约 48-64px 视觉效果）
3. **绿色短横线**：标题下方，宽约 40px，高 4px，作为分隔
4. **副标题**：灰色，1-2 行，描述文章核心内容
5. **评估维度列表**：每行一个图标 + 粗体标题 + 灰色一行说明

### 中间区域（30%）

1. **产品/方案卡片**：纵向排列 3-5 个
2. 每个卡片包含：产品 Logo/图标 + 名称（粗体）+ 一句话定位（灰色）
3. 右侧配 3D 轻质感立方体或图标（绿色调）
4. 卡片之间用虚线/箭头连接到右侧架构图

### 右侧区域（35%）

1. **架构/概念图**：展示文章核心概念的关系
2. 使用圆形/圆角矩形节点 + 箭头/虚线连接
3. 中心节点突出（如 "AI Agent Loop"、"MCP Gateway"、"Embedding Router"）
4. 周围节点为子概念或流程步骤
5. 绿色为主色调，灰色边框

### 底部能力栏

1. 浅灰色背景条，横向排列 4-6 个标签
2. 每个标签：小图标 + 粗体短词 + 灰色一行说明
3. 总结文章涵盖的核心能力维度

---

## 按文章类型的封面变体

### comparison（对比文章）

- 标签：`2026 COMPARISON`
- 中间区域：列出被对比的 2-5 个产品
- 右侧：展示对比维度的统一评估框架
- 底部：评估能力标签

### best-of / top-n（排行/选型文章）

- 标签：`2026 TOP PICKS`
- 中间区域：列出推荐的 4-6 个方案
- 右侧：展示选型决策流程或使用场景图
- 底部：选型维度标签

### tutorial（教程文章）

- 标签：`TUTORIAL`
- 中间区域：展示工具/技术栈组件
- 右侧：流程图（输入→处理→输出）
- 底部：技术栈标签

### deep-dive / analysis（深度解读）

- 标签：`DEEP DIVE`
- 中间区域：核心概念的分层展示
- 右侧：内部架构图
- 底部：技术关键词标签

### launch / product-updates（产品发布）

- 标签：`PRODUCT UPDATE`
- 中间区域：新能力/新集成展示
- 右侧：能力如何融入 Agent 工作流的图
- 底部：核心价值标签

---

## 生成规则

### 呼吸感与留白（2026-08-03 新增）

**封面最常见的问题是文字太多、信息过密。** 必须平衡信息量和视觉舒适度：

- **标题最多 6-8 个英文单词**，不要把完整文章标题塞进去
- **副标题最多 1 行 10 个词**，超过就砍
- **左侧评估维度最多 4 项**，不是 6-8 项
- **每个元素之间留 20-30px 视觉间距**
- **底部能力栏最多 4 个标签**，不是 6 个
- **右侧架构图节点最多 5 个**，不要画成蜘蛛网
- **整体画面至少 25% 是留白/空间**

#### 呼吸感对照表

| ❌ 过密 | ✅ 有呼吸感 |
|---------|-----------|
| 标题 3 行 + 副标题 2 行 | 标题 1-2 行 + 副标题 1 行 |
| 6 个评估维度 + 6 个产品卡 + 8 节点架构图 | 4 个维度 + 3 个产品卡 + 4 节点图 |
| 底部 6 个标签挤满一行 | 底部 3-4 个标签，标签间有间距 |
| 所有区域顶满无边距 | 四周 40-60px padding，区域间 24px gap |

#### Prompt 中加入留白指令

在 prompt 末尾追加：
```
IMPORTANT: Leave generous whitespace between all elements. 
The cover must feel spacious, not cramped. 
At least 25% of the canvas should be empty white space.
Limit text to headline (max 8 words) + subtitle (max 10 words).
```

### 必须

- ✅ 全部英文（标题、副标题、标签、图内文字）
- ✅ 白色/浅灰背景
- ✅ 信息密度高：标题 + 副标题 + 维度列表 + 产品列表 + 架构图 + 底部栏
- ✅ SandBase 绿色作为唯一强调色
- ✅ 16:9 比例
- ✅ 在小缩略图（200×112px）下标题仍可辨认
- ✅ 英文和中文文章共用同一张封面（按 slug 共享）

### 禁止

- ❌ 暗色/黑色背景
- ❌ 中文文字（包括中文标题、中文标签、中文说明）
- ❌ 纯抽象图无文字（封面必须有英文标题和信息内容）
- ❌ 紫色、蓝色渐变、霓虹发光
- ❌ 真人、设备、屏幕截图
- ❌ 模型名称拼写错误
- ❌ 假 Logo（如果不确定 Logo 样子，用通用图标代替）
- ❌ 空旷无内容的画面

---

## Prompt 构建策略

封面由图像生成模型一次性生成（包含文字和布局），不再使用"背景+确定性叠加"模式。

Prompt 结构：

```
Blog cover image for an article titled "{EN_TITLE}".

Layout: white background, 16:9, information-dense technical comparison cover.

Left column (35%):
- Top-left: green rounded label "{ARTICLE_TYPE_LABEL}"
- Large bold black headline: "{EN_TITLE}" (2-3 lines)
- Green horizontal divider line below title
- Gray subtitle: "{EN_SUBTITLE}"
- Evaluation dimensions list with icons:
  {DIMENSIONS}

Middle column (30%):
- Vertical stack of {N} product cards, each with:
  {PRODUCT_CARDS}
- Light 3D isometric green cube icons beside each card
- Dashed connecting lines to right-side diagram

Right column (35%):
- Architecture/concept diagram showing {CONCEPT}
- Central node: "{CENTRAL_CONCEPT}"
- Surrounding nodes connected by green arrows/lines

Bottom bar:
- Light gray background strip with {N} capability labels:
  {CAPABILITY_LABELS}

Style: clean editorial infographic, flat/light-3D, white canvas, 
SandBase green (#20B987) as only accent color, black text, gray descriptions.
No dark backgrounds, no gradients, no photos, no Chinese text.
All text must be in English and clearly legible.
```

---

## 验收标准

每张封面生成后必须检查：

- [ ] 背景是白色/浅灰，不是暗色
- [ ] 所有文字为英文，无中文
- [ ] 标题清晰可读，无拼写错误
- [ ] 信息密度接近基准图（有标题+维度+产品列表+架构图+底部栏）
- [ ] 绿色是唯一强调色
- [ ] 小缩略图下标题仍然可辨认
- [ ] 产品名称拼写正确
- [ ] 无空旷无内容的区域

---

## 按文章 Category 的封面分类策略

全部 ~100 篇文章按 `category` 字段分为 6 个封面批次。每类有不同的构图侧重和 prompt 变量，但共享上述统一视觉系统。

### 类型 1：对比类 `model-comparison`（~18 篇）

A vs B 类文章。构图侧重"公平对决"：

| 属性 | 值 |
|------|------|
| 标签 | `2026 COMPARISON` |
| 中栏 | 2-4 个平等的供应商卡片，各带细色线条和一行用例标签 |
| 右栏 | 中立的决策门连接 agent 工作流节点 |
| 底部 | 五项能力评估栏 |
| 视觉感受 | 研究性产品地图，不是稀疏概念图或领奖台 |

适用文章示例：
- `claude-code-vs-codex-vs-openclaw-2026`
- `vllm-vs-sglang-2026`
- `gpt-5-6-vs-claude-5-agents-2026`
- `autogen-vs-crewai-multi-agent-showdown-2026`
- `litellm-vs-openrouter-2026`
- `dify-vs-langgraph-2026`

### 类型 2：Top N / 榜单类 `best-of` + `agent-best-picks`（~14 篇）

最佳推荐 / 选型指南类。构图侧重"市场地图"：

| 属性 | 值 |
|------|------|
| 标签 | `2026 TOP PICKS` |
| 左栏 | 标题 + 简短描述 + 四个筛选标准 |
| 中栏 | 5-6 个平等的供应商卡片，带一行能力标签 |
| 右栏 | agent 工作流循环 + 小型结果面板 |
| 底部 | 全宽能力栏 |
| 视觉感受 | 研究性市场地图，不是排名领奖台或奖杯 |

适用文章示例：
- `best-image-to-video-models-agents-2026`
- `best-ai-image-generation-apis-2026`
- `best-open-source-ai-agent-frameworks-2026`
- `ai-agent-infrastructure-stack-2026`
- `best-mcp-servers-2026-agent-tool-infrastructure`
- `best-ai-sandboxes-agent-development-secure-execution`

### 类型 3：单模型介绍类 `model-introduction`（~15 篇）

单个模型深度解析。构图以产品卡片为视觉中心：

| 属性 | 值 |
|------|------|
| 标签 | `MODEL INTRODUCTION` |
| 中栏 | 一个大型抽象神经网络形态，单个高亮节点 |
| 右栏 | 模型能力矩阵或性能对比图 |
| 特征 | 产品名称作为核心视觉元素，留出充足标题空间 |
| 视觉感受 | 产品发布页风格，聚焦单一主角 |

适用文章示例：
- `claude-opus-4-7-coding-agents-2026`
- `deepseek-v4-open-source-1m-context-2026`
- `gpt-5-6-luna-sol-terra-explained`
- `kimi-k3-moonshot-1m-context-2026`
- `claude-opus-5-deep-dive-2026`

### 类型 4：教程类 `tutorials`（~10 篇）

实操教程。构图侧重代码/流程图感：

| 属性 | 值 |
|------|------|
| 标签 | `TUTORIAL` |
| 中栏 | 工具/技术栈组件展示 |
| 右栏 | 三步路径流程图（输入→处理→输出） |
| 特征 | 偏技术实操感，仍保持白底信息密集布局 |
| 禁止 | 不出现可读代码或真实 shell 命令 |

适用文章示例：
- `connecting-mcp-servers-to-your-agent-2026`
- `cost-dashboard-agent-anthropic-sdk`
- `build-social-monitor-agent-openai-sdk`
- `batch-image-generation-agent-tutorial`
- `xiaohongshu-kol-screening-agent-tutorial`

### 类型 5：Agent 生态 / 用例类 `agent-use-cases` + `agent-daily-news`（~24 篇）

架构解析、设计模式、生态新闻。构图侧重工作流和概念连接：

| 属性 | 值 |
|------|------|
| 标签 | `DEEP DIVE`（深度分析）或 `2026 COMPARISON`（涉及对比） |
| 中栏 | 核心概念分层展示 / 能力节点列表 |
| 右栏 | 输入→处理→输出工作流图，抽象几何节点 |
| 特征 | 简洁系统架构图，小组已验证能力节点连接到 agent 工作流枢纽 |

适用文章示例：
- `production-ai-agents-need-a-runtime-layer`
- `agent-memory-architectures-compared-2026`
- `mcp-vs-function-calling-ai-agent-tool-integration`
- `inside-openhands-ai-coding-agent-architecture`
- `5-agent-design-patterns-robust-cost-effective-ai-systems`

### 类型 6：其他（产品更新 / 开发者工具 / 定价指南 / 行业洞察）（~16 篇）

| 子分类 | 标签 | 构图特征 |
|--------|------|----------|
| `product-updates` | `PRODUCT UPDATE` | 一个新能力节点通过绿色细线加入生态系统图 |
| `developer-tools` | `2026 COMPARISON` | 密集开发者工具决策板，左栏标题+任务决策列表，中栏 4-6 供应商卡片 |
| `pricing-guides` | `PRICING GUIDE` | 成本 vs 输出的平衡图，简单方块+方向线 |
| `industry-insights` | `INDUSTRY INSIGHTS` | 单条趋势线穿过小型数据点组 |

---

## 批量重新生成优先级

| 批次 | 分类 | 数量 | 优先级 | 原因 |
|------|------|------|--------|------|
| 1 | 对比类 `model-comparison` | ~18 | ⭐⭐⭐ | 视觉差异最明显，最容易验证效果 |
| 2 | 榜单类 `best-of` / `agent-best-picks` | ~14 | ⭐⭐⭐ | SEO 流量大户，封面统一性最重要 |
| 3 | 单模型 `model-introduction` | ~15 | ⭐⭐ | 模板化程度高，每篇有一个主角 |
| 4 | 教程类 `tutorials` | ~10 | ⭐⭐ | 封面风格稍偏代码感 |
| 5 | Agent 生态 `agent-use-cases` + `agent-daily-news` | ~24 | ⭐ | 概念类文章，封面灵活度大 |
| 6 | 其他 `product-updates` / `developer-tools` / `pricing-guides` | ~16 | ⭐ | 按需处理 |

**重新生成脚本**：`sandbase-blog/scripts/ai-content-generator/regen-covers.sh`

运行方式：
```bash
# 全量 dry-run 看列表
SANDBASE_API_KEY=xxx ./regen-covers.sh --dry-run

# 先试几张看效果
SANDBASE_API_KEY=xxx ./regen-covers.sh --limit=3

# 全量执行（约 3 分钟/张，93 张 ≈ 5 小时）
SANDBASE_API_KEY=xxx ./regen-covers.sh
```

---

## 封面生成完整工作流（必须遵守）

> ⚠️ 生成的图片 URL（`media.sandbase.ai/files/`）是**临时地址**，不能直接用于博客。
> 必须上传到 `static.sandbase.ai` 后才算完成。

> ⚠️⚠️ **两步流程，缺一不可**：
> 1. `generate_blog_cover_url.py` 只生成**纯背景**（无文字）
> 2. `render_launch_cover.py` 在背景上渲染**确定性文字**（标题/副标题/能力标签）
>
> 直接把背景图当封面发布 = 无文字封面 = 不合格。

### 工作流三步走

```
Step 1: 生成背景
  → 调用 SandBase API (nano-banana-pro) 生成抽象背景
  → 获得临时 URL: media.sandbase.ai/files/xxx/0.jpg
  → 背景图无文字（prompt 明确禁止 text/letters）

Step 2: 渲染文字（确定性叠加）
  → 下载背景图到本地
  → 创建 config JSON（headline, subtitle, eyebrow, capability_line）
  → 运行 render_launch_cover.py 叠加标题和标签
  → 输出最终封面（带文字）

Step 3: 上传到永久存储
  → 上传最终封面到 COS (static.sandbase.ai/blog/covers/{slug}.jpg)
  → 将永久 URL 写入 EN 和 ZH 文章的 image 字段
```

### 工具和脚本

| 步骤 | 脚本 | 位置 |
|------|------|------|
| 生成（单张） | `cover-generator.ts` 的 `generateCoverImage()` | sandbase-blog/scripts/ai-content-generator/ |
| 生成（批量） | `regen-all-covers.ts`（模型：`openai/gpt-image-2`） | sandbase-blog/scripts/ai-content-generator/ |
| 上传到 static | `migrate_covers.py` | sandbase-blog/scripts/ |
| 生成+上传（launch 包） | `generate_blog_cover_url.py` | sandbase-daily-ops/skills/api-launch-publish/scripts/ |

### 批量重新生成完整命令

```bash
# 1. 生成新封面（写入 media.sandbase.ai 临时 URL 到 frontmatter）
cd sandbase-blog/scripts/ai-content-generator
export $(grep -v '^#' ~/.config/sandbase/.env | xargs)
./regen-covers.sh --limit=5   # 或去掉 --limit 全量跑

# 2. 上传到 static.sandbase.ai（替换 frontmatter 中的临时 URL）
cd sandbase-blog/scripts
python3 migrate_covers.py               # EN
python3 migrate_covers.py --locale zh-CN # ZH
```

### URL 格式规则

| 域名 | 性质 | 能否用于生产 |
|------|------|-------------|
| `media.sandbase.ai/files/` | 临时（图片生成 API 返回） | ❌ 不能 |
| `media.sandbase.ai/uploads/` | 半永久（手动上传） | ⚠️ 可用但不推荐 |
| `static.sandbase.ai/blog/covers/` | 永久（COS CDN） | ✅ 唯一推荐 |

### 前置条件

环境变量（在 `~/.config/sandbase/.env` 中）：

```
SANDBASE_API_KEY=sk-xxx        # 图片生成 API
COS_SECRET_ID=AKIDxxx          # 腾讯云 COS 上传
COS_SECRET_KEY=xxx             # 腾讯云 COS 上传
COS_REGION=ap-singapore        # COS 区域
```

### 验收标准补充

- [ ] 最终 frontmatter 中的 image URL 以 `https://static.sandbase.ai/blog/covers/` 开头
- [ ] 不存在 `media.sandbase.ai/files/` 的临时 URL 残留
- [ ] EN 和 ZH 版本使用同一个封面 URL
