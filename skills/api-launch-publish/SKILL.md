---
name: api-launch-publish
description: Prepare a blog-first, multilingual SandBase API launch package. Use when the user gives an API, provider, capability, or Agent Service and wants publish-ready materials for SandBase Blog, LinkedIn, X/Twitter, Discord, Medium, DEV Community, Zhihu, Xiaohongshu, or future channels, including platform-native rewrites, author voice, claims checks, reusable SandBase API-generated covers, and Xiaohongshu article-screenshot carousels.
---

# API 上线发布

## Purpose

Convert a new API, provider integration, or Agent Service into a repeatable launch package for SandBase.

Default channels:

1. SandBase Blog (canonical source)
2. LinkedIn
3. X / Twitter
4. Discord
5. Medium
6. Zhihu

Optional channels when requested:

- DEV Community
- Xiaohongshu
- WeChat Channels

Do not copy-and-paste one post across channels. Read `references/publication-matrix.md` for the native structure, canonical-link rule, and length for every selected channel.

## Required Inputs

Accept rough input from the user, then normalize into:

```json
{
  "api_name": "Exa Search",
  "headline": "Exa Search on SandBase.ai",
  "provider": "Exa",
  "provider_description": "AI-native web search engine that finds exact content using semantic search.",
  "sandbase_service_name": "AI Web Research Agent",
  "sandbase_value": "Help agents discover, connect, and reuse semantic web search inside real-world workflows.",
  "ecosystem_role": "An external research capability in the SandBase ecosystem of APIs, models, MCP servers, skills, sandboxes, and Agent Services.",
  "capabilities": ["Web Search", "Extraction", "Highlights", "Summary", "Artifacts"],
  "use_cases": ["Company Research", "Competitor Monitor", "Lead Research", "Market Map"],
  "audience": ["Founder", "FDE", "Sales", "Investor", "Builder"],
  "status": "available",
  "docs_url": "",
  "demo_url": "",
  "canonical_url": "",
  "seo_review": {
    "primary_query": "AI search API for agents",
    "reader": "AI builders comparing research capabilities",
    "search_intent": "commercial investigation",
    "location_code": 2840,
    "language_code": "en",
    "seed_keywords": ["agent web search API", "semantic search API"],
    "target_domain": "sandbase.ai"
  },
  "channels": ["blog", "linkedin", "x", "discord"],
  "xiaohongshu": {
    "source_article": "compare",
    "carousel_pages": 6,
    "hook_direction": "specific misconception or decision",
    "pinned_comment_goal": "invite builders to share their current choice"
  },
  "locales": ["en", "zh-CN"],
  "author": {
    "name": "David Li",
    "role": "Founder, SandBase.ai",
    "voice": "technical founder who has built infrastructure and speaks plainly about trade-offs",
    "approved_first_person_facts": [],
    "opinions": []
  },
  "source_facts": [],
  "claim_constraints": []
}
```

`source_facts` is the claims ledger. Every date, metric, customer name, compatibility claim, benchmark, and first-person experience must either appear there with a source URL or be omitted. `approved_first_person_facts` is the only source for "I/we tested", "we learned", or equivalent personal claims.

If inputs are missing, infer conservatively. Ask only if the missing detail changes the launch claim, compliance posture, product positioning, or author truthfulness.

## Positioning Rule

Always separate the provider layer from the SandBase layer:

```text
<Provider> provides <raw capability>.
SandBase makes that capability discoverable, composable, and reusable by agents.
```

Preferred public formula:

```text
<API> is available through the SandBase ecosystem.
Help your agent connect <raw capability> to real-world work.
```

SandBase is not the deployment home for the provider's API. It is the ecosystem and delivery layer that helps agents find, connect, orchestrate, and reuse external capabilities. Those capabilities may be APIs, models, MCP servers, skills, sandboxes, connectors, or Agent Services.

Read `references/ecosystem-positioning.md` before writing copy. Never say that a third-party provider is "deployed on SandBase" unless the user explicitly confirms that deployment fact.


Read `references/differentiation-positioning.md` before writing any SandBase comparison or positioning paragraph. The core differentiator is **Agent Runtime orchestration** (unified contract, session context, tool orchestration, skill reuse, sandbox execution, observability, smart routing), not API aggregation or price. Evaluate competitors neutrally and recommend them where they genuinely fit better.
## SOP

