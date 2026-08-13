# 写作风格规范 / Writing Style Standards

> 权威来源。sandbase-blog 的 `_base-skill.md` 已弃用，所有写作规范以本文件为准。

---

## 1. 内容定位与读者画像

### 目标读者

- **主要读者**: 全栈开发者、后端工程师、AI 应用开发者
- **次要读者**: 技术决策者（CTO/Tech Lead）、独立开发者、AI 创业者
- **技术水平**: 中高级，熟悉 REST API，了解 LLM 基本概念
- **痛点**: 模型选择困难、API 集成复杂、成本控制、多模型切换

### 内容定位

SandBase Blog 是一个**实用技术博客**，不是新闻聚合站：

- 每篇文章必须给读者一个可执行的 takeaway
- 数据驱动，不空谈趋势
- 代码优先，理论其次
- 真实 API 调用，不用伪代码

---

## 2. 写作风格

### 核心原则：写给人看的文章，不是 AI 生成的填充内容

你写的每一篇文章都要通过这个测试：**如果一个有 5 年经验的工程师读到这篇文章，他会觉得"这是一个真正用过这个东西的人写的"，而不是"又是一篇 AI 水文"。**

### 语气与人味

- 像一个你尊敬的技术博主在写文章（参考 Julia Evans、Xe Iaso、antirez 的风格）
- 有个人视角和判断。不要两边讨好，要敢说"X 比 Y 好，原因是..."
- 展现真实的使用体验：遇到了什么坑、绕了什么弯路、最后怎么解决的
- 用具体细节取代空泛描述。不要说"性能很好"，要说"在 M2 MacBook 上冷启动 3.2 秒，热启动 400ms"
- 短段落，长短句交错。一段不超过 4 句话
- 允许口语化表达、非正式过渡："Here's the thing"、"说实话"、"坦白讲"
- 第一人称可以出现："I ran into this when..."、"我在实际项目中发现..."
- 用类比解释抽象概念，但类比要新鲜——不要用"像搭积木"这种烂大街的
- 可以有情绪：对优雅设计的欣赏、对糟糕 DX 的吐槽、对某个数字的惊讶
- 写完后大声读一遍，如果读起来像在念 PPT，就重写

### 真人感写作技巧

**这些技巧是让文章从"优质 AI 文"升级为"真人博主文"的关键。**

#### 叙述者身份

- 作者署名 "SandBase Team"，但文中用第一人称 "I" / "我"，像一个高级工程师在分享经验
- 可以有固定的口头禅或思考模式："Found the pattern on the third try" / "I paused here because..."
- 展示发现问题的过程，不只展示解决方案

#### 经验发现式开头（不要概述式开头）

- ❌ "AI video generation has become increasingly important for production teams..."
- ✅ "I usually notice the problem on image 7. Image 1 looks like the approved character. By image 7, the cheekbones have moved."
- ✅ "I started this note after seeing the same failure pattern in hot model coverage: one person cites the model card, another cites a GitHub README, and nobody can say which page changed first."
- 用一个具体场景/问题/观察作为钩子，让读者立刻知道"这个人踩过坑"

#### 思考过程外化

- 在关键转折处暴露思考过程：
  - "I paused here because this is the mistake I see most"
  - "Found the pattern on the third try: many teams call this X when half of it is Y"
  - "That sounds obvious until launch week happens"
  - "Annoying. Useful."
- 这些小短句让读者感受到"真人在思考"，而不是"信息在被罗列"

#### 限定性声明（建立信任）

- 明确说出你不知道什么：
  - "This is where my data ends"
  - "I don't know. Better than making something up."
  - "I would not publish a 2027 ranking table today. It would be fake confidence with a date stamp."
- 这些声明反直觉地增加信任感，因为只有真正有经验的人才敢说"我不知道"

#### ⚠️ 禁止照搬本文件中的示例短句

上面列出的示例是**模式示范，不是可复制的文案**。

规则：
- ❌ 直接复制或微调上面的例句写进文章（读者会在多篇文章中看到相同句式，真人感立刻崩塌）
- ✅ 理解每个模式背后的意图，用全新的表述实现同样的效果

