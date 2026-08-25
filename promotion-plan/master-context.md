# SandBase Promotion Master Context

Last verified: 2026-08-24
Owner: SandBase growth operations
System of record: `sandbaseai/sandbase-daily-ops`

## 1. North-star objective

Increase qualified, non-brand Google discovery by 100× while turning that discovery into API adoption, Skill installs, CLI connections, GitHub engagement, and repeat usage.

- Frozen primary baseline: 119 non-brand Google clicks in the rolling 28-day GSC window captured 2026-08-23.
- Target: 11,900 non-brand Google clicks in a comparable rolling 28-day window.
- Supporting baseline: 515 whole-site clicks, 44,665 whole-site impressions; 168 Blog clicks, 5,578 Blog impressions; 9,131 non-brand impressions at 1.3% CTR.
- Measurement source: Google Search Console through the `sandbase-blog` operations workflow.
- Review cadence: daily leading indicators; 14-day and 28-day outcome reviews.

Never redefine success around page count, impressions alone, generated drafts, or unverified ranking estimates.

## 2. Canonical positioning

### Umbrella statement

**SandBase turns AI capabilities into deliverable agent workflows: one API surface for models and real-world APIs, portable Skills for repeatable work, a CLI/MCP bridge for agent clients, and a local-first Harness for governed execution.**

### Short API statement

**One API for LLMs, image generation, video generation, and real-world tools.**

### Product pillars

| Pillar | Job | Primary audience | Boundary |
|---|---|---|---|
| SandBase API / Store | Discover and call LLM, image, video, audio, embedding, moderation, search, social, data, and other APIs through a shared account and operational surface | AI application developers, Agent builders, FDEs | Do not imply every modality shares one literal schema or lifecycle |
| SandBase Skills | Package repeatable research, marketing, social-intelligence, and business workflows for compatible agents | Codex, Claude Code, Cursor, Gemini CLI, DeepSeek Harness users | Skills define procedure; they are not themselves hosted models or API execution |
| SandBase CLI / MCP bridge | Connect supported AI clients to SandBase model/API discovery and execution | Developers who want local setup and MCP access | Lightweight bridge, not a full durable Agent runtime |
| SandBase Harness | Run persistent, sandboxed, auditable Agents on local or self-owned infrastructure | Platform and infrastructure teams | Runtime/control layer, not a model marketplace or visual workflow builder |
| SandBase Blog | Capture search intent and explain models, APIs, tools, comparisons, migrations, and production trade-offs | Search visitors and technical evaluators | Editorial evidence and education, not unsupported product claims |
| SandBase Docs | Convert intent into successful setup, API calls, schemas, and troubleshooting | Developers ready to evaluate or integrate | Operational source of truth; time-sensitive catalog claims require current verification |

### Message hierarchy

1. Start with the reader's task: call a model/API, install a workflow, connect an Agent client, or run governed Agents.
2. Explain the relevant SandBase pillar in one sentence.
3. State the integration or operating boundary honestly.
4. Link to a runnable quickstart or install path.
5. Offer adjacent pillars only when they help the same task.

Avoid leading with an undifferentiated list of thousands of capabilities. Breadth supports the decision; it is not the decision.

## 3. Canonical surfaces and ownership

| Surface | Canonical URL | Owning repository | Role in the funnel | Primary CTA |
|---|---|---|---|---|
| Website | https://www.sandbase.ai/ | `sandbase-monorepo` (private) | Category positioning, product discovery, conversion | Explore Store / create API key |
| Docs | https://www.sandbase.ai/docs/ | `sandbase-docs` | Evaluation-to-first-call conversion | Complete quickstart / make first call |
| Store | https://www.sandbase.ai/docs/store/ | `sandbase-docs` and product catalog | Capability discovery | Select a current model or API |
| Blog | https://blog.sandbase.ai/ | `sandbase-blog` (private) | SEO/GEO acquisition and technical education | Continue to Docs, Store, GitHub, or a related guide |
| GitHub organization | https://github.com/sandbaseai | `.github` | Developer trust, open-source discovery, referral network | Open the relevant repository / star / install |
| Skills | https://github.com/sandbaseai/sandbase-skills | `sandbase-skills` | Workflow-led acquisition | Preview or install a Skill |
| CLI/MCP | https://github.com/sandbaseai/cli | `cli` | Local client onboarding | Connect a supported client |
| Harness | https://github.com/sandbaseai/sandbase-harness | `sandbase-harness` | Runtime adoption | Install and run locally |
| Daily operations | https://github.com/sandbaseai/sandbase-daily-ops | `sandbase-daily-ops` | Context, experiments, evidence, and audit | Read plan / inspect results |

`docs.sandbase.ai` did not resolve during the 2026-08-23 audit. New promotion must use `https://www.sandbase.ai/docs/` until DNS and redirects are deliberately repaired. The `sandbase-docs` README still contains stale `docs.sandbase.ai` links and must be corrected in its owning repository.