Read `references/content-depth-truth.md` before writing any article. Every article must include real scenarios, specific numbers, comparison matrices, and architecture analysis. No shallow feature lists or vague adjectives. All numbers must be traceable to production API responses or official sources.

1. Normalize the API into a launch config.
2. Write the core one-liner.
3. Write three SandBase Blog drafts in the SandBase Blog Markdown format: the owned product landing article, a comparison article, and a 2026 Top N article.
4. Create native rewrites for every requested platform and locale.
5. Write LinkedIn copy.
6. Write X/Twitter copy.
7. Write Discord announcement.
8. When Xiaohongshu is selected, choose the comparison or Top N article as the source, then create a 4-8 page article-screenshot storyboard, a strong cover hook, native caption, tags, and a first comment. Do not reuse the overseas product-launch cover as the Xiaohongshu carousel.
9. Generate one reusable blog/social cover URL.
10. Write the generated cover URL into blog frontmatter and `launch-pack.md`.
11. If the user also wants mobile/social variants, run `scripts/generate_api_launch_images.py` through SandBase API using `openai/gpt-image-2`.
12. When SEO data is needed, use `scripts/dataforseo_seo_review.py` to create an evidence pack for the declared keyword, market, and search intent. This is a billable external request and requires explicit operator approval through `--allow-billable-requests`.
13. Run the independent Content, Visual, SEO, GEO, and DataForSEO Evidence Reviewer described in `references/reviewer-role.md`. It must write `review-report.md` and can return only `APPROVED` or `REVISE`.
14. Fix every blocking issue, then run the package checks in `references/quality-gates.md`.
15. Save all outputs under `outputs/<api-slug>-launch/`.

Run the structural package check before handoff:

```bash
python scripts/validate_content_package.py \
  --input outputs/<api-slug>-launch/input.json \
  --package outputs/<api-slug>-launch \
  --require-approved-review
```

When DataForSEO evidence is requested, add `--require-dataforseo-evidence`. The evidence call is deliberately not automatic:

```bash
python scripts/dataforseo_seo_review.py \
  --input outputs/<api-slug>-launch/input.json \
  --package outputs/<api-slug>-launch \
  --env-file /absolute/path/to/.env.local \
  --allow-billable-requests
```

The environment file must contain `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD`. Never commit it. DataForSEO data validates query/intent fit; it does not prove rankings, reader demand, or product-market fit.

### DataForSEO Editorial Loop

When a package has `seo_review`, the order is mandatory:

1. Define one primary query, intended reader, intent, location, language, and up to nine supporting queries in `input.json`.
2. Run `dataforseo_seo_review.py` and archive `dataforseo-seo-evidence.json` and `.md` inside the launch package.
3. Revise the three canonical articles before review:
   - **Owned launch:** answer the primary task directly and name the provider, SandBase Agent Service, and relevant capability boundaries.
   - **Comparison:** organize by the actual decision implied by the SERP, include trade-offs, and avoid an unsupported winner claim.
   - **Top N:** present a shortlist or clear evaluation method. Do not use numbered ranks unless an explicit, reproducible scoring method is disclosed.
4. If the article quotes a DataForSEO metric or SERP observation publicly, name DataForSEO, market, and retrieval date. Never turn a sampled result into a traffic, ranking, or demand promise.
5. The independent reviewer reads the evidence pack, records its findings under `## DataForSEO Evidence`, and can block publication for an intent mismatch.

## Canonical Article, Platform Rewrites, and Locales

Write three related SandBase Blog articles per locale: one owned product landing article, one comparison article, and one 2026 Top N article. Then make a new argument for each external publishing surface; do not summarize mechanically.

- **SandBase Blog:** durable technical source of truth. Original research, decision rules, evidence, and canonical URL.
- **Medium:** a founder-led argument or field note for a broad global technical audience. Add a canonical link to SandBase when the article substantially overlaps.
- **DEV Community:** a builder tutorial, implementation note, or comparison with a concrete setup path. Add a canonical link when it overlaps.
- **Zhihu:** a Chinese answer or long-form analysis beginning with a question people would actually ask; lead with conclusion and explain the reasoning in Chinese.
- **Xiaohongshu:** a Chinese article-screenshot carousel led by a practical, curiosity-inducing hook. Use the comparison or Top N article as evidence; write platform-native caption, tags, and first comment. Do not post a generic product-poster carousel.
- **LinkedIn / X / Discord:** distribution assets, not miniature blogs.

