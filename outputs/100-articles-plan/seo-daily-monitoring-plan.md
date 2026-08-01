# SEO 每日巡检方案

> 目标：每天自动检查文章收录、排名、流量，生成巡检报告
> 创建日期：2026-08-01

---

## 数据源

| 数据源 | 能看什么 | 成本 | 需要什么凭据 |
|---|---|---|---|
| Google Search Console API | 展示、点击、CTR、平均排名、收录状态 | 免费 | Service Account JSON |
| DataForSEO SERP | 精确排名位置、竞争对手排名 | ~$0.05/关键词/次 | 已有 |
| GA4 Reporting API | 页面浏览、用户数、停留时间、跳出率 | 免费 | Service Account JSON |

建议三个都接入，但 **GSC 是核心**——它是唯一能告诉你"Google 给了你多少展示"的来源。

---

## 你需要做的（一次性，约 10 分钟）

### Step 1: 创建 Google Cloud Service Account

1. 打开 https://console.cloud.google.com/
2. 选择或创建一个项目（如 "sandbase-seo-monitor"）
3. 左侧菜单 → IAM & Admin → Service Accounts → Create Service Account
4. 名称随意（如 "seo-daily-check"），点 Create
5. 权限页跳过（不需要项目级权限），点 Done
6. 点进刚创建的 Service Account → Keys → Add Key → Create new key → JSON → 下载

### Step 2: 授权 GSC 访问

1. 打开 https://search.google.com/search-console/
2. 选择 `www.sandbase.ai` 属性
3. 设置 → 用户和权限 → 添加用户
4. 邮箱填 Service Account 的邮箱（类似 `seo-daily-check@sandbase-seo-monitor.iam.gserviceaccount.com`）
5. 权限选"完整"或"受限"（受限够用，只读）

### Step 3: 启用 API

1. 在 Google Cloud Console → APIs & Services → Enable APIs
2. 搜索并启用：
   - "Google Search Console API"（也叫 "Search Console API"）
   - "Google Analytics Data API"（GA4，可选）

### Step 4: 把凭据文件放到服务器

```bash
# 上传后放到安全位置
mkdir -p ~/.config/sandbase
# 把下载的 JSON 文件传到这里：
# ~/.config/sandbase/google-service-account.json
chmod 600 ~/.config/sandbase/google-service-account.json
```

### Step 5: 安装依赖

```bash
pip install google-auth google-auth-httplib2 google-api-python-client
```

完成后告诉我"凭据放好了"，我立刻写巡检脚本并设 cron。

---

## 每日巡检脚本功能（我来写）

```
每天早 8 点自动执行：

1. GSC 数据拉取（前一天）
   - 100 篇文章各自的展示/点击/CTR/平均排名
   - 哪些新 URL 被收录了
   - 哪些查询词匹配到了我们的文章
   - 404 错误和爬取问题

2. DataForSEO 排名检查（每周一次，省钱）
   - 13 个高价值关键词的精确排名
   - 排名变化趋势（对比上周）

3. 生成巡检报告
   - 收录进度：N/100 篇已收录
   - 排名变化：哪些文章进了前 10/前 30
   - 流量 Top 10 文章
   - 异常告警：排名大跌、新 404、爬取错误

4. 推送报告
   - 存到 outputs/seo-daily-reports/YYYY-MM-DD.md
   - 可选：webhook 推送摘要到 Slack/飞书
```

---

## 预期报告样例

```markdown
# SEO 巡检报告 2026-08-15

## 收录状态
- 已收录: 87/100 (87%)
- 本周新收录: 12 篇
- 未收录: 13 篇（列表见下）

## 流量 Top 5（昨日）
| 文章 | 展示 | 点击 | CTR | 排名 |
|---|---|---|---|---|
| best-image-to-video-models-agents-2026 | 1,240 | 89 | 7.2% | 8.3 |
| anthropic-cache-pricing-5m-1h-explained | 340 | 42 | 12.4% | 4.1 |
| ...

## 排名变化
- ⬆️ anthropic-cache-pricing: #12 → #4 (+8)
- ⬆️ best-image-to-video: #28 → #8 (+20)
- ➡️ llm-api-pricing: #15 (unchanged)
- ⬇️ gpt-5-6-release: #9 → #14 (-5)

## 告警
- ⚠️ 3 篇文章 14 天未收录（需检查）
- ⚠️ normalizing-431 排名从 #20 跌出 top 30

## 建议动作
1. 未收录的 13 篇：提交 URL inspection 请求
2. anthropic-cache-pricing 进前 5 且 CTR 12%：考虑扩展 cluster
3. gpt-5-6-release 排名下跌：检查是否有新竞争内容
```

---

## 成本

| 项目 | 频率 | 成本 |
|---|---|---|
| GSC API | 每天 | 免费 |
| GA4 API | 每天 | 免费 |
| DataForSEO 排名 | 每周一 | ~$0.65/周（13 词） |
| **月总计** | | **~$2.60/月** |

---

## 等你完成后我做什么

1. 写 `seo_daily_check.py` 脚本（含 GSC + DataForSEO）
2. 设 cron job 每天早 8 点跑
3. 设 webhook 推送摘要（如果你要）
4. 第一次跑后根据数据调整巡检维度
