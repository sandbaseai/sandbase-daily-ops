# Publication Matrix

Use the selected channel as the constraint. A canonical article is source material, not a script to be copied everywhere.

| Channel | Job | Native opening | Shape | Canonical policy | CTA |
|---|---|---|---|---|---|
| SandBase Blog | Durable source of truth | A technical tension or decision | 1,200-2,000 words; evidence, table, FAQ | Self-canonical | Docs, product, GitHub |
| LinkedIn | Founder/company distribution | What changed and why it matters now | 120-250 words; short paragraphs | Link to SandBase Blog | Discuss, try, read |
| X | Fast technical signal | One sharp claim or observation | 220 characters where possible; thread only when earned | Link or quoted follow-up | Reply with experience |
| Discord | Builder update | What shipped and how to use it | 80-160 words; bullets accepted | Link to docs/blog | Give feedback |
| Medium | Global founder argument | A counterintuitive observation from the field | 900-1,500 words; narrative plus decisions | Add canonical URL to SandBase for overlapping content | Read source / follow |
| DEV Community | Practical builder discovery | The implementation problem | 800-1,400 words; runnable setup, code, caveats | Add canonical URL to SandBase for overlapping content | Try the repo/docs |
| Zhihu | Chinese search and credibility | Answer a natural user question immediately | 1,500-3,000 Chinese characters; conclusion first, explain with cases | Link to the original SandBase article naturally; no forced duplicate | Ask a technical question |
| Xiaohongshu | Chinese discovery and audience building | A concrete payoff, misconception, or decision | Strong hook cover plus 4-8 screenshots from a Chinese Compare or Top N article; 300-800 Chinese characters | No long external link in body | Comment with a keyword |
| WeChat Channels | Short-video reach | Spoken tension in first 3 seconds | 45-120 seconds; one claim per video | Mention article/project naturally | Comment or follow |

## Platform Decisions

- Do not publish the same title to Blog, Medium, DEV Community, and Zhihu.
- Do not make Medium or DEV Community a thin SEO clone. Choose one distinct angle: field note, decision framework, tutorial, benchmark interpretation, or postmortem.
- For external long-form reposts that substantially overlap the SandBase Blog, include the canonical URL in frontmatter when supported. If a platform does not support canonical metadata, state the original source near the top and use a different lead, examples, and conclusion.
- Keep company voice on SandBase Blog and LinkedIn. Use a technical founder voice on Medium, DEV Community, and Zhihu only when approved author facts support it.
- Xiaohongshu is not a reduced LinkedIn post. The carousel itself should provide the evidence: a readable article headline, source excerpts, decision framework, or comparison table. The caption only completes the argument.

## Output Naming

```text
blog/en/<canonical-slug>.md
blog/zh-CN/<canonical-slug>.md
medium/en/<argument-slug>.md
devto/en/<tutorial-or-practical-slug>.md
zhihu/zh-CN/<question-led-slug>.md
xiaohongshu/zh-CN/<article-screenshot-carousel-slug>.md
social/linkedin.md
social/x.md
social/discord.md
```
