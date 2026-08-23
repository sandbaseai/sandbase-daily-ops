# Open-source growth ledger

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

## Recording rules

For every later action, record the timestamp, repository, objective, source
problem, exact implementation/PR or release URL, validation, distribution
channel, direct star count before and after, observed referral or engagement,
deployment state, result, and the next hypothesis. Never buy, trade, automate,
or manufacture stars, followers, comments, issues, forks, or contributors.
