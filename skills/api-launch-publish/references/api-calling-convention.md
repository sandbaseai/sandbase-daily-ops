# SandBase API 调用规范（代码示例用）

> 本文件定义博客文章中代码示例的正确写法。SandBase 没有专属 SDK。
> 创建日期：2026-08-01

---

## 核心规则

1. **SandBase 没有 SDK**。所有调用都是标准 HTTP 请求。
2. LLM 调用可以用 OpenAI SDK 或 Anthropic SDK（因为协议兼容），但必须设 `base_url`。
3. 非 LLM 调用（社媒数据 API、图片生成、视频生成）**必须用 HTTP 直接调 `/v1/run`**，不能用 OpenAI SDK。

---

## 三种调用模式

### 模式 1：LLM（sync，协议兼容）

LLM 走标准 OpenAI/Anthropic 协议，可以用对应 SDK：

```python
# OpenAI 协议兼容（GPT 系列、DeepSeek、Kimi 等）
from openai import OpenAI
client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="sk-...")
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-5",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=1000
)
print(response.choices[0].message.content)
```

```python
# Anthropic 协议兼容（Claude 系列）
from anthropic import Anthropic
client = Anthropic(base_url="https://api.sandbase.ai", api_key="sk-...")
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.content[0].text)
```

### 模式 2：数据 API（sync，POST /v1/run）

社媒数据等同步 API，直接 HTTP POST：

```python
import requests

response = requests.post(
    "https://api.sandbase.ai/v1/run",
    headers={"Authorization": "Bearer sk-...", "Content-Type": "application/json"},
    json={
        "model": "douyin/search/challenge-search-v1",
        "keyword": "AI创作",
        "count": 20
    }
)
result = response.json()
# result 直接是数据，无需轮询
```

```bash
curl -X POST https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "douyin/search/challenge-search-v1", "keyword": "AI创作", "count": 20}'
```

**请求参数**：每个模型的参数看 `unified_schema` 中的 `GenerationRequest.properties`。
**响应**：同步返回 JSON 数据。

### 模式 3：图片/视频生成（async，POST /v1/run → GET 轮询）

异步模型需要两步：提交 → 轮询结果。

```python
import requests
import time

API_KEY = "sk-..."
BASE = "https://api.sandbase.ai"

# Step 1: Submit generation
submit = requests.post(
    f"{BASE}/v1/run",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json={
        "model": "minimax/h3/text-to-video",
        "prompt": "A cinematic shot of a cat walking on a beach at sunset",
        "duration": 5,
        "aspect_ratio": "16:9"
    }
).json()

task_id = submit["id"]
print(f"Submitted: {task_id}, status: {submit['status']}")

# Step 2: Poll for result
while True:
    result = requests.get(
        f"{BASE}/v1/run/{task_id}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    ).json()

    status = result["status"]
    print(f"Status: {status}")

    if status in ("completed", "failed", "timeout"):
        break
    time.sleep(3)

# Step 3: Get output URL
if status == "completed":
    video_url = result["outputs"][0]["url"]
    print(f"Video: {video_url}")
```

**注意**：图片模型的轮询端点有的是 `/v1/generations/{id}`（Seedream、Qwen-Image），有的是 `/v1/run/{id}`（MiniMax H3、Kling）。以各模型 `unified_schema` 中的 paths 为准。

### 图片生成示例（Seedream）

```python
# Submit
submit = requests.post(
    f"{BASE}/v1/run",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json={
        "model": "bytedance/seedream/5.0/pro",
        "prompt": "A minimalist product photo of wireless earbuds on white marble",
        "aspect_ratio": "1:1",
        "output_format": "png"
    }
).json()

task_id = submit["id"]

# Poll (注意：Seedream 用 /v1/generations/{id})
while True:
    result = requests.get(
        f"{BASE}/v1/generations/{task_id}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    ).json()
    if result["status"] in ("completed", "failed", "timeout"):
        break
    time.sleep(2)

if result["status"] == "completed":
    image_url = result["outputs"][0]["url"]
```

---

## 每个模型的参数来源

每个模型的 `unified_schema.components.schemas.GenerationRequest.properties` 定义了可用参数。

### 常用模型参数速查

| 模型 | 必填参数 | 可选参数 | 轮询端点 |
|---|---|---|---|
| `minimax/h3/text-to-video` | prompt, duration | aspect_ratio, resolution | `/v1/run/{id}` |
| `kwaivgi/kling-video/v3` | prompt | image, video, duration, aspect_ratio, resolution, multi_prompt, generate_audio | `/v1/run/{id}` |
| `bytedance/seedream/5.0/pro` | prompt | aspect_ratio, output_format | `/v1/generations/{id}` |
| `alibaba/qwen-image-3` | prompt | aspect_ratio, output_format | `/v1/generations/{id}` |
| `douyin/search/*` | 各端点不同 | — | 同步，无需轮询 |
| `weibo/web-v2/*` | 各端点不同 | — | 同步，无需轮询 |

---

## 禁止的写法

- ❌ 用 `openai.OpenAI().chat.completions.create()` 调图片/视频/数据 API
- ❌ 用 `extra_body` 传参给非 LLM 模型
- ❌ 用 `messages=[]` 调非 LLM 模型
- ❌ 说"SandBase SDK"或"SandBase Python 客户端"
- ❌ 编造不存在的参数名（必须查 unified_schema）

---

## 正确表述

- ✅ "SandBase 兼容 OpenAI 和 Anthropic 协议，LLM 调用可以直接用对应 SDK"
- ✅ "非 LLM 能力通过 POST /v1/run 调用，参数按模型的 schema 传入"
- ✅ "异步模型（图片/视频）需要提交后轮询结果"
- ✅ "所有调用只需一把 API Key + 标准 HTTP"