English and Chinese blog posts can share a slug, but Chinese must be a native rewrite, not a sentence-by-sentence translation. For any additional locale, read `references/localization.md` before drafting.

## Author Voice and Human Standard

Read `references/author-voice.md` before writing long-form content.

The article should sound like a person with real judgment, not a corporate content pipeline:

- Start from a tension, trade-off, surprise, or practical decision. Do not open with generic market context.
- Write a point of view and its limits. Name where another approach is better.
- Use a first-person observation only when it is in `approved_first_person_facts`.
- Prefer a concrete engineering consequence over generic adjectives such as "powerful", "seamless", or "game-changing".
- Do not manufacture interviews, usage, customers, benchmarks, or emotions to make a post feel real.
- Vary structure by platform. A human writer adapts to the room.

## Copy Defaults

### Blog

Use a clear technical founder style:

```text
Article 1: owned product landing article
Article 2: comparison article
Article 3: 2026 Top N roundup article
```

Every product launch should create three SandBase Blog articles:

1. An owned product landing article that explains the capability through the SandBase ecosystem and gives readers a direct next step.
2. A same-category comparison article that highlights the current product's strengths without sounding like an ad.
3. A "2026 Top N" same-category roundup article that places the current product in a broader market map.

The owned product article is the canonical SandBase conversion page. The comparison and Top N articles are the outward-facing discovery pieces: distribute them externally, and use either one as the source for Xiaohongshu article screenshots.

Blog length target: 1200-2000 words for SEO-oriented posts unless the user asks for shorter launch copy.

When the launch package is intended for the real SandBase blog, follow `references/blog-format.md` and `references/author-voice.md`.
Default to producing:

- `blog/en/<product-vs-competitors-slug>.md`
- `blog/zh-CN/<product-vs-competitors-slug>.md`
- `blog/en/<top-n-category-slug>.md`
- `blog/zh-CN/<top-n-category-slug>.md`
- `blog/en/<product-on-sandbase-slug>.md`
- `blog/zh-CN/<product-on-sandbase-slug>.md`
- `blog/content-index-row.md`

Medium and Zhihu are default channels, so every launch also produces:

- `medium/en/<slug>.md` for the selected English long-form angle
- `zhihu/zh-CN/<slug>.md` for the selected Chinese question-led angle
- `manifest.json` recording canonical URL, localization status, image URL, source facts, and publication status

When `channels` additionally includes DEV Community, also produce:

- `devto/en/<slug>.md` for every selected English builder angle

When `channels` includes Xiaohongshu, additionally produce:

- `xiaohongshu/zh-CN/<article-screenshot-carousel-slug>.md` containing the cover hook, exact screenshot order, caption, tags, and first comment

The English and Chinese posts must share the same slug. The Chinese post is a native rewrite, not a literal translation.

### LinkedIn

Use 6-10 short lines. Lead with product progress.

Template:

```text
<API> is now available through the SandBase ecosystem.

<One sentence about what builders can now do.>

First use cases:
- <use case>
- <use case>
- <use case>

<Provider> provides <raw capability>.
SandBase helps agents connect and reuse it in real-world workflows.

From fragmented capabilities to connected Agent Services.
```

### X / Twitter

Default to one concise post. Use thread only if the user asks.

Template:

```text
<API> is now available through SandBase.

Use <provider capability> inside SandBase agent workflows:

- <capability>
- <capability>
- <capability>

First use cases: <use cases>.

Connect your agent to the real world.
```

### Discord

Use a practical builder announcement. Include what changed, how to try it, and where to give feedback.

Template:

```text
New ecosystem capability: <API>

Agents can now discover and reuse <provider capability> in SandBase workflows.

Useful for:
- <use case>
- <use case>
- <use case>

Try it with: <docs/demo link if available>
Feedback welcome in this channel.
```

## Image Style

Use the fixed SandBase visual system. Read `references/visual-system.md` for the complete cover generation workflow.

**Critical rule**: Generated image URLs from `media.sandbase.ai/files/` are **temporary**. They must be uploaded to `static.sandbase.ai/blog/covers/` via `sandbase-blog/scripts/migrate_covers.py` before publication. The only acceptable final URL pattern is `https://static.sandbase.ai/blog/covers/{slug}.{ext}`.

