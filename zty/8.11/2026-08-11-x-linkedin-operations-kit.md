# SandBase X + LinkedIn 运营工具包

> 建立日期：2026-08-11  
> 适用账号：X 品牌账号 `@SandbaseAI`；LinkedIn 创始人账号 `David Li`  
> 主要受众：AI Agent 开发者、AI 基础设施团队、技术创始人、平台工程师  
> 使用原则：先核实事实，再发布；同一主题按平台重写，不直接复制。

## 1. 两个平台分别做什么

| 平台 | 账号角色 | 主要任务 | 推荐内容 | 频率 | 默认 CTA |
|---|---|---|---|---|---|
| X | SandBase 品牌账号 | 快速建立技术认知、参与热点、获得开发者回复 | 尖锐观点、短 Demo、产品证据、Thread、开发者回复 | 每天 1–2 条原创帖，另做 5–8 条高质量回复 | Reply / View demo / Read docs |
| LinkedIn | David Li 创始人账号 | 建立创始人判断力、解释产品方向、连接合作对象 | 创始人观点、产品取舍、Build in Public、复盘、生态观察 | 每周 2–3 篇 | Discuss / Connect / Read more |

### X 的表达方式

- 第一行只讲一个清晰判断或问题。
- 尽量控制在 220 个英文字符左右；内容确实需要展开时才写 Thread。
- 优先使用截图、短录屏、代码、trace 或实际输出。
- 不要把 X 写成压缩版新闻稿。

### LinkedIn 的表达方式

- 建议 120–250 个英文单词，使用短段落。
- 结构为：发生了什么 → 为什么重要 → 具体机制或例子 → 取舍 → 一个问题。
- 允许有创始人判断，但第一人称经历、客户结果和数字必须有证据。
- 不要直接复制 X，也不要把博客开头原样粘贴过来。

## 2. 对外定位和内容边界

### 当前核心信息

> SandBase helps agents connect to the real world.

SandBase 是帮助 Agent 发现、连接、编排和复用外部能力的生态与交付层。这些能力可以包括 API、模型、MCP server、skill、sandbox、connector 和 Agent Service。

可使用的短句：

- `Connect your agent to the real world.`
- `From external capabilities to connected agent workflows.`
- `One ecosystem for the capabilities your agent needs to get work done.`
- `Connecting tools is easy. Running them safely, observably, and repeatedly is the hard part.`

### 未经团队确认不要发布

- 客户名称、Logo、评价、调用量、收入和转化数据。
- 性能、价格、免费额度、上线时间和路线图。
- “最强”“第一”“零故障”“完全自治”“生产级”等绝对承诺。
- 将第三方能力描述成由 SandBase 开发、托管或部署。
- 尚未公开的合作、融资、安全或合规信息。

第三方能力的正确写法：

```text
<Provider> contributes <specific external capability>.
SandBase makes it available as a composable capability for agent workflows.
```

## 3. 内容支柱

| 栏目 | 要回答的问题 | X 形式 | LinkedIn 形式 | 所需证据 |
|---|---|---|---|---|
| Runtime Reality | Agent 从 Demo 到真实运行时，哪里最容易失败？ | 观点短帖、Checklist、Thread | 创始人判断、技术取舍 | 架构、trace、真实故障或文档 |
| Built on SandBase | 本周具体做成了什么？ | Demo、截图、产品更新 | Build in Public、决策背景 | 可公开版本、截图、录屏、链接 |
| What Stops the Agent? | 状态、重试、权限、成本、沙箱中哪个环节会阻断任务？ | 单一痛点、投票、问答 | 场景分析、失败复盘 | 真实场景或可验证示例 |
| Ecosystem Capability | 新 API、模型、MCP 或 skill 能让 Agent 完成什么？ | 上线短帖、用例列表 | 能力价值和工作流说明 | Provider 官方来源、SandBase 页面 |
| Founder Notes | 为什么做这个选择？放弃了什么？ | 一句话判断或 Quote post | 创始人长帖 | David 本人的真实经历和判断 |

建议内容比例：

- 40% 技术教育与观点。
- 30% 产品证据与 Demo。
- 20% Build in Public 与创始人内容。
- 10% 产品发布和直接推广。

## 4. 每周固定节奏

