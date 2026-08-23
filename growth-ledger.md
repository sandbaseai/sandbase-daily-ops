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

## Recording rules

For every later action, record the timestamp, repository, objective, source
problem, exact implementation/PR or release URL, validation, distribution
channel, direct star count before and after, observed referral or engagement,
deployment state, result, and the next hypothesis. Never buy, trade, automate,
or manufacture stars, followers, comments, issues, forks, or contributors.
