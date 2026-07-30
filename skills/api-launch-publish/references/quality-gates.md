# Quality Gates

Run this review before a package is ready for publishing.

## Facts and Claims

- [ ] Every metric, date, product status, integration, named customer, and compatibility claim appears in `source_facts` with a source URL or is removed.
- [ ] Every first-person assertion appears in `author.approved_first_person_facts` or is rewritten.
- [ ] The copy does not imply GA, enterprise support, or product availability beyond the given status.

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

## Package

- [ ] `input.json` contains author, locales, channels, source facts, and claim constraints.
- [ ] `manifest.json` records files, canonical URL, image URL, localization state, and publication state.
- [ ] The cover URL is reused consistently where a shared image is intended.