| 日期 | X | LinkedIn | 当天准备 |
|---|---|---|---|
| 周一 | Runtime Reality 尖锐观点 | 创始人观点：本周关键判断 | 一个技术问题和 David 的判断 |
| 周二 | 产品截图或 30–60 秒 Demo | 不发或参与评论 | 真实产品画面、命令、输出 |
| 周三 | Checklist、图示或 Thread | 教育型短文或架构解释 | 3–5 个具体检查项 |
| 周四 | 参与 AI Agent、MCP、模型或 sandbox 热点 | 不发或连接潜在合作对象 | 5–8 个相关公开讨论 |
| 周五 | Build in Public 短帖 | 产品进展、失败或取舍复盘 | 本周真实变化和可公开证据 |
| 周末 | 投票、问题、轻量复盘 | 通常不发 | 汇总本周数据和高价值反馈 |

最低可执行版本：每周发布 5 条 X、2 条 LinkedIn、完成 25 条有内容的 X 回复。

## 5. 每日工作流

### 上午：收集素材（10 分钟）

- [ ] 查看开发团队当天的产品、API、模型、Docs、GitHub 和 Bug 更新。
- [ ] 记录一项可公开变化，并向负责人确认。
- [ ] 找出一个与 Agent runtime、MCP、sandbox、routing 或 observability 有关的讨论。
- [ ] 检查昨天评论和私信中重复出现的问题。

### 写作与审核（15–25 分钟）

- [ ] 为 X 写一个观点或证据帖。
- [ ] 判断该主题是否值得改写成 LinkedIn；不是每天都要发。
- [ ] 给每条内容只设置一个 CTA。
- [ ] 检查所有数字、兼容性、客户和产品能力表述。
- [ ] 由产品或技术负责人审核新功能和技术结论。

### 发布后（15 分钟）

- [ ] 保存帖子 URL、发布时间和内容类型。
- [ ] 优先回复真实问题，不复制统一回复。
- [ ] 记录高价值反对意见、产品问题和合作线索。
- [ ] 24–48 小时后补录曝光、互动、点击和有效对话。

## 6. 每日素材输入卡

每天把下面内容填好后即可开始写作：

```text
日期：
今天的产品变化：无 / ...
经过确认、可以公开的事实：
相关页面或官方来源：
今天最值得讨论的行业问题：
希望触达的人：开发者 / 创始人 / 合作方 / 其他
今天可以提供的证据：截图 / Demo / 数据 / 代码 / 暂无
今天的 CTA：回复 / 看 Demo / 读文档 / 试用 / 联系
昨天表现：曝光 ...；互动 ...；点击 ...；有效回复 ...
禁止提及：
```

## 7. X 文案模板

### 模板 A：尖锐观点

```text
<One sharp technical judgment.>

<Explain the failure or consequence in one sentence.>

<Name the practical check or next step.>

<One question CTA.>
```

### 模板 B：产品证据 / Demo

```text
We tested <specific workflow> today.

Input: <verified input>
Agent action: <verified action>
Output: <verified result>

The useful part isn't <surface feature>. It's <operational value>.

<Demo or docs link>
```

### 模板 C：Build in Public

```text
This week at SandBase:

Shipped: <verified change>
Learned: <real lesson>
Next: <public next step>

The trade-off we're still working through: <honest constraint>.
```

### 模板 D：生态能力上线

```text
<API / model / tool> is now available through the SandBase ecosystem.

Agents can use it for:
- <verified use case>
- <verified use case>
- <verified use case>

<Provider> provides <raw capability>. SandBase makes it composable in agent workflows.

<One CTA + link>
```

### 模板 E：参与他人讨论

```text
The connection layer solves <what it solves>. The runtime still has to handle <specific operational problem>.

I'd also check <one useful consideration>. How are you handling it today?
```

回复必须针对原帖内容改写，不能批量复制。

## 8. LinkedIn 文案模板

### 模板 A：创始人观点

```text
<A concrete tension builders face.>

My current view: <David's approved judgment>.

The reason is practical.

<Specific mechanism or example.>

This approach is not always the right choice. <Name the trade-off and who should choose another path.>

At SandBase, we're focused on <verified product direction>.

How are you handling <one specific question>?
```

### 模板 B：产品进展

```text
We shipped <verified change> at SandBase.

What changed:
• <change>
• <change>
• <change>

Why it matters for agent builders:
<Concrete workflow consequence.>

The limitation we're still working through is <honest constraint>.

<One CTA or question>
```

