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

## Recording rules

For every later action, record the timestamp, repository, objective, source
problem, exact implementation/PR or release URL, validation, distribution
channel, direct star count before and after, observed referral or engagement,
deployment state, result, and the next hypothesis. Never buy, trade, automate,
or manufacture stars, followers, comments, issues, forks, or contributors.
