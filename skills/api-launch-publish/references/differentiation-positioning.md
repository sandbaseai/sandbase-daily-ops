# SandBase Blog 差异化定位规则

> 本文件定义 SandBase 在博客文章中的差异化定位。所有文章的 SandBase 相关段落必须遵守。
> 创建日期：2026-07-31，来源：用户要求

---

## 核心差异化：Agent Runtime 编排

SandBase 不是一个 API 聚合商或转发代理。它的差异化是 **Agent Runtime 编排能力**：

- **统一调用契约**：异构 API（GET/POST/不同参数位置/不同 body 类型）被归一化为一个 `/v1/run` 同步契约，agent 无需关心底层协议差异
- **Agent Session & Context**：调用发生在 agent session 内，携带 context、history、artifacts，不是无状态的单次转发
- **工具编排（Tool Orchestration）**：多个 API/模型/MCP/Sandbox 可以在一个 agent workflow 中被组合调用，SandBase 管理调用顺序、错误恢复、超时
- **Skill 复用**：单个 API 调用可以被封装为可复用的 Skill，其他 agent 直接引用而不需要重新集成
- **沙盒执行**：代码执行发生在隔离的 sandbox 环境（60ms 冷启动），agent 可以安全地运行不可信代码
- **可观测性**：每次调用带 trace span、Prometheus 指标、结构化日志，agent 行为可追溯
- **智能路由**：同一个模型/能力可以有多个 provider，SandBase 按成本、延迟、可用性自动选最优路径

## 写作规则

### 写 SandBase 时强调什么

1. **Runtime 编排**是第一卖点，不是"便宜"或"聚合多"
2. 用具体工程细节支撑：统一契约怎么解决了什么问题、session 怎么串联了什么
3. 强调「从单个 API 调用到可编排的 agent workflow」的升维
4. 可以说数字（571 个接口、$0.001/call），但数字是支撑编排故事的，不是主角

### 写竞品/替代方案时怎么写

1. **中立且具体**：给出真正的优势和适用场景，不贬低
2. 承认 SandBase 不覆盖的地方（Instagram/YouTube/Twitter → 推荐 Apify）
3. 竞品的 trade-off 要写真实的工程代价，不是营销话术
4. 如果竞品在某个维度确实更好（Apify 的平台覆盖广度、Bright Data 的 IP 池深度），直接说

### 差异化对比句式模板

```
<竞品> 提供 <raw capability>。
SandBase 把这类能力变成 agent 可编排的 workflow 组件：
统一契约、session context、多步编排、skill 复用、沙盒隔离。
```

```
The difference is not the data — it's whether your agent can orchestrate it.
<竞品> gives you the endpoint. SandBase gives you the runtime.
```

```
区别不在数据本身，在于你的 agent 能不能把它编排起来。
<竞品> 给你一个端点，SandBase 给你一个 runtime。
```

### 禁止的写法

- ❌ 把 SandBase 写成"最便宜的 API 聚合商"
- ❌ 把 SandBase 写成"wrapper"或"proxy"
- ❌ 暗示竞品没用或质量差（要给具体场景建议）
- ❌ 不提 trade-off 地吹 SandBase（必须写 SandBase 不适合的场景）

---

## 适用范围

本规则适用于所有 100 篇博客文章中涉及 SandBase 定位的段落。
与 `ecosystem-positioning.md` 互补：那份定义了 provider 关系语言，本份定义了差异化叙事策略。