### Repository authority boundary

- `sandbase-monorepo` is the protected main product repository. Promotion operations may inspect it, prepare a feature branch, and open a PR, but must **never push directly to its main branch or trigger its production deployment**. A human/operator owns merge and deployment approval there.
- The separate Blog, Docs, GitHub tool repositories, and `sandbase-daily-ops` may continue through their normal feature-branch, PR, merge, and deployment workflows under the current operator authorization.
- A terminal instruction such as “continue,” “finish,” or “daily audit” does not widen this boundary.

## 4. Public GitHub portfolio

### Core products

- `sandbase-harness` — local-first Agent runtime; strongest current GitHub discovery surface (630 stars at audit time).
- `sandbase-skills` — 88 installable Agent Skills and portable workflow distribution (49 stars).
- `cli` — local CLI/MCP bridge for 25 AI client targets and SandBase capabilities (41 stars).
- `sandbase-docs` — public documentation source and API positioning (1 star).
- `.github` — organization landing page and cross-product navigation.
- `sandbase-daily-ops` — public promotion and SEO operating ledger.

### Ecosystem and authority assets

- `deepseek-harness-handbook`, `dsh-plugin-store`, `dsh-kit`, `dsh101` — DeepSeek Harness education, plugins, and community discovery.
- `awesome-agent-runtime`, `awesome-native-agent-platforms`, `agent-sandbox-cookbook` — category authority and infrastructure discovery.
- `sandbase-agents` — reusable Agent Service registry and delivery standard.
- `global-ai-cold-start` — public growth case study.
- `sandbase-lab-sitecheck` — product-led demonstration of Agent website understanding.
- `homebrew-tap` — CLI installation and migration surface.

Public repositories must maintain a useful first-screen description, relevant homepage, focused topics, current install command, license, release status, and contextual links to—not generic repetition of—the appropriate API, Docs, Blog, Skills, CLI, or Harness path.

## 5. Audience and intent map

| Audience | Search / discovery task | Best entry surface | Conversion path |
|---|---|---|---|
| AI app developer | Find an OpenAI-compatible, LLM, image, video, or unified API | Blog comparison or capability page | Article → Docs/Store → key → first call |
| Agent builder | Add search, social, data, media, or model capabilities | Skills/GitHub/Blog tutorial | Skill preview → CLI/MCP or API → successful workflow |
| Platform engineer | Route models or operate durable, governed Agents | GitHub comparison/runtime content | Harness/CLI README → install → local proof |
| FDE / solution engineer | Assemble a repeatable customer workflow | Blog use case + Skills | Use case → Skill → API execution → reusable delivery package |
| Chinese developer | Evaluate APIs and Agent tools in native Chinese | Chinese Blog counterpart / bilingual README | Native content → localized install/Docs path |

## 6. SEO and content clusters

### Commercial API intent

- Primary: `OpenAI API alternatives`, `OpenRouter alternatives`, `unified AI API`, `OpenAI compatible API`, `LLM API`, `image generation API`, `video generation API`.
- Supporting: multimodal AI API, model gateway, self-hosted LLM proxy, API pricing, provider routing, image-to-video API.
- Required content shape: answer-first opening, explicit alternatives, operating model, trade-offs, migration checks, current primary sources, and a next step.

### Workflow and tool intent

- Agent Skills, MCP server, AI search API, social data API, web research Agent, marketing automation API, data APIs for Agents.
- Required bridge: describe the workflow separately from the provider or execution layer.

### X/Twitter API opportunity