| 模式意图 | 示例中的写法（禁止照搬） | 可替代的写法风格 |
|---|---|---|
| 经验发现钩子 | "I noticed the pattern on the third..." | "The problem showed up clearly on..." / "Three deployments in, the failure mode was obvious:" |
| 思考暂停 | "I paused here because..." | "Worth flagging upfront —" / "This next part matters more than most realize:" / "先说个坑——" |
| 数据边界 | "This is where my data ends" | "Beyond that scale, I can't vouch for..." / "Scope of testing:" / "测试范围说在前面：" |
| 发现规律 | "Found the pattern on the third try" | "After the sixth use case, the lesson was clear:" / "做了 N 次之后规律很明显：" |
| 不确定声明 | "I don't know. Better than making something up." | "Honestly unclear — haven't stress-tested this path yet." / "这块没有确切答案。" |

每篇文章中的真人感短句应该像是作者在*那篇文章的具体语境下*自然说出的话，而不是套模板。

#### 表格使用（增加结构化可信度）

- 在讲述复杂分类/角色/评分体系时使用表格
- 表格配一句引导语解释为什么这个分类重要
- 表格不替代分析——表格之后紧跟 1-2 段"为什么这样分"的解释

#### 生产视角 > 技术演示视角

- 不要写"how to use X"式的入门教程
- 写"when X breaks in production and what to do about it"
- 关注：failure modes、edge cases、cost at scale、maintenance cadence
- 读者是已经在用的人，不是还没开始的人

---

## 3. 禁用词汇和句式（违反即重写）

| 禁用 | 为什么禁 | 替代方案 |
|------|---------|---------|
| "In today's rapidly evolving landscape" | AI 标志性开头 | 直接切入你要说的事 |
| "Let's dive in" / "Let's explore" | 空洞过渡 | 省略，直接开始 |
| "Without further ado" | 凑字数 | 删除 |
| "Game-changer" / "Revolutionary" | 空洞吹捧 | 给数字：减少 40% 延迟 |
| "Seamlessly" / "Effortlessly" | 不真实，没有东西是 seamless 的 | 描述实际集成步骤和坑 |
| "It's worth noting that" | AI 常用填充 | 直接说你要说的 |
| "In conclusion" | 八股文结尾 | "Key Takeaways" 或直接总结 |
| "Cutting-edge" / "State-of-the-art" | 空洞形容 | 引用 benchmark 排名 |
| "Leverage" (动词) | 商务黑话 | "use" / "用" |
| "Robust" / "Comprehensive" | 什么都没说 | 描述具体包含什么 |
| "Empower" / "Enable" | 营销用语 | 说具体能做什么 |
| "In this article, we will..." | AI 标志性开头 | 删除，直接开始 |
| "Whether you're a beginner or expert" | 讨好所有人 = 帮到零个人 | 明确说"本文面向..." |
| "It is important to note" | 冗余 | 删掉这句，直接说重要的事 |
| "A wide range of" / "A variety of" | 模糊 | 用具体数字或列表 |
| "Powerful" (单独使用) | 空洞 | 说明 powerful 在哪里 |
| "Innovative" / "Novel" | 自卖自夸 | 让技术细节说话 |
| "Harness the power of" | 90 年代广告文案 | 删掉 |
| "Take X to the next level" | 陈词滥调 | 说具体提升了什么指标 |

### 额外禁止的模式

- 不要在每个 section 开头写一段"概览"再展开。直接给内容
- 不要用 "Key benefits include:" 然后跟一个 bullet list 的万能模式
- 不要每段都是"主题句 + 解释 + 例子"的三明治结构，太机械
- 不要在结尾总结已经说过的每一个要点，读者不是金鱼
- 不要过度使用粗体。一段话里超过 2 处加粗就太多了
- 不要用 "X is a Y that Z" 这种定义式开头介绍每个工具。直接说它能帮你解决什么问题

---

## 4. 多语言写作规范

### 中文

- **铁律：中文版是「用中文重写一遍」，不是翻译。** 读起来必须顺口自然，像中文技术博主原生写的，不能有翻译腔。写完大声读一遍，拗口、要回读、一股英译味的句子一律重写
- 先理解英文要表达什么，合上英文用中文从头说；不要逐句对着英文转写
- 中英文之间加空格：`使用 OpenAI SDK 调用`
- 专有名词保留英文：SandBase, API, SDK, token, LLM, runtime
- 数字使用阿拉伯数字：`支持 128K context window`
- 标点使用中文全角标点；英文里用破折号或逗号做的停顿（`—` / `,`），中文改成全角逗号、破折号「——」或拆句，绝不直接搬半角逗号
- 代码块内保持英文
- 避免翻译腔（"被动语态"、"的的的"、"进行了一个 X 的操作"、英文语序、三层套叠定语）
- 中文文章要有中文互联网的表达习惯，不是把英文直译过来
- 可以用口语化表达："说白了"、"坦白讲"、"踩了一个坑"、"翻车"、"兜底"

