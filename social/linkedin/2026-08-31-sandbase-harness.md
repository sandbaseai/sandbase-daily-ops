# LinkedIn draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

When an Agent moves from a chat window into an engineering workflow, the hard question is no longer only which model to call. Platform teams also need to know where sessions live, which tools may run, what needs approval, and how to reconstruct a failed run.

SandBase Harness v0.3.8 is the open-source, local-first runtime for that layer. It provides persistent sessions, an MCP bridge, explicit approvals, credential scoping, audit/replay records, and replaceable Docker, Kubernetes, and worker execution backends.

This makes it useful for teams evaluating self-owned Agent infrastructure: start locally, connect an MCP client, and inspect the session and tool boundaries before deciding how to deploy it.

The important qualification is deployment-specific: Docker, Kubernetes, and worker backends do not provide identical isolation properties. SandBase Harness does not claim universal microVM or kernel isolation.

Read the installation guide and source-backed release details: https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md

The portable Agent Plugin is publicly source-indexed at https://agent-plugins.directory/sandbaseai/sandbase-harness. The repository's plugin metadata is now v0.1.1; the directory is a discovery catalog only, and its displayed revision is awaiting refresh.

An additional public discovery result is the SandBase Harness entry in the Agent Skills & Tools section of https://github.com/aloth/awesome-ai-agents. This is a community-list inclusion, not a security certification or project endorsement.