Read `references/image-formats.md` before generating images.
Read `references/visual-system.md` before generating images.
Use `references/channel-copy-template.md` when producing `launch-pack.md`.
Use `references/xiaohongshu-format.md` when producing Xiaohongshu materials.
Use `references/blog-format.md` when producing blog-ready Markdown files.
Use `references/publication-matrix.md` for platform-native rewrites.
Use `references/localization.md` for locale-specific drafting.
Use `references/author-voice.md` and `references/quality-gates.md` before handoff.
Use `references/reviewer-role.md` for the required independent review pass.

## Image Generation

Default path: generate one visual background through SandBase Image API, render deterministic SandBase typography over it, then reuse the final asset everywhere.

For `comparison` and `top-n` articles, set `cover_kind` in the image config. The final cover must contain the exact eyebrow, headline, subtitle, and capability label from the deterministic renderer. Never publish the generated background by itself.

Use the blog cover service path for Blog, LinkedIn, X/Twitter, and Discord:

```bash
python scripts/generate_blog_cover_url.py \
  --title "Exa Search on SandBase.ai" \
  --description "Turn AI-native web search into reusable SandBase Agent Services for research, monitoring, and lead workflows." \
  --category product-updates \
  --article-type launch \
  --out-json outputs/exa-search-launch/cover-url.json \
  --update-markdown outputs/exa-search-launch/blog/en/exa-search-on-sandbase.md \
  --update-markdown outputs/exa-search-launch/blog/zh-CN/exa-search-on-sandbase.md
```

The URL-only fallback script calls:

```json
{
  "model": "google/nano-banana-pro",
  "aspect_ratio": "16:9",
  "output_format": "png"
}
```

It returns a public image URL. Use it only when a public URL is required before a final composed asset can be uploaded. For controlled typography, use `generate_api_launch_images.py`, which calls the SandBase API and renders the final local asset.

Reuse the final cover asset in:

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
  --out-dir outputs/exa-search-launch \
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
  manifest.json
  input.json
  review-report.md
  blog/en/<product-vs-competitors-slug>.md
  blog/zh-CN/<product-vs-competitors-slug>.md
  blog/en/<top-n-category-slug>.md
  blog/zh-CN/<top-n-category-slug>.md
  blog/en/<product-on-sandbase-slug>.md
  blog/zh-CN/<product-on-sandbase-slug>.md
  blog/content-index-row.md
  medium/en/<platform-native-argument-slug>.md
  zhihu/zh-CN/<question-led-slug>.md
  devto/en/<optional-builder-slug>.md
  xiaohongshu/zh-CN/<optional-article-screenshot-carousel-slug>.md
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
- Blog output includes the owned product landing article plus both outward-facing article types: comparison and 2026 Top N.
- Blog output includes EN/ZH when requested or when publishing to SandBase Blog.
- Chinese blog copy reads like native Chinese technical writing, not translation.
- Provider is not positioned as the main product.
- SandBase value is explicit.
- Claims are not inflated.
- Discord copy is practical and not too polished.
- Every selected external long-form channel has a native angle and its canonical-link policy is correct.
- Every locale is a native rewrite with local search intent, examples, idiom, and CTA; it is not a literal translation.
- Every first-person line can be traced to `approved_first_person_facts`.
- Every public fact, metric, date, customer claim, and compatibility claim can be traced to `source_facts`.
- The long-form draft has a clear author judgment, a named trade-off, and at least one concrete decision rule.
- Image text is readable and matches the SandBase site style.
- A single reusable cover URL is generated first when publishing to Blog/LinkedIn/X/Discord.
- All generated images used the SandBase API path, not built-in image tools.
- The generated visual contains no model-rendered words, logos, UI screenshots, fake metrics, or fake provider claims.
- The final title, eyebrow, subtitle, and capability label are rendered deterministically from the launch config.
- An independent reviewer has written `review-report.md` with `Status: APPROVED`; a `REVISE` result blocks publication.
- The reviewer has visually checked final raster assets, not just prompts or frontmatter.
- Every final cover has a readable deterministic headline; a text-free generated background is not itself a publishable cover.
- The final cover uses a durable URL from `static.sandbase.ai/blog/covers/`. Temporary URLs from `media.sandbase.ai/files/` must be migrated via `migrate_covers.py` before publication.
- Public copy describes the integration as a SandBase ecosystem capability, not a provider deployment on SandBase.
- Xiaohongshu uses a strong native hook and a 4-8 page article-screenshot carousel sourced from the comparison or Top N article; it does not reuse the generic overseas launch poster.
