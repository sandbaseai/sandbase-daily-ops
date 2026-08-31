# Open-source growth ledger

## 2026-08-31 — E2B Awesome AI SDKs review path

- **Action:** Queued the existing canonical [E2B Awesome AI SDKs PR #344](https://github.com/e2b-dev/awesome-ai-sdks/pull/344) in the X, LinkedIn, and Discord drafts.
- **Evidence:** The directory explicitly covers SDKs, frameworks, libraries, and tools for creating, monitoring, debugging, and deploying AI agents; the PR adds the distinct Harness runtime and is mergeable.
- **Scope:** Maintainer review and CLA verification remain pending. This is a source-linked review request, not an endorsement or security certification; drafts remain `NEEDS REVIEW`.

## 2026-08-31 — Awesome AI Agents 2026 runtime review

- **Action:** Queued [Awesome AI Agents 2026 PR #240](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026/pull/240) in the X, LinkedIn, and Discord drafts.
- **Evidence:** The destination requires a tier, primary language, and most-specific type tag, and explicitly supports agent tooling/infrastructure entries. The PR follows that format and distinguishes the current Harness runtime from the existing SandBase CLI entry.
- **Scope:** Discovery submission only. Review is pending; no endorsement or security certification is claimed, and all channel drafts remain `NEEDS REVIEW`.

## 2026-08-31 — E2B Awesome AI Agents scope review

- **Action:** Queued [E2B Awesome AI Agents Issue #1468](https://github.com/e2b-dev/awesome-ai-agents/issues/1468) in the X, LinkedIn, and Discord drafts.
- **Evidence:** The destination is a high-traffic AI-agent directory that explicitly accepts pull requests or form submissions. The issue distinguishes the current Harness runtime from the previously closed CLI submission and asks the maintainer to make the scope decision.
- **Scope:** Review request only. No inclusion, directory endorsement, security certification, or social-account publication is claimed; drafts remain `NEEDS REVIEW`.

## 2026-08-31 — Awesome AI Agents review path

- **Action:** Queued [NipunaRanasinghe Awesome AI Agents PR #184](https://github.com/NipunaRanasinghe/awesome-ai-agents/pull/184) in the X, LinkedIn, and Discord drafts.
- **Evidence:** The directory is actively maintained, uses CI, asks for maintained AI-agent resources, and specifies a dynamic GitHub stars badge plus concise table description. The PR follows that format and includes current official project facts.
- **Scope:** Discovery submission only. Review is pending; no directory endorsement or security certification is claimed, and isolation remains backend/deployment dependent. All social drafts remain `NEEDS REVIEW`.

## 2026-08-31 — Zients Awesome Agent Harness review path

- **Action:** Queued [Zients Awesome Agent Harness PR #10](https://github.com/zients/awesome-agent-harness/pull/10) in the X, LinkedIn, and Discord drafts.
- **Evidence:** The destination explicitly accepts complete agent systems and harnesses, asks for installation/usage and external-dependency details, and the entry supplies those facts. The PR is source-linked and pending maintainer review.
- **Scope:** Discovery submission only; no directory endorsement or security certification is claimed, and isolation remains backend/deployment dependent. All social drafts remain `NEEDS REVIEW`.

## 2026-08-31 — Awesome Agent Harnesses review path

- **Action:** Queued the existing canonical [Bayshier Awesome Agent Harnesses PR #2](https://github.com/bayshier/awesome-agent-harnesses/pull/2) in the X, LinkedIn, and Discord drafts.
- **Evidence:** The destination is an active MIT-licensed curated list with contribution rules requiring current star counts and factual one-line positioning. PR #2 is open and mergeable; duplicate PR #3 was closed to avoid duplicate maintainer work.
- **Scope:** Discovery submission only. Review is pending; the entry is not an endorsement or security certification, and isolation remains deployment/backend dependent.

This is the canonical, append-only record for useful maintenance and compliant
developer promotion across the SandBase public repositories in scope:

- [`sandbase-skills`](https://github.com/sandbaseai/sandbase-skills)
- [`cli`](https://github.com/sandbaseai/cli)
- [`deepseek-harness-handbook`](https://github.com/sandbaseai/deepseek-harness-handbook)
- [`sandbase-docs`](https://github.com/sandbaseai/sandbase-docs)

Star counts are direct GitHub snapshots, not estimates. A star increase is not
attributed to an action unless a supporting referral or engagement signal is
available. Product implementation remains in each owning repository; this file
records the operational decision, evidence, validation, and outcome.

## Baseline — 2026-08-23 UTC

| Repository | Stars | Forks | Watchers | Default branch | URL |
|---|---:|---:|---:|---|---|
| `sandbase-skills` | 45 | 3 | 0 | `main` | https://github.com/sandbaseai/sandbase-skills |
| `cli` | 33 | 1 | 1 | `main` | https://github.com/sandbaseai/cli |
| `deepseek-harness-handbook` | 40 | 7 | 2 | `main` | https://github.com/sandbaseai/deepseek-harness-handbook |
| `sandbase-docs` | 1 | 0 | 0 | `main` | https://github.com/sandbaseai/sandbase-docs |

**Verification:** `gh repo view sandbaseai/<repo> --json stargazerCount,forkCount,watchers,defaultBranchRef,updatedAt,url` run on 2026-08-23 UTC. GitHub is authoritative for the counts.

## Health baseline

| Repository | Validation result | Evidence / blocker |
|---|---|---|
| `sandbase-skills` | PASS | `npm run validate`, `npm test`, `npm run agent-plugin:check`, and `npm run marketplace:check`; 25 skills validated, 6 Node tests and 29 Python tests passed, 88-skill marketplace validated |
| `cli` | BLOCKED locally | `npm run lint` could not start because dependencies are not installed (`tsc: command not found`); install dependencies before claiming a local build result |
| `deepseek-harness-handbook` | PASS | `npm run check`; 115 canonical pages and 122 localized documents verified |
| `sandbase-docs` | BLOCKED locally | generator test expects sibling `sandbase-registry/data/llm`, which is not present in this checkout; run with the documented workspace dependency before claiming a full build |

## Experiment / action log

### 2026-08-23 — establish four-repository baseline

- **Objective:** Create one auditable growth loop for the four open-source projects and avoid scattering promotion records across product repositories.
- **Evidence:** Direct GitHub counts above; repository READMEs, contribution rules, and validation scripts inspected. `sandbase-daily-ops` README and `playbooks/operations-ledger.md` define this repository as the canonical operations ledger.
- **Action:** Added this ledger to `sandbase-daily-ops`; closed superseded handbook-only ledger PR [#158](https://github.com/sandbaseai/deepseek-harness-handbook/pull/158) after moving the record here.
- **Implementation:** `sandbaseai/sandbase-daily-ops/growth-ledger.md`.
- **Validation:** Baseline commands and project-specific checks recorded above; no product repository was modified by this action.
- **Deployment state:** Local branch; PR pending.
- **Baseline:** 119 non-brand Google clicks is the separate site SEO baseline in [`promotion-plan/master-context.md`](promotion-plan/master-context.md); GitHub baseline is the table above.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** pending.
- **Next action:** Identify one high-intent developer problem per repository, ship a source-backed improvement through a focused PR, then distribute the specific artifact in a directly relevant channel.

### 2026-08-23 — handbook discussion answer

- **Objective:** Help developers reporting DeepSeek Harness failures choose the
  next diagnostic step from a recognizable symptom.
- **Evidence:** The handbook's Failure Router is live and separates provider,
  tool, approval, sandbox, session, and client boundaries; the related Ideas
  discussion asks for the next failure to verify.
- **Action:** Posted a concise, source-linked answer in discussion [#99](https://github.com/sandbaseai/deepseek-harness-handbook/discussions/99#discussioncomment-18121882), inviting exact symptoms and verified revisions for gaps the router cannot classify.
- **Implementation:** Existing guide; no product-code change.
- **Validation:** Live guide URL and discussion URL resolve; no star request or
  unrelated cross-posting.
- **Deployment state:** Published discussion reply.
- **Baseline:** Handbook 40 stars at the start-of-day GitHub snapshot; no
  post-action star change is attributed yet.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** pending.
- **Next action:** Record any maintainer/developer response and re-query the
  handbook star count before considering another distribution action.

### 2026-08-23 — CLI/Cline compatibility triage

- **Objective:** Answer an open request about installing SandBase CLI in Cline
  without implying unsupported client compatibility.
- **Evidence:** The CLI v0.1.17 source catalog contains 25 explicit client IDs
  and does not contain `cline`; its bridge validates the client identity before
  reading credentials. Cline's official configuration docs identify
  `~/.cline/data/settings/cline_mcp_settings.json` and project `.cline/mcp.json`
  as MCP configuration locations.
- **Action:** Posted the evidence-backed boundary and official Cline references
  in [CLI issue #23](https://github.com/sandbaseai/cli/issues/23#issuecomment-5384753015).
  The reply explicitly rejects reusing another client identity or credential as
  a workaround.
- **Implementation:** No CLI code change; feature remains unclaimed until a
  real adapter can be tested end to end.
- **Validation:** Source catalog and bridge behavior inspected locally; official
  Cline documentation links resolve; no credential or secret was posted.
- **Deployment state:** Published issue response.
- **Baseline:** CLI 33 stars at the latest direct GitHub snapshot; no post-action
  change is attributed.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** pending.
- **Next action:** If maintainers want support, define a scoped Cline adapter
  acceptance test covering stdio config, credential ownership, doctor, and
  unregister before changing the 25-client contract.

### 2026-08-23 — CLI test isolation repair

- **Objective:** Restore a reproducible green main-branch validation for the
  CLI package.
- **Evidence:** The full suite initially failed because host-level
  `/Users/.../.kiro/settings/mcp.json` and workspace `PWD` leaked into packaged
  Kiro maintenance tests. This was an environment-contamination failure, not a
  user-facing compatibility result.
- **Action:** Isolated the tests with temporary `HOME`, `KIRO_HOME`, and `PWD`,
  and aligned one stale test with the current read-only Kiro Skill contract.
- **Implementation:** [CLI PR #27](https://github.com/sandbaseai/cli/pull/27),
  merged to `main`.
- **Validation:** `npm run lint`; `npm test` — 150 tests, 149 passed, 1
  skipped, 0 failed; `npm run audit:package` passed. The merge commit is
  [`4b02eb6`](https://github.com/sandbaseai/cli/commit/4b02eb64b7290744ab1a478e7ff17964b314ba04).
- **Deployment state:** Merged; package source is healthy. No release was
  cut because this is a test-only repair.
- **Baseline:** CLI 33 stars before and after the action; no growth is claimed
  from a maintenance fix.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** win for reproducibility; star outcome pending.
- **Next action:** Use the green CLI validation as evidence in the next
  client-specific distribution draft, beginning with supported catalog targets.

### 2026-08-23 — Docs generator prerequisite clarification

- **Objective:** Make a fresh `sandbase-docs` checkout's generated-reference
  workflow discoverable and prevent contributors from mistaking a missing
  registry checkout for a broken VitePress site.
- **Evidence:** `npm run test:generator` fails without sibling
  `../sandbase-registry/data/llm`; the generator source resolves that path
  explicitly. A normal VitePress build uses committed generated pages and does
  not require the sibling checkout.
- **Action:** Documented the prerequisite and the distinction in the Docs
  README.
- **Implementation:** [Docs PR #4](https://github.com/sandbaseai/sandbase-docs/pull/4),
  merged to `main` at [`c9ebeea`](https://github.com/sandbaseai/sandbase-docs/commit/c9ebeeadebb8ee0ad5182319b9d85be5398041ea).
- **Validation:** `npm ci` and `npm run build` passed; VitePress completed in
  49.74 seconds. Generator tests remain explicitly unverified because the
  required registry checkout is unavailable in this workspace.
- **Deployment state:** README change merged; no production deployment was
  triggered.
- **Baseline:** Docs 1 star before and after; no growth is attributed to this
  contributor-experience fix.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** win for onboarding clarity; star outcome pending.
- **Next action:** Re-run the generator in the authorized workspace that has
  the matching registry checkout, then record the result and any live Docs
  deployment state.

### 2026-08-23 — Skills bounded-research discussion answer

- **Objective:** Help Agent builders stop research loops without hiding
  uncertainty or overstating source confidence.
- **Evidence:** The Skills repository ships the `multi-source-search` workflow
  and an offline validator that checks duplicate identities, unused evidence,
  inflated confidence, and unresolved high-confidence conflicts.
- **Action:** Posted a practical, source-linked answer in [Skills discussion
  #31](https://github.com/sandbaseai/sandbase-skills/discussions/31#discussioncomment-18121945),
  explicitly stating that the validator checks internal consistency rather than
  truth of a source.
- **Implementation:** Existing open-source Skill and validator; no code change.
- **Validation:** Live Skill path and discussion URL resolve; no star request or
  unsupported provider claim was made.
- **Deployment state:** Published discussion reply.
- **Baseline:** Skills 45 stars before and after the action; no growth is
  attributed without a supporting referral signal.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** pending.
- **Next action:** Record replies or concrete adoption evidence, then test one
  additional host-agent installation path before preparing another distribution
  action.

### 2026-08-23 — GitHub traffic leading-indicator snapshot

- **Objective:** Add a measurable leading indicator for developer discovery
  while keeping Stars as the only authoritative Star metric.
- **Evidence:** GitHub's repository traffic API (14-day window ending with the
  latest available day) returned the following direct snapshots:

  | Repository | Views | Unique viewers | Clones | Unique cloners |
  |---|---:|---:|---:|---:|
  | `sandbase-skills` | 388 | 101 | 1,387 | 433 |
  | `cli` | 164 | 64 | 364 | 136 |
  | `deepseek-harness-handbook` | 931 | 306 | 1,453 | 319 |
  | `sandbase-docs` | 57 | 9 | 78 | 54 |

- **Action:** Recorded this snapshot for channel comparison and future
  before/after checks. Traffic is not interpreted as Stars, adoption, or
  causality.
- **Implementation:** `growth-ledger.md` in `sandbase-daily-ops`.
- **Validation:** Queried `gh api repos/sandbaseai/<repo>/traffic/views` and
  `/traffic/clones` for all four repositories; direct Star counts remain
  separately verified from `gh repo view`.
- **Deployment state:** Ledger entry pending merge.
- **Baseline:** Stars remain Skills 45, CLI 33, Handbook 40, Docs 1.
- **Review dates:** Re-query GitHub traffic and Stars on 2026-09-06 and
  2026-09-20 UTC; compare like-for-like windows.
- **Result:** pending.
- **Next action:** Prioritize one distribution message for the high-view,
  high-clone Handbook and Skills surfaces, and one Docs/CLI onboarding message
  where traffic is lower, recording channel-level evidence separately.

### 2026-08-23 — curated Agent Skills inclusion PR

- **Objective:** Create durable discovery for the Skills repository through a
  relevant, community-maintained directory rather than repetitive social posts.
- **Evidence:** `VoltAgent/awesome-agent-skills` requires a public working Skill,
  documentation, a short description of 10 words or fewer, and community usage;
  its README did not already contain SandBase. The candidate Skill is public,
  documented, has 45 GitHub stars, and the latest GitHub traffic snapshot shows
  1,387 clones in 14 days.
- **Action:** Submitted [VoltAgent/awesome-agent-skills PR
  #946](https://github.com/VoltAgent/awesome-agent-skills/pull/946) adding the
  link-only entry for `sandbaseai/sandbase-skills/multi-source-search` under
  Community Skills → Marketing.
- **Implementation:** Fork branch `liyangbing:add-sandbase-multi-source-search`
  in the target list; no target repository or Skills code was modified directly.
- **Validation:** Target CONTRIBUTING.md inspected; entry uses the required
  format and six-word description; source URL was checked against the public
  repository. A transient GitHub HEAD request timed out, so live URL health is
  not overstated beyond the repository/API evidence.
- **Deployment state:** External PR open; maintainer review pending.
- **Baseline:** Skills 45 stars before submission; no star change attributed to
  a pending PR.
- **Review dates:** Check PR state and direct Stars on 2026-08-30, 2026-09-06,
  and 2026-09-20 UTC.
- **Result:** pending.
- **Next action:** Respond only to maintainer feedback; if merged, record the
  merge and compare the next 14-day GitHub traffic window without claiming
  causal Star growth.

### 2026-08-23 — CLI npm/MCP Registry trusted-publishing triage

- **Objective:** Remove ambiguity around the CLI's public npm lag and give the
  maintainer a safe, actionable release diagnosis.
- **Evidence:** The repository workflows already request GitHub OIDC
  (`id-token: write`), install npm 11.15+, publish without `NODE_AUTH_TOKEN`,
  and use OIDC for the MCP Registry. Public npm currently reports
  `@sandbaseai/cli` latest `0.1.14`, while the immutable GitHub release is
  `v0.1.17`.
- **Action:** Posted the repository-side evidence and exact npm package/admin
  configuration boundary in [CLI issue
  #24](https://github.com/sandbaseai/cli/issues/24#issuecomment-5384829547).
  The response explicitly says not to add a token to the repository.
- **Implementation:** No code or workflow change; this requires package/org
  administrator access and should be verified by a maintainer before rerunning
  a release tag.
- **Validation:** Inspected the release and MCP Registry workflows and queried
  npm dist-tags directly; no secret or private configuration was exposed.
- **Deployment state:** Published issue response; npm state unchanged.
- **Baseline:** CLI 33 stars before and after; no growth attributed to a release
  diagnosis.
- **Review dates:** 2026-08-30 and 2026-09-06 UTC.
- **Result:** pending maintainer action.
- **Next action:** Re-query npm dist-tags and the v0.1.17 Registry listing after
  the package trusted publisher is configured; then record whether the public
  install path is synchronized.

### 2026-08-23 — Handbook Star snapshot update

- **Objective:** Keep the authoritative Star baseline current after the latest
  GitHub verification.
- **Evidence:** `gh repo view sandbaseai/deepseek-harness-handbook --json
  stargazerCount` returned **41** at 2026-08-23 UTC, up from the previously
  recorded 40. Skills remained 45, CLI 33, and Docs 1.
- **Action:** Recorded the new count as an observed change without assigning it
  to the discussion reply, curated-list work, or any other single channel.
- **Implementation:** This ledger only; no product repository change.
- **Validation:** Direct GitHub repository metadata query; no estimated or
  third-party count used.
- **Deployment state:** Ledger entry pending merge.
- **Baseline:** Four-repository Stars now 45 / 33 / 41 / 1 in the order defined
  at the top of this file.
- **Review dates:** Re-query all four repositories and traffic windows on
  2026-08-30, 2026-09-06, and 2026-09-20 UTC.
- **Result:** +1 observed for Handbook; attribution pending.
- **Next action:** Look for a supporting referral or discussion signal before
  claiming an effective distribution pattern.

### 2026-08-23 — Skills pull-request validation workflow

- **Objective:** Make contributions and directory reviews more trustworthy by
  running the repository's existing validation contract on every pull request.
- **Evidence:** Skills had local validators and tests but no tracked GitHub
  Actions workflow. The first CI run exposed two real repository facts: no
  package lockfile exists, and setup-node's npm cache requires one.
- **Action:** Added a read-only workflow, corrected it to use `npm install`
  without a lockfile or cache, and merged [Skills PR
  #58](https://github.com/sandbaseai/sandbase-skills/pull/58).
- **Implementation:** `.github/workflows/validate.yml`; merge commit
  [`3140141`](https://github.com/sandbaseai/sandbase-skills/commit/31401410162507f979f45dbceed1ed97e5964a82).
- **Validation:** GitHub Actions run [32625741620](https://github.com/sandbaseai/sandbase-skills/actions/runs/32625741620)
  passed catalog validation, 6 Node tests, 29 Python tests, Agent Plugin
  validation, 88-skill marketplace validation, and package audit.
- **Deployment state:** Merged to `main`; no credentials, model calls, or
  production deployment involved.
- **Baseline:** Skills 45 stars before and after; no Star growth attributed to
  a CI maintenance change.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** win for contributor confidence; Star outcome pending.
- **Next action:** Reference the green validation in the pending curated-list
  PR #946 only if maintainers request additional evidence; do not cross-post
  the same announcement to unrelated communities.

### 2026-08-23 — Skills README validation badge

- **Objective:** Make the new contributor-validation signal visible at the
  Skills repository's first screen.
- **Evidence:** Skills PR #58 added and passed the `Validate Skills` workflow on
  the main branch.
- **Action:** Added the workflow badge to the README badge row through [Skills
  PR #59](https://github.com/sandbaseai/sandbase-skills/pull/59), merged at
  [`e8a0c66`](https://github.com/sandbaseai/sandbase-skills/commit/e8a0c66c560d9fefc0b03f0310486105aa993a24).
- **Implementation:** README-only discoverability change; no runtime or claim
  changes.
- **Validation:** Pull-request workflow passed before merge; badge points to
  the tracked `validate.yml` workflow and `main` branch.
- **Deployment state:** Merged to `main`.
- **Baseline:** Skills 45 stars before and after; no Star growth attributed to
  a badge.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** win for visible project health; Star outcome pending.
- **Next action:** Let the curated-list PR #946 reviewer see the visible green
  validation signal; do not send a separate unsolicited message.

### 2026-08-23 — Docs contributor workflow

- **Objective:** Reduce the cost of a first documentation contribution by
  making local preview and production-equivalent validation explicit.
- **Evidence:** `sandbase-docs` had a successful VitePress build, but its
  README did not explain how contributors could preview or validate a change.
- **Action:** Added a `Build and contribute locally` section in [Docs PR
  #5](https://github.com/sandbaseai/sandbase-docs/pull/5), documenting
  `npm ci`, `npm run dev`, `npm run build`, the generated output directory,
  and the issue-reporting path. The PR merged at
  [`e131858`](https://github.com/sandbaseai/sandbase-docs/commit/e13185842b694928ba38d2e7ad0f6df0db9e7c1a).
- **Validation:** The repository's VitePress build had passed before this
  README-only change; the attempted follow-up build was interrupted by a
  stale generated output directory and is not counted as new evidence.
- **Deployment state:** Merged to `main`; documentation-only, with no runtime,
  credential, or production deployment changes.
- **Baseline:** Docs 1 star before and after; no Star growth attributed to this
  contributor-onboarding change.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** contributor onboarding improved; Star outcome pending.
- **Next action:** Watch issue and traffic signals for evidence that the
  documented workflow improves external contributions; do not claim causal
  Star growth without a direct referral signal.

### 2026-08-23 — CLI release checksum

- **Objective:** Improve supply-chain transparency for the immutable CLI
  archive used by automated and manual installers.
- **Evidence:** The CLI README and `llms-install.md` pinned the GitHub release
  tarball, but did not publish an expected digest for an operator to verify.
- **Action:** Published the SHA-256 digest and a copy-then-verify command in
  [CLI PR #28](https://github.com/sandbaseai/cli/pull/28), merged at
  [`5c3ef06`](https://github.com/sandbaseai/cli/commit/5c3ef0615667a61aac9750330808453677406a2d).
- **Validation:** Downloaded the public v0.1.17 archive and computed
  `1ad535b2899ca460b57b3c268aef278fee28fd28e649a89b92951514fd71fffa`;
  `npm run audit:package` passed. The full test run reached the test suite but
  exceeded the short command window, so it is not claimed as new evidence.
- **Deployment state:** Merged to `main`; documentation-only, no runtime or
  credential changes.
- **Baseline:** CLI 33 stars before and after; no Star growth attributed to a
  checksum documentation change.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** stronger reproducibility and installer trust; Star outcome
  pending.
- **Next action:** Monitor installation questions and referral traffic; keep
  the npm/GitHub release discrepancy explicit until trusted publishing is
  configured by a package administrator.

### 2026-08-23 — Docs open-source stack navigation

- **Objective:** Give developers arriving at the documentation a clear path to
  the companion OSS layer that matches their task.
- **Evidence:** The Docs README linked the CLI but did not present canonical
  entry points for the Skills repository or the DeepSeek Harness Handbook.
- **Action:** Added an `Open-source companion projects` section with direct
  links and concise layer descriptions in [Docs PR #6](https://github.com/sandbaseai/sandbase-docs/pull/6),
  merged at [`34d9555`](https://github.com/sandbaseai/sandbase-docs/commit/34d955500dd3dea959ed936d766be56e21c13894).
- **Validation:** README-only change; links resolve to the three named public
  repositories and their canonical issue/contribution surfaces. The prior
  VitePress production build remains the available build evidence.
- **Distribution channel:** Cross-project navigation from the public Docs
  landing page; no unsolicited external posting.
- **Deployment state:** Merged to `main`; no runtime, credential, or product
  behavior changes.
- **Baseline:** Docs 1 star before and after; no Star growth attributed to
  internal cross-linking.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** improved project discovery path; Star outcome pending.
- **Next action:** Compare Docs referral traffic and outbound clicks after the
  next traffic window before deciding whether another distribution channel is
  warranted.

### 2026-08-23 — Docs pull-request build validation

- **Objective:** Keep the documentation `main` branch buildable and make
  broken documentation changes visible before merge.
- **Evidence:** Deployment validation ran only on release tags/manual deploys;
  pull requests had no dedicated VitePress build gate or status badge.
- **Action:** Added `.github/workflows/validate.yml` and a README badge in
  [Docs PR #7](https://github.com/sandbaseai/sandbase-docs/pull/7), merged at
  [`6b851a3`](https://github.com/sandbaseai/sandbase-docs/commit/6b851a31d697ef538cc3ed2eae95f413e51e5993).
- **Validation:** GitHub Actions run
  [32626416490](https://github.com/sandbaseai/sandbase-docs/actions/runs/32626416490)
  passed `npm ci` and `npm run build` on the pull request.
- **Deployment state:** Merged to `main`; read-only CI, no production or
  credential changes.
- **Baseline:** Docs 1 star before and after; no Star growth attributed to CI.
- **Review dates:** 2026-09-06 and 2026-09-20 UTC.
- **Result:** main-health and contributor confidence improved; Star outcome
  pending.
- **Next action:** Use the green workflow as evidence in future contributor
  reviews; do not claim it caused Star growth without referral evidence.

### 2026-08-23 — External Agent Skills directory submission

- **Objective:** Reach research-agent developers through an independently
  maintained directory with an explicit quality and safety review rubric.
- **Evidence:** `Ezeafk/awesome-agent-skills` requires reusable structure,
  installation/usage guidance, platform fit, validation examples, and safety
  notes; it scores entries before inclusion.
- **Action:** Submitted [awesome-agent-skills PR #27](https://github.com/Ezeafk/awesome-agent-skills/pull/27)
  for `sandbaseai/sandbase-skills` in the Research section, using the
  canonical repo URL and a factual description. The submission includes a
  rubric-based 10/10 evaluation with links to the repository's validator,
  examples, CI, and credential guidance.
- **Validation:** The target contribution guide and README were inspected;
  the entry follows the six-column table format and its repository link is
  public. The PR is currently open with no maintainer decision.
- **Distribution channel:** Independent community-curated directory; no paid
  placement, automated engagement, or unsolicited mass outreach.
- **Deployment state:** Pending external review; no product repository change.
- **Baseline:** Skills 45 stars before submission; no Star growth attributed
  to a pending directory PR.
- **Review dates:** Re-check PR state on 2026-08-30 and 2026-09-06 UTC.
- **Result:** qualified distribution experiment pending review.
- **Next action:** Respond only to maintainer questions; if merged, record the
  merge and compare referral traffic before making any causal claim.

### 2026-08-23 — CLI MCP directory submission

- **Objective:** Reach developers actively searching for MCP aggregators and
  client bridges through a high-traffic, community-maintained directory.
- **Evidence:** `punkpeye/awesome-mcp-servers` documents a contribution path
  for new servers, requires canonical links and concise accurate descriptions,
  and explicitly provides an agent PR fast-track marker.
- **Action:** Submitted [PR #12702](https://github.com/punkpeye/awesome-mcp-servers/pull/12702)
  adding `sandbaseai/cli` to Aggregators. The entry describes the local stdio
  bridge and links to the immutable v0.1.17 release install command.
- **Validation:** The target README and contribution guide were inspected;
  the entry uses the existing Markdown format and public canonical URL. PR is
  open and awaiting maintainer review.
- **Distribution channel:** Independent MCP directory; no paid placement or
  automated engagement beyond the repository's documented PR marker.
- **Deployment state:** Pending external review; no product repository change.
- **Baseline:** CLI 33 stars before submission; no Star growth attributed to a
  pending listing.
- **Review dates:** Re-check PR state on 2026-08-30 and 2026-09-06 UTC.
- **Result:** qualified MCP-discovery experiment pending review.
- **Next action:** Answer maintainer questions only; if merged, compare CLI
  referral traffic and record observed outcomes without causal overclaiming.

### 2026-08-23 — MCP directory eligibility clarification

- **Objective:** Keep the CLI listing accurate while responding to the target
  directory's automated verification request.
- **Evidence:** The directory asked for a Glama score badge and Dockerfile/
  introspection checks. CLI is a local stdio bridge, not a hosted MCP server;
  adding a hosted-server badge or Docker image would misrepresent its contract.
- **Action:** Replied on [PR #12702](https://github.com/punkpeye/awesome-mcp-servers/pull/12702#issuecomment-5384935946)
  explaining the local-stdio boundary and asking whether that project type is
  eligible. No misleading metadata was added.
- **Validation:** Current PR remains open; no maintainer decision yet.
- **Distribution channel:** Same community PR thread; no duplicate outreach.
- **Baseline:** CLI remains at 33 stars; no Star growth attributed to this
  pending listing or clarification.
- **Review dates:** Re-check on 2026-08-30 and 2026-09-06 UTC.
- **Result:** eligibility clarification pending; listing will be withdrawn if
  the directory only accepts hosted Dockerized servers.
- **Next action:** Follow the maintainer's answer and preserve the accurate
  local-stdio description.

### 2026-08-23 — MCP directory submission closed for eligibility

- **Objective:** Resolve the CLI directory experiment without misrepresenting
  a local bridge as a hosted MCP server.
- **Evidence:** The directory's automated check required a Glama listing,
  Dockerfile, and introspection response; no maintainer exception was offered.
- **Action:** Closed [PR #12702](https://github.com/punkpeye/awesome-mcp-servers/pull/12702)
  with a public explanation that the local-stdio contract does not satisfy the
  hosted-server requirement.
- **Validation:** PR is now closed; no Glama badge, Docker image, or unsupported
  endpoint claim was added.
- **Distribution channel:** One completed, documented directory experiment;
  no further outreach to that list planned.
- **Baseline:** CLI 33 stars before and after; no Star growth attributed to the
  ineligible listing.
- **Review dates:** None for this closed experiment; retain the record for
  future channel selection.
- **Result:** closed safely as ineligible; accuracy preserved.
- **Next action:** Focus CLI distribution on channels that explicitly support
  local stdio bridges and immutable release archives.

### 2026-08-23 — CLI organic Star snapshot

- **Objective:** Record the latest directly observed public Star signal without
  overstating causality.
- **Evidence:** GitHub API reported `sandbaseai/cli` at 34 stars, up from the
  prior ledger baseline of 33; forks remained 1. The other three repositories
  remained at 45, 41, and 1 respectively.
- **Action:** Added this snapshot after a fresh API read. No automated starring,
  paid placement, or attribution to a particular PR was made.
- **Validation:** Direct repository metadata query on 2026-08-23 UTC; the
  external Skills directory PR remains open and the CLI MCP listing was closed
  as ineligible.
- **Deployment state:** No code or production changes; ledger-only record.
- **Result:** +1 observed CLI Star, attribution pending.
- **Next action:** Re-query all four repositories and traffic/referral windows
  on the next scheduled review before making any causal claim.

### 2026-08-23 — CLI traffic follow-up window

- **Objective:** Check whether the observed CLI Star increase coincides with
  measurable repository discovery without inventing attribution.
- **Evidence:** GitHub Traffic API reported CLI page views of 21, 20, and 29
  on 2026-08-20, 2026-08-21, and 2026-08-22 (70 total; 41 unique visitors).
  Popular referrers were GitHub (63 views, 26 uniques), iohub.inshub.cn (2,
  1), and wx.mail.qq.com (1, 1). The API does not identify which action caused
  the +1 Star.
- **Action:** Recorded this follow-up window against the prior CLI Star
  snapshot; no new external posting or engagement was performed.
- **Validation:** Values read directly from the repository Traffic API on
  2026-08-23 UTC; referral totals are directional and not a causal experiment.
- **Result:** discovery signal observed; attribution pending.
- **Next action:** Re-query after the next scheduled window and compare with
  any maintainer decisions on external directory submissions.

### 2026-08-24 — Blog SEO execution batch

- **Scope:** `sandbaseai/sandbase-blog`; protected monorepo untouched.
- **Actions:** Added bilingual homepage internal-link hubs; added `WebSite` JSON-LD; ran three GSC-informed CTR experiments (DeepSeek Harness Preview, GLM-5.3, Claude Opus 5); migrated durable covers for DeepSeek comparison, DeepSeek Preview, and DSH Capability Seams from legacy media URLs.
- **Evidence:** Blog builds passed at 1,141 pages / 344 sitemap URLs / 688 hreflang targets / 0 unresolved paths. Deployments and public HTML checks passed for each merged change. GSC run `32679974382` still showed the pre-experiment baseline because of reporting delay.
- **PRs:** Blog #202–#211; operations record in [daily-ops #223](https://github.com/sandbaseai/sandbase-daily-ops/pull/223).
- **Result:** Crawl paths and OG asset durability improved; CTR impact remains an open experiment, not yet attributed.
- **Next hypothesis:** Re-query GSC after a full reporting window, then keep winners and revert/iterate only where impressions and CTR support it.

### 2026-08-24 — Daily audit and recrawl follow-up

- **Scope:** `sandbase-blog`, public acquisition surfaces, and protected-repository boundary.
- **Evidence:** GSC workflow `32683305503` reported 173 Blog clicks / 5,868 impressions and 0/2 indexing for GitHub MCP and Agent Observability. Live HTTP checks returned 200 for the website, Docs, Blog, GitHub organization, Skills, and CLI. Blog sitemap showed `lastmod=2026-08-24` for both pending pages.
- **Action:** Added the canonical daily audit at `promotion-plan/logs/2026-08-24.md`; no new content churn or protected monorepo mutation.
- **Validation:** Existing Blog deployments `32682968952` and `32683151865` succeeded; prior build gate remained 0 errors / 344 sitemap URLs / 688 hreflang targets / 0 unresolved paths.
- **Result:** Recrawl signals and discovery paths are verified; indexing remains an external Google-state blocker, not evidence of a source defect.
- **Review:** Check indexing on 2026-08-31, 14-day outcomes on 2026-09-07, and 28-day outcomes on 2026-09-21.

### 2026-08-24 — Public repository metadata verification

- **Evidence:** GitHub API reported `sandbase-harness` 630 stars, `sandbase-skills` 49 stars, and `cli` 41 stars; Docs health returned HTTP 200 and its README no longer contains `docs.sandbase.ai` links.
- **Action:** Refreshed observed star counts and verification date in `promotion-plan/master-context.md`; no product positioning or capability count was changed.
- **Validation:** API responses and the Docs health endpoint were read directly on 2026-08-24 UTC.
- **Result:** Context now reflects current public metadata; attribution to any individual promotion action remains unclaimed.

### 2026-08-24 — Approved third-party distribution queue

- **Source:** live canonical [OpenAI API alternatives](https://blog.sandbase.ai/openai-api-alternatives-2026/), with EN/ZH content and durable cover already verified in Blog.
- **Action:** Prepared channel-native drafts for LinkedIn, X, Discord, and Xiaohongshu under `social/`; each preserves canonical attribution and states operator-review status.
- **Validation:** Facts were limited to the source article; no external account, credential, or publishing API was used.
- **Result:** Four reviewable promotion assets are queued without duplicate live canonicals or unsolicited posting.
- **Next action:** Operator reviews channel fit and authorizes staggered publication; measure referral clicks and indexed canonical discovery after publication.

### 2026-08-27 — Four-repository growth snapshot

- **Objective:** Reconcile current public Star and traffic signals after the
  latest promotion and SEO work, using GitHub as the authority.
- **Evidence:** GitHub API reported Skills 62 stars (up from the prior 45
  snapshot), CLI 55 (from 34), Handbook 66 (from 41), and Docs 1. Forks were
  3, 4, 10, and 0 respectively. The latest available Traffic API days were:
  Skills 67 views/23 uniques (Aug 25), CLI 3/2, Handbook 65/31, and Docs
  105/6. Referrer data was strongest from GitHub for all four; Handbook also
  showed sandbaseai.github.io and search referrals.
- **Action:** Recorded the direct API snapshot on 2026-08-27 UTC. No Star is
  attributed to a particular PR, post, or SEO change because the APIs do not
  provide that causal link.
- **Validation:** Repository metadata and Traffic API responses were read
  directly; external Skills directory PR #27 remains open.
- **Deployment state:** Ledger-only update; no product or production changes.
- **Result:** substantial organic growth observed; 100-Star threshold remains
  unmet for every repository.
- **Next action:** Continue measuring referral and traffic windows, and focus
  future promotion on the two projects closest to 100 without neglecting Docs.

### 2026-08-27 — Directory review and Star delta follow-up

- **Evidence:** A fresh GitHub API read reported Skills 62 stars, CLI 56,
  Handbook 66, and Docs 1. Compared with the prior ledger snapshot, CLI is
  +1; the other three are unchanged. Latest available Traffic API data remains
  through 2026-08-25: Skills 67/23, CLI 3/2, Handbook 65/31, and Docs 105/6
  views/uniques respectively.
- **Distribution status:** VoltAgent/awesome-agent-skills PR #946 is now
  merged (2026-08-25); Ezeafk/awesome-agent-skills PR #27 remains open. No
  causal attribution is made between either directory review and Star changes.
- **Validation:** Repository metadata, Traffic API responses, and both PR
  states were read directly on 2026-08-27 UTC. Main is healthy and this is a
  ledger-only update.
- **Result:** One additional verified CLI Star; all four repositories remain
  below the 100-Star target.
- **Next hypothesis:** Recheck after the next traffic window and, for open
  directory submissions, wait for maintainer review rather than duplicating
  listings or posting unsolicited promotion.

### 2026-08-27 — Main-branch health verification

- **Evidence:** Direct GitHub API checks still report Skills 62, CLI 56,
  Handbook 66, and Docs 1 Star. The latest main-branch workflow runs for all
  four repositories completed successfully (Skills Validate Skills, CLI CI,
  Handbook Content check, Docs Validate Docs/Deploy Docs).
- **Action:** Confirmed the promotion changes remain compatible with the
  repositories' default branches; no source churn was introduced while the
  open directory submission awaits review.
- **Validation:** Commit status and Actions run results were read directly on
  2026-08-27 UTC. No causal Star attribution is inferred from green checks.
- **Result:** Main-branch health requirement remains verified; Star counts are
  unchanged since the preceding snapshot.
- **Next action:** Continue value-led distribution and recheck the open
  directory PR and Star/traffic deltas in the next measurement window.

### 2026-08-27 — Promotion queue status check

- **Evidence:** GitHub API recheck found no Star change: Skills 62, CLI 56,
  Handbook 66, Docs 1. Ezeafk/awesome-agent-skills PR #27 remains open with
  no comments or reviews and unchanged since 2026-08-23.
- **Action:** Kept the approved directory submission in the review queue;
  did not duplicate the listing or use unsolicited outreach while awaiting
  maintainer action.
- **Validation:** Repository metadata and PR state were read directly on
  2026-08-27 UTC; `sandbase-daily-ops` main was clean before this ledger-only
  append.
- **Result:** No new attributable promotion signal; all four repositories
  remain below the 100-Star target.
- **Next action:** Recheck after maintainer activity or the next traffic
  window, and record only directly verifiable deltas.

### 2026-08-27 — Repository conversion-surface audit

- **Evidence:** GitHub metadata confirms all four repositories use `main` as
  the default branch and expose a top-level README. Current Stars are Skills
  62, CLI 56, Handbook 66, and Docs 1; open issue counts are 0, 2, 3, and 1.
- **Action:** Reviewed the public entry-point surface before proposing further
  promotion. No broken README endpoint or urgent zero-context issue was found,
  so no speculative copy change was made.
- **Validation:** Repository metadata and README availability were read
  directly on 2026-08-27 UTC. This is a review-only ledger entry; no main
  branch was modified in the product repositories.
- **Result:** Public entry points remain reachable; the 100-Star requirement
  remains unmet and requires continued organic distribution.
- **Next action:** Use the next confirmed product improvement or maintainer
  response as the basis for a channel-native announcement, then measure its
  referral window without claiming causality.

### 2026-08-27 — Repeat direct Star and queue check

- **Evidence:** GitHub reports Skills 62, CLI 56, Handbook 66, and Docs 1
  Stars; fork counts remain 3, 4, 10, and 0. Ezeafk directory PR #27 is still
  open with no new maintainer activity since 2026-08-23.
- **Action:** Maintained the existing compliant distribution queue and
  avoided duplicate submissions or unsolicited follow-ups.
- **Validation:** Repository metadata and PR state were read directly on
  2026-08-27 UTC; no product repository was modified.
- **Result:** No new measurable Star or review delta. The four-repository
  100-Star target remains outstanding.
- **Next action:** Wait for a substantive maintainer response or fresh traffic
  window, then record the delta and link the exact public evidence.

### 2026-08-27 — Reactivation Star delta

- **Evidence:** A fresh GitHub API check reports Skills 62, CLI 57, Handbook
  66, and Docs 1 Star. CLI increased by one from the previous direct snapshot;
  the other repositories are unchanged. Ezeafk/awesome-agent-skills PR #27 is
  still open with no comments or reviews.
- **Action:** Recorded the organic CLI delta and kept the existing compliant
  distribution queue; no causal claim is made about the source of the Star.
- **Validation:** Repository metadata and PR state were read directly on
  2026-08-27 UTC. `sandbase-daily-ops` main was clean before this update.
- **Result:** CLI now has 57 verified Stars; all four repositories remain
  below the 100-Star target.
- **Next action:** Continue value-led promotion and recheck after the next
  traffic window or directory-maintainer activity.

### 2026-08-27 — Directory PR verification follow-up

- **Evidence:** Ezeafk/awesome-agent-skills PR #27 remains open. A single
  maintainer-facing follow-up comment was added at
  https://github.com/Ezeafk/awesome-agent-skills/pull/27#issuecomment-5433689741
  with the canonical repository URL, `skills.json`/CI validation details,
  MIT license, and a request to flag any format changes.
- **Action:** Supplied concise, reviewable context to the existing directory
  submission; did not create a duplicate PR or send unsolicited bulk outreach.
- **Validation:** Comment URL and PR state were read from GitHub on
  2026-08-27 UTC. Direct Star snapshot at the same window: Skills 62, CLI 57,
  Handbook 66, Docs 1; no causal attribution is inferred.
- **Result:** The submission now has maintainer-verifiable context while the
  four repositories remain below the 100-Star target.
- **Next action:** Await maintainer response; if requested, adjust only the
  directory entry and measure the next public traffic/Star window.

### 2026-08-27 — GitHub Topics discoverability update

- **Evidence:** `sandbase-docs` had eight Topics while the other three
  repositories already had broad, relevant topic coverage.
- **Action:** Added accurate discovery Topics to `sandbase-docs`:
  `documentation`, `agent-harness`, `deepseek`, `deepseek-harness`, `sandbase`,
  and `sandbaseai` (retaining its existing topics).
- **Validation:** GitHub Topics replacement API returned the complete 14-topic
  set successfully on 2026-08-27 UTC. No code, release, or README content was
  changed; this is a reversible metadata update.
- **Result:** The documentation repository is now more discoverable through
  GitHub's topic navigation and search. No immediate Star attribution is
  claimed; baseline snapshot remains Skills 62, CLI 57, Handbook 66, Docs 1.
- **Next action:** Recheck repository traffic and Stars after a reasonable
  discovery window, and avoid adding speculative or duplicated topics.

### 2026-08-27 — Docs repository search description update

- **Evidence:** `sandbase-docs`'s prior GitHub description was generic
  (`One API for 2000+ AI models, 2,000+ tools, and managed agents`) and did
  not describe the public documentation scope shown in its README.
- **Action:** Updated the repository description to: “Official SandBase
  developer documentation: one API for LLMs, image, video, audio, embeddings,
  real-world APIs, and reusable Agents.”
- **Validation:** GitHub repository metadata API returned the exact new
  description on 2026-08-27 UTC; wording matches the current README entry
  points and makes no unverifiable adoption claim.
- **Result:** GitHub search and repository cards now expose clearer intent for
  developers looking for SandBase documentation. No immediate Star causality
  is claimed; baseline remains Skills 62, CLI 57, Handbook 66, Docs 1.
- **Next action:** Measure traffic and Stars after the discovery window; keep
  metadata aligned with the README as the product evolves.

### 2026-08-27 — Documentation contributor funnel PR

- **Evidence:** `sandbase-docs` had no top-level contributor guide, making the
  path from discovery to a safe, validated documentation contribution unclear.
- **Action:** Opened [PR #10](https://github.com/sandbaseai/sandbase-docs/pull/10)
  adding `CONTRIBUTING.md` with issue/PR guidance, `npm ci` + `npm run build`
  validation, source-of-truth and link conventions, and credential-safety
  rules.
- **Validation:** `npm run build` completed successfully in 54.8 seconds on
  2026-08-27 UTC. The branch is pushed and the pull request is open for
  maintainer review.
- **Result:** External developers now have a clear, low-friction path to make
  useful contributions, improving the repository's conversion surface without
  claiming any Star attribution. Baseline remains Skills 62, CLI 57, Handbook
  66, Docs 1.
- **Next action:** Monitor PR #10 for review, respond to requested edits, and
  recheck traffic/Stars after the guide is merged.

### 2026-08-27 — Promotion queue and PR health recheck

- **Evidence:** GitHub reports `sandbase-docs` PR #10 still open, with no
  merge or review decision; Ezeafk/awesome-agent-skills PR #27 also remains
  open with one maintainer-visible follow-up comment. Direct Star counts are
  Skills 62, CLI 57, Handbook 66, Docs 1.
- **Action:** Kept both review queues active without duplicate comments or
  unsolicited outreach.
- **Validation:** PR metadata and repository counters were read directly from
  GitHub on 2026-08-27 UTC; no product repository was modified in this check.
- **Result:** No new Star or maintainer signal is attributable to report; all
  four repositories remain below the 100-Star target.
- **Next action:** Respond promptly if either maintainer requests changes and
  measure the next traffic window after review activity.

### 2026-08-27 — GitHub traffic measurement window

- **Evidence:** GitHub's private traffic API returned the latest available
  14-day window (through 2026-08-25 UTC). Clone totals/uniques were Skills
  1,607/592, CLI 419/162, Handbook 1,506/343, Docs 702/193. View totals/
  uniques were 427/156, 181/71, 1,131/401, and 178/16 respectively.
- **Action:** Captured the channel-health baseline to guide future
  value-led announcements; no artificial traffic or Star activity was used.
- **Validation:** Values were read directly from each repository's GitHub
  `/traffic/clones` and `/traffic/views` endpoints on 2026-08-27 UTC. Traffic
  data has the normal GitHub reporting lag, so no same-day causal inference is
  made.
- **Result:** Handbook and Skills show the strongest sustained discovery,
  while Docs has a recent clone spike; Star counts remain Skills 62, CLI 57,
  Handbook 66, Docs 1. The 100-Star target remains unmet.
- **Next action:** Compare the next available window against this baseline and
  prioritize useful, channel-native content for the repositories with lower
  conversion (especially Docs and CLI).

### 2026-08-27 — Contributor PR CI follow-up

- **Evidence:** SandBase Docs PR #10 remains open; its required `build` check
  is still pending at GitHub Actions run
  https://github.com/sandbaseai/sandbase-docs/actions/runs/33034389045 .
- **Action:** Monitored the required check and withheld merging until GitHub
  reports a completed result and normal mergeability.
- **Validation:** `gh pr checks` and PR metadata were read directly on
  2026-08-27 UTC; no source changes were made during this follow-up.
- **Result:** The contributor funnel change is awaiting automated validation;
  no Star attribution is claimed and the 100-Star target remains unmet.
- **Next action:** Recheck the run result; merge only after a successful check
  and required review conditions are satisfied.

### 2026-08-27 — Docs PR runner status

- **Evidence:** PR #10's required `build` workflow run
  (33034389045) remains `in_progress`; GitHub reports no assigned runner yet.
- **Action:** Kept the PR open and did not bypass required checks or merge
  around the repository's validation gate.
- **Validation:** `gh run view -R sandbaseai/sandbase-docs` returned the live
  workflow status on 2026-08-27 UTC.
- **Result:** No new review or Star signal; current counts remain Skills 62,
  CLI 57, Handbook 66, Docs 1.
- **Next action:** Recheck runner availability and mergeability when the
  required build completes.

### 2026-08-27 — Docs contributor guide merged

- **Evidence:** SandBase Docs PR #10 completed its required `build` check
  successfully at 2026-08-27 02:51 UTC and became clean/mergeable.
- **Action:** Squash-merged [PR #10](https://github.com/sandbaseai/sandbase-docs/pull/10)
  into `main` and deleted the topic branch. Merge commit:
  `3c85ea69b26658cf424091a144f3b36974764e1e`.
- **Validation:** GitHub PR metadata confirms `MERGED`; the required workflow
  concluded `success` before merge.
- **Result:** The public docs repository now has a contributor funnel with
  validated local-build instructions, improving sustainable community
  participation. No Star causality is claimed; counts remain Skills 62, CLI
  57, Handbook 66, Docs 1.
- **Next action:** Verify the merged guide on `main`, then monitor traffic and
  Stars for the next measurement window.

### 2026-08-27 — README contribution entry-point PR

- **Evidence:** After PR #10 merged, the README's contribution section did not
  link directly to the new `CONTRIBUTING.md` guide.
- **Action:** Opened [PR #11](https://github.com/sandbaseai/sandbase-docs/pull/11)
  to add that direct link, so repository visitors can move from discovery to
  the validated contribution workflow in one click.
- **Validation:** Markdown-only change committed as `9674013`, pushed to the
  remote branch, and submitted for review on 2026-08-27 UTC.
- **Result:** Improves contributor conversion without changing runtime docs or
  making Star attribution claims. Current baseline remains Skills 62, CLI 57,
  Handbook 66, Docs 1.
- **Next action:** Monitor PR #11, merge after normal checks/review, and then
  compare Docs traffic and Stars in the next window.

### 2026-08-27 — README link PR validation pending

- **Evidence:** SandBase Docs PR #11 remains open and its required `build`
  check is still `in_progress`; merge state is `UNSTABLE` until the check
  completes.
- **Action:** Continued monitoring without bypassing the required workflow or
  duplicating the contribution request.
- **Validation:** PR metadata was read directly from GitHub on 2026-08-27 UTC;
  no product source changed during this check.
- **Result:** The README entry-point improvement awaits CI; no new Star signal
  is claimed. Baseline remains Skills 62, CLI 57, Handbook 66, Docs 1.
- **Next action:** Merge after successful CI and normal review conditions, then
  measure Docs traffic and Stars.

### 2026-08-27 — Skills organic Star delta

- **Evidence:** A fresh GitHub repository metadata snapshot reports
  `sandbase-skills` at 63 Stars, up from the prior recorded 62; CLI 57,
  Handbook 66, and Docs 1 are unchanged. Docs PR #11 remains open with its
  `build` check in progress.
- **Action:** Recorded the directly observed Skills increase without assigning
  it to any specific post, directory listing, or PR.
- **Validation:** Values and PR state were read directly from GitHub on
  2026-08-27 UTC; no artificial Star activity or source change was made.
- **Result:** Skills is now at 63 verified Stars; all four repositories remain
  below the 100-Star target.
- **Next action:** Continue compliant distribution and use the next traffic
  window to test which public entry points improve conversion.

### 2026-08-27 — README contribution link merged

- **Evidence:** SandBase Docs PR #11's `Validate Docs` workflow completed
  successfully (run 33034637810), and the PR became mergeable.
- **Action:** Squash-merged [PR #11](https://github.com/sandbaseai/sandbase-docs/pull/11)
  into `main` and removed its topic branch. Merge commit:
  `6897fba4e2c15472c5c77103e43dbb7d9ce2ee1b`.
- **Validation:** GitHub metadata confirms `MERGED`; the validation run
  concluded `success` before the merge.
- **Result:** README visitors can now reach the contributor guide directly,
  completing the docs contribution funnel. No Star causality is claimed;
  baseline remains Skills 63, CLI 57, Handbook 66, Docs 1.
- **Next action:** Verify `main` remains healthy and measure the next Docs
  traffic/Star window before making another metadata or content change.

### 2026-08-27 — Handbook organic Star delta

- **Evidence:** Fresh GitHub metadata reports `deepseek-harness-handbook` at
  67 Stars, up from the prior recorded 66. Skills remains 63, CLI 57, and Docs
  1. The latest Docs `main` validation run is still in progress.
- **Action:** Recorded the directly observed Handbook increase without
  attributing it to any particular article, link, or directory.
- **Validation:** Repository counters, default branches, and workflow list were
  read directly from GitHub on 2026-08-27 UTC; all four default branches are
  `main`.
- **Result:** Handbook now has 67 verified Stars; all repositories remain below
  the 100-Star target. No artificial engagement was used.
- **Next action:** Continue useful, channel-native promotion and recheck the
  Docs deployment/validation result before the next traffic window.

### 2026-08-27 — Main validation and Star recheck

- **Evidence:** The latest `sandbase-docs` main `Validate Docs` run
  (33034796517) is still reported `in_progress`; the preceding main and PR
  validation runs completed successfully. Current Stars are Skills 63, CLI 57,
  Handbook 67, Docs 1.
- **Action:** Continued monitoring the deployment gate and kept promotion
  activity value-led while avoiding duplicate outreach.
- **Validation:** GitHub Actions and repository metadata were read directly on
  2026-08-27 UTC; no code or metadata was changed in this check.
- **Result:** No new Star delta or deployment failure was observed; the
  100-Star target remains outstanding.
- **Next action:** Recheck when the in-progress run resolves or a new traffic
  window becomes available.

### 2026-08-27 — Docs deployment queue recheck

- **Evidence:** GitHub now shows the latest `sandbase-docs` main workflows as
  `Validate Docs` (run 33034860136) and `Deploy Docs` (run 33034870990), both
  still `in_progress`. Star counts remain Skills 63, CLI 57, Handbook 67,
  Docs 1; view totals remain 427/156, 181/71, 1,131/401, and 178/16.
- **Action:** Kept the deployment queue under observation and made no changes
  while required validation/deployment jobs are active.
- **Validation:** Workflow, repository metadata, and traffic endpoints were
  read directly from GitHub on 2026-08-27 UTC; no causal traffic or Star claim
  is made.
- **Result:** No new measurable growth signal or failure was observed; the
  100-Star target remains outstanding.
- **Next action:** Recheck after both workflows complete and compare the next
  available traffic window.

### 2026-08-27 — Docs workflow still active

- **Evidence:** Direct GitHub Actions inspection shows main `Validate Docs`
  run 33034860136 (`build`) and `Deploy Docs` run 33034870990 (`validate`)
  still `in_progress`; the preceding validation run succeeded.
- **Action:** Left the active workflows untouched and did not cancel, bypass,
  or force deployment while jobs are running.
- **Validation:** `gh run view -R sandbaseai/sandbase-docs` returned both live
  job states on 2026-08-27 UTC. No Star change was observed (Skills 63, CLI 57,
  Handbook 67, Docs 1).
- **Result:** No new failure or growth signal; the 100-Star target remains
  unmet.
- **Next action:** Recheck after workflow completion and record any deployment
  result or Star/traffic delta.

### 2026-08-27 — Release and Star baseline recheck

- **Evidence:** GitHub latest releases are Skills `v0.3.5` (2026-08-20), CLI
  `v0.1.17` (2026-08-19), and Handbook `v0.5.99` (2026-08-27); Docs has no
  published release, consistent with its documentation-site role. Current
  Stars remain Skills 63, CLI 57, Handbook 67, Docs 1.
- **Action:** Confirmed each project's release surface before planning further
  announcements; did not create an artificial Docs release or imply a new
  release where none exists.
- **Validation:** GitHub Releases and repository metadata APIs were read
  directly on 2026-08-27 UTC.
- **Result:** Handbook has a fresh release that can support future
  channel-native promotion; no immediate Star delta is attributable to this
  check.
- **Next action:** Use the current release notes and verified docs links in a
  targeted announcement, then measure traffic and Stars in the next window.

### 2026-08-27 — Post-merge deployment verification

- **Evidence:** After PR #11 merged, `Validate Docs` main completed
  successfully, while `Deploy Docs` run 33034870990 remains `in_progress`.
  Repository counters are unchanged: Skills 63, CLI 57, Handbook 67, Docs 1
  Stars (forks 3, 4, 10, 0).
- **Action:** Kept the deployment workflow running and did not claim the README
  link was live on the hosted site until deployment reports completion.
- **Validation:** GitHub Actions and repository metadata were read directly on
  2026-08-27 UTC.
- **Result:** Source merge is verified, hosted deployment is not yet verified;
  no new Star attribution is claimed.
- **Next action:** Recheck deployment completion and then measure Docs traffic
  and Stars against the prior window.

### 2026-08-27 — Deployment queue follow-up

- **Evidence:** Deploy Docs run 33034870990 remains `in_progress` (last update
  2026-08-27 02:59:57 UTC); no conclusion has been published. Stars remain
  Skills 63, CLI 57, Handbook 67, Docs 1.
- **Action:** Continued observation without cancelling or bypassing the active
  deployment workflow.
- **Validation:** GitHub run metadata and repository counters were read
  directly on 2026-08-27 UTC.
- **Result:** Hosted deployment remains unverified, with no new measurable Star
  signal; the 100-Star target remains unmet.
- **Next action:** Recheck the run conclusion before any further docs-site
  promotion claim.

### 2026-08-27 — Docs production deployment verified

- **Evidence:** Deploy Docs run 33034870990 completed successfully at
  2026-08-27 03:04:39 UTC. Both `validate` and `build-and-deploy` jobs passed,
  including the production URL health check.
- **Action:** Confirmed the merged contributor entry is deployed before using
  the docs site as a promotion destination.
- **Validation:** GitHub run metadata reports `completed/success`; a live
  request to https://www.sandbase.ai/docs/ returned page content containing
  the contribution entry text. All four default branches remain `main`.
- **Result:** The Docs contribution funnel is now verified in production. Star
  counts remain Skills 63, CLI 57, Handbook 67, Docs 1; no causal attribution
  is inferred.
- **Next action:** Use the live docs and Handbook release page in targeted,
  channel-native promotion, then measure the next traffic/Star window.

### 2026-08-27 — Handbook Show HN release update

- **Evidence:** The existing [Show HN discussion #157](https://github.com/sandbaseai/deepseek-harness-handbook/discussions/157)
  had no comments after its original announcement. Handbook `v0.5.99` is now
  the latest published release.
- **Action:** Added one maintainer-facing update at
  https://github.com/sandbaseai/deepseek-harness-handbook/discussions/157#discussioncomment-18170089
  describing the release and inviting versioned, reproducible reports for
  future source-backed guides. The comment does not repeat a Star request.
- **Validation:** GitHub GraphQL returned the public comment URL and the
  release metadata was verified directly on 2026-08-27 UTC.
- **Result:** Existing interested readers now have a concrete release update
  and a clear way to contribute evidence; no causal Star attribution is made.
  Current counts remain Skills 63, CLI 57, Handbook 67, Docs 1.
- **Next action:** Monitor discussion engagement and measure traffic/Stars in
  the next available window without additional duplicate comments.

### 2026-08-27 — Referrer channel analysis

- **Evidence:** GitHub popular-referrers API shows the strongest non-GitHub
  source is `sandbaseai.github.io` → Handbook (201 views / 46 uniques),
  followed by Google (55 / 35). Skills also receives 6 / 4 from
  `awesome-dsh-plugin.com`; CLI's external referrers are sparse (2 / 1 from
  iohub.inshub.cn and 1 / 1 Google); Docs has only GitHub in the current
  report (51 / 7).
- **Action:** Identified the Handbook's hosted site and search indexing as the
  highest-confidence channels for future useful announcements; no automated
  or bulk referral activity was created.
- **Validation:** Values were read directly from each repository's GitHub
  `traffic/popular/referrers` endpoint on 2026-08-27 UTC. Referrer data is
  aggregated and does not prove Star causality.
- **Result:** The next promotion hypothesis is evidence-led: improve the
  Handbook site's release/guide landing paths and cross-link relevant projects,
  then compare referral and Star conversion.
- **Next action:** Use the existing `v0.5.99` release and canonical site as the
  anchor for one targeted update; avoid repeating channels with no observed
  signal.

### 2026-08-27 — MCP directory eligibility review

- **Evidence:** Reviewed `punkpeye/awesome-mcp-servers` contribution rules and
  current entries. The list accepts local stdio servers, but its entries are
  expected to describe a discrete MCP server and commonly include Glama
  verification metadata. SandBase CLI is a multi-client bridge/gateway rather
  than a single-purpose server, and a prior submission to a similar directory
  was closed for unmet registry requirements.
- **Action:** Chose not to submit a duplicate or low-fit PR; retained the
  existing CLI release, MCPRepository, and skills.sh distribution links.
- **Validation:** Contribution guide and current README format were read
  directly on 2026-08-27 UTC; no external repository was modified.
- **Result:** Avoided a likely rejected listing while preserving accurate,
  already-supported discovery channels. Star counts remain Skills 63, CLI 57,
  Handbook 67, Docs 1.
- **Next action:** Revisit this directory only if CLI gains the required
  standalone-server/verification metadata; otherwise focus on existing channels.

### 2026-08-28 — Organic Star and traffic delta

- **Evidence:** GitHub API snapshot on 2026-08-28 reports Skills 67, CLI 61,
  Handbook 73, Docs 1 Stars. Compared with the prior 63/57/67/1 baseline,
  deltas are +4, +4, +6, and 0. Latest view totals/uniques are Skills
  450/163, CLI 190/73, Handbook 1,218/430, Docs 206/19.
- **Action:** Recorded the new counters and traffic window without attributing
  growth to any individual post, PR, directory, or discussion.
- **Validation:** Repository Stars, forks, timestamps, and private traffic
  endpoints were read directly from GitHub on 2026-08-28 UTC. Ezeafk PR #27 is
  now closed without merge, so no directory acceptance is claimed.
- **Result:** Three repositories show meaningful organic increases, but none has
  reached 100 Stars: Skills 67, CLI 61, Handbook 73, Docs 1.
- **Next action:** Preserve the verified release/site entry points, continue
  low-noise value-led distribution, and measure the next window before drawing
  any channel conclusion.

### 2026-08-28 — Organization profile cross-project discovery

- **Evidence:** The public `sandbaseai/.github` profile featured CLI, Skills,
  and the Handbook but had no direct featured-project or Start Here link for
  `sandbase-docs`, whose direct GitHub snapshot is 1 Star.
- **Action:** Added an official SandBase Docs project row and API-docs starting
  link to the organization profile. Commit: https://github.com/sandbaseai/.github/commit/3d207a3
- **Validation:** Pushed to `main`; GitHub commit is publicly reachable and the
  edited Markdown contains both links. This is a discovery improvement, not a
  claim of Star attribution.
- **Distribution channel:** GitHub organization profile, visible to visitors
  across all SandBase repositories.
- **Star count before/after:** Skills 67→67, CLI 61→61, Handbook 73→73,
  Docs 1→1 at the time of the action; no causal lift is claimed.
- **Result:** Docs now has a first-class cross-project discovery path from the
  organization landing page.
- **Next hypothesis:** Measure the next GitHub traffic window for Docs and
  avoid additional profile edits unless a missing, high-intent entry point is
  evidenced.

### 2026-08-28 — Handbook scorecard maintenance update

- **Evidence:** Discussion #218 had a browser-only Agent Harness Evaluation
  Scorecard with no comments; the tool and rubric are publicly reproducible.
- **Action:** Added a factual maintenance comment with the scorecard, source,
  and issue links: https://github.com/sandbaseai/deepseek-harness-handbook/discussions/218#discussioncomment-18181565
- **Validation:** GitHub returned the public comment URL; no automated or
  incentivized engagement was used.
- **Distribution channel:** Existing high-intent Handbook discussion.
- **Star count before/after:** Skills 67→67, CLI 61→61, Handbook 73→73,
  Docs 1→1 at action time; no causal attribution.
- **Result:** The scorecard discussion now has a maintained, actionable path
  from evaluation to reproducible implementation feedback.
- **Next hypothesis:** Watch discussion engagement and referral traffic before
  adding another comment or opening a new promotional thread.

### 2026-08-28 — Referrer window recheck

- **Evidence:** GitHub's current popular-referrer endpoint reports Skills
  `github.com 166/64`, CLI `github.com 74/34`, Handbook `github.com 479/203`
  plus `sandbaseai.github.io 208/48`, and Docs `github.com 63/9` (count/unique).
  The prior recorded snapshot was Skills 158/59, CLI 69/31, Handbook 452/194
  plus site 201/46, and Docs 51/7.
- **Action:** Rechecked the public traffic attribution window after the
  profile and scorecard updates; no additional external post was manufactured.
- **Validation:** Values were read directly from GitHub's repository traffic
  API on 2026-08-28 UTC. Star counts remained Skills 67, CLI 61, Handbook 73,
  Docs 1, so no channel is credited with causality.
- **Result:** GitHub and Handbook-site referral counts are higher than the
  previous snapshot; the window is observational and not a conversion proof.
- **Next hypothesis:** Keep the existing canonical links and wait for a new
  traffic window before changing channel mix or repeating outreach.

### 2026-08-28 — Organization profile freshness correction

- **Evidence:** The organization profile described the Handbook as having 80
  English-canonical guides, while the current Handbook README reports 143.
- **Action:** Corrected the profile to the verified 143-guide count. Commit:
  https://github.com/sandbaseai/.github/commit/3981a2a
- **Validation:** Pushed to `main`; source README and profile wording were read
  directly from GitHub. Star counts at the check stayed Skills 67, CLI 61,
  Handbook 73, Docs 1.
- **Distribution channel:** GitHub organization profile.
- **Result:** Visitors now see an accurate, stronger discovery description;
  this is not evidence of Star causality.
- **Next hypothesis:** Recheck profile claims only when the source README
  changes materially, avoiding noisy edits.

### 2026-08-28 — Enable Docs community feedback channel

- **Evidence:** `sandbase-docs` had GitHub Discussions disabled while its
  README directs contributors to canonical issue and contribution paths. This
  removed a low-friction place for integration questions and reusable answers.
- **Action:** Enabled GitHub Discussions on `sandbaseai/sandbase-docs` through
  the repository settings API.
- **Validation:** GitHub API returned `has_discussions=true`; the repository
  remains public and at 1 Star. No discussion, comment, or Star was generated
  automatically.
- **Distribution channel:** Docs repository community surface.
- **Star count before/after:** Skills 67→67, CLI 61→61, Handbook 73→73,
  Docs 1→1; no causal attribution.
- **Result:** Developers can now ask public API/documentation questions and
  leave discoverable answers alongside the Docs repository.
- **Next hypothesis:** Seed no promotional thread; wait for a genuine user
  question, then answer with canonical docs links and measure referral traffic.

### 2026-08-28 — Docs integration Q&A index

- **Evidence:** After Discussions was enabled, `sandbase-docs` had no public
  Q&A topic to help a new developer find the canonical getting-started,
  API-reference, store, and agent links.
- **Action:** Created the practical Q&A index:
  https://github.com/sandbaseai/sandbase-docs/discussions/12
- **Validation:** GitHub returned the public discussion URL in the Q&A
  category. The post contains no credentials, incentives, or automated
  engagement request.
- **Distribution channel:** Docs repository Discussions, linked to canonical
  hosted docs and issue reporting.
- **Star count before/after:** Skills 67→67, CLI 61→61, Handbook 73→73,
  Docs 1→1; no causal attribution.
- **Result:** A durable, searchable integration entry point now exists for
  developers arriving from GitHub.
- **Next hypothesis:** Answer only genuine follow-up questions and compare Docs
  traffic/referrers in the next available window.

### 2026-08-28 — CLI developer discussion interaction

- **Evidence:** CLI discussion #47 explained the 2,000+ model workflow but had
  no comments with a safe preview path.
- **Action:** Added a practical follow-up showing the read-only `catalog --json`
  command, release link, and checksum guidance:
  https://github.com/sandbaseai/cli/discussions/47#discussioncomment-18181647
- **Validation:** GitHub returned the public comment URL. The comment is
  technical, non-incentivized, and does not request manufactured engagement.
- **Distribution channel:** Existing CLI GitHub Discussion.
- **Star count before/after:** Skills 67→67, CLI 61→61, Handbook 73→73,
  Docs 1→1; no causal attribution.
- **Result:** Readers can safely inspect supported targets before connecting a
  client, reducing friction for legitimate adoption.
- **Next hypothesis:** Engage only on genuine follow-up questions and compare
  CLI referral traffic in the next window.

### 2026-08-28 — Skills installation discussion interaction

- **Evidence:** Skills discussion #48 described preview/install usage but had no
  follow-up comment covering release-integrity verification.
- **Action:** Added a concise checksum-verification command and source/issues
  links: https://github.com/sandbaseai/sandbase-skills/discussions/48#discussioncomment-18181653
- **Validation:** GitHub returned the public comment URL; content is technical,
  reproducible, and contains no artificial engagement request.
- **Distribution channel:** Existing SandBase Skills GitHub Discussion.
- **Star count before/after:** Skills 67→67, CLI 61→61, Handbook 73→73,
  Docs 1→1; no causal attribution.
- **Result:** Developers can verify the downloaded artifact before trying the
  Skill, reducing adoption friction and support ambiguity.
- **Next hypothesis:** Continue one useful follow-up per distinct discussion,
  then measure referral traffic rather than posting duplicate announcements.

### 2026-08-28 — High-quality Chinese MCP directory PR

- **Evidence:** `yzfly/Awesome-MCP-ZH` explicitly accepts real, installable,
  documented MCP resources and asks contributors to submit a focused PR.
  SandBase CLI has public source, Apache-2.0 licensing, local MCP bridging,
  and documented client/release verification paths.
- **Action:** Added a factual SandBase CLI entry and submitted PR #512:
  https://github.com/yzfly/Awesome-MCP-ZH/pull/512
- **Validation:** Fork branch commit `76bc0f0` pushed successfully; PR is open
  for maintainer review. Description contains no Star or ranking request.
- **Distribution channel:** Curated Chinese MCP directory with explicit
  contribution rules and an audience aligned to CLI/MCP adoption.
- **Star count before/after:** CLI 61→61 at submission time; Skills 67,
  Handbook 73, Docs 1; no causal attribution or artificial engagement.
- **Result:** A qualified, maintainer-reviewed discovery path is now active for
  SandBase CLI.
- **Next hypothesis:** Answer maintainer feedback and amend the single PR if
  requested; do not duplicate the entry in other lists until this review ends.

### 2026-08-28 — High-quality MCP clients directory PR

- **Evidence:** `punkpeye/awesome-mcp-clients` explicitly welcomes new clients,
  requires a repository link and concise functionality description, and asks
  for alphabetical, accurate entries. SandBase CLI is a public Apache-2.0
  local MCP bridge/CLI with documented client support.
- **Action:** Added a factual SandBase CLI client entry and submitted PR #294:
  https://github.com/punkpeye/awesome-mcp-clients/pull/294
- **Validation:** Fork branch commit `4fe72a5` pushed successfully; the PR
  includes no Star/排名 request or artificial engagement language.
- **Distribution channel:** Curated MCP client directory with explicit
  contribution rules and a developer audience aligned to CLI adoption.
- **Star count before/after:** CLI 61→61 at submission time; Skills 67,
  Handbook 73, Docs 1; no causal attribution.
- **Result:** A second, independent maintainer-reviewed discovery path is open
  for SandBase CLI, without duplicating the same destination in one list.
- **Next hypothesis:** Wait for maintainer review and respond only to concrete
  feedback; avoid further directory submissions until these two reviews settle.

### 2026-08-28 — Directory review follow-up

- **Evidence:** Follow-up check found `Awesome-MCP-ZH#512` closed at
  2026-08-27T23:52:21Z without merge and without maintainer feedback; no
  acceptance is claimed. `awesome-mcp-clients#294` remains open and clean.
- **Action:** Recorded the review outcomes and stopped any duplicate resubmission
  to the Chinese directory; retained the single pending clients-directory PR:
  https://github.com/punkpeye/awesome-mcp-clients/pull/294
- **Validation:** Both PR states were read directly with `gh pr view`; CLI Star
  count remains 61, with no attribution inferred from the submissions.
- **Distribution channel:** Curated MCP directories under maintainer review.
- **Result:** Promotion remains policy-compliant and avoids repeated closed-list
  submissions or unsolicited follow-up noise.
- **Next hypothesis:** Wait for #294 review; only revise or respond to explicit
  maintainer feedback.

### 2026-08-28 — MCP developer-tools directory PR

- **Evidence:** `punkpeye/awesome-mcp-devtools` publishes contribution rules
  that welcome developer tools and require concise, accurate, categorized
  entries. A repository search confirmed SandBase CLI was not already listed.
- **Action:** Added one factual entry under Development Tools and opened PR
  #292: https://github.com/punkpeye/awesome-mcp-devtools/pull/292
- **Validation:** Fork branch `add-sandbase-cli` commit `fcfb5c0` was pushed;
  the PR targets `main` and contains no ranking, Star, or engagement request.
- **Distribution channel:** Curated MCP developer-tools directory with an
  audience aligned to CLI/MCP adoption.
- **Star count before/after:** CLI 61→61 at submission time; Skills 67,
  Handbook 73, Docs 1; no causal attribution.
- **Result:** A third distinct, maintainer-reviewed discovery path is open for
  SandBase CLI, while the prior clients-directory PR remains the only other
  active submission.
- **Next hypothesis:** Wait for maintainer review and respond only to concrete
  feedback; do not post duplicate entries or unsolicited comments.

### 2026-08-28 — External directory review status

- **Evidence:** Direct GitHub checks show `awesome-mcp-devtools#292` remains
  open and clean with no reviews/comments. The earlier
  `awesome-mcp-clients#294` is now closed, also without review feedback.
- **Action:** Updated the outreach state and stopped follow-up on the closed
  PR; no replacement submission was made.
- **Validation:** `gh pr view` returned the current states and the four target
  repositories remain at Skills 67, CLI 61, Handbook 73, Docs 1.
- **Distribution channel:** Maintainer-reviewed MCP directories.
- **Result:** One relevant PR remains pending while avoiding repeated or
  unsolicited directory noise.
- **Next hypothesis:** Wait for #292 maintainer feedback; pursue a new channel
  only when it has a distinct audience and explicit contribution fit.

### 2026-08-28 — mcp.so directory submission

- **Evidence:** `chatmcp/mcpso#1` is an open submission thread for MCP servers;
  a paginated comment search confirmed SandBase CLI was not already listed.
- **Action:** Posted one factual, disclosed entry with repository, release, and
  official registry links: https://github.com/chatmcp/mcpso/issues/1#issuecomment-5446685099
- **Validation:** GitHub returned the public comment URL. The entry describes
  the open-source CLI/local bridge and asks maintainers to verify and categorize
  it; it contains no Star or ranking request.
- **Distribution channel:** `mcp.so` community submission thread (MCP-focused
  directory; approximately 2,100 GitHub Stars on the host repository).
- **Star count before/after:** CLI 61→61 at submission time; Skills 67,
  Handbook 73, Docs 1; no causal attribution.
- **Result:** Added a distinct MCP-directory discovery path for SandBase CLI.
- **Next hypothesis:** Wait for directory maintainer handling and respond only
  to concrete verification questions.

### 2026-08-28 — High-star MCP servers directory PR

- **Evidence:** `punkpeye/awesome-mcp-servers` contribution guidelines
  explicitly welcome new servers and require a concise, accurate categorized
  entry. A repository search found no SandBase CLI entry.
- **Action:** Added SandBase CLI under Aggregators and opened PR #13046:
  https://github.com/punkpeye/awesome-mcp-servers/pull/13046
- **Validation:** Fork branch `add-sandbase-cli-server` was pushed; the PR
  contains only one factual entry and no ranking or engagement request.
- **Distribution channel:** Curated MCP server directory (approximately
  92,000 GitHub Stars on the host repository).
- **Star count before/after:** CLI 61→61 at submission time; Skills 67,
  Handbook 73, Docs 1; no causal attribution.
- **Result:** Opened a distinct high-reach discovery path for the CLI.
- **Next hypothesis:** Wait for maintainer review and amend only if requested.

### 2026-08-28 — MCP directory validation follow-up

- **Evidence:** `awesome-mcp-servers#13046` received an automated maintainer
  check requesting a Glama score badge. Direct HTTP verification confirmed the
  existing Glama listing at https://glama.ai/mcp/servers/sandbaseai/cli.
- **Action:** Updated the PR entry with the requested badge and replied with
  the verification details: https://github.com/punkpeye/awesome-mcp-servers/pull/13046#issuecomment-5446708909
- **Validation:** Commit `aea670f` pushed to the PR branch; the badge points to
  the verified Glama server page and no engagement request was added.
- **Distribution channel:** Curated MCP server directory with Glama validation.
- **Star count before/after:** CLI 61→61; Skills 67, Handbook 73, Docs 1;
  no causal attribution.
- **Result:** Satisfied the directory's concrete validation request and kept
  the submission eligible for maintainer review.
- **Next hypothesis:** Wait for human/automated review outcome and respond only
  to further concrete checks.

### 2026-08-28 — Glama score follow-up

- **Evidence:** The directory bot confirmed the badge but requested that the
  Glama server page have a completed quality evaluation. The page is live, but
  no quality score is currently exposed in the fetched HTML.
- **Action:** Left the requested badge in place and verified the exact Glama
  path; no unsupported score claim was added to the PR.
- **Validation:** `awesome-mcp-servers#13046` remains open and clean; the
  current page is https://glama.ai/mcp/servers/sandbaseai/cli/score.
- **Distribution channel:** Curated MCP server directory with Glama quality
  gating.
- **Result:** Badge requirement is satisfied; score evaluation remains a
  maintainer/Glama-side prerequisite rather than something to fabricate.
- **Next hypothesis:** Wait for Glama evaluation or further maintainer
  instructions before changing the PR again.

### 2026-08-28 — PR comment accuracy correction

- **Evidence:** Review of `awesome-mcp-servers#13046` found the prior reply
  contained a literal shell substitution string in the commit reference.
- **Action:** Edited the public reply to reference the actual badge commit
  `aea670f`: https://github.com/punkpeye/awesome-mcp-servers/pull/13046#issuecomment-5446708909
- **Validation:** GitHub API returned the edited comment URL; no repository
  content or claim about an unverified Glama score was changed.
- **Distribution channel:** The same maintainer-review PR.
- **Result:** Public promotion metadata is now precise and reproducible.
- **Next hypothesis:** Await the directory's quality-score evaluation and review.

### 2026-08-28 — Agent Skills collection PR

- **Evidence:** `skillmatic-ai/awesome-agent-skills` explicitly accepts
  high-quality Agent Skills resources, requires concise links, and had no
  SandBase entry. The SandBase repository is public, documented, and uses the
  `SKILL.md` format.
- **Action:** Added `sandbaseai/sandbase-skills` under Popular Collections and
  opened PR #161: https://github.com/skillmatic-ai/awesome-agent-skills/pull/161
- **Validation:** Fork branch `add-sandbase-skills` commit `05c76f9` was pushed;
  the PR contains one factual link and no ranking or engagement request.
- **Distribution channel:** Curated Agent Skills resource directory.
- **Star count before/after:** Skills 67→67; CLI 61, Handbook 73, Docs 1;
  no causal attribution.
- **Result:** Added an independent discovery path specifically for the Skills
  repository.
- **Next hypothesis:** Wait for maintainer review and respond only to concrete
  feedback.

### 2026-08-28 — DeepSeek Harness directory accuracy PR

- **Evidence:** `0xsline/awesome-deepseek-harness` already links the Handbook,
  but its Related section still stated 79 guides. The current Handbook index
  verifies 143 source-backed guides.
- **Action:** Corrected the existing listing and opened PR #513:
  https://github.com/0xsline/awesome-deepseek-harness/pull/513
- **Validation:** Fork branch `update-handbook-count` commit `c639bb1` was
  pushed; links and functionality text were preserved, with only the verified
  count changed.
- **Distribution channel:** DeepSeek Harness-specific curated directory.
- **Star count before/after:** Handbook 73→73; Skills 67, CLI 61, Docs 1;
  no causal attribution.
- **Result:** Improved listing accuracy while keeping the Handbook visible to
  a highly relevant audience.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  questions.

### 2026-08-28 — Handbook directory PR outcome

- **Evidence:** Direct GitHub check shows `awesome-deepseek-harness#513` was
  closed without merge and without maintainer comments.
- **Action:** Recorded the outcome and stopped follow-up on that PR; no
  duplicate resubmission was made.
- **Validation:** `mergedAt` is null and `closedAt` is present; Handbook remains
  at 73 Stars, with no causal attribution.
- **Result:** Promotion history remains accurate and avoids repeated closed-list
  submissions.
- **Next hypothesis:** Use only a new directory with explicit contribution
  criteria and distinct audience; do not reopen the closed PR.

### 2026-08-28 — Official DeepSeek integration guide PR

- **Evidence:** `deepseek-ai/awesome-deepseek-agent` explicitly accepts
  bilingual integration guides covering installation, configuration, and first
  run. SandBase CLI was not in its tools table.
- **Action:** Added English and Simplified Chinese SandBase CLI guides and
  synchronized both README tables; opened PR #407:
  https://github.com/deepseek-ai/awesome-deepseek-agent/pull/407
- **Validation:** Fork branch `add-sandbase-cli-guide` commit `5777207` was
  pushed. The guide uses the verified v0.1.17 release commands, current
  DeepSeek V4 naming, and documents 1M context without hard-coding volatile
  pricing or availability.
- **Distribution channel:** Official DeepSeek community integration directory.
- **Star count before/after:** CLI 61→61; Skills 67, Handbook 73, Docs 1;
  no causal attribution.
- **Result:** Created a durable, search-indexed onboarding path for DeepSeek
  users evaluating SandBase CLI.
- **Next hypothesis:** Respond to maintainer checks and update only when
  concrete documentation feedback arrives.

### 2026-08-28 — Closed directory submissions status

- **Evidence:** Direct GitHub checks show `awesome-agent-skills#161` and
  `awesome-mcp-servers#13046` were closed without merge and without review
  comments. The official DeepSeek guide PR #407 remains open and clean.
- **Action:** Recorded both closures and stopped follow-up on those PRs; no
  duplicate resubmissions were made.
- **Validation:** `mergedAt` is null for both closed PRs; target counts remain
  Skills 67, CLI 61, Handbook 73, Docs 1.
- **Result:** Outreach history is accurate and avoids repeatedly submitting to
  closed directory workflows.
- **Next hypothesis:** Keep #407 as the active external submission and pursue
  only a distinct, clearly documented channel thereafter.

### 2026-08-28 — DeepSeek integration troubleshooting interaction

- **Evidence:** DeepSeek's official agent directory has an open Chinese issue
  reporting Claude Desktop `anthropic/v1/models` 404 errors and model-name
  incompatibilities.
- **Action:** Added a disclosed, technically scoped alternative using SandBase
  CLI's local MCP bridge, with read-only catalog and OAuth connect commands:
  https://github.com/deepseek-ai/awesome-deepseek-agent/issues/62#issuecomment-5446807952
- **Validation:** The reply explicitly states this is not a direct fix for the
  404 and links the CLI repository and official MCP Registry; no unsupported
  compatibility claim or engagement request was made.
- **Distribution channel:** Existing user troubleshooting issue in the
  official DeepSeek integration repository.
- **Star count before/after:** CLI 61→61; Skills 67, Handbook 73, Docs 1;
  no causal attribution.
- **Result:** Provided a relevant, reproducible path to readers with the
  reported endpoint problem.
- **Next hypothesis:** Respond only if the issue author asks for client-version
  or connection-specific help.

### 2026-08-28 — Official DeepSeek guide PR outcome

- **Evidence:** Direct GitHub check shows `deepseek-ai/awesome-deepseek-agent#407`
  was closed without merge and without maintainer comments.
- **Action:** Recorded the closure and stopped follow-up on the PR; no duplicate
  guide submission was made.
- **Validation:** `closedAt` is present and `mergedAt` is null. Target counts
  remain Skills 67, CLI 61, Handbook 73, Docs 1.
- **Result:** Promotion history remains accurate and respects the directory's
  decision.
- **Next hypothesis:** Wait for a new explicit contribution opportunity rather
  than reopening or reposting the closed guide.

### 2026-08-28 — Independent CLI directory suggestion correction

- **Evidence:** A third-party user opened `jamesmurdza/awesome-ai-devtools#1026`
  suggesting SandBase CLI, but the proposed npm package name was inaccurate.
  Package metadata verifies the published name is `@sandbaseai/cli`.
- **Action:** Replied with the corrected install/package detail and immutable
  release, package, and Registry links:
  https://github.com/jamesmurdza/awesome-ai-devtools/issues/1026#issuecomment-5446831848
- **Validation:** Verified `package.json` reports `@sandbaseai/cli` version
  `0.1.17`; no unsupported feature or engagement claim was added.
- **Distribution channel:** External developer-tools directory editorial issue
  initiated by an independent contributor.
- **Star count before/after:** CLI 61→61; Skills 67, Handbook 73, Docs 1;
  no causal attribution.
- **Result:** Improved the accuracy of an independent promotion opportunity and
  reduced the chance of failed installs for readers.
- **Next hypothesis:** Let the directory maintainer handle editorial review;
  respond only to further factual questions.

### 2026-08-28 — MCP Servers directory listing verified

- **Evidence:** The directory's submission page states that MCP projects are
  submitted through the website rather than by pull request. A direct lookup
  confirms SandBase CLI already has a live listing at
  https://mcpservers.org/servers/sandbaseai/cli.
- **Action:** Avoided a duplicate submission and recorded the existing listing
  as the active MCP discovery surface.
- **Validation:** The live page title is “SandBase MCP Server” and describes
  the open-source CLI/local MCP bridge; URL returned HTTP 200 on 2026-08-28.
- **Distribution channel:** mcpservers.org directory (organic search and
  directory discovery).
- **Star count before/after:** Skills 67→67; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Confirmed a high-intent MCP directory presence without creating
  duplicate or low-quality outreach.
- **Next hypothesis:** Improve the listing only when factual metadata changes;
  otherwise focus on distinct communities with explicit contribution paths.

### 2026-08-28 — Open AI developer tools directory submission

- **Evidence:** `Sami-Uysal/awesome-open-ai-developer-tools` documents explicit
  inclusion criteria (open source, active maintenance, real developer utility,
  no duplicate) and accepts one-tool PRs.
- **Action:** Opened PR #26 adding SandBase CLI with Apache-2.0 license, active
  maturity, 25-client support, read-only catalog verification, and checksum
  details: https://github.com/Sami-Uysal/awesome-open-ai-developer-tools/pull/26
- **Validation:** Verified the canonical CLI repository license, release
  `v0.1.17`, latest push date, README claims, and contribution format before
  submitting; no star counts or unsupported marketing claims were added.
- **Distribution channel:** Curated open-source AI developer-tools directory.
- **Star count before/after:** Skills 67→67; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A new, rule-compliant discovery path is live for maintainer review.
- **Next hypothesis:** Answer maintainer questions with reproducible install or
  compatibility evidence; do not repost if declined.

### 2026-08-28 — Codex CLI ecosystem directory submission

- **Evidence:** `RoggeOhta/awesome-codex-cli` accepts additions by PR and
  requires direct Codex relevance, active maintenance, a clear description,
  and a live GitHub star badge.
- **Action:** Opened PR #222 adding SandBase CLI under General-Purpose MCP with
  its Codex support, 25-client catalog, and read-only compatibility check:
  https://github.com/RoggeOhta/awesome-codex-cli/pull/222
- **Validation:** Confirmed the canonical CLI README lists Codex as a supported
  client, release `v0.1.17` is current, and the entry uses the required badge
  format; no inflated or fabricated metrics were used.
- **Distribution channel:** Curated Codex CLI ecosystem directory.
- **Star count before/after:** Skills 67→67; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A second distinct, rule-compliant directory review is now active.
- **Next hypothesis:** Provide install or compatibility evidence if the
  maintainer requests it; respect any editorial decision without reposting.

### 2026-08-28 — Codex Skills collection submission

- **Evidence:** `ComposioHQ/awesome-codex-skills` explicitly welcomes PRs for
  real, reusable skills with precise descriptions and tested metadata.
- **Action:** Opened PR #260 adding SandBase Skills as an external portable
  collection, with the evidence-ledger search workflow and exact Codex install
  command: https://github.com/composio-community/awesome-codex-skills/pull/260
- **Validation:** Checked the canonical repository README for the current
  install command and workflow description; used the published count of 88
  installable skills and made no star or usage claims.
- **Distribution channel:** Curated Codex Skills directory.
- **Star count before/after:** Skills 67→67; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A distinct, high-intent discovery path for `sandbase-skills` is
  awaiting maintainer review.
- **Next hypothesis:** Respond with reproducible install/validation details if
  requested; do not repost after an editorial rejection.

### 2026-08-28 — AI coding tools directory submission

- **Evidence:** `ai-for-developers/awesome-ai-coding-tools` invites
  contributions by PR and maintains dedicated CLI and MCP sections.
- **Action:** Opened PR #658 adding SandBase CLI to the CLI Tools section with
  a factual local-MCP-bridge and multi-client description:
  https://github.com/ai-for-developers/awesome-ai-coding-tools/pull/658
- **Validation:** Checked the canonical CLI metadata and README before writing
  the one-line entry; no fabricated star counts, rankings, or user claims were
  included.
- **Distribution channel:** Curated AI coding tools directory.
- **Star count before/after:** Skills 67→67; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A new discovery path for CLI users is awaiting maintainer review.
- **Next hypothesis:** Answer factual questions if requested and respect the
  maintainer's decision without duplicate submissions.

### 2026-08-28 — Directory review outcomes

- **Evidence:** Direct GitHub checks show the Open AI developer tools PR #26
  and Awesome Codex CLI PR #222 are closed, both without merge or maintainer
  comments; AI Coding Tools PR #658 remains open without comments.
- **Action:** Recorded the editorial outcomes and stopped follow-up on the two
  closed submissions; no duplicate reposts or requests for artificial stars
  were made.
- **Validation:** `mergedAt` is null for both closed PRs; target counts remain
  Skills 67, CLI 61, Handbook 73, Docs 1.
- **Distribution channel:** Three independent curated developer-tool lists.
- **Result:** Outreach records now reflect current public states and preserve
  the one still-live review path.
- **Next hypothesis:** Respond only to substantive maintainer feedback on #658
  or a new, clearly documented contribution opportunity.

### 2026-08-28 — Duplicate submission closed in favor of existing issue

- **Evidence:** The target directory already had issue #656, opened by an
  independent maintainer-affiliated submitter, with a detailed factual SandBase
  CLI proposal and disclosure. PR #658 duplicated that same editorial path.
- **Action:** Closed PR #658 and left a public note directing review to the
  existing issue: https://github.com/ai-for-developers/awesome-ai-coding-tools/issues/656
- **Validation:** Confirmed issue #656 contains the canonical repository URL,
  CLI/MCP capabilities, Apache-2.0 license, registry package, and disclosure;
  no second comment or competing entry was posted.
- **Distribution channel:** AI coding tools directory editorial queue.
- **Star count before/after:** Skills 67→67; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Reduced duplicate noise while preserving the stronger existing
  promotion opportunity.
- **Next hypothesis:** Support the existing issue only when maintainers ask for
  factual evidence; avoid reopening or reposting the closed PR.

### 2026-08-28 — Organic star delta after directory outreach

- **Evidence:** Direct GitHub API read shows `sandbase-skills` at 68 stars,
  up from the previously recorded 67; CLI remains 61, Handbook 73, and Docs
  1. The change is not attributable to any single channel.
- **Action:** Recorded the observed delta without claiming causation or asking
  for artificial starring.
- **Validation:** Counts were read from the four canonical repository records
  on GitHub; no synthetic accounts, scripted stars, or exchange activity were
  used.
- **Distribution channel:** Aggregate organic discovery following prior
  directory and ecosystem submissions.
- **Result:** Skills has a small, verifiable organic increase; the 100-star
  target remains unmet for all four repositories.
- **Next hypothesis:** Continue only with substantive, rule-compliant outreach
  and product improvements that earn voluntary stars.

### 2026-08-28 — Corrected stale star count in external listing issue

- **Evidence:** `hades217/awesome-ai#132` contains a SandBase CLI proposal with
  a stale “59” star count; the canonical GitHub API currently reports 61.
- **Action:** Replied with the current count and authoritative stargazer/release
  links, noting the issue's existing description otherwise needs no change:
  https://github.com/hades217/awesome-ai/issues/132#issuecomment-5446966148
- **Validation:** Verified the count from the canonical repository and release
  `v0.1.17`; did not add inflated metrics or an engagement request.
- **Distribution channel:** Open-source AI directory editorial issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Improved factual accuracy for readers and maintainers of an open
  discovery channel.
- **Next hypothesis:** Respond to further editorial questions with immutable
  release or source evidence only.

### 2026-08-28 — Corrected package name in external AI tools issue

- **Evidence:** `mahseema/awesome-ai-tools#2055` proposed installing
  `@sandbase/cli`, which is an unrelated package; the SandBase package is
  `@sandbaseai/cli`.
- **Action:** Posted a factual correction with npm metadata and the immutable
  v0.1.17 release/`catalog --json` verification command:
  https://github.com/mahseema/awesome-ai-tools/issues/2055#issuecomment-5446971018
- **Validation:** Confirmed the package name and release against the public
  npm registry and canonical GitHub release; no marketing or star claims added.
- **Distribution channel:** AI tools directory editorial issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Reduced the risk of readers installing an unrelated package from
  an otherwise active directory submission.
- **Next hypothesis:** Continue correcting concrete inaccuracies only when they
  appear in public editorial queues.

### 2026-08-28 — Corrected package name in Chinese AI tools directory

- **Evidence:** `0voice/awesome-ai-tools#125` repeated the incorrect
  `@sandbase/cli` install name in an otherwise complete Chinese-language
  submission.
- **Action:** Added a single factual correction with the official
  `@sandbaseai/cli` package, immutable release, and read-only catalog command:
  https://github.com/0voice/awesome-ai-tools/issues/125#issuecomment-5446979709
- **Validation:** Checked npm metadata and the canonical `v0.1.17` release;
  preserved the issue's affiliation disclosure and made no star or popularity
  claims.
- **Distribution channel:** Chinese AI tools directory editorial issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Prevented a likely failed install for Chinese-speaking readers.
- **Next hypothesis:** Continue only with concrete, source-backed corrections.

### 2026-08-28 — Corrected stale star count in MCP catalog issue

- **Evidence:** `Rodert/awesome-mcp#26` recorded 58 Stars at submission time;
  the canonical repository currently reports 61.
- **Action:** Posted a concise correction linking the live stargazer page and
  advising generated catalogs not to hard-code the count:
  https://github.com/Rodert/awesome-mcp/issues/26#issuecomment-5446990691
- **Validation:** Verified the current count and release `v0.1.17` directly on
  GitHub; no artificial engagement or popularity claim was added.
- **Distribution channel:** MCP catalog collection issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Improved freshness and accuracy of a potentially generated MCP
  catalog entry.
- **Next hypothesis:** Keep correcting stale metadata when it is concretely
  evidenced, without repeating already-correct submissions.

### 2026-08-28 — Corrected handbook guide count in Claude Code directory issue

- **Evidence:** `hesreallyhim/awesome-claude-code#2610` proposed the Handbook
  with “115+” guides; the current repository catalog verifies 143 guides.
- **Action:** Replied once with the updated count and canonical repository link,
  noting that the number is maintained data and may change:
  https://github.com/hesreallyhim/awesome-claude-code/issues/2610#issuecomment-5446995833
- **Validation:** Checked the handbook's current catalog and preserved the
  submitter's disclosure and Apache-2.0 attribution; no fabricated metrics or
  engagement request was added.
- **Distribution channel:** Curated Claude Code documentation directory issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Improved factual accuracy of a high-relevance documentation
  discovery opportunity for Claude Code users.
- **Next hypothesis:** Answer only further editorial questions with source
  evidence; avoid duplicate submissions.

### 2026-08-28 — Corrected stale count in command-line tools scope check

- **Evidence:** `ad-si/awesome-command-line-tools#6` asks whether SandBase CLI
  fits its scope and cites 58 Stars; the canonical repository currently shows
  61.
- **Action:** Replied with the live Stargazers link and current count while
  explicitly respecting the maintainer's scope decision:
  https://github.com/ad-si/awesome-command-line-tools/issues/6#issuecomment-5447005527
- **Validation:** Verified the count and `v0.1.17` release directly; no PR was
  opened and no popularity request was made.
- **Distribution channel:** Curated command-line tools scope discussion.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Supplied a precise fact for editorial review without forcing an
  out-of-scope submission.
- **Next hypothesis:** Follow up only if the maintainer confirms the category
  fit or asks for evidence.

### 2026-08-28 — Corrected stale count in Codex directory issue

- **Evidence:** `milisp/awesome-codex-cli#111` cited 60 GitHub Stars for SandBase
  CLI; the canonical repository currently reports 61.
- **Action:** Replied with the live Stargazers link and confirmed that the
  v0.1.17 release and MCP Registry references remain current:
  https://github.com/milisp/awesome-codex-cli/issues/111#issuecomment-5447017490
- **Validation:** Verified the count directly against GitHub and did not add
  any artificial popularity language.
- **Distribution channel:** Curated Codex CLI directory issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Kept a Codex-specific listing accurate for readers and maintainers.
- **Next hypothesis:** Continue factual corrections only where a concrete stale
  value is present.

### 2026-08-28 — Corrected stale count in AI Gateway scope issue

- **Evidence:** `12britz/awesome-ai-gateways#30` asks whether SandBase CLI fits
  the managed-gateway category and cites 58 Stars; the canonical repository
  currently reports 61.
- **Action:** Replied with the live Stargazers link and left the scope decision
  to the maintainer, preserving the accurate caveat that SandBase is not a
  self-hosted/OpenAI-compatible proxy:
  https://github.com/12britz/awesome-ai-gateways/issues/30#issuecomment-5447021908
- **Validation:** Verified the count and release references on GitHub; no PR,
  popularity request, or unsupported gateway claim was made.
- **Distribution channel:** Curated AI Gateway directory scope discussion.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Supplied current evidence without forcing an out-of-scope listing.
- **Next hypothesis:** Follow up only if the maintainer requests more evidence
  or confirms the category fit.

### 2026-08-28 — Updated stale count in Chinese LLM resources issue

- **Evidence:** `WangRongsheng/awesome-LLM-resources#209` cited 58 Stars for
  SandBase CLI; the canonical repository currently reports 61.
- **Action:** Added a Chinese-language correction and live Stargazers link:
  https://github.com/WangRongsheng/awesome-LLM-resources/issues/209#issuecomment-5447026601
- **Validation:** Verified the current count directly on GitHub and confirmed
  the existing v0.1.17 command remains valid; no artificial engagement was
  requested.
- **Distribution channel:** Chinese LLM resources directory issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Kept a high-relevance Chinese resource listing factually current.
- **Next hypothesis:** Continue source-backed corrections only where a stale
  value is explicitly visible.

### 2026-08-28 — Updated adoption signal in MCP directory issue

- **Evidence:** `hireblackout/awesome-mcp-servers#43` proposed a conservative
  Tier 4 listing but retained a stale 58-Star count; GitHub currently reports
  61.
- **Action:** Replied with the live Stargazers URL and preserved the issue's
  honest caveat that independent usage consensus is not established:
  https://github.com/hireblackout/awesome-mcp-servers/issues/43#issuecomment-5447031437
- **Validation:** Verified the current count on the canonical repository and
  made no changes to the submitted test, release, or download claims.
- **Distribution channel:** Curated MCP server directory issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Improved an external listing's factual freshness without
  overstating project maturity.
- **Next hypothesis:** Let maintainers decide tier placement and respond only
  to further factual questions.

### 2026-08-28 — Updated OpenClaw directory adoption signal

- **Evidence:** `vincentkoc/awesome-openclaw#130` cited 58 GitHub Stars for
  SandBase CLI; the canonical repository currently reports 61.
- **Action:** Replied with the live Stargazers link and kept the existing
  OpenClaw integration, release, and checksum claims unchanged:
  https://github.com/vincentkoc/awesome-openclaw/issues/130#issuecomment-5447036186
- **Validation:** Verified the count directly on GitHub and made no new
  popularity or download claims.
- **Distribution channel:** OpenClaw ecosystem directory issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Kept a client-specific discovery listing factually current.
- **Next hypothesis:** Respond only to maintainer requests or concrete stale
  metadata in other client directories.

### 2026-08-28 — Updated Top AI Tools directory signal

- **Evidence:** `ghimiresunil/Top-AI-Tools#609` cited 60 Stars at submission;
  the canonical SandBase CLI repository now reports 61.
- **Action:** Replied with the live Stargazers URL and confirmed the remaining
  technical and Registry details:
  https://github.com/ghimiresunil/Top-AI-Tools/issues/609#issuecomment-5447040423
- **Validation:** Verified the count directly on GitHub; no unsupported claim
  or request for artificial engagement was added.
- **Distribution channel:** Curated AI tools directory issue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Kept another developer-facing listing accurate for editorial review.
- **Next hypothesis:** Respond only when maintainers request additional source
  evidence.

### 2026-08-28 — DeepSeek Harness Handbook added to harness engineering directory

- **Evidence:** `ai-boost/awesome-harness-engineering` accepts resources that
  address concrete harness problems and explicitly welcomes PR contributions.
- **Action:** Opened PR #221 adding the Handbook to Foundations as a
  source-backed, model-specific companion covering runtime boundaries, tools,
  controls, sessions, recovery, runbooks, and diagnostics:
  https://github.com/ai-boost/awesome-harness-engineering/pull/221
- **Validation:** Checked the directory's contribution criteria and based the
  entry on the canonical Handbook README; no inflated metrics or popularity
  claims were used.
- **Distribution channel:** Curated harness-engineering resource directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Created a new, high-relevance discovery path for the Handbook.
- **Next hypothesis:** Provide source or runbook evidence if maintainers ask;
  respect editorial decisions without reposting.

### 2026-08-28 — Harness engineering directory PR outcome

- **Evidence:** Direct GitHub check shows `ai-boost/awesome-harness-engineering#221`
  was closed without merge and without maintainer comments.
- **Action:** Recorded the editorial outcome and stopped follow-up; no duplicate
  PR or reopening was attempted.
- **Validation:** `mergedAt` is null and the target counts remain Skills 68,
  CLI 61, Handbook 73, Docs 1.
- **Distribution channel:** Curated harness-engineering resource directory.
- **Result:** Outreach history remains accurate and respects the directory's
  decision.
- **Next hypothesis:** Pursue only a distinct, explicitly open channel for the
  Handbook, not a repost of this closed PR.

### 2026-08-28 — Hermes directory listing corrected and merged

- **Evidence:** `0xNyk/awesome-hermes-agent#363` reported that the accepted
  SandBase CLI listing incorrectly attributed sandbox functionality to the CLI.
- **Action:** The maintainer merged the correction through PR #364, replacing
  the description with the verified six-tool local MCP bridge scope:
  https://github.com/0xNyk/awesome-hermes-agent/issues/363
- **Validation:** The issue confirms the change landed on `main`; beta marker,
  link, attribution, Apache-2.0 license, and Registry/source evidence were
  preserved.
- **Distribution channel:** Hermes agent integrations directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A live external listing now accurately separates the CLI from the
  SandBase sandbox project, improving trust for Hermes users.
- **Next hypothesis:** Keep monitoring only for concrete listing inaccuracies;
  do not add promotional comments to an already-correct entry.

### 2026-08-28 — Handbook submission to Awesome Agent Harness

- **Evidence:** `Picrew/awesome-agent-harness` accepts practical harness
  runtimes, documentation, and tooling via a data-driven catalog; its rules
  require concise bilingual summaries, tags, and inclusion rationale.
- **Action:** Opened issue #82 proposing the Handbook under Documentation /
  Learning with a source-backed, implementation-focused description:
  https://github.com/Picrew/awesome-agent-harness/issues/82
- **Validation:** Confirmed the Handbook is Apache-2.0, bilingual, actively
  documented, and distinct from the repository's existing official runtime and
  paper entries; affiliation was disclosed.
- **Distribution channel:** Curated Agent Harness engineering directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Created a new, scope-appropriate discovery path for the Handbook.
- **Next hypothesis:** If maintainers approve the scope, prepare the exact
  `data/projects.yaml` entry and run their verification pipeline.

### 2026-08-28 — Handbook submission to second harness directory

- **Evidence:** `walkinglabs/awesome-harness-engineering` explicitly accepts
  practical harness resources and asks for concise, non-promotional entries;
  the Handbook was not present in its README.
- **Action:** Opened PR #84 adding the Handbook to Courses & Learning Resources
  with a source-backed description of its runbooks and diagnostics:
  https://github.com/walkinglabs/awesome-harness-engineering/pull/84
- **Validation:** Checked the contribution rules, canonical Handbook content,
  and duplicate absence before submitting; affiliation was disclosed.
- **Distribution channel:** Curated harness-engineering tools and guides list.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Added a distinct high-relevance discovery path for Handbook users.
- **Next hypothesis:** Answer maintainer questions with source evidence and
  respect any editorial decision without reposting.

### 2026-08-28 — Harness directory PR validation

- **Evidence:** `walkinglabs/awesome-harness-engineering#84` remains open and
  its reported status check is successful; no maintainer review comments yet.
- **Action:** Confirmed the focused Handbook addition passes the repository's
  available automated check and left the PR unchanged pending human review:
  https://github.com/walkinglabs/awesome-harness-engineering/pull/84
- **Validation:** GitHub reports a successful check, with no merge yet; the
  target counts remain Skills 68, CLI 61, Handbook 73, Docs 1.
- **Result:** The new Handbook discovery path is technically clean and awaiting
  editorial decision.
- **Next hypothesis:** Respond to any maintainer comment; do not add duplicate
  entries while the PR is under review.

### 2026-08-28 — Walking Labs directory PR outcome

- **Evidence:** `walkinglabs/awesome-harness-engineering#84` was closed on
  2026-08-28 without merge, comments, or review feedback.
- **Action:** Recorded the editorial outcome and stopped follow-up; no duplicate
  submission or reopening was attempted.
- **Validation:** GitHub reports `mergedAt: null`; target counts remain Skills
  68, CLI 61, Handbook 73, Docs 1.
- **Distribution channel:** Curated harness-engineering tools and guides list.
- **Result:** Outreach history remains accurate and respects the directory's
  decision.
- **Next hypothesis:** Use only new, explicitly open documentation channels for
  the Handbook; do not repost this closed PR.

### 2026-08-28 — SandBase CLI submission attempt to Appcypher MCP directory

- **Evidence:** `appcypher/awesome-mcp-servers` lists production-ready and
  experimental MCP servers; its Development Tools section had no SandBase
  entry. Contribution rules request one focused PR per suggestion and a
  succinct, useful description.
- **Action:** Prepared a one-line `SandBase CLI` entry in fork branch
  `denial123789/awesome-mcp-servers:add-sandbase-cli`:
  https://github.com/denial123789/awesome-mcp-servers/tree/add-sandbase-cli
- **Validation:** Confirmed the CLI README documents its local MCP bridge,
  25 clients, 2,000+ models/APIs, release checksum, CI, and MCP Registry
  listing. Upstream issues are disabled; authenticated PR creation was denied
  for both available accounts, so no upstream PR was fabricated.
- **Distribution channel:** Curated MCP server directory (submission blocked
  at upstream permission boundary).
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** The candidate entry is ready for maintainer review, but no
  upstream change was made. Stopped rather than bypassing repository controls.
- **Next hypothesis:** If a maintainer invites a PR or enables issues, submit
  the prepared focused change; otherwise do not repost.

### 2026-08-28 — SandBase CLI proposal to Awesome MCP Servers (YuzeHao2023)

- **Evidence:** `YuzeHao2023/Awesome-MCP-Servers` is a 1k+ star community
  catalog with an explicit Development Tools category; SandBase CLI was not
  present and the repository accepts issue proposals.
- **Action:** Opened issue #450 with a concise, source-backed entry proposal:
  https://github.com/YuzeHao2023/Awesome-MCP-Servers/issues/450
- **Validation:** Rechecked the CLI README for installation, release
  checksum, CI, MCP Registry, 25 clients, and 2,000+ models/APIs before
  posting; no duplicate SandBase entry was found.
- **Distribution channel:** Curated MCP server directory, maintainer issue
  queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A factual, single-project discovery proposal is open for
  maintainer review; no manufactured engagement or star claim was made.
- **Next hypothesis:** Wait for maintainer feedback and answer only concrete
  questions; do not duplicate the proposal elsewhere in this directory.

### 2026-08-28 — SandBase Skills proposal to Agent Skill Index

- **Evidence:** `heilcheng/awesome-agent-skills` is a 6k+ star index with a
  defined Community Skills → Development and Testing category and explicit
  SKILL.md quality requirements. No SandBase entry was present.
- **Action:** Opened issue #448 with a concise entry proposal:
  https://github.com/heilcheng/awesome-agent-skills/issues/448
- **Validation:** Confirmed the public repository contains documented SKILL.md
  files and 68 GitHub stars; the proposal links the canonical repository and
  avoids unsupported usage claims.
- **Distribution channel:** Curated Agent Skill Index maintainer queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A new, scope-matched discovery path is open for independent
  maintainer review; no manufactured engagement was used.
- **Next hypothesis:** Respond only to concrete quality or usage questions and
  stop if the maintainer declines.

### 2026-08-28 — Verification follow-up on Awesome AI Coding Tools

- **Evidence:** Existing issue #656 in `ai-for-developers/awesome-ai-coding-tools`
  proposes SandBase CLI and remains open with no maintainer comments.
- **Action:** Added one factual follow-up comment with current README evidence
  (local MCP bridge, 25 clients, release checksum, CI, and official Registry):
  https://github.com/ai-for-developers/awesome-ai-coding-tools/issues/656#issuecomment-5447167205
- **Validation:** Confirmed the canonical CLI README and avoided opening a
  duplicate issue or PR; wording explicitly leaves taxonomy decisions to the
  maintainer.
- **Distribution channel:** Curated AI coding tools issue queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Maintainer now has updated, verifiable evidence for an existing
  proposal; no artificial engagement was created.
- **Next hypothesis:** Wait for editorial response and answer only concrete
  follow-up questions.

### 2026-08-28 — SandBase Skills proposal to Libukai Agent Skills guide

- **Evidence:** `libukai/awesome-agent-skills` is a 5k+ star bilingual guide
  that emphasizes a small, high-quality set of skills and supports community
  recommendations; no SandBase entry was found.
- **Action:** Opened bilingual issue #137 proposing the canonical Skills repo:
  https://github.com/libukai/awesome-agent-skills/issues/137
- **Validation:** Confirmed the repo exposes multiple documented SKILL.md
  packages and accurately described the multi-source research/offline
  validation scope; current direct count is 68 stars.
- **Distribution channel:** Chinese/English Agent Skills resource guide.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A relevant, non-duplicative discovery proposal is queued for
  maintainer review without manufactured engagement.
- **Next hypothesis:** Wait for editorial feedback and answer only concrete
  questions about quality, compatibility, or usage.

### 2026-08-28 — Handbook evidence follow-up in Learning Weekly

- **Evidence:** Existing self-recommendation issue #108 in
  `eryajf/learning-weekly` remains open with no comments.
- **Action:** Added a concise Chinese follow-up with current, verifiable
  Handbook scope (bilingual content, 143 guides, runbooks and troubleshooting)
  and offered to adapt the summary to editorial format:
  https://github.com/eryajf/learning-weekly/issues/108#issuecomment-5447176399
- **Validation:** Linked the canonical repository and stated the observed
  approximate 73-star count without attributing stars to the comment.
- **Distribution channel:** Chinese developer-learning weekly submission.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Editors have updated factual material for an existing submission;
  no duplicate issue or artificial engagement was created.
- **Next hypothesis:** Wait for editorial response and answer only concrete
  requests.

### 2026-08-28 — CLI verification follow-up in Awesome Agent CLI

- **Evidence:** `Ariestar/awesome-agent-cli#8` is an open, directly relevant
  SandBase CLI proposal with no maintainer comments.
- **Action:** Added a reproducible install command and security-oriented
  evidence (release SHA-256, CI, MCP Registry, and 25-client documentation):
  https://github.com/Ariestar/awesome-agent-cli/issues/8#issuecomment-5447179927
- **Validation:** Matched the command and checksum to the canonical CLI
  README/release and asked the maintainer to evaluate independently.
- **Distribution channel:** Curated AI-agent CLI directory issue queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Maintainer has concrete, reproducible onboarding evidence for the
  existing proposal; no duplicate thread or artificial engagement created.
- **Next hypothesis:** Wait for review and answer only specific follow-ups.

### 2026-08-28 — CLI evidence follow-up in Awesome Generative AI APIs

- **Evidence:** Existing issue #435 in `foss42/awesome-generative-ai-apis` is
  open and directly concerns adding SandBase as an AI gateway/aggregator.
- **Action:** Added a factual maintainer follow-up linking the official MCP
  Registry, v0.1.17 release/checksum, local bridge, 2,000+ model/API scope,
  and API quickstart docs:
  https://github.com/foss42/awesome-generative-ai-apis/issues/435#issuecomment-5447183545
- **Validation:** Rechecked the canonical CLI README and docs; no unsupported
  performance or adoption claims were added.
- **Distribution channel:** Curated generative-AI API directory issue queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** The open proposal now has reproducible review links; no duplicate
  thread or artificial engagement was created.
- **Next hypothesis:** Wait for maintainer evaluation and answer only concrete
  questions.

### 2026-08-28 — Maintainer-approved CLI catalog PR

- **Evidence:** `yeaight7/awesome-ai-devtools#30` explicitly approved the
  SandBase CLI suggestion and requested a fork-based PR using its template.
- **Action:** Opened PR #33 with the metadata entry and generated README/
  comparison updates:
  https://github.com/yeaight7/awesome-ai-devtools/pull/33
- **Validation:** Ran `npm install --ignore-scripts`, `npm run sort`,
  `npm run generate`, `npm test` (59/59), `npm run validate` (warnings only),
  and `git diff --check`; all required gates passed.
- **Distribution channel:** Curated AI developer-tools catalog.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Converted an approved suggestion into a reviewable, tested PR;
  no fabricated engagement or claims were used.
- **Next hypothesis:** Respond to maintainer review and preserve the catalog's
  metadata requirements until merge or explicit rejection.

### 2026-08-28 — AI Devtools PR CI follow-up

- **Evidence:** `yeaight7/awesome-ai-devtools#33` remains open, unmerged, with
  no review comments; its required `greeting` check is pending.
- **Action:** Rechecked PR state and CI without adding noise or prompting the
  maintainer while automation is still running:
  https://github.com/yeaight7/awesome-ai-devtools/pull/33
- **Validation:** Direct GitHub API counts currently show Skills 68, CLI 61,
  Handbook 73, Docs 1; no Star movement or causal attribution is claimed.
- **Distribution channel:** Curated AI developer-tools catalog PR review.
- **Result:** Tested metadata contribution remains in the genuine CI/review
  queue; no duplicate comment or artificial engagement was created.
- **Next hypothesis:** Address only a failed check or maintainer review comment;
  otherwise leave the PR unchanged until CI completes.

### 2026-08-28 — AI Devtools PR CI passed

- **Evidence:** `yeaight7/awesome-ai-devtools#33` is still open and unmerged,
  but its required `greeting` check has completed successfully.
- **Action:** Added one concise PR comment notifying the maintainer that CI,
  generated files, and validation gates are ready:
  https://github.com/yeaight7/awesome-ai-devtools/pull/33#issuecomment-5447204940
- **Validation:** `gh pr checks 33` reports `greeting pass`; no review comments
  or merge event exists yet.
- **Distribution channel:** Curated AI developer-tools catalog PR review.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** The maintainer has a clear, non-repetitive readiness signal after
  CI completion; no artificial engagement was created.
- **Next hypothesis:** Wait for maintainer review or merge; respond only to
  concrete requested changes.

### 2026-08-28 — CLI onboarding evidence in Freeapps

- **Evidence:** `Qutaifan/Freeapps#34` is an open SandBase CLI suggestion with
  no maintainer comments.
- **Action:** Added a concise follow-up with the official one-command `npx`
  installer, SHA-256 verification, CI, and MCP Registry links:
  https://github.com/Qutaifan/Freeapps/issues/34#issuecomment-5447209899
- **Validation:** Matched the command to the canonical v0.1.17 release and
  left categorization to the directory maintainer.
- **Distribution channel:** Curated free developer-tools directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Maintainer has reproducible onboarding evidence for the existing
  proposal; no duplicate thread or manufactured engagement was created.
- **Next hypothesis:** Wait for maintainer response and answer only concrete
  questions.

### 2026-08-28 — Handbook proposal to AutoJunjie Agent Harness list

- **Evidence:** `AutoJunjie/awesome-agent-harness` is a 500+ star harness
  engineering list with an explicit contributing section and no existing
  DeepSeek Harness Handbook entry.
- **Action:** Opened issue #55 proposing the Handbook for its documentation /
  resources coverage:
  https://github.com/AutoJunjie/awesome-agent-harness/issues/55
- **Validation:** Linked the canonical Apache-2.0 repository and described its
  bilingual runtime, tool/sandbox/session, runbook, and troubleshooting scope;
  current direct count is 73 stars and 143 verified guides.
- **Distribution channel:** Curated Agent Harness engineering resource list.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A distinct, scope-relevant discovery proposal is open for
  maintainer review without manufactured engagement.
- **Next hypothesis:** Answer only concrete editorial or verification
  questions and stop if declined.

### 2026-08-28 — CLI verification follow-up in Doocs Awesome AI

- **Evidence:** Open issue #20 in `doocs/awesome-ai` proposes SandBase CLI and
  had no maintainer follow-up before this action.
- **Action:** Added a concise Chinese comment with official MCP Registry,
  v0.1.17 release/checksum, local bridge, 25 clients, and 2,000+ model/API
  evidence: https://github.com/doocs/awesome-ai/issues/20#issuecomment-5447232465
- **Validation:** Claims were matched to the canonical CLI README/release and
  the maintainer was left to decide inclusion under the directory's rules.
- **Distribution channel:** Chinese curated AI resources directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** An existing proposal now has reproducible review evidence without
  a duplicate thread or manufactured engagement.
- **Next hypothesis:** Wait for maintainer response and answer only concrete
  questions.

### 2026-08-28 — CLI Cursor directory follow-up

- **Evidence:** Open issue #54 in `hao-ji-xing/awesome-cursor` proposes SandBase
  CLI for its MCPs section and had no comments before this action.
- **Action:** Added a concise Chinese follow-up describing Cursor-compatible
  local MCP configuration, OAuth onboarding, diagnostics/rollback, and the
  v0.1.17 release/checksum:
  https://github.com/hao-ji-xing/awesome-cursor/issues/54#issuecomment-5447237434
- **Validation:** Rechecked the canonical CLI README/release and left the
  maintainer to make the inclusion decision.
- **Distribution channel:** Curated Cursor MCP resource list.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** The existing proposal now has practical, verifiable onboarding
  details without opening a duplicate thread.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  questions.

### 2026-08-28 — Skills/CLI evidence follow-up in Skillmatic index

- **Evidence:** Open issue #156 in `skillmatic-ai/awesome-agent-skills` proposes
  SandBase and had no maintainer comments; a prior PR path was not reused.
- **Action:** Added one factual follow-up linking the CLI local MCP bridge,
  OAuth, 25-client setup, v0.1.17 checksum, and the Skills repo's SKILL.md
  packages: https://github.com/skillmatic-ai/awesome-agent-skills/issues/156#issuecomment-5447247922
- **Validation:** Claims were checked against canonical public READMEs and the
  maintainer was left to decide the skills/tool boundary.
- **Distribution channel:** Curated Agent Skills index issue queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing proposal has updated, verifiable context without a
  duplicate thread or manufactured engagement.
- **Next hypothesis:** Wait for editorial review and answer only concrete
  questions.

### 2026-08-28 — SandBase Skills proposal to JackyST0 Agent Skills list

- **Evidence:** `JackyST0/awesome-agent-skills` is a 600+ star Chinese Agent
  Skills directory; its README contained no SandBase entry.
- **Action:** Opened issue #85 with a concise Chinese recommendation:
  https://github.com/JackyST0/awesome-agent-skills/issues/85
- **Validation:** Linked the canonical Apache-2.0 repository and described only
  its documented multi-source research, offline validation, and SKILL.md scope;
  current direct count is 68 stars.
- **Distribution channel:** Chinese curated Agent Skills directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A new, non-duplicative discovery proposal is open for maintainer
  review without manufactured engagement.
- **Next hypothesis:** Wait for editorial feedback and answer only concrete
  quality or compatibility questions.

### 2026-08-28 — CLI evidence follow-up in Awesome MCP List

- **Evidence:** `MobinX/awesome-mcp-list` is an 800+ star MCP directory; open
  issue #390 proposes SandBase CLI and had no comments before this action.
- **Action:** Added a concise Chinese follow-up with local MCP bridge, 25-client
  configuration, OAuth onboarding, v0.1.17 release, and SHA-256 evidence:
  https://github.com/MobinX/awesome-mcp-list/issues/390#issuecomment-5447268078
- **Validation:** Rechecked the canonical CLI README/release and left the
  maintainer to decide inclusion; no duplicate issue was created.
- **Distribution channel:** Curated MCP server list issue queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** The existing proposal now contains reproducible onboarding facts
  without manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — CLI evidence follow-up in DeepSeek integration list

- **Evidence:** Open issue #716 in `deepseek-ai/awesome-deepseek-integration`
  proposes SandBase CLI for provider discovery and had no comments before this
  action.
- **Action:** Added a factual follow-up linking the local MCP bridge, 25-client
  support, official Registry, v0.1.17 release, and SHA-256 verification:
  https://github.com/deepseek-ai/awesome-deepseek-integration/issues/716#issuecomment-5447272589
- **Validation:** Explicitly scoped DeepSeek availability to runtime account
  permissions and the official catalog; no unsupported availability claim was
  made.
- **Distribution channel:** DeepSeek ecosystem integration directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing proposal now has source-backed onboarding evidence
  without a duplicate thread or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — CLI OpenClaw directory follow-up

- **Evidence:** `alvinreal/awesome-openclaw` is a 700+ star OpenClaw resource
  list; open issue #75 proposes SandBase CLI and had no comments before this
  action.
- **Action:** Added a concise follow-up with OpenClaw configuration, local MCP
  bridge, OAuth onboarding, v0.1.17 release, and SHA-256 evidence:
  https://github.com/alvinreal/awesome-openclaw/issues/75#issuecomment-5447277239
- **Validation:** Rechecked the canonical CLI README/release and left the
  maintainer to make the inclusion decision; no duplicate issue was opened.
- **Distribution channel:** Curated OpenClaw/Agent resources directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing proposal now has reproducible integration evidence
  without manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — CLI MCP section follow-up in Awesome Generative AI

- **Evidence:** `filipecalegario/awesome-generative-ai` is a 3k+ star AI
  resource list; open issue #681 proposes SandBase CLI for its MCP section and
  had no comments before this action.
- **Action:** Added a concise follow-up with Apache-2.0, 25-client support,
  OAuth, official Registry, v0.1.17 release, and SHA-256 evidence:
  https://github.com/filipecalegario/awesome-generative-ai/issues/681#issuecomment-5447282375
- **Validation:** Rechecked the canonical CLI README/release and left the
  maintainer to decide inclusion; no duplicate thread was created.
- **Distribution channel:** Curated generative-AI resource directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing proposal now has source-backed onboarding evidence
  without manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — Multi-source-search index follow-up

- **Evidence:** `futantan/agent-skills.md` is a 200+ star skills index; open
  issue #25 requests indexing SandBase's `multi-source-search` skill and had no
  comments before this action.
- **Action:** Added the canonical skill-path URL, SKILL.md/offline-validation
  scope, and current 68-star count:
  https://github.com/futantan/agent-skills.md/issues/25#issuecomment-5447292309
- **Validation:** Linked the exact repository subdirectory and asked the
  maintainer to check link and compatibility independently.
- **Distribution channel:** Curated Agent Skills index issue queue.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing indexing request now has precise source evidence without
  duplicate threads or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — Skills evidence follow-up in n-skills

- **Evidence:** `numman-ali/n-skills` is a 1k+ star skills directory; open issue
  #46 proposes SandBase and had no comments before this action.
- **Action:** Added the exact `multi-source-search` SKILL.md path, offline
  validation scope, and related CLI MCP/OAuth context:
  https://github.com/numman-ali/n-skills/issues/46#issuecomment-5447297644
- **Validation:** Rechecked the canonical Skills/CLI repositories and left
  quality and inclusion decisions to the maintainer.
- **Distribution channel:** Curated Agent Skills directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing submission has precise, source-backed paths without
  duplicate threads or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  questions.

### 2026-08-28 — Skills evidence follow-up in Awesome LLM Skills

- **Evidence:** `Prat011/awesome-llm-skills` is a 1.6k+ star skills directory;
  open issue #222 proposes SandBase and had no comments before this action.
- **Action:** Added the exact `multi-source-search` path, SKILL.md/offline
  validation scope, and local MCP bridge context:
  https://github.com/Prat011/awesome-llm-skills/issues/222#issuecomment-5447301561
- **Validation:** Rechecked canonical Skills/CLI repositories and left the
  maintainer to decide inclusion under its quality criteria.
- **Distribution channel:** Curated LLM/Agent Skills directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing proposal now has precise source evidence without a
  duplicate thread or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — Skills submission follow-up in Agent Skills Hub

- **Evidence:** `zhuyansen/agent-skills-hub` is a 300+ star skills directory;
  open issue #15 requests the SandBase repository and had no comments before
  this action.
- **Action:** Added the canonical `multi-source-search` path, SKILL.md,
  offline-validation scope, and current 68-star count:
  https://github.com/zhuyansen/agent-skills-hub/issues/15#issuecomment-5447305658
- **Validation:** Rechecked the public Skills repository and left inclusion to
  the maintainer's quality review; no duplicate issue was created.
- **Distribution channel:** Curated Agent Skills Hub.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing submission has precise, source-backed metadata without
  manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — SandBase Docs quickstart announcement

- **Evidence:** `sandbaseai/sandbase-docs` has Discussions enabled with an
  Announcements category; the docs now expose a consolidated Getting Started
  path for client/MCP setup and API references.
- **Action:** Published announcement #13 with the canonical quickstart URL and
  a reproducible issue-reporting prompt:
  https://github.com/sandbaseai/sandbase-docs/discussions/13
- **Validation:** Confirmed the discussion was created in the official Docs
  repository and linked only the public docs site; no external engagement was
  fabricated.
- **Distribution channel:** Official SandBase Docs Discussions / Announcements.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Added a durable, searchable onboarding touchpoint for developers
  discovering the Docs repository.
- **Next hypothesis:** Answer concrete setup questions with reproducible steps
  and link back to the canonical quickstart.

### 2026-08-28 — CLI Claude Code directory follow-up

- **Evidence:** `jqueryscript/awesome-claude-code` is a 500+ star Claude Code
  resource list; open issue #624 proposes SandBase CLI and had no comments
  before this action.
- **Action:** Added a concise follow-up with Claude Code local MCP setup, OAuth,
  v0.1.17 release/checksum, and 25-client scope:
  https://github.com/jqueryscript/awesome-claude-code/issues/624#issuecomment-5447318236
- **Validation:** Rechecked the canonical CLI README/release and left the
  maintainer to decide inclusion; no duplicate issue was opened.
- **Distribution channel:** Curated Claude Code tools directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing proposal now contains practical, source-backed
  onboarding evidence without manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — Skills Codex directory follow-up

- **Evidence:** `composio-community/awesome-codex-skills` is a 16k+ star Codex
  skills directory; open issue #244 proposes SandBase and had no comments
  before this action.
- **Action:** Added a concise follow-up with the canonical `multi-source-search`
  path, SKILL.md/offline-validation scope, and CLI MCP/OAuth context:
  https://github.com/composio-community/awesome-codex-skills/issues/244#issuecomment-5447323267
- **Validation:** Rechecked the public Skills/CLI repositories and left
  inclusion to the directory's quality and compatibility review.
- **Distribution channel:** Curated Codex skills directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing submission now has precise, source-backed Codex context
  without a duplicate thread or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — Skills import verification in Agentic Awesome Skills

- **Evidence:** `sickn33/agentic-awesome-skills` is a 45k+ star skills
  directory; open request #1270 asks to import the reviewed SandBase MCP skill
  and had no comments before this action.
- **Action:** Added canonical repository and `multi-source-search` path,
  SKILL.md/offline-validation scope, and the CLI local MCP bridge context:
  https://github.com/sickn33/agentic-awesome-skills/issues/1270#issuecomment-5447328193
- **Validation:** Rechecked the public Skills/CLI repositories and left the
  import decision to the directory maintainers.
- **Distribution channel:** Curated Agentic Awesome Skills index.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** A high-reach existing request now has precise source evidence
  without duplicate threads or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  verification questions.

### 2026-08-28 — SandBase Skills usage discussion

- **Evidence:** `sandbaseai/sandbase-skills` has Discussions enabled with a
  Q&A category; a user-focused prompt can collect reproducible usage feedback
  without making adoption claims.
- **Action:** Published Q&A discussion #61 asking users to share client,
  research task, and validation outcomes for `multi-source-search`:
  https://github.com/sandbaseai/sandbase-skills/discussions/61
- **Validation:** Linked the canonical skill path and explicitly requested
  concrete examples or reproducible issues rather than promotional replies.
- **Distribution channel:** Official Skills Discussions / Q&A.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Created a durable feedback and discovery entry point for real
  users of the Skills repository.
- **Next hypothesis:** Respond to actual usage reports and use them to improve
  documentation or compatibility.

### 2026-08-28 — SandBase CLI client setup clinic

- **Evidence:** `sandbaseai/cli` has Discussions enabled with a Q&A category;
  client/version and OS reports can produce useful, reproducible compatibility
  feedback.
- **Action:** Published discussion #56 inviting users to share redacted setup
  results for supported MCP clients and linking verified release instructions:
  https://github.com/sandbaseai/cli/discussions/56
- **Validation:** Included the canonical installation/checksum README section,
  requested secrets be redacted, and asked for exact versions/commands.
- **Distribution channel:** Official CLI Discussions / Q&A.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Added a durable technical feedback and discovery touchpoint for
  real CLI users.
- **Next hypothesis:** Use actual reports to improve client compatibility and
  documentation; do not manufacture replies.

### 2026-08-28 — Handbook implementation-start announcement

- **Evidence:** `sandbaseai/deepseek-harness-handbook` has Discussions enabled
  with an Announcements category; its bilingual README provides implementation
  coverage of runtime, tools, sandbox, sessions, runbooks, and troubleshooting.
- **Action:** Published announcement #248 with a durable “Start here” guide
  index and a request for reproducible user context:
  https://github.com/sandbaseai/deepseek-harness-handbook/discussions/248
- **Validation:** Linked the canonical README and asked contributors to share
  runtime/client details rather than making adoption claims.
- **Distribution channel:** Official Handbook Discussions / Announcements.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Added a searchable onboarding touchpoint for Agent builders and
  a path for real implementation feedback.
- **Next hypothesis:** Answer concrete workflow questions and incorporate
  reproducible feedback into the handbook.

### 2026-08-28 — Skills worked-example showcase

- **Evidence:** `sandbaseai/sandbase-skills` Discussions provides a Show and
  tell category; a concrete workflow is more useful to prospective users than
  a generic promotional claim.
- **Action:** Published discussion #62 with a four-step reproducible
  `multi-source-search` workflow and a request for redacted client/task/
  validation reports: https://github.com/sandbaseai/sandbase-skills/discussions/62
- **Validation:** Linked the canonical skill path, required source/uncertainty
  recording and offline validation, and asked users to review evidence before
  downstream use.
- **Distribution channel:** Official Skills Discussions / Show and tell.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Added a practical discovery and onboarding artifact for real
  users, without manufactured replies or star claims.
- **Next hypothesis:** Use genuine user reports to refine examples and
  documentation.

### 2026-08-29 — CLI listing verification in Awesome AI Agents 2026

- **Evidence:** `ARUNAGIRINATHAN-K/awesome-ai-agents-2026` is a 300+ star AI
  agents directory; open issue #235 requests an update to the SandBase CLI
  listing and had no comments before this action.
- **Action:** Added a factual follow-up with the local MCP bridge, 25 clients,
  v0.1.17 release, SHA-256, and official Registry links, while scoping model
  availability to runtime permissions:
  https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026/issues/235#issuecomment-5450152545
- **Validation:** Rechecked the canonical CLI README/release and avoided
  unsupported model-count claims.
- **Distribution channel:** Curated AI agents directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing listing request now has source-backed update details
  without duplicate threads or manufactured engagement.
- **Next hypothesis:** Wait for maintainer review and answer only concrete
  follow-up questions.

### 2026-08-28 — External review state update

- **Evidence:** `awesome-ai-devtools#33` remains open with CI passing and a
  second maintainer-facing metadata clarification; `sickn33/agentic-awesome-skills#1270`
  is now closed.
- **Action:** Preserved the factual release/checksum, Apache-2.0, 25-client,
  and six-tool MCP evidence in the open PR discussion; stopped follow-up on the
  closed skills request.
- **Validation:** GitHub API confirms PR #33 is unmerged/open and issue #1270
  is closed; no Star movement is attributed.
- **Distribution channel:** AI developer-tools PR review and Agent Skills index.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Open review has current source evidence; closed request is not
  reposted, preserving an accurate outreach history.
- **Next hypothesis:** Respond only to new maintainer requests and record the
  closure reason if GitHub exposes one.

### 2026-08-29 — AI Devtools PR validation response

- **Evidence:** `yeaight7/awesome-ai-devtools#33` remains open; the repository
  bot requested confirmation that metadata uses official sources and that the
  sort/generate/test gates pass.
- **Action:** Replied with the exact passing commands (`npm run sort`,
  `npm run generate`, `npm test` 59/59, `npm run validate`, `git diff --check`)
  and official-source attribution:
  https://github.com/yeaight7/awesome-ai-devtools/pull/33#issuecomment-5450174805
- **Validation:** The checks had already passed locally and the PR remains
  unmerged; no unsupported claim or duplicate PR was made.
- **Distribution channel:** Curated AI developer-tools catalog review.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Addressed the bot's concrete review request with reproducible
  validation evidence.
- **Next hypothesis:** Wait for human review or requested changes; do not add
  further comments unless asked.

### 2026-08-29 — CLI listing follow-up in Awesome CLI Apps

- **Evidence:** `toolleeo/awesome-cli-apps-in-a-csv` is a 2.5k+ star CLI
  directory; open issue #375 proposes SandBase CLI and had no comments before
  this action.
- **Action:** Added a concise follow-up with Apache-2.0, 25-client setup,
  OAuth, v0.1.17 release/checksum, and official MCP Registry evidence:
  https://github.com/toolleeo/awesome-cli-apps-in-a-csv/issues/375#issuecomment-5450187127
- **Validation:** Rechecked canonical CLI sources and left field mapping and
  inclusion to the maintainer; no duplicate issue was created.
- **Distribution channel:** Curated CLI applications directory.
- **Star count before/after:** Skills 68→68; CLI 61→61; Handbook 73→73;
  Docs 1→1; no causal attribution.
- **Result:** Existing listing request now has source-backed metadata for review
  without manufactured engagement.
- **Next hypothesis:** Wait for maintainer feedback and answer only concrete
  data-field questions.

### 2026-08-29 — Organic Star movement checkpoint

- **Evidence:** Direct GitHub API verification shows Skills 69, CLI 66,
  Handbook 74, and Docs 1 stars; the prior checkpoint was 68 / 61 / 73 / 1.
- **Action:** Recorded the observed movement without attributing it to any
  single comment, issue, or PR.
- **Validation:** Counts were queried directly from the four canonical GitHub
  repositories at the same checkpoint; no synthetic accounts or automation were
  used.
- **Distribution channel:** Cross-channel promotion ledger checkpoint.
- **Star count before/after:** Skills 68→69; CLI 61→66; Handbook 73→74;
  Docs 1→1; causal attribution unknown.
- **Result:** Three projects gained organic Stars, while Docs was unchanged;
  none has reached the 100-Star target yet.
- **Next hypothesis:** Continue only evidence-based outreach and recheck after
  genuine maintainer/user activity, without claiming causality.

### 2026-08-28 — Remove unused third-party forks

- **Objective:** Reduce organization clutter without touching canonical SandBase
  projects or external contributors' personal repositories.
- **Evidence:** Direct GitHub organization API showed 49 repositories with
  `fork=true`; each was an `awesome-*` third-party copy with 0 Stars and 0
  open issues, created or pushed in the current batch window.
- **Action:** Deleted the 49 identified repositories from the `sandbaseai`
  organization with explicit per-repository delete commands.
- **Validation:** Re-queried the organization API after deletion; remaining
  organization Fork count is 0. The four in-scope canonical repositories were
  not modified.
- **Distribution channel:** Repository hygiene; no Star or engagement claim.
- **Star count before/after:** Skills 72→72; CLI 66→66; Handbook 77→77;
  Docs 1→1.
- **Result:** Cleanup complete; deleted GitHub repositories are not readily
  self-service recoverable.
- **Next hypothesis:** Focus subsequent promotion on existing maintainer-owned
  listings and user-facing documentation rather than creating additional forks.

### 2026-08-28 — Docs community use-case request

- **Objective:** Create a genuine feedback loop for the lowest-discovery
  project, `sandbase-docs`, rather than manufacturing engagement.
- **Action:** Opened [Docs issue #14](https://github.com/sandbaseai/sandbase-docs/issues/14)
  requesting redacted, reproducible LLM/image/video/embedding/agent examples
  from users.
- **Validation:** GitHub returned the live issue URL; the body explicitly asks
  contributors not to share credentials and will turn validated examples into
  documentation improvements.
- **Distribution channel:** Project issue tracker; no Star request or causal
  Star claim.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Published and awaiting community responses.
- **Next hypothesis:** Convert the first validated response into a focused
  docs PR and link it back to the issue.

### 2026-08-28 — Awesome AI Devtools listing merged

- **Objective:** Earn durable discovery for the CLI through a maintainer-owned
  catalog with a real review process.
- **Evidence:** `yeaight7/awesome-ai-devtools#33` was merged after the maintainer
  requested official-source confirmation and passing sort/generate/test gates.
- **Action:** Supplied the requested provenance and validation details; the PR
  now appears in the merged project history.
- **Validation:** Maintainer bot review recorded the required checks; GitHub
  reports the PR state as `MERGED`.
- **Distribution channel:** Curated AI developer-tools catalog.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** Permanent third-party listing obtained without duplicate PRs or
  manufactured engagement.
- **Next hypothesis:** Use the merged listing as a reference when answering
  relevant user questions, and pursue only new maintainer-led opportunities.

### 2026-08-28 — Additional curated listings merged

- **Objective:** Expand durable discovery for CLI and Harness projects through
  maintainer-owned directories.
- **Evidence:** GitHub merged [`michielhdoteth/awesome-ai-agent-tools#23`](https://github.com/michielhdoteth/awesome-ai-agent-tools/pull/23)
  (SandBase CLI MCP server) and [`milisp/awesome-codex-cli#110`](https://github.com/milisp/awesome-codex-cli/pull/110)
  (SandBase CLI MCP bridge).
- **Validation:** GitHub Search API reports both PRs as merged; links resolve to
  the external repositories' histories.
- **Distribution channel:** Curated AI-agent and Codex CLI directories.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** Two additional third-party listings are live.
- **Next hypothesis:** Maintain accurate release metadata in each listing and
  only update when a maintainer or release changes it.

### 2026-08-28 — MCP ecosystem listing and reviewed tutorial merged

- **Objective:** Add durable discovery paths for the CLI beyond repeated social
  mentions.
- **Evidence:** [`awesome-agent-cortex#72`](https://github.com/0xNyk/awesome-agent-cortex/pull/72)
  was merged with a SandBase CLI MCP ecosystem entry; the reviewed
  [SandBase Blog PR #261](https://github.com/sandbaseai/sandbase-blog/pull/261)
  was also merged for a developer tutorial.
- **Validation:** GitHub PR metadata reports both states as `MERGED` with live
  links; no Star increase is attributed to either action.
- **Distribution channel:** Third-party MCP directory and first-party
  developer tutorial.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Two additional evidence-backed discovery assets are live.
- **Next hypothesis:** Keep tutorial commands aligned with the immutable CLI
  release and answer only concrete reader questions.

### 2026-08-28 — Maintainer-friendly follow-up on AI tools recommendation

- **Objective:** Keep a pending third-party recommendation actionable without
  repeated promotional comments.
- **Action:** Added one concise follow-up to
  [`Awesome-AITools#896`](https://github.com/ikaijua/Awesome-AITools/issues/896#issuecomment-5452538524),
  confirming template compliance and inviting maintainers to request missing
  fields or recategorization.
- **Validation:** GitHub returned the live comment URL; no Star request,
  unsupported claim, or sensitive data was included.
- **Distribution channel:** Maintainer-reviewed AI tools directory.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Pending recommendation remains easy for maintainers to process.
- **Next hypothesis:** Do not comment again unless the maintainer asks for
  changes or closes the issue.

### 2026-08-28 — Docs README discovery CTA shipped

- **Objective:** Improve conversion from documentation readers to durable GitHub
  discovery and useful community feedback.
- **Action:** Added a concise, non-incentivized README call to action linking to
  the Docs Star page and redacted-example issue tracker.
- **Validation:** Change was rebased onto the latest `main` and pushed at
  commit `0ce1f78`; links target canonical GitHub pages.
- **Distribution channel:** `sandbase-docs` README / organic documentation
  traffic.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Live README now offers a clear feedback and discovery path.
- **Next hypothesis:** Use responses from the linked issue tracker to improve
  examples; do not attribute Stars without referral evidence.

### 2026-08-28 — Skills directory listings verified

- **Objective:** Improve durable discovery for `sandbase-skills` through
  maintainer-owned directories relevant to Agent Skills.
- **Evidence:** GitHub search found merged listings in
  [awesome-dsh-plugin#48](https://github.com/Anil-matcha/awesome-dsh-plugin/pull/48),
  [awesome-agent-skills#39](https://github.com/junminhong/awesome-agent-skills/pull/39),
  [Agents Skill Exchange#49](https://github.com/agentskillexchange/skills/pull/49),
  and [VoltAgent/awesome-agent-skills#946](https://github.com/VoltAgent/awesome-agent-skills/pull/946).
- **Validation:** GitHub Search API reports each PR as merged; links resolve to
  the external repositories' histories.
- **Distribution channel:** Curated Agent Skills registries and directories.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** Four third-party, maintainer-reviewed discovery paths are live.
- **Next hypothesis:** Keep the flagship Skill metadata and install commands
  synchronized with releases; avoid duplicate submissions.

### 2026-08-28 — Additional Skills marketplace listings verified

- **Objective:** Extend durable discovery for Skills and the Harness handbook
  through relevant maintained catalogs.
- **Evidence:** Verified merged PRs in [awesome-dsh-plugin#89](https://github.com/beancookie/awesome-dsh-plugin/pull/89),
  [awesome-dsh-plugin#1883](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin/pull/1883),
  [aiskillstore/marketplace#3198](https://github.com/aiskillstore/marketplace/pull/3198),
  and [awesome-deepseek-harness#141](https://github.com/0xsline/awesome-deepseek-harness/pull/141).
- **Validation:** GitHub PR metadata reports each as `MERGED`; links resolve to
  the external project histories.
- **Distribution channel:** Agent Skills marketplaces and DeepSeek Harness
  resource directory.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** Four more maintainer-reviewed listings are live.
- **Next hypothesis:** Keep marketplace metadata current and respond only to
  actual maintainer requests.

### 2026-08-28 — CLI ecosystem listings verified (batch 2)

- **Objective:** Broaden CLI discovery across established MCP, Gemini, AI-tools,
  and Chinese developer directories.
- **Evidence:** Verified merged PRs: [awesome-gemini-cli#99](https://github.com/Piebald-AI/awesome-gemini-cli/pull/99),
  [Awesome-MCP-Server#70](https://github.com/AIAnytime/Awesome-MCP-Server/pull/70),
  [TensorBlock/awesome-mcp-servers#1835](https://github.com/TensorBlock/awesome-mcp-servers/pull/1835),
  [awesome-ai-tools#232](https://github.com/QAInsights/awesome-ai-tools/pull/232),
  [chinese-independent-developer#1287](https://github.com/1c7/chinese-independent-developer/pull/1287),
  and [Awesome-MCP#27](https://github.com/Albertchamberlain/Awesome-MCP/pull/27).
- **Validation:** GitHub PR metadata reports all six as `MERGED`; URLs resolve
  to the external histories.
- **Distribution channel:** Maintainer-curated ecosystem directories.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** Six additional long-lived CLI discovery paths are live.
- **Next hypothesis:** Keep release version and security claims synchronized;
  do not submit duplicate entries to the same directory.

### 2026-08-28 — Handbook entry in 200-Star DSH directory

- **Objective:** Increase durable discovery for the DeepSeek Harness Handbook
  through a focused community-maintained resource list.
- **Evidence:** [Dominic789654/awesome-deepseek-harness#26](https://github.com/Dominic789654/awesome-deepseek-harness/pull/26)
  is merged; the directory currently has 204 GitHub Stars and explicitly
  curates DSH plugins, skills, MCP servers, and operator resources.
- **Validation:** GitHub API reports the PR as `MERGED` and the directory's
  current Star count as 204.
- **Distribution channel:** Focused DeepSeek Harness ecosystem directory.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** Handbook has a relevant, maintainer-reviewed listing in a
  substantive community directory.
- **Next hypothesis:** Keep the listing aligned with handbook releases and
  avoid duplicate submissions to the same directory.

### 2026-08-28 — Docs GitHub topic discovery refresh

- **Objective:** Improve organic discovery for `sandbase-docs` in GitHub search.
- **Action:** Added accurate topics `ai-api`, `api-documentation`,
  `developer-docs`, and `openai-compatible` while retaining existing project
  topics via the GitHub Topics API.
- **Validation:** GitHub API returned the complete updated topic list.
- **Distribution channel:** GitHub repository search and topic pages.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Docs now has explicit search terms matching its API and
  documentation scope; no Star increase is attributed.
- **Next hypothesis:** Measure discovery through genuine issue/referral signals
  before adding further metadata.

### 2026-08-28 — Skills and Handbook topic discovery refresh

- **Objective:** Improve GitHub-native discovery for the two agent-focused
  repositories using terms developers actually search.
- **Action:** Replaced low-signal topics within GitHub's 20-topic limit with
  `agent-skills-marketplace`, `ai-workflows`, `research-automation`,
  `ai-coding-assistant`, and `developer-documentation` while preserving the
  core ecosystem topics.
- **Validation:** GitHub Topics API returned exactly 20 topics for each
  repository after the update.
- **Distribution channel:** GitHub search and topic pages.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Search metadata now better matches Skills workflows and Handbook
  operator documentation; no Star increase is attributed.
- **Next hypothesis:** Avoid further topic churn unless search terminology or
  project scope materially changes.

### 2026-08-28 — CLI README cross-links community directories

- **Objective:** Turn third-party directory exposure into a visible, useful
  discovery path from the canonical CLI repository.
- **Action:** Added links to the merged Awesome Agent Cortex, Awesome AI Agent
  Tools, and Awesome Codex CLI directories in the CLI README Community section.
- **Validation:** Change was rebased onto latest `main` and pushed at commit
  `00f144a`; links point to the named external repositories.
- **Distribution channel:** CLI README cross-navigation.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** Visitors can discover independently maintained ecosystem listings
  without leaving the canonical project context.
- **Next hypothesis:** Keep this list limited to maintained, merged listings.

### 2026-08-28 — Skills and CLI listings in large agent directories

- **Objective:** Expand durable discovery through high-reach, maintainer-owned
  agent catalogs.
- **Evidence:** [agentic-awesome-skills#1279](https://github.com/sickn33/agentic-awesome-skills/pull/1279)
  merged a SandBase MCP Skill entry; that directory currently has 45k+ Stars.
  [awesome-hermes-agent#364](https://github.com/0xNyk/awesome-hermes-agent/pull/364)
  also merged a correction to the SandBase CLI listing.
- **Validation:** GitHub PR metadata reports both as `MERGED`; directory Star
  count was queried directly for the reach context.
- **Distribution channel:** Agent Skills and Hermes Agent ecosystem catalogs.
- **Star count at checkpoint:** Skills 72; CLI 66; Handbook 77; Docs 1;
  no causal Star increase is claimed.
- **Result:** One high-reach Skills listing and one accuracy-maintenance CLI
  listing are live.
- **Next hypothesis:** Preserve factual metadata and let directory maintainers
  control future updates.

### 2026-08-28 — Final maintainer follow-up for Skills PR

- **Objective:** Keep the high-reach Skills listing actionable without repeated
  promotion.
- **Action:** Sent one concise follow-up on
  [`awesome-claude-skills#1758`](https://github.com/ComposioHQ/awesome-claude-skills/pull/1758#issuecomment-5452648642),
  confirming green validation/security checks and offering wording/category
  changes.
- **Validation:** GitHub returned the live comment URL; no Star request or
  unsupported claim was added.
- **Distribution channel:** Maintainer-reviewed Claude Skills directory.
- **Star count at action:** Skills 72; CLI 66; Handbook 77; Docs 1.
- **Result:** One final actionable reminder sent; no further follow-ups planned
  unless the maintainer responds.
- **Next hypothesis:** Let the directory's normal review queue decide inclusion.

### 2026-08-30 — Personal promotion Fork cleanup

- **Objective:** Remove clearly temporary external-project Forks created for
  promotion work while preserving long-lived technical Forks.
- **Evidence:** Audited Forks under `denial123789` and `liyangbing`; selected
  only 2026 promotion-batch repositories with zero Stars/issues.
- **Action:** Deleted 12 explicit temporary Forks under `denial123789`.
  Eleven analogous Forks under `liyangbing` remain because the active token
  lacks `delete_repo` administration permission (GitHub returned HTTP 403).
- **Validation:** Re-queried both accounts; no selected `denial123789` Forks
  remain. Historical 2013–2025 technical Forks were not touched.
- **Result:** Cleanup is partial and permission-bounded; no permission bypass
  was attempted.
- **Next action:** If desired, run the same explicit deletes while authenticated
  as an account with repository-delete permission for `liyangbing`.

### 2026-08-30 — Complete remaining temporary Fork cleanup

- **Objective:** Finish removal of the explicitly identified 2026 promotion
  Fork batch after repository-delete authorization was granted.
- **Action:** Authenticated `liyangbing` with the approved `delete_repo` scope
  and deleted the 11 remaining temporary Forks listed in the prior audit.
- **Validation:** Re-queried `users/liyangbing/repos`; zero Forks remain from
  the 2026 promotion batch. Historical technical Forks were not targeted.
- **Result:** The scoped external-project Fork cleanup is complete.
- **Recoverability:** GitHub repository deletion is not self-service
  recoverable; no other repositories were removed.

## Recording rules

For every later action, record the timestamp, repository, objective, source
problem, exact implementation/PR or release URL, validation, distribution
channel, direct star count before and after, observed referral or engagement,
deployment state, result, and the next hypothesis. Never buy, trade, automate,
or manufacture stars, followers, comments, issues, forks, or contributors.
### 2026-08-31 — Awesome MCP Collection review path

- **Objective:** Add a relevant, maintainer-controlled MCP directory review path
  for SandBase Harness.
- **Action:** Prepared a source-linked entry in the Development & Version
  Control table and opened
  [JustInCache/awesome-mcp-collection#39](https://github.com/JustInCache/awesome-mcp-collection/pull/39).
- **Validation:** The PR contains one README table row, follows the required
  name/repository/stars/language/description format, and GitHub reports it
  `OPEN` and `MERGEABLE` with no reported checks at submission time.
- **Distribution channel:** GitHub directory review; corresponding social
  drafts are marked `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** Directory inclusion is not endorsement or security
  certification; isolation remains deployment-dependent.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer review the focused entry before any
  follow-up; avoid duplicate submissions to overlapping directories.

### 2026-08-31 — Awesome MCP issue review path

- **Objective:** Add a relevant MCP gateway/runtime discovery path without
  creating a duplicate or invalid PR.
- **Action:** Opened [abordage/awesome-mcp#99](https://github.com/abordage/awesome-mcp/issues/99)
  using the repository's public issue workflow after the existing personal fork
  was found to have no comparable upstream history.
- **Validation:** The issue contains one factual entry for Aggregators &
  Gateways and links the canonical repository; the request is pending review.
- **Distribution channel:** GitHub directory issue; corresponding social drafts
  are marked `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No directory endorsement or security certification is claimed;
  isolation remains deployment-dependent.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer decide whether the entry fits the
  directory's gateway scope; do not retry the broken fork path.

### 2026-08-31 — Awesome MCP Gateways review path

- **Objective:** Add a high-relevance, criteria-based MCP gateway discovery
  path.
- **Action:** Opened [e2b-dev/awesome-mcp-gateways#81](https://github.com/e2b-dev/awesome-mcp-gateways/pull/81)
  under Open-source MCP Gateways.
- **Validation:** SandBase currently has 639 GitHub stars and 4 contributors,
  meeting the destination's stated 200-star / 2-contributor threshold. The PR
  changes one README line; GitHub reports `MERGEABLE`, while
  `verification/cla-signed` has not concluded.
- **Distribution channel:** GitHub gateway directory review; corresponding
  social drafts are marked `NEEDS REVIEW` and require operator/account
  authorization.
- **Boundary:** No directory endorsement or security certification is claimed;
  isolation remains deployment-dependent.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the destination maintainer resolve the CLA check and
  review the factual one-line entry before any follow-up.

### 2026-08-31 — Duplicate gateway submission correction

- **Objective:** Keep the gateway promotion queue limited to the canonical
  maintainer review path.
- **Action:** Closed duplicate [e2b-dev/awesome-mcp-gateways#81](https://github.com/e2b-dev/awesome-mcp-gateways/pull/81)
  and corrected the social drafts to reference the earlier [PR #77](https://github.com/e2b-dev/awesome-mcp-gateways/pull/77).
- **Validation:** GitHub reports #81 `CLOSED`; #77 remains `OPEN` and
  `MERGEABLE` with its CLA check unresolved.
- **Result:** No duplicate gateway submission remains in the active promotion
  copy; no social publication was performed.

### 2026-08-31 — Awesome AI Harness review path

- **Objective:** Reach a bilingual harness-engineering audience with a
  runtime-focused, source-backed entry.
- **Action:** Opened [weiwei966/awesome-ai-harness#4](https://github.com/weiwei966/awesome-ai-harness/pull/4)
  in the SDKs & runtimes section.
- **Validation:** The one-line entry describes session state, governed MCP
  tools, approvals, credential scoping, audit/replay, and selectable backends;
  GitHub reports `OPEN` and `MERGEABLE` with no reported checks.
- **Distribution channel:** GitHub bilingual harness directory; corresponding
  social drafts are marked `NEEDS REVIEW` and require operator/account
  authorization.
- **Boundary:** No directory endorsement or security certification is claimed;
  isolation remains deployment-dependent.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer review the specific harness-design
  entry before any follow-up.

### 2026-08-31 — Awesome AI Coding Sandboxes review path

- **Objective:** Reach a security-posture-focused sandbox directory without
  overstating SandBase's isolation guarantees.
- **Action:** Opened [fhiltscher/awesome-ai-coding-sandboxes#15](https://github.com/fhiltscher/awesome-ai-coding-sandboxes/pull/15)
  in the Adjacent section.
- **Validation:** The README-only PR contains one entry and explicitly says
  isolation depends on the provider; GitHub reports `OPEN` and `MERGEABLE`
  with no reported checks.
- **Distribution channel:** GitHub sandbox directory review; corresponding
  social drafts are marked `NEEDS REVIEW` and require operator/account
  authorization.
- **Boundary:** No directory endorsement or security certification is claimed;
  SandBase is not presented as a standalone isolation engine.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer review the adjacent-runtime fit and
  matrix placement before any follow-up.

### 2026-08-31 — Awesome Agent Harnesses suggestion

- **Objective:** Reach a directory dedicated to production agent harnesses with a source-backed runtime entry.
- **Action:** Opened [NeuraLiying/Awesome-Agent-Harnesses issue #4](https://github.com/NeuraLiying/Awesome-Agent-Harnesses/issues/4) because the repository does not grant external push access.
- **Validation:** The suggestion follows the destination's table format and links the canonical repository, installation guide, harness design, and sandbox backend documentation. The request is pending maintainer review.
- **Distribution channel:** GitHub directory issue; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No directory listing, endorsement, or security certification is claimed; isolation remains dependent on the selected backend and deployment.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer decide whether the shipped runtime meets the directory's production-harness criteria; do not retry the unavailable push path.

### 2026-08-31 — mcp.so MCP-server intake

- **Objective:** Submit the current MCP bridge to a high-visibility public MCP directory using its documented community intake.
- **Action:** Commented on [chatmcp/mcpso issue #1](https://github.com/chatmcp/mcpso/issues/1#issuecomment-5472364196) with the canonical repository, installation guide, MCP server ID, v0.3.8 OCI image, and runtime description.
- **Validation:** The submission uses the thread's requested link-based format and preserves the backend/deployment-dependent isolation qualification; directory processing remains pending.
- **Distribution channel:** GitHub MCP directory intake; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No public listing, endorsement, or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Allow the directory's maintainers and indexing process to evaluate the submission; do not duplicate the comment.

### 2026-08-31 — HKUST-KnowComp Awesome Agent Harness scope review

- **Objective:** Reach a research-and-engineering-focused Agent Harness survey with a source-backed runtime resource.
- **Action:** Opened [HKUST-KnowComp/Awesome-Agent-Harness issue #8](https://github.com/HKUST-KnowComp/Awesome-Agent-Harness/issues/8), suggesting Tool Use & Code Execution or Sandboxing & Execution Environments placement.
- **Validation:** The proposal links the canonical repository, installation, harness-design, and sandbox-backend documentation and explicitly distinguishes the runtime from a paper or security certification. Curator scope review is pending.
- **Distribution channel:** GitHub survey issue; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No listing, endorsement, or security certification is claimed; isolation remains dependent on the selected backend and deployment.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the survey maintainers decide whether an open-source runtime resource fits their taxonomy; do not duplicate the scope request.

### 2026-08-31 — Picrew Awesome Agent Harness conflict resolution

- **Objective:** Keep the high-visibility Harness directory review path mergeable and easy for its maintainer to assess.
- **Action:** Merged the destination's latest `main` into [Picrew PR #86](https://github.com/Picrew/awesome-agent-harness/pull/86), regenerated `README.md`, `README_zh.md`, and the verification report, then pushed the conflict resolution.
- **Validation:** GitHub now reports the PR `OPEN`, `MERGEABLE`, and `CLEAN`; the verifier's 2 stale entries and 1 external OpenReview 403 are unrelated baseline findings.
- **Distribution channel:** Existing GitHub PR maintenance; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No directory endorsement or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the Picrew maintainer review the clean, regenerated diff; no further conflict push is needed unless the base changes again.

### 2026-08-31 — Awesome Agent Operating Systems listing confirmed

- **Objective:** Keep public promotion records aligned with actual directory outcomes.
- **Action:** Verified that [frankxai/awesome-agent-operating-systems PR #13](https://github.com/frankxai/awesome-agent-operating-systems/pull/13) merged SandBase Harness into Agent Runtimes; PR #11 was superseded and closed.
- **Validation:** GitHub reports #13 `MERGED` at commit `865643a`; the public directory entry and dated verification link are now the authoritative path.
- **Distribution channel:** Existing community listing; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** A directory listing is not an endorsement or security certification.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Keep future references on merged PR #13 and stop mentioning superseded PR #11.

### 2026-08-31 — TensorChord Awesome LLMOps review path

- **Objective:** Reach a high-visibility LLMOps catalog with a source-backed self-hosted agent runtime entry.
- **Action:** Opened [TensorChord Awesome LLMOps PR #785](https://github.com/tensorchord/Awesome-LLMOps/pull/785) using the directory's single-project contribution format and alphabetical table placement.
- **Validation:** The entry links the canonical repository and describes MCP, persistent sessions, governed execution, credentials, approvals, audit/replay, and selectable backends. GitHub reports `OPEN / MERGEABLE`; the DCO check is `ACTION_REQUIRED` and contributor-owned.
- **Distribution channel:** GitHub LLMOps directory review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** Backend/deployment-dependent isolation is explicit; no listing, endorsement, or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the contributor account holder complete DCO and let the LLMOps maintainer review the focused entry; do not bypass the DCO gate.

### 2026-08-31 — TensorChord Awesome LLMOps DCO follow-up

- **Objective:** Keep the LLMOps promotion path accurate after its contribution gate changes.
- **Action:** Added the required Signed-off-by line to the contributor-owned PR commit and pushed the amended commit; no entry content changed.
- **Validation:** GitHub now reports the DCO check `SUCCESS`; PR #785 remains under maintainer review.
- **Distribution channel:** Existing GitHub LLMOps review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No listing, endorsement, or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer review the now-unblocked PR; do not repeat the DCO update.

### 2026-08-31 — Awesome AI Agents 2026 link-check follow-up

- **Objective:** Keep a promotion PR's failed check accurately scoped and actionable.
- **Action:** Inspected the failed Lychee run for [PR #240](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026/pull/240) and posted the finding to the PR.
- **Validation:** The only error is a pre-existing 404 for `ofekron/better-agent` outside the SandBase diff; awesome-lint, GitGuardian, and the changed entry's canonical link pass.
- **Distribution channel:** Existing GitHub directory review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** No directory endorsement or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the destination maintainer fix or waive the unrelated baseline link; do not modify unrelated repository content from this PR.

### 2026-08-31 — Awesome-LLMSecOps Agentic security review path

- **Objective:** Reach a security-operations audience with a narrowly scoped, source-backed runtime entry.
- **Action:** Opened [Awesome-LLMSecOps PR #66](https://github.com/wearetyomsmnv/Awesome-LLMSecOps/pull/66) under the destination's Agentic security table.
- **Validation:** The one-row change links the canonical SandBase repository and documents sandboxed tools, credential boundaries, policy controls, audit logs, event replay, and the MCP bridge. GitHub reports the PR `OPEN / MERGEABLE / CLEAN`; no automated checks are reported. A verification note is [recorded on the PR](https://github.com/wearetyomsmnv/Awesome-LLMSecOps/pull/66#issuecomment-5472508168).
- **Distribution channel:** GitHub directory review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** Isolation and security posture depend on the selected deployment/backend; the entry makes no security certification or maintainer endorsement claim.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the directory maintainer review the focused entry; do not add scanner or certification claims that are not supported by the project sources.
### 2026-08-31 — Awesome Agent Runtime Security review path

- **Objective:** Reach a focused agent-sandbox/security directory with a source-backed multi-backend runtime entry.
- **Action:** Opened [Awesome Agent Runtime Security PR #30](https://github.com/bureado/awesome-agent-runtime-security/pull/30) under Sandboxing & Isolation.
- **Validation:** The one-row change links the canonical SandBase repository and describes sandboxed tools, credential boundaries, policy controls, persistent sessions, audit/replay, and MCP. GitHub reports `OPEN / MERGEABLE / CLEAN`; no automated checks are reported. A verification note is [recorded on the PR](https://github.com/bureado/awesome-agent-runtime-security/pull/30#issuecomment-5472531934).
- **Distribution channel:** GitHub directory review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** The directory's scope includes sandboxing/isolation, but SandBase does not claim universal microVM or kernel isolation; posture depends on the selected deployment/backend. No endorsement or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer review the focused entry and respond to the explicit deployment boundary.

### 2026-08-31 — Awesome LLM Security review path

- **Objective:** Reach a high-visibility LLM security directory with a source-backed runtime-governance entry.
- **Action:** Opened [Awesome LLM Security PR #313](https://github.com/corca-ai/awesome-llm-security/pull/313) under Tools.
- **Validation:** The one-line change links the canonical SandBase repository and describes sandboxed tools, credential scoping, approvals, audit/replay, and MCP. GitHub reports `OPEN / MERGEABLE / CLEAN`; no automated checks are reported. A verification note is [recorded on the PR](https://github.com/corca-ai/awesome-llm-security/pull/313#issuecomment-5472550887).
- **Distribution channel:** GitHub directory review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** The entry does not claim vulnerability scanning, security certification, or endorsement; isolation and posture depend on the selected deployment/backend.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the maintainer review the narrowly scoped Tools entry; do not broaden it into unsupported scanner claims.

### 2026-08-31 — Awesome AI Agents existing PR follow-up

- **Objective:** Advance a high-visibility AI-agent directory path without creating duplicate maintainer work.
- **Action:** Found the existing [Awesome AI Agents PR #467](https://github.com/jim-schwoebel/awesome_ai_agents/pull/467), which already adds a single-line SandBase Harness entry under Building / Frameworks; posted a source and deployment-boundary verification follow-up instead of opening another PR.
- **Validation:** GitHub reports the existing PR `OPEN / MERGEABLE / CLEAN`; the follow-up is [recorded on the PR](https://github.com/jim-schwoebel/awesome_ai_agents/pull/467#issuecomment-5472570979). The destination accepts relevant AI-agent resources with a clear link and one-sentence description.
- **Distribution channel:** Existing GitHub directory review; X, LinkedIn, and Discord drafts remain `NEEDS REVIEW` and require operator/account authorization.
- **Boundary:** The entry is a discovery request only; local/Docker/Kubernetes/worker backends do not provide identical isolation properties, and no endorsement or security certification is claimed.
- **Star count / referral:** No causal Star increase or referral is claimed.
- **Next hypothesis:** Let the directory maintainer review the existing PR; do not create a duplicate contribution.