### 模板 C：失败复盘

```text
<What failed or surprised the team.>

The first explanation was <initial assumption>.
The actual issue was <verified cause>.

We changed <specific decision> because <reason>.

The lesson for agent builders: <useful conclusion without exaggeration>.

What failure mode has been hardest for your team to reproduce?
```

### 模板 D：API / 能力上线

```text
<API> is now available through the SandBase ecosystem.

Agents can now use <provider capability> inside connected workflows.

First use cases:
• <use case>
• <use case>
• <use case>

<Provider> provides <raw capability>.
SandBase helps agents discover, connect, orchestrate, and reuse it alongside other capabilities.

<One CTA + verified link>
```

## 9. 可进入审核的种子文案

以下文案没有客户、性能或上线声明，但发布前仍需确认它们与当前产品定位一致。

### X 种子 1：Runtime

```text
Connecting a tool is not the same as running an agent reliably.

The hard part starts after the first successful call: state, retries, permissions, artifacts, and traces.

That is the runtime problem we're focused on at SandBase.
```

### X 种子 2：MCP

```text
MCP helps an agent reach a tool.

It doesn't automatically answer:
• Where does the task run?
• What survives a failure?
• Who can inspect the trace?

Connection is one layer. Execution control is another.
```

### X 种子 3：讨论型

```text
What stops your agent most often in a real workflow?

A. Tool failure
B. Lost state
C. Unbounded retries
D. Missing permissions
E. Something else

Reply with the failure mode you wish was easier to reproduce.
```

### LinkedIn 种子 1：创始人判断

```text
A useful distinction in AI agent infrastructure is the difference between connection and execution.

Giving an agent access to more models and tools expands what it can attempt. It does not automatically make the workflow repeatable, observable, or safe to operate.

The runtime still has to answer practical questions: Where does code execute? What state survives a failure? How are retries controlled? Which artifacts and traces can a team inspect later?

Our focus at SandBase is the layer between isolated capabilities and work that can be delivered reliably to real users.

Not every workflow needs a full runtime. But once an agent carries state, invokes several tools, or runs for more than one step, these operational questions become difficult to ignore.

Which runtime problem is creating the most friction for your team today?
```

### LinkedIn 种子 2：Build in Public 骨架

```text
One thing we changed at SandBase this week: <verified change>.

The visible feature is <surface change>. The more important decision was <technical or product decision>.

We made that choice because <verified reason or observation>.

The trade-off is <honest limitation>. For teams that only need <simpler case>, a lighter approach may still be the better option.

Our next step is <public next step>.

How would you evaluate this trade-off in your own agent workflow?
```

## 10. 一份素材如何改成两平台内容

| 原始素材 | X | LinkedIn |
|---|---|---|
| 新功能 | 一句话变化 + 一张截图 + 链接 | 为什么做、用户影响、取舍、下一步 |
| Demo | 15–30 秒片段 + 结果 | 问题、工作流、机制、限制、完整 Demo |
| Bug / 失败 | 意外现象 + 一条经验 | 初始判断、真实原因、修复决策、经验 |
| 博客 | 最尖锐结论或一张图 | 独立的创始人观点，链接博客作为证据 |
| 行业热点 | Quote post + 补充判断 | 热点背后的长期问题和团队选择 |
| API 上线 | 能力、3 个用例、一个 CTA | Provider 与 SandBase 的不同角色及工作流价值 |

## 11. 7 天启动清单

| 天数 | X | LinkedIn | 需要团队提供 |
|---|---|---|---|
| Day 1 | Runtime 种子 1 | 创始人判断种子 1 | 确认对外一句话定位 |
| Day 2 | 一项真实产品截图或短 Demo | 不发 | 可公开功能、画面、链接 |
| Day 3 | MCP 种子 2或相关 Thread | 技术教育帖 | 技术负责人审核 |
| Day 4 | 参与 5–8 个相关讨论 | 不发 | 当天热点和优先互动名单 |
| Day 5 | 本周 Build in Public | Build in Public 骨架 | 本周真实变化、取舍、下一步 |
| Day 6 | 讨论型种子 3 | 不发 | 集中回复评论 |
| Day 7 | 一周复盘或最佳帖二次分发 | 不发 | 两个平台 Analytics |

## 12. 发布前检查

