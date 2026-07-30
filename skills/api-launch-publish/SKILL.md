---
name: api-launch-publish
description: Prepare a standard SandBase API launch package. Use when the user gives an API/provider/capability name and description and wants Codex to publish or prepare launch materials for Blog, LinkedIn, X/Twitter, and Discord, including positioning, concise social copy, blog draft, Discord announcement, and one reusable SandBase API-generated cover URL.
---

# API 上线发布

## Purpose

Convert a new API, provider integration, or Agent Service into a repeatable launch package for SandBase.

Initial channels:

1. Blog
2. LinkedIn
3. X / Twitter
4. Discord

Do not add Xiaohongshu, WeChat Channels, or other channels unless the user asks. Keep the first SOP focused.

## Required Inputs

Accept rough input from the user, then normalize into:

```json
{
  "api_name": "Exa Search",
  "headline": "Exa Search on SandBase.ai",
  "provider": "Exa",
  "provider_description": "AI-native web search engine that finds exact content using semantic search.",
  "sandbase_service_name": "AI Web Research Agent",
  "sandbase_value": "Turn semantic web search into reusable agent workflows.",
  "capabilities": ["Web Search", "Extraction", "Highlights", "Summary", "Artifacts"],
  "use_cases": ["Company Research", "Competitor Monitor", "Lead Research", "Market Map"],
  "audience": ["Founder", "FDE", "Sales", "Investor", "Builder"],
  "status": "available",
  "docs_url": "",
  "demo_url": ""
}
```

If inputs are missing, infer conservatively. Ask only if the missing detail changes the launch claim, compliance posture, or product positioning.

## Positioning Rule

Always separate the provider layer from the SandBase layer:

```text
<Provider> provides <raw capability>.
SandBase turns it into <agent-ready workflow / reusable Agent Service>.
```

Preferred public formula:

```text
<API> on SandBase.ai
From <raw API/capability> to reusable Agent Services.
```

Avoid positioning SandBase as a thin wrapper. SandBase is the runtime, workflow, session, skill, and artifact layer.

## SOP

1. Normalize the API into a launch config.
2. Write the core one-liner.
3. Write the blog drafts in the SandBase Blog Markdown format.
4. Write LinkedIn copy.
5. Write X/Twitter copy.
6. Write Discord announcement.
7. Generate one reusable blog/social cover URL.
8. Write the generated cover URL into blog frontmatter and `launch-pack.md`.
9. If the user also wants mobile/social variants, run `scripts/generate_api_launch_images.py` through SandBase API using `openai/gpt-image-2`.
10. Save all outputs under `outputs/<api-slug>-launch/`.

## Copy Defaults

### Blog

Use a clear technical founder style:

```text
Article 1: comparison article
Article 2: 2026 Top N roundup article
```

Every product launch should create two SEO-oriented blog articles:

1. A same-category comparison article that highlights the current product's strengths without sounding like an ad.
2. A "2026 Top N" same-category roundup article that places the current product in a broader market map.

Blog length target: 1200-2000 words for SEO-oriented posts unless the user asks for shorter launch copy.

When the launch package is intended for the real SandBase blog, follow `references/blog-format.md`.
Default to producing:

- `blog/en/<product-vs-competitors-slug>.md`
- `blog/zh-CN/<product-vs-competitors-slug>.md`
- `blog/en/<top-n-category-slug>.md`
- `blog/zh-CN/<top-n-category-slug>.md`
- `blog/content-index-row.md`

The English and Chinese posts must share the same slug. The Chinese post is a native rewrite, not a literal translation.

### LinkedIn

Use 6-10 short lines. Lead with product progress.

Template:

```text
<API> is now available on SandBase.ai.

<One sentence about what builders can now do.>

First use cases:
- <use case>
- <use case>
- <use case>

<Provider> provides <raw capability>.
SandBase turns it into an agent-ready workflow.

From APIs to reusable Agent Services.
```

### X / Twitter

Default to one concise post. Use thread only if the user asks.

Template:

```text
<API> on SandBase.ai.

Use <provider capability> inside SandBase agent workflows:

- <capability>
- <capability>
- <capability>

First use cases: <use cases>.

From APIs to Agent Services.
```

### Discord

Use a practical builder announcement. Include what changed, how to try it, and where to give feedback.

Template:

```text
New API available: <API> on SandBase.ai

You can now use <provider capability> inside SandBase workflows.

Useful for:
- <use case>
- <use case>
- <use case>

Try it with: <docs/demo link if available>
Feedback welcome in this channel.
```

## Image Style

Match the SandBase website:

- White or near-white background.
- Subtle square grid.
- Huge black geometric sans-serif headline.
- Small uppercase eyebrow label with wide letter spacing.
- Minimal green accent lines, buttons, and pills.
- Thin-line product/runtime diagram.
- No serif headline.
- No beige magazine style.
- No fake logos, fake metrics, fake users, fake dashboards.
- No dark cyberpunk style.

Read `references/image-formats.md` before generating images.
Use `references/channel-copy-template.md` when producing `launch-pack.md`.
Use `references/blog-format.md` when producing blog-ready Markdown files.

## Image Generation

Default path: generate once, reuse everywhere.

Use the blog cover service path for Blog, LinkedIn, X/Twitter, and Discord:

```bash
python scripts/generate_blog_cover_url.py \
  --title "Exa Search on SandBase.ai" \
  --description "Turn AI-native web search into reusable SandBase Agent Services for research, monitoring, and lead workflows." \
  --category product-updates \
  --article-type launch \
  --out-json /Users/liyb/Documents/Codex/2026-06-26/new-chat/outputs/exa-search-launch/cover-url.json \
  --update-markdown /Users/liyb/Documents/Codex/2026-06-26/new-chat/outputs/exa-search-launch/blog/en/exa-search-on-sandbase.md \
  --update-markdown /Users/liyb/Documents/Codex/2026-06-26/new-chat/outputs/exa-search-launch/blog/zh-CN/exa-search-on-sandbase.md
```

The script calls:

```json
{
  "model": "google/nano-banana-pro",
  "aspect_ratio": "16:9",
  "output_format": "png"
}
```

It returns a public image URL. Reuse that URL in:

- Blog frontmatter `image`
- LinkedIn post image
- X/Twitter post image
- Discord announcement image
- `launch-pack.md`

Optional path: generate local channel-specific PNGs.

Use the SandBase API path only.

```bash
SANDBASE_API_KEY=... python scripts/generate_api_launch_images.py \
  --config references/example-api-launch.json \
  --out-dir /Users/liyb/Documents/Codex/2026-06-26/new-chat/outputs/exa-search-launch \
  --formats 16x9 4x5
```

The script must call:

```json
{
  "model": "openai/gpt-image-2",
  "output_format": "png",
  "quality": "high"
}
```

## Output Files

Minimum:

```text
outputs/<api-slug>-launch/
  launch-pack.md
  blog/en/<product-vs-competitors-slug>.md
  blog/zh-CN/<product-vs-competitors-slug>.md
  blog/en/<top-n-category-slug>.md
  blog/zh-CN/<top-n-category-slug>.md
  blog/content-index-row.md
```

With images:

```text
outputs/<api-slug>-launch/
  launch-pack.md
  cover-url.json
  <api-slug>-16x9.png
  <api-slug>-4x5.png
```

## Quality Check

Before final response:

- Copy is concise enough for the channel.
- Blog has a clear point of view and valid SandBase Blog frontmatter.
- Blog output includes both required article types: comparison and 2026 Top N.
- Blog output includes EN/ZH when requested or when publishing to SandBase Blog.
- Chinese blog copy reads like native Chinese technical writing, not translation.
- Provider is not positioned as the main product.
- SandBase value is explicit.
- Claims are not inflated.
- Discord copy is practical and not too polished.
- Image text is readable and matches the SandBase site style.
- A single reusable cover URL is generated first when publishing to Blog/LinkedIn/X/Discord.
- All generated images used the SandBase API path, not built-in image tools.