The public SandBase catalog currently exposes a Twitter vendor surface at [`/vendor/twitter`](https://www.sandbase.ai/vendor/twitter), verified 2026-08-25. Observed routes include search timeline, trending, tweet detail, user profile, user media, replies, followers, followings, comments, retweet-user list, and a `user-post-tweet` route. Treat read routes as data/API content opportunities. Treat posting as a side-effecting capability that requires explicit operator authorization and must never be implied by a Blog tutorial.

### Runtime and infrastructure intent

- Agent runtime, Agent sandbox, tool governance, audit/replay, persistent Agent sessions, model gateway, coding Agent infrastructure.
- Required bridge: Harness for governed execution; CLI for lightweight connection; API for hosted capabilities.

### Localization

Every substantial Blog publication defaults to English plus native `zh-CN` under the same slug. Chinese is not a literal translation. GitHub core READMEs should maintain at least English and Chinese where the repository already supports localization.

## 7. Channel roles

| Channel | What it should do | What it should not do |
|---|---|---|
| Website | Explain category and route high-intent visitors | Become a feed of shallow keyword pages |
| Docs | Produce a successful first call and accurate reference | Carry speculative marketing claims |
| Blog | Own search questions, comparisons, tutorials, and releases | Publish English-only or evidence-free articles |
| GitHub | Demonstrate working open source and create trusted referrals | Copy identical promotional blocks into every README |
| DEV / Medium / Zhihu | Adapt approved canonical articles for relevant communities | Duplicate canonicals without review or credentials |
| Social / communities | Distribute useful evidence and invite discussion | Spam Reddit, HN, Discord, or unrelated communities |

## 8. Blog publication contract

All Blog work begins with `sandbase-blog/skills/blog/SKILL.md` and follows its current references. Unless the Skill explicitly permits an exception, publication requires:

- English and native Chinese counterparts with the same slug;
- correct author persona (`Sophie Lin` for API comparisons);
- dedicated durable cover on `static.sandbase.ai`;
- normally three useful, inspected evidence screenshots with dated captions;
- content-index entry;
- primary-source fact ledger and three review passes;
- `npm test`, `npm run check`, and `npm run build`;
- feature branch, PR, successful deployment, and live EN/ZH verification.

DataForSEO is billable and is called only through SandBase API after operator approval. Record query, reader, intent, market, language, retrieval date, keyword metrics, and sampled SERP. It is decision evidence, never a ranking guarantee.

## 9. Conversion and internal-link architecture

```text
Search / GitHub / community discovery
  → task-specific Blog article or repository
  → current Docs / Store / install guide
  → API key, Skill install, CLI connection, or Harness run
  → successful first workflow
  → repeat use, star, backlink, case study, or referral
```

Every acquisition page should have one primary next step. Cross-links must be contextual: API articles link to the relevant schema/quickstart; Skill pages link to execution only when the workflow needs SandBase; Harness pages link to hosted APIs only as an alternative capability source.

## 10. Measurement model

### Daily leading indicators

- GSC non-brand clicks, impressions, CTR, and position-5–20 opportunities.
- High-impression/low-CTR pages and query-to-page mismatch.
- Sitemap health, indexability, hreflang, canonical, 404/5xx, deployment failures.
- GitHub stars, clones/referrals where available, release/install path health, stale metadata.
- First-call and install path availability; link health across website, Docs, Blog, and GitHub.

### Outcome reviews

- 14 days: early query/page movement, indexing, CTR direction, referrals.
- 28 days: comparable rolling-window non-brand clicks against 119 baseline; cluster and conversion contribution.
- Do not attribute a sitewide change to one experiment without page/query and time-window evidence.

## 11. Current priority queue

1. Correct and monitor the two API-alternatives hubs now published bilingually.
2. Optimize the GSC position-5–20 / low-CTR queue: DeepSeek Harness preview, GLM 5.3 release, and Claude Opus 5.
3. Verify the corrected Docs README deployment and monitor the restored CLI setup route.
4. Build supporting API cluster pages only where search intent is distinct and primary evidence exists.
5. Prepare approved DEV/Medium/Zhihu adaptations; publish only with credentials and operator-reviewed channel fit.
6. Review equivalent GSC windows after 14 and 28 days.

## 11A. Hot-source pool for daily editorial discovery

Use these companies as a bounded discovery pool for daily Blog topic research. Prefer official X accounts, product announcements, release notes, engineering blogs, and named maintainers over reposts. X signals are topic discovery only; every publishable claim still requires primary-source verification.

1. Anthropic / Claude
2. OpenAI
3. Google DeepMind
4. Google Cloud
5. Vercel
6. Cloudflare
7. OpenRouter
8. Hugging Face
9. Zhipu AI / 智谱
10. MiniMax
11. Moonshot AI / Kimi
12. DeepSeek
13. Meta AI
14. xAI
15. Mistral AI
16. Cohere
17. Together AI
18. Replicate
19. Groq
20. E2B

Daily selection rule: first check the current GSC opportunity queue and existing content index, then use this pool to find a distinct reader task. Do not convert a viral post into a Blog article without a source ledger, product-boundary check, and operator confirmation of the proposed title.

## 12. Context update rules

Update this file when any of the following changes: canonical domain, product name, primary value proposition, API base URL, documented capability count, supported client count, Skill count, owning repository, audience, conversion path, baseline, or success metric.

Every update must include the date, evidence URL or repository commit, owner, and any downstream surfaces requiring synchronization. Conflicts are resolved in favor of current production Docs and verified runtime behavior, followed by repository code and approved product decisions; old Blog copy or cached search snippets are not authoritative.

### 2026-08-24 metadata verification

- Evidence: GitHub repository metadata API for [`sandbase-harness`](https://api.github.com/repos/sandbaseai/sandbase-harness), [`sandbase-skills`](https://api.github.com/repos/sandbaseai/sandbase-skills), and [`cli`](https://api.github.com/repos/sandbaseai/cli); Docs health endpoint [`/docs/health`](https://www.sandbase.ai/docs/health) returned HTTP 200.
- Owner: SandBase growth operations.
- Change: refreshed observed star counts only; product positioning, client counts, Skill count, and canonical URLs unchanged.
- Downstream: daily audit and growth ledger updated in the same execution batch.
