# Quality Gates

Run this review before a package is ready for publishing.

## Facts and Claims

- [ ] Every metric, date, product status, integration, named customer, and compatibility claim appears in `source_facts` with a source URL or is removed.
- [ ] Every first-person assertion appears in `author.approved_first_person_facts` or is rewritten.
- [ ] The copy does not imply GA, enterprise support, or product availability beyond the given status.
- [ ] The copy does not say a third-party capability is deployed, hosted, or owned by SandBase unless that fact is explicitly approved.
- [ ] The SandBase role is clear: it connects an agent to an ecosystem of external real-world capabilities.

## Author and Language

- [ ] The article opens with a tension or decision, not generic market context.
- [ ] It includes a judgment, a mechanism, and a real trade-off.
- [ ] Chinese content is a native rewrite, not a translation.
- [ ] Each platform has a distinct lead, title, and CTA.

## Platform and SEO

- [ ] SandBase Blog is the canonical source when the subject overlaps.
- [ ] Medium and DEV Community include canonical attribution when supported or a clear original-source link when not.
- [ ] Blog follows frontmatter, internal-link, external-source, table, FAQ, and image-alt requirements.
- [ ] Social posts fit their channel and do not contain a pasted blog opening.
- [ ] Every canonical blog article declares a primary query, reader, and search intent in `review-report.md`.
- [ ] Title, H1, description, slug, canonical URL, and social image describe the same topic and are indexable.
- [ ] Every technical/product claim links to a primary source; relevant SandBase setup, store, docs, or related-post links are included when useful.
- [ ] Compare and Top N articles include a clear decision table or "choose X when" guidance.

## GEO

- [ ] The opening 80-120 words answer what it is, who it is for, and when to use it.
- [ ] English contains a quotable `TL;DR` / `Key takeaway`; Chinese contains `先说结论`, each with 3-5 standalone factual bullets.
- [ ] Provider, API, SandBase Agent Service, and core capabilities use stable, unambiguous names throughout.
- [ ] The article names a meaningful limitation or trade-off, rather than presenting a universal winner.
- [ ] Important claims have a named primary source and date where the fact can change.
- [ ] Article JSON-LD validates; FAQPage JSON-LD is used only for genuine FAQ content.
- [ ] Xiaohongshu uses a 4-8 page article-screenshot storyboard from the Chinese Compare or Top N article, not an overseas product-launch poster.
- [ ] The Xiaohongshu cover is a specific hook rather than only an API or provider name; the body has no long external link.
- [ ] Xiaohongshu output includes caption, 3-6 relevant tags, and a first comment that invites a concrete reply.

## Package

- [ ] `input.json` contains author, locales, channels, source facts, and claim constraints.
- [ ] `manifest.json` records files, canonical URL, image URL, localization state, and publication state.
- [ ] The cover URL is reused consistently where a shared image is intended.
- [ ] The image model created only the abstract background. All visible words were rendered by the deterministic cover renderer.
- [ ] The final image follows the safe area, contrast, format, and typography rules in `visual-system.md`.
- [ ] `review-report.md` exists and says `Status: APPROVED`; any `REVISE` finding blocks publishing.
- [ ] The reviewer visually inspected every final cover raster, not only its prompt or URL.
- [ ] Every publishable cover has a deterministic, readable title that matches the article headline or an approved short form.
- [ ] Final image URLs use `media.sandbase.ai/uploads/`, `media.sandbase.ai/files/`, or a versioned first-party blog asset path. Model-provider URLs, signed URLs, browser blobs, and temporary URLs are rejected.
