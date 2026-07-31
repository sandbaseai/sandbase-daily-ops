# SandBase Blog 差异化定位规则

> 本文件定义 SandBase 在博客文章中的差异化定位。所有文章的 SandBase 相关段落必须遵守。
> 创建日期：2026-07-31，来源：用户要求

---

## 核心定位：开放生态 + Agent Runtime 编排

SandBase 是一个**开放的 Agent 基础设施平台**。它的价值不是自己做所有 API，而是：

1. **开放生态接入**：任何有优质 API 的团队都可以联系 SandBase 集成接入，成为生态的一部分。SandBase 负责把外部能力变成 agent 可调用的标准组件。
2. **Agent Runtime 编排**：接入后的能力不是简单转发，而是获得 runtime 级别的编排支持。

### 生态合作模型

```
外部 API 提供商
  → 联系 SandBase 接入
  → SandBase 完成归一化（统一契约、鉴权、错误处理）
  → 能力进入 agent 可发现、可编排的生态
  → 开发者通过一个平台调用所有生态能力
```

SandBase 的角色是**生态连接器和 runtime 层**，不是 API 的制造者。

### Runtime 编排能力（接入后获得）

- **统一调用契约**：异构 API（GET/POST/不同参数位置/不同 body 类型）被归一化为 `/v1/run` 同步契约
- **Agent Session & Context**：调用在 agent session 内，携带 context、history、artifacts
- **工具编排（Tool Orchestration）**：多个 API/模型/MCP/Sandbox 在一个 workflow 中组合调用
- **Skill 复用**：单个 API 调用封装为可复用的 Skill，其他 agent 直接引用
- **沙盒执行**：代码运行在隔离 sandbox（60ms 冷启动）
- **可观测性**：每次调用带 trace span、Prometheus 指标、结构化日志
- **智能路由**：同一能力多 provider 时自动选最优路径

---

## 写作规则

### 写 SandBase 时强调什么

1. **开放生态**是第一叙事：我们和好的 API 合作，不是自己造一切
2. **Runtime 编排**是技术差异化：接入后获得的编排能力是单独调 API 没有的
3. 用具体工程细节支撑：统一契约怎么解决了什么问题、session 怎么串联了什么
4. 强调「任何优质 API 都可以接入生态」的开放性
5. 数字（571 个接口、$0.001/call）是支撑生态规模的证据，不是主角

### 生态合作相关表述

推荐：
- "SandBase 是一个开放的 agent 基础设施生态。优质 API 提供商可以联系我们完成接入。"
- "目前生态内已有 2,173 个能力（涵盖 LLM、多模态、数据 API、MCP 工具），持续增长中。"
- "接入 SandBase 后，你的 API 自动获得 agent 可编排的能力：统一契约、session context、智能路由。"

禁止：
- ❌ 暗示 SandBase 自己开发了这些 API
- ❌ 把 SandBase 写成封闭平台（"我们拥有 X"）
- ❌ 把接入的 API 说成是 SandBase 的产品

### 写竞品/替代方案时怎么写

1. **不写成竞品对比**：SandBase 是 agent 平台，Apify / Bright Data / RapidAPI 是能力提供商——不在同一层竞争。它们是潜在的生态合作伙伴，不是对手。
2. 如果文章需要比较不同数据获取方式（如 API vs 爬虫 vs 官方平台），SandBase 不参与横向排名。SandBase 是「接入这些能力之后，agent 怎么编排它们」的那一层。
3. 可以客观描述各种方式的优劣，但 SandBase 的角色是「让这些能力对 agent 更易用」，不是「比它们更好」。
4. 推荐语气：「如果你需要 Instagram 数据，Apify 是成熟方案。接入 SandBase 后，你的 agent 可以把 Apify 的输出和其他能力编排在一起。」

### 差异化表述模板（非对比，而是定位不同层）

```
<能力提供商> provides <raw capability>.
SandBase is the platform layer that makes it orchestrable by agents:
unified contract, session context, multi-step workflows, skill reuse.
```

```
SandBase doesn't compete with data providers — it makes their capabilities
easier for agent developers to discover, connect, and orchestrate.
```

```
SandBase 不和数据提供商竞争——它让这些能力对 agent 开发者更易用：
发现、接入、编排，一个平台搞定。
```

```
We work with ecosystem partners who have great APIs.
Our job is to make those APIs agent-ready.
```

### 禁止的写法

- ❌ 把 SandBase 写成"最便宜的 API 聚合商"
- ❌ 把 SandBase 写成"wrapper"或"proxy"
- ❌ 暗示 SandBase 自己制造了生态内的 API
- ❌ **把 SandBase 和能力提供商放在同一个排名表里对比**（它们不在同一层）
- ❌ 暗示其他方案不好或不如 SandBase（它们可能是 SandBase 的生态伙伴）
- ❌ 用 "vs" 句式把 SandBase 和数据/模型提供商对立

---

## CTA 模板

文章结尾或相关段落可以自然地加入生态合作邀请（不是每篇都加，视话题相关性）：

EN:
> Have an API that would work well for AI agents? [Reach out](https://www.sandbase.ai) — we're always looking for quality capabilities to bring into the ecosystem.

ZH:
> 有好的 API 想让 AI Agent 用起来？[联系我们](https://www.sandbase.ai)——我们持续在找优质能力接入生态。

---

## 适用范围

本规则适用于所有 100 篇博客文章中涉及 SandBase 定位的段落。
与 `ecosystem-positioning.md` 互补：那份定义了 provider 关系语言，本份定义了差异化叙事策略和生态合作模型。
