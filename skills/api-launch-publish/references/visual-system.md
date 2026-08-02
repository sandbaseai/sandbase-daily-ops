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
