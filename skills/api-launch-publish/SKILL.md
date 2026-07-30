---
name: api-launch-publish
description: Prepare a standard SandBase API launch package. Use when the user gives an API/provider/capability name and description and wants Codex to publish or prepare launch materials for Blog, LinkedIn, X/Twitter, and Discord, including positioning, concise social copy, blog draft, Discord announcement, and optional SandBase API-generated gpt-image-2 launch images.
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
3. Write the blog draft.
4. Write LinkedIn copy.
5. Write X/Twitter copy.
6. Write Discord announcement.
7. Generate or update image prompts.
8. If the user wants images, run `scripts/generate_api_launch_images.py` through SandBase API using `openai/gpt-image-2`.
9. Save all outputs under `outputs/<api-slug>-launch/`.

## Copy Defaults

### Blog

Use a clear technical founder style:

```text
Title
Why this API matters
What the provider does
What SandBase adds
First use cases
From API to Agent Service
What comes next
```

Blog length target: 600-1000 words unless the user asks for shorter.

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

## Image Generation

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
```

With images:

```text
outputs/<api-slug>-launch/
  launch-pack.md
  <api-slug>-16x9.png
  <api-slug>-4x5.png
```

## Quality Check

Before final response:

- Copy is concise enough for the channel.
- Blog has a clear point of view.
- Provider is not positioned as the main product.
- SandBase value is explicit.
- Claims are not inflated.
- Discord copy is practical and not too polished.
- Image text is readable and matches the SandBase site style.
- All generated images used the SandBase API path, not built-in image tools.