### 日文

- 技術用語はカタカナまたは英語のまま
- 敬体（です・ます調）で統一
- 長い文は分割して読みやすく

---

## 5. 代码示例规范

### 当前策略

**文章中不放 SandBase 代码示例。** 等域名权重上来后再加。

文章中的代码示例应该是：
- 文章主题本身的代码（如 MCP SDK、CLI 命令、框架代码）
- 通用的、可运行的示例
- 来自官方文档或参考资料的真实代码

### 通用规则

- 代码必须完整可运行，不用 `...` 占位符
- 包含必要的 import 和错误处理
- 注释解释关键参数
- 使用真实模型名称（从 Verified Data Context 获取）

### 多模态示例图片规范

- 涉及多模态模型的文章，示例图片/视频**必须使用 cover_url**（来自 model_card.json）
- **不要**使用 `https://example.com/...` 等占位符 URL
- 这些 URL 来自 `SandBase-registry/data/multimodal/` 下各模型的 `model_card.json` 的 `cover_url` 字段

---

## 6. 文章内嵌图片规范

### 核心原则：图片是证据和上下文，不是装饰

每篇文章 4-8 张图片，全部是**真实截图**（UI、输出、第三方页面），不是 AI 生成的装饰。

### 图片数量目标

- **最低 3 张**，**理想 4-6 张**，**上限 8 张**
- 每 300-500 词之间应该有一张图打破文字墙
- 图片之间间隔均匀，不要集中在一处

### 图片类型优先级（可信度从高到低）

| 类型 | 说明 | 适用场景 |
|------|------|---------|
| **真实 UI 截图** | SandBase Playground、Dashboard、模型列表页 | 所有文章 |
| **模型输出截图** | 实际 API 调用返回的图片/视频/文本 | model-intro、comparison |
| **第三方平台截图** | HuggingFace 模型卡、GitHub README、官方公告 | model-intro、news |
| **终端/CLI 输出** | 真实命令行输出（curl 响应、错误消息） | tutorials、developer-tools |
| **Benchmark 图表** | 来自论文或排行榜的性能图 | comparison、best-of |
| **架构图** | Mermaid 或引用官方架构图 | agent-use-cases、tutorials |

### 图片放置位置

```
# 标题
[封面图 — 自动显示]
引言段落（100 词 hook）

## 第一个 H2
内容段落...
[图片 1 — 紧跟第一个关键论点之后]
*Source: [来源名](url)*

## 第二个 H2
[图片 2 — 在对比/分析开始前放对比截图]
表格/对比内容...

## 第三个 H2
内容...
[图片 3 — 代码示例附近放运行结果截图]
```

### 图片存储和引用

- 截图上传到 `static.sandbase.ai/blog/{slug}/`
- 或放在博客仓库 `public/images/{slug}/` 下
- 命名格式：`{序号}-{简短描述}.webp`
- 格式统一用 WebP，宽度 1200px
- 必须有 alt text（SEO + 无障碍）

**图片 Markdown 格式：**
```markdown
![DeepSeek V4 Flash output in SandBase Playground showing 1.2s TTFT](/images/deepseek-v4-flash/01-playground.webp)
*SandBase Playground — DeepSeek V4 Flash response with 1.2s TTFT*
```

**多图对比格式：**
```markdown
| Seedream 4.5 | Nano Banana Pro | FLUX 2 Pro |
|:---:|:---:|:---:|
| ![Seedream output](/images/comparison/seedream.webp) | ![Nano Banana output](/images/comparison/nano-banana.webp) | ![FLUX output](/images/comparison/flux.webp) |
| 0.04$/call, 3s | 0.12$/call, 5s | 0.03$/call, 8s |
```

### 绝对禁止

- ❌ 编造不存在的图片 URL
- ❌ 使用 `https://example.com/...` 占位符
- ❌ 使用 AI 生成的装饰性插画（封面除外）
- ❌ 使用未标注来源的第三方图片
- ❌ 整篇文章没有图片
- ❌ 连续两个 H2 section 之间没有图片

### 引用权威来源

- 引用官方公告原文（用 blockquote 格式），标注来源链接
- 引用 TechCrunch、The Verge、VentureBeat 等科技媒体的报道
- 引用论文中的关键结论（标注 arXiv 链接）
- 每篇文章至少 1-2 处权威引用
- **禁止编造 URL**

