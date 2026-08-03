# 博客文章截图与部署 SOP

> 写完文章后的标准流程：截图配图 → 构建验证 → 部署 → 索引提交。

---

## 一、截图配图（通过 SandBase DataForSEO API）

### 截图 API 调用方式

```bash
export $(grep -v '^#' ~/.config/sandbase/.env | xargs)

curl -s -X POST https://api.sandbase.ai/v1/run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -d '{
    "model": "dataforseo/v3/on_page/page_screenshot",
    "url": "https://目标网页URL",
    "browser_preset": "desktop",
    "full_page_screenshot": false,
    "disable_cookie_popup": true,
    "accept_language": "en"
  }'
```

### 参数说明

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `browser_preset` | 视口尺寸 | `desktop`(1920x1080) / `mobile`(390x844) / `tablet`(1024x1366) |
| `full_page_screenshot` | 是否截整页 | `false`（只截可见区域，避免太长） |
| `disable_cookie_popup` | 关闭 cookie 弹窗 | `true` |
| `accept_language` | 语言 | `en` |
| `browser_screen_width` | 自定义宽 | 覆盖 preset，最小 240 最大 9999 |

### 返回结构

```json
{
  "outputs": [{
    "tasks": [{
      "result": [{
        "items": [{"image": "https://api.dataforseo.com/cdn/screenshot/..."}]
      }]
    }]
  }]
}
```

截图 URL 在 `outputs[0].tasks[0].result[0].items[0].image`。

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 骨架屏/内容没加载 | SPA 页面 JS 未执行完 | 换静态页面或等模型提供 SSR 版本 |
| Cookie 弹窗遮挡 | `disable_cookie_popup` 不生效 | 有些站点弹窗不标准，换别的 URL |
| "Target URL is invalid" | URL 格式问题或 robots.txt 禁止 | 检查 URL 是否有特殊字符，换备选 |
| 内容被 CDN 拦截 | IP 池被识别为爬虫 | 加 `"switch_pool": true` 或 `"ip_pool_for_scan": "us"` |

### 推荐截图源

| 目的 | 推荐 URL | 备注 |
|------|----------|------|
| 模型规格 | `https://www.together.ai/models/{model}` | 渲染稳定，有 benchmark 数据 |
| 模型定价 | `https://openrouter.ai/{vendor}/{model}` | 有详细价格表 |
| 排行榜 | `https://artificialanalysis.ai/leaderboards/models` | 渲染稳定，数据表格清晰 |
| Qwen 官方 | `https://qwen.ai/blog?id={post-id}` | 需要确认 SSR 正确加载 |
| Qwen 聊天 | `https://chat.qwen.ai` | 展示模型选择器 |
| 阿里云平台 | `https://www.alibabacloud.com/en/solutions/generative-ai/qwen` | 企业定位全貌 |
| Hugging Face | `https://huggingface.co/{org}` | 开源社区数据 |
| GitHub | `https://github.com/{org}` | 仓库和 star 数据 |

### 截图后处理

1. **下载到本地验证**：
```bash
curl -sLo /tmp/screenshot.png "https://api.dataforseo.com/cdn/screenshot/..."
```

2. **检查截图内容**（用 Image 工具查看，确认无弹窗/骨架屏）

3. **上传到 COS 永久存储**：
```bash
cd /root/kiro/sandbase-monorepo/sandbase-registry
export $(grep -v '^#' .env | xargs)
./sandbase-registry upload-file --file /tmp/screenshot.png --key blog/screenshots/{描述性文件名}.png
```

4. **插入文章**：
```markdown
![Alt 描述](https://static.sandbase.ai/blog/screenshots/{文件名}.png)
*Caption 说明截图内容和来源*
```

---

## 二、构建验证

```bash
cd /root/kiro/sandbase-blog
npm run check   # 0 errors
npm run build   # 确认 page count 正确
```

---

## 三、部署（Blog 直接 push main）

```bash
cd /root/kiro/sandbase-blog

# Stage 所有改动的文件
git add src/content/en/{slug}.md src/content/zh-CN/{slug}.md scripts/ai-content-generator/content-index.md

# Commit（包含文章摘要和 SEO 数据）
git commit -m "feat(blog): add {文章标题}

- EN + ZH versions
- Screenshots from {来源}
- Google Indexing + IndexNow submitted"

# Push 触发 Cloudflare Pages 自动部署
git push origin main
```

部署后约 1-2 分钟 Cloudflare Pages 构建完成，可访问 `https://blog.sandbase.ai/blog/{slug}/` 验证。

---

## 四、索引提交

### Google Indexing API

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/indexing']
creds = service_account.Credentials.from_service_account_file(
    '/root/.config/sandbase/google-service-account.json', scopes=SCOPES)
service = build('indexing', 'v3', credentials=creds)

urls = [
    'https://blog.sandbase.ai/blog/{slug}/',
    'https://blog.sandbase.ai/blog/zh-CN/{slug}/',
]
for url in urls:
    body = {'url': url, 'type': 'URL_UPDATED'}
    service.urlNotifications().publish(body=body).execute()
    print(f'✅ {url}')
```

### IndexNow (Yandex + Bing)

```bash
cd /root/kiro/sandbase-daily-ops
export $(grep -v '^#' ~/.config/sandbase/.env | xargs)
python3 scripts/submit_indexnow.py --limit 12
```

> ⚠️ Bing 目前 403，需重新验证 Webmaster Tools。Yandex 正常 202。

---

## 五、SEO 优化检查流程（配合 DataForSEO）

### 查询关键词搜索量

```bash
curl -s -X POST https://api.sandbase.ai/v1/run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -d '{
    "model": "dataforseo/v3/keywords_data/google_ads/search_volume/live",
    "keywords": ["keyword1", "keyword2"],
    "language_code": "en",
    "location_code": 2840
  }'
```

### 查询 SERP 竞品排名

```bash
curl -s -X POST https://api.sandbase.ai/v1/run \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -d '{
    "model": "dataforseo/v3/serp/google/organic/live/regular",
    "keyword": "target keyword",
    "language_code": "en",
    "location_code": 2840,
    "depth": 10
  }'
```

### GSC 数据分析（识别优化机会）

```python
# 通过 sc-domain:sandbase.ai 查询
# 重点关注：
# - 高曝光低CTR（title/desc需优化）
# - pos 10-20（冲首页机会）
# - pos<10 零点击（snippet需改善）
```

---

## 六、文件路径速查

```
# 博客内容
/root/kiro/sandbase-blog/src/content/en/{slug}.md
/root/kiro/sandbase-blog/src/content/zh-CN/{slug}.md

# 内容索引
/root/kiro/sandbase-blog/scripts/ai-content-generator/content-index.md

# 封面生成
/root/kiro/sandbase-blog/scripts/ai-content-generator/regen-one.ts

# 截图上传工具
/root/kiro/sandbase-monorepo/sandbase-registry/sandbase-registry upload-file

# IndexNow 提交
/root/kiro/sandbase-daily-ops/scripts/submit_indexnow.py

# Google SA 凭证
/root/.config/sandbase/google-service-account.json

# 环境变量
~/.config/sandbase/.env
```