For a practical DeepSeek Harness walkthrough, the newly refreshed [English article](https://blog.sandbase.ai/deepseek-harness-developer-preview-2026/) and [Chinese article](https://blog.sandbase.ai/zh-CN/deepseek-harness-developer-preview-2026/) now use the pinned v0.3.8 integration and current installation links. The pages are live after a successful production deployment.

Recent ecosystem review submissions include [Awesome MCP Collection](https://github.com/JustInCache/awesome-mcp-collection/pull/39), [Awesome Agent OS](https://github.com/cueos/awesome-agent-os/pull/3), and [Awesome X-Ops](https://github.com/xlabs-club/awesome-x-ops/pull/250). These are pending maintainer review, not endorsements.

An additional public listing is now live in [Awesome AI Engineering](https://github.com/Eric-LLMs/Awesome-AI-Engineering/pull/4), alongside the previously merged ecosystem entries.

Two additional discovery submissions are now in review: [MeshKore](https://meshkore.com/submit), submission #14, and [Agent Switchboard PR #44](https://github.com/assafbar2/agentswitchboard.dev/pull/44). They are review-controlled and are not being presented as live listings or endorsements.

The Hugging Face [agent-harness registry PR #2432](https://github.com/huggingface/huggingface.js/pull/2432) now includes a corrective commit that removes `MANAGED_AGENTS_HOME` as an identity marker because it is a data-directory override. Tasks formatting, lint, TypeScript, and Cursor Bugbot checks pass; Hugging Face maintainer merge remains pending.

The new [gVisor integration guide PR #14517](https://github.com/google/gvisor/pull/14517) documents a Docker → `runsc` → gVisor path for selected DeepSeek Harness commands. It keeps Harness policy, Docker/OCI configuration, and gVisor kernel isolation as separate layers. SandBase Harness is a complementary Harness-side reference, not a replacement for gVisor or a universal isolation/security claim.

The latest review queue also includes [Agentic Community Landscape PR #2](https://github.com/agentic-community/agentic-landscape/pull/2), [Awesome AI Agent Engineering PR #1](https://github.com/sspoisk/awesome-ai-agent-engineering/pull/1), and [MyMCPTools issue #8](https://github.com/shibley/mymcptools/issues/8). Each submission uses official repository and release evidence and remains subject to the destination maintainer's review.

The security-oriented [Awesome-LLMSecOps PR #66](https://github.com/wearetyomsmnv/Awesome-LLMSecOps/pull/66) proposes a single, source-linked SandBase Harness entry under Agentic security. It describes documented runtime controls and explicitly preserves the deployment/backend-dependent isolation boundary; the PR is clean and mergeable, with maintainer review pending. It is a discovery request, not an endorsement or security certification.

Separately, [MCPVault now exposes a public auto-indexed listing](https://mcpvault.io/servers/sandbase-harness). The page is currently marked unclaimed and its quality signals are computed from public repository data; this is an independent discovery page, not a project-maintainer certification.

Two additional community review paths are now open: [Collective AI Tools Issue #332](https://github.com/hanishrao/collective-ai-tools/issues/332), submitted separately from the existing SandBase CLI entry, and [Awesome Agent Skills PR #79](https://github.com/philipbankier/awesome-agent-skills/pull/79), which adds the runtime to its MCP infrastructure section. Both remain pending maintainer review.

The [Awesome MCP List PR #409](https://github.com/MobinX/awesome-mcp-list/pull/409) is another focused community listing request, adding SandBase Harness to AI Agents & Frameworks. It remains pending maintainer review and does not represent an endorsement.

The [Awesome Agent Runtimes PR #4](https://github.com/beejmaxx/awesome-agent-runtimes/pull/4) takes a deliberately maturity-aware path: it proposes SandBase Harness for the project's watchlist, with the 180-day and 5,000-star gates recorded explicitly. Review is pending; no core-catalog inclusion is claimed.

The infrastructure-focused [Awesome Agent Infra PR #6](https://github.com/shenli/awesome-agent-infra/pull/6) adds SandBase Harness to its Runtime and Control Plane table. It remains pending maintainer review and is not an endorsement.

The [Awesome AI Developer Stack PR #2](https://github.com/masrisystems/awesome-ai-developer-stack/pull/2) adds SandBase Harness to a broader MCP Servers directory table. It remains pending maintainer review and uses the official repository as its source.

The current review queue also includes [Awesome CLI Coding Agents PR #314](https://github.com/bradAGI/awesome-cli-coding-agents/pull/314), [Awesome Terminal Agents PR #5](https://github.com/EnigmaYYYY/awesome-terminal-agents/pull/5), and [Awesome Agent Cortex PR #74](https://github.com/0xNyk/awesome-agent-cortex/pull/74). Each is a focused discovery request awaiting the destination maintainer's review; the earlier Wenyu #213 was superseded by merged [#228](https://github.com/WenyuChiou/awesome-agentic-ai-zh/pull/228).

These listings should be read as community review paths, not endorsements or security certifications. Isolation remains dependent on the selected deployment backend.

An additional infrastructure-focused submission is [Awesome Agent Infrastructure PR #23](https://github.com/backblaze-labs/awesome-agent-infrastructure/pull/23), which proposes SandBase Harness for its Execution Sandboxes section. The PR follows the repository's `entries.yaml` contribution format and is awaiting maintainer review; it is not a listing or endorsement yet.

The sandbox-focused [Awesome Agent Sandboxes PR #9](https://github.com/dloss/awesome-agent-sandboxes/pull/9) proposes a concise Containers entry for SandBase Harness. It remains a community review request, with the important qualification that isolation depends on the selected backend and deployment configuration.

Another focused review request is [Awesome Agent Sandbox PR #4](https://github.com/fishman/awesome-agent-sandbox), which adds SandBase Harness to a coding-agent sandbox comparison table. The entry describes its local, Docker, Kubernetes, and worker options without implying identical isolation guarantees across deployments.

The structured [Awesome Agent Sandboxes PR #59](https://github.com/msyvr/awesome-agent-sandboxes/pull/59) adds SandBase Harness metadata to a maintained sandbox landscape and regenerates its README, JSON, and reference outputs. It remains pending maintainer review; the entry explicitly separates local path isolation from backend-dependent deployment properties.

The security-focused [Awesome Agent Sandboxing PR #2](https://github.com/IronSecCo/awesome-agent-sandboxing/pull/2) proposes SandBase Harness for its Self-hosted Agent Runtimes section. It is a factual review request, not a security certification, and keeps the backend/deployment isolation boundary explicit.

The focused [Awesome Agent Runtime Security PR #30](https://github.com/bureado/awesome-agent-runtime-security/pull/30) proposes SandBase Harness for the directory's Sandboxing & Isolation section. It uses a single source-linked row, keeps the deployment/backend qualification explicit, and is currently clean and mergeable while maintainer review is pending. It is a discovery request, not an endorsement or security certification.

The high-visibility [Awesome LLM Security PR #313](https://github.com/corca-ai/awesome-llm-security/pull/313) proposes SandBase Harness for the Tools section as a runtime-governance reference. It describes documented tool boundaries, credential scoping, approvals, audit/replay, and MCP without calling the project a vulnerability scanner; the PR is clean and mergeable while maintainer review is pending. Isolation remains deployment/backend dependent, and the submission is not an endorsement or security certification.

The existing [Awesome AI Agents PR #467](https://github.com/jim-schwoebel/awesome_ai_agents/pull/467) already adds a single-line SandBase Harness entry to the AI-agent resources list. It is clean and mergeable while maintainer review is pending. We followed up on that existing contribution instead of opening a duplicate; the source-backed entry remains a discovery request, not an endorsement or security certification.

The active [Jenqyang Awesome AI Agents PR #460](https://github.com/Jenqyang/Awesome-AI-Agents/pull/460) proposes SandBase Harness for Applications → Tools. It follows the directory's standard-OSS, maintainability, and neutral-description rules; the PR is clean and mergeable while maintainer review is pending. The entry describes independently self-hostable capabilities without pricing or hosted-upsell language and is not an endorsement or security certification.

The high-traffic [E2B Awesome AI Agents Issue #1468](https://github.com/e2b-dev/awesome-ai-agents/issues/1468) received a source-backed scope follow-up clarifying that SandBase Harness is a separate self-hosted runtime/MCP bridge from the previously closed CLI submission. The maintainer still controls the scope decision; this remains a review request rather than a listing or endorsement.

The existing [Slava Awesome AI Agents PR #403](https://github.com/slavakurilyak/awesome-ai-agents/pull/403) already proposes a SandBase Harness entry in a 2,195-star AI-agent directory. It is clean and mergeable while maintainer review is pending; we added current installation, release, MCP Registry, and deployment-boundary evidence to that PR instead of opening a duplicate.

The existing [Scottcjn Awesome Agents PR #59](https://github.com/Scottcjn/awesome-agents/pull/59) adds SandBase Harness to an Agent platforms/frameworks directory. It is clean and mergeable while maintainer review is pending; a source-backed installation and deployment-boundary verification follow-up was added to the existing PR rather than creating a duplicate.

For MCP directory hygiene, the older duplicate [Awesome MCP Servers PR #13188](https://github.com/punkpeye/awesome-mcp-servers/pull/13188) was closed in favor of canonical [PR #13240](https://github.com/punkpeye/awesome-mcp-servers/pull/13240). The canonical `check-submission` passed, while the maintainer/Glama gate remains pending; future references should use #13240 only.

The DeepSeek Harness Handbook [bridge refresh PR #291](https://github.com/sandbaseai/deepseek-harness-handbook/pull/291) is now merged at `425dd255`, after catalog cleanup restored its verification gate. The [Sunrisepeak dsh-index PR #43](https://github.com/Sunrisepeak/dsh-index/pull/43) updates the indexed SandBase Harness descriptor from v0.3.7 to v0.3.8. The submitted revision passed its build and SandBase boot checks, but the PR currently needs a rebase before merge; no index publication is claimed.

The [Awesome Agent Sandbox PR #2](https://github.com/vivy-yi/awesome-agent-sandbox/pull/2) is another focused community review request, adding SandBase Harness to a Self-hosted / Open Source sandbox table. It remains pending maintainer review and uses a concise, capability-oriented description.

The broader [Awesome Sandbox PR #27](https://github.com/restyler/awesome-sandbox/pull/27) proposes a dedicated case study covering SandBase Harness's self-hosted runtime, tool governance, persistent sessions, audit/replay, and selectable sandbox providers. It remains pending maintainer review, with the backend-dependent isolation boundary stated explicitly.

The structured [AI Agent Sandboxes PR #3](https://github.com/pjlsergeant/ai-sandboxes/pull/3) proposes an evidence-linked dataset entry for SandBase Harness. It records official source links, persistent sessions, MCP/tool governance, approvals, audit/replay, and selectable backends while preserving the distinction between local path isolation and backend-specific properties.

The [AgentFirst directory PR #46](https://github.com/bradvin/agentfirst.directory/pull/46) now has its repository-managed submitter/media metadata verified locally and by the remote `enrich` check; maintainer review remains pending.

For developer discovery, [Awesome AI Coding Tools PR #665](https://github.com/ai-for-developers/awesome-ai-coding-tools/pull/665) proposes adding SandBase Harness to its MCP Servers and Directories section. The entry links the canonical repository and describes the local stdio bridge and self-hosted runtime; directory review is pending.

The new [Awesome MCP Collection PR #39](https://github.com/JustInCache/awesome-mcp-collection/pull/39) proposes SandBase Harness for its Development & Version Control category. The entry records the TypeScript/Apache-2.0 project, MCP bridge, sandboxed sessions, credentials, approvals, audit, and replay; it remains a maintainer review request rather than an endorsement or security certification.

An additional review request is open in [Awesome MCP issue #99](https://github.com/abordage/awesome-mcp/issues/99), proposing SandBase Harness for Aggregators & Gateways. It is a factual, source-linked directory request and remains subject to maintainer review; it is not an endorsement or security certification.

The canonical [Awesome MCP Gateways PR #77](https://github.com/e2b-dev/awesome-mcp-gateways/pull/77) proposes SandBase Harness for the Open-source MCP Gateways list. GitHub reports the PR as mergeable; its CLA verification is awaiting a conclusion, so this remains a maintainer review request rather than an endorsement or security certification.

The new [Awesome AI Harness PR #4](https://github.com/weiwei966/awesome-ai-harness/pull/4) proposes SandBase Harness for the SDKs & runtimes section. The entry explains session state, governed MCP tools, approvals, credential scoping, audit/replay, and selectable deployment backends; it remains a factual maintainer review request, not an endorsement or security certification.

The new [Awesome AI Coding Sandboxes PR #15](https://github.com/fhiltscher/awesome-ai-coding-sandboxes/pull/15) proposes SandBase Harness for the directory's Adjacent runtimes section. It explicitly distinguishes a provider-backed runtime from a standalone isolation engine; review is pending and the entry is not a security certification.

The existing [Awesome Agent Harnesses PR #2](https://github.com/bayshier/awesome-agent-harnesses/pull/2) proposes SandBase Harness for Platforms & Frameworks. It is a source-linked maintainer review request; no endorsement or security certification is implied.

The new [Awesome Agent Harness PR #10](https://github.com/zients/awesome-agent-harness/pull/10) proposes SandBase Harness for Agent Systems & Harnesses. The entry keeps model-provider requirements and backend/deployment-dependent isolation explicit; review is pending and no endorsement or security certification is implied.

The new [Awesome AI Agents PR #184](https://github.com/NipunaRanasinghe/awesome-ai-agents/pull/184) proposes SandBase Harness for the directory's Core Frameworks section. It follows the dynamic stars-badge table format and remains a factual maintainer review request; no endorsement or security certification is implied.

The [E2B Awesome AI Agents Issue #1468](https://github.com/e2b-dev/awesome-ai-agents/issues/1468) asks the directory maintainer to decide whether SandBase Harness should be reviewed as a distinct runtime entry from the closed SandBase CLI submission. This is a scope question, not a claim of inclusion or endorsement.

That scope request now has a direct [PR #1473](https://github.com/e2b-dev/awesome-ai-agents/pull/1473) with a factual open-source runtime entry and official repository, installation, and release links. The PR is mergeable; its required CLA check awaits contributor signature, so no directory listing or endorsement is claimed.

The new [Awesome AI Agents 2026 PR #240](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026/pull/240) proposes the current SandBase Harness runtime under Agent Tooling and Infrastructure, distinct from the existing CLI entry. It follows the directory's required tier/language/type format; maintainer review is pending.

The destination's link-check failure was traced to a pre-existing `ofekron/better-agent` 404 outside the PR diff; the SandBase repository link and other PR checks pass. The finding is documented for the maintainer, and no endorsement or security certification is claimed.

The existing [E2B Awesome AI SDKs PR #344](https://github.com/e2b-dev/awesome-ai-sdks/pull/344) proposes SandBase Harness for the SDK/framework/tool directory. The entry links the official runtime documentation and remains a factual review request; CLA completion is still required from the contributor account holder.

A new focused review path is open in [Awesome Agent Harnesses issue #4](https://github.com/NeuraLiying/Awesome-Agent-Harnesses/issues/4). It suggests SandBase Harness for the directory's Production Harnesses, SDKs & Frameworks section, with links to the runtime, installation guide, harness design, and backend documentation. Inclusion remains subject to the destination maintainer's review; this is not an endorsement or security certification.

SandBase Harness was also submitted to the public [mcp.so MCP-server intake](https://github.com/chatmcp/mcpso/issues/1#issuecomment-5472364196) with the canonical repository, MCP server ID, v0.3.8 OCI image, and setup guide. Any directory listing remains subject to the destination's process; the submission is not an endorsement or security certification.

A further scope review is open in [HKUST-KnowComp's Awesome Agent Harness issue #8](https://github.com/HKUST-KnowComp/Awesome-Agent-Harness/issues/8). The proposal positions SandBase Harness as a source-linked runtime resource, with possible placement under Tool Use & Code Execution or Sandboxing & Execution Environments. Curator review is pending, and the project is not presented as a research paper or security certification.

The existing [Picrew Awesome Agent Harness PR #86](https://github.com/Picrew/awesome-agent-harness/pull/86) was also synchronized with the destination's latest `main` and regenerated successfully. It now reports CLEAN/MERGEABLE; two stale entries and one external OpenReview 403 remain as destination-wide baseline findings, not SandBase entry failures.

An additional public directory result is now confirmed: [Awesome Agent Operating Systems PR #13](https://github.com/frankxai/awesome-agent-operating-systems/pull/13) merged SandBase Harness into Agent Runtimes. The earlier PR #11 was superseded by #13; the entry is a community directory listing and not an endorsement or security certification.

SandBase Harness is also proposed in [TensorChord Awesome LLMOps PR #785](https://github.com/tensorchord/Awesome-LLMOps/pull/785), a high-visibility LLMOps catalog. The one-line entry covers the self-hosted runtime, MCP bridge, governance controls, audit/replay, and selectable execution backends. The PR is OPEN/MERGEABLE; DCO completion remains contributor-owned and maintainer review is pending.

Follow-up: the DCO check for PR #785 now passes after the signed-off contribution commit was pushed. Maintainer review remains pending, and the catalog is not presented as an endorsement or security certification.

The latest public project update is available in [official Discussion #116](https://github.com/sandbaseai/sandbase-harness/discussions/116#discussioncomment-18211980), which links the v0.3.8 installation source, merged handbook integration, and current dsh-index review status. Feedback is invited on backend selection, MCP schemas, session lifecycle, and audit/replay gaps.

The project is also under curator review in [AAE Agent Engineering issue #1](https://github.com/Lxcardoza993/AAE/issues/1) for its Agent Harness category. The submission is source-backed and remains a candidate only, not an endorsement or security certification.

A new scope discussion is open in [Kubernetes Agent Sandbox issue #1500](https://github.com/kubernetes-sigs/agent-sandbox/issues/1500), asking whether a source-linked SandBase Harness compatibility or deployment example belongs in the Agent Sandbox documentation. The two projects are described as complementary layers; no existing adapter, inclusion, or endorsement is claimed, and maintainer guidance is pending.