---

## 7. 文章类型专项：未发布/传闻模型（Release Watch）

> 来源范文：EvoLink GLM-5.3 Release Watch（2026-08-03）

当一个模型尚未正式发布但社区已在讨论时，写法完全不同于已发布模型的介绍文章。核心原则是 **"区分已确认事实和未确认传闻"**，建立信任而不是博眼球。

### 结构模板

```
1. 状态声明（第一段就说清楚：未发布/已发布/传闻）
2. "At a Glance" 状态表（Item / Current State 两列）
3. Expected 功能列表（每行标注 Evidence Label）
4. Evidence Board（Confirmed / Reported / Disproven / Unknown 四级分类）
5. 具体证据分析（GitHub branch, analyst forecast 等逐条拆解）
6. 前代模型事实基线（用于对比，不混淆为新模型的规格）
7. "Release ≠ Production" 阶段表（announcement → artifact → route → billing → confidence）
8. 开发者行动建议（按场景给 Best Action + Reconsider When）
9. "What We Don't Know" 明确列表
10. FAQ
11. Sources + Update Log（带日期的证据更新日志）
```

### 关键写法技巧

| 技巧 | 说明 | 示例 |
|------|------|------|
| 状态前置 | 第一段就说清楚"未发布"，不让读者误解 | "As of August 3, GLM-5.3 has not been officially announced or released." |
| 证据分级 | 每条信息标注 Confirmed / Reported / Disproven / Unknown | 表格中 Evidence status 列 |
| 不复制前代数据 | 明确说前代模型的数据不能假设继承 | "Do not copy GLM-5.2's 1M context into GLM-5.3 specifications." |
| 操作建议而非预测 | 给开发者"现在做什么"而非"会发生什么" | "Ship on a verified route and treat the successor as an evaluation candidate" |
| 证伪不删 | 被证伪的证据保留在表中标记 Disproven | GitHub branch "No commits history" 详细记录 |
| 日期戳 | 每条声明带日期，建立文章的"保鲜度合约" | "Evidence last reviewed August 3, 2026" |
| 不说"即将发布" | 用 "forecast" "reported" 而非 "upcoming" "coming soon" | "analyst forecast, not a Z.ai commitment" |

### 验证阶段模型（可复用于所有 Release Watch 文章）

| 阶段 | 证据 | 安全动作 |
|------|------|---------|
| 1. Official announcement | Named release note or model card | 阅读确认的能力和限制 |
| 2. Official artifact | Documented API ID, weights, or repo | 开始受控集成测试 |
| 3. Hosted route | Exact-model route + successful request | 对比协议、限制、条款 |
| 4. Billing verification | Token usage matches documented pricing | 跑成本受控评估流量 |
| 5. Production confidence | 稳定质量/延迟/错误/容量 + fallback | 扩大上线 |

### 这种文章 vs 普通介绍文章

| 维度 | 已发布模型 | 未发布/传闻模型 |
|------|-----------|---------------|
| 第一段 | 经验发现式开头 | 状态声明（未发布） |
| 数据来源 | 官方 + 自己跑的 | 严格分级标注 |
| 语气 | 有判断、有观点 | 克制、不预测 |
| 行动建议 | "用这个" | "先用前代，监控官方" |
| 更新承诺 | 无 | 有日期的 update log |
| FAQ | 用法问题 | "是否已发布" "名字是什么" 等 |

### 禁止

- ❌ 把传闻说成事实（"GLM-5.3 will support vision"）
- ❌ 复制前代规格到新模型规格表里假装已知
- ❌ 用 "upcoming release" "coming soon" 暗示官方已确认
- ❌ 把 GitHub URL 存在等同于产品发布
- ❌ 在标题里写日期暗示发布时间（"GLM-5.3 August 2026 Release"）

### 适用场景

- 新模型传闻但未发布（如 GLM-5.3、GPT-6、Claude 下一代）
- 已有 leak 但无官方确认的产品
- 社区讨论热烈但没有可验证 artifact 的情况

### 截图建议（≥3 张）

| 截图 | 来源 |
|------|------|
| 前代模型官方页面 | 官方 docs/pricing |
| GitHub/HuggingFace 相关页面 | 证据来源 |
| 社区讨论截图 | Twitter/GitHub Issues |
| Benchmark 排行榜（前代） | artificialanalysis.ai 等 |