每条帖子必须全部通过：

- [ ] 第一行具体，不使用 `AI is changing everything`、`game-changer`、`seamlessly` 等空泛表达。
- [ ] 读者不点击链接也能获得一个有用判断或信息。
- [ ] 产品、Provider、API、模型和能力名称准确。
- [ ] 技术结论有产品、文档、代码、截图或官方来源支持。
- [ ] 所有数字、日期、客户、兼容性和第一人称经历均可证明。
- [ ] 没有把第三方能力写成 SandBase 自有、托管或部署的产品。
- [ ] 没有泄露 Token、API Key、Cookie、后台截图敏感信息或未公开路线图。
- [ ] 图片文字在手机上可读；链接已经打开验证。
- [ ] 同一内容已经根据 X / LinkedIn 的用途重写。
- [ ] 只有一个 CTA。

## 13. 数据记录模板

每条帖子发布后新增一行：

| Date | Platform | Post URL | Format | Pillar | Hook | Impressions | Engagements | Profile Visits | Link Clicks | Qualified Replies | Leads | Decision |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| YYYY-MM-DD | X / LinkedIn |  | Short / Thread / Demo / Founder |  |  |  |  |  |  |  |  | 保留 / 重写 / 停止 / 扩大 |

LinkedIn 如果后台字段不同，至少记录曝光、reactions、comments、reposts、profile views 和新增连接；有效回复比单纯点赞更重要。

## 14. 每周复盘模板

```text
复盘周期：

1. 本周发布
- X 原创：
- X 高质量回复：
- LinkedIn：

2. 表现最好内容
- 链接：
- 栏目与形式：
- 为什么有效：钩子 / 证据 / 话题 / 分发 / 其他

3. 表现最差内容
- 链接：
- 问题：开头抽象 / 缺乏证据 / CTA 不清 / 受众错误 / 其他

4. 有效信号
- 目标开发者回复：
- 官网或文档点击：
- 私信、试用或合作线索：
- 重复出现的问题：

5. 下周决策
- 扩大：
- 重写：
- 停止：
- 新实验：
```

## 15. 仓库内可用工具

| 用途 | 文件 | 使用说明 |
|---|---|---|
| X 30 天计划 | `zty/8.10/sandbase-x-30-day-plan.md` | 作为逐日主题主线 |
| 渠道长度与结构 | `skills/api-launch-publish/references/publication-matrix.md` | 决定 X 与 LinkedIn 的写法 |
| 发布文案模板 | `skills/api-launch-publish/references/channel-copy-template.md` | API / 能力上线时套用 |
| 创始人语气 | `skills/api-launch-publish/references/author-voice.md` | 写 David LinkedIn 前检查 |
| 产品定位 | `skills/api-launch-publish/references/ecosystem-positioning.md` | 核对 SandBase 与 Provider 的关系 |
| 内容质量检查 | `skills/api-launch-publish/references/quality-gates.md` | 产品发布前使用 |
| 热点检索 | `scripts/daily_hot_topics.py` | 需先改 Windows 路径并配置个人 `SANDBASE_API_KEY` |
| 封面生成 | `skills/api-launch-publish/scripts/generate_api_launch_images.py` | 需 API Key；社媒优先 16:9 |

`scripts/cross_post.py` 目前只支持 DEV.to 和 Medium，不支持 X 或 LinkedIn，不纳入当前日常流程。

## 16. 文件归档规则

建议把每日内容保存在：

```text
zty/<月.日>/social/
  YYYY-MM-DD-content-plan.md
  x.md
  linkedin.md
  weekly-review.md
```

每条文案状态统一使用：`Draft`、`Fact Check`、`Approved`、`Published`、`Measured`。

账号密码、Token、API Key、Cookie 和导出的凭证不得写入任何 Markdown、脚本或 Git 提交中。

## 17. 与 Codex 的每日协作口令

最简指令：

```text
执行 X + LinkedIn 第 N 天。
产品变化：...
可公开事实：...
可用证据：...
```

预期返回：

1. 一条 X 主帖和一个备选开头。
2. 是否适合改写成 LinkedIn；适合时提供完整草稿。
3. 所需截图、Demo 或来源。
4. 5–8 个值得参与的讨论及定制回复方向。
5. 发布顺序、唯一 CTA 和审核风险。
6. 次日需要提前准备的素材。

