# X draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

An agent runtime needs more than a model call: it needs a place for sessions to persist, tools to pass through explicit controls, and runs to leave evidence.

SandBase Harness v0.3.8 is a local-first TypeScript runtime with an MCP bridge, persistent sessions, approvals, audit/replay, and Docker/Kubernetes/worker execution backends.

Try the MCP setup: https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md

DeepSeek Harness walkthrough: https://blog.sandbase.ai/deepseek-harness-developer-preview-2026/

Now publicly listed in Awesome AI Engineering: https://github.com/Eric-LLMs/Awesome-AI-Engineering/pull/4

New directory submissions are under review: MeshKore (#14) https://meshkore.com/submit and Agent Switchboard PR #44 https://github.com/assafbar2/agentswitchboard.dev/pull/44

Hugging Face agent-harness registry PR: https://github.com/huggingface/huggingface.js/pull/2432 (review pending)

More ecosystem submissions: Agentic Community Landscape PR #2 https://github.com/agentic-community/agentic-landscape/pull/2, Awesome AI Agent Engineering PR #1 https://github.com/sspoisk/awesome-ai-agent-engineering/pull/1, and MyMCPTools issue #8 https://github.com/shibley/mymcptools/issues/8. All are pending maintainer review.

Security-oriented discovery: Awesome-LLMSecOps PR #66 https://github.com/wearetyomsmnv/Awesome-LLMSecOps/pull/66 adds SandBase Harness under Agentic security. The PR is clean and mergeable; maintainer review is pending. This is a source-linked discovery request, not an endorsement or security certification, and isolation remains deployment/backend dependent.

Public discovery: MCPVault now has an auto-indexed, unclaimed listing https://mcpvault.io/servers/sandbase-harness (automated signal, not a maintainer certification).

Boundary: isolation depends on the selected deployment backend; this is not a universal microVM or kernel-isolation claim.

Additional community review paths: Collective AI Tools #332 https://github.com/hanishrao/collective-ai-tools/issues/332 and Awesome Agent Skills PR #79 https://github.com/philipbankier/awesome-agent-skills/pull/79. Both are pending maintainer review.

Another pending listing request: Awesome MCP List PR #409 https://github.com/MobinX/awesome-mcp-list/pull/409. It adds SandBase Harness to AI Agents & Frameworks; review is pending.

For a maturity-gated runtime catalog, Awesome Agent Runtimes PR #4 https://github.com/beejmaxx/awesome-agent-runtimes/pull/4 proposes SandBase Harness for its watchlist. Review is pending; no core-catalog inclusion is claimed.

Infrastructure review: Awesome Agent Infra PR #6 https://github.com/shenli/awesome-agent-infra/pull/6 adds SandBase Harness to Runtime and Control Plane. Maintainer review is pending.

Another community review path: Awesome AI Developer Stack PR #2 https://github.com/masrisystems/awesome-ai-developer-stack/pull/2 adds SandBase Harness to its MCP Servers table. Review is pending.

Further review paths: Awesome CLI Coding Agents PR #314 https://github.com/bradAGI/awesome-cli-coding-agents/pull/314, Awesome Agentic AI 中文 PR #213 https://github.com/WenyuChiou/awesome-agentic-ai-zh/pull/213, Awesome Terminal Agents PR #5 https://github.com/EnigmaYYYY/awesome-terminal-agents/pull/5, Awesome Agent Sandbox PR #2 https://github.com/yanmxa/awesome-agent-sandbox/pull/2, and Awesome Agent Cortex PR #74 https://github.com/0xNyk/awesome-agent-cortex/pull/74. All remain pending maintainer review.

These are discovery submissions only; inclusion is not endorsement or security certification. Isolation depends on the selected deployment backend.

New infrastructure review path: Awesome Agent Infrastructure PR #23 https://github.com/backblaze-labs/awesome-agent-infrastructure/pull/23 adds SandBase Harness to Execution Sandboxes. Maintainer review is pending; no listing, endorsement, or security certification is claimed.

Another sandbox review path: Awesome Agent Sandboxes PR #9 https://github.com/dloss/awesome-agent-sandboxes/pull/9 adds SandBase Harness to Containers. It is pending maintainer review; isolation remains backend/deployment dependent.

New coding-agent sandbox review: Awesome Agent Sandbox PR #4 https://github.com/fishman/awesome-agent-sandbox adds SandBase Harness to its Container Sandboxes list and comparison table. Maintainer review is pending; no endorsement or security certification is claimed.

Structured sandbox catalog review: Awesome Agent Sandboxes PR #59 https://github.com/msyvr/awesome-agent-sandboxes/pull/59 adds SandBase Harness metadata and regenerated reference outputs. Maintainer review is pending; backend/deployment isolation limits remain explicit.

Security-focused runtime review: Awesome Agent Sandboxing PR #2 https://github.com/IronSecCo/awesome-agent-sandboxing/pull/2 adds SandBase Harness to Self-hosted Agent Runtimes. Review is pending; this is not a security certification.

Runtime-security directory review: Awesome Agent Runtime Security PR #30 https://github.com/bureado/awesome-agent-runtime-security/pull/30 adds SandBase Harness to Sandboxing & Isolation. The PR is clean and mergeable; maintainer review is pending. This is a source-linked discovery request, not an endorsement or security certification, and isolation remains deployment/backend dependent.

High-visibility security directory review: Awesome LLM Security PR #313 https://github.com/corca-ai/awesome-llm-security/pull/313 adds SandBase Harness to Tools as a runtime-governance reference. The PR is clean and mergeable; maintainer review is pending. This is not a vulnerability-scanner claim, endorsement, or security certification, and isolation remains deployment/backend dependent.

Existing AI-agent directory review: Awesome AI Agents PR #467 https://github.com/jim-schwoebel/awesome_ai_agents/pull/467 already contains a single-line SandBase Harness entry. The PR is clean and mergeable; maintainer review is pending. This update follows the existing PR rather than creating a duplicate; the entry is a source-linked discovery request, not an endorsement or security certification.

New active AI-agent directory review: Jenqyang Awesome AI Agents PR #460 https://github.com/Jenqyang/Awesome-AI-Agents/pull/460 adds SandBase Harness to Applications → Tools. The PR is clean and mergeable; maintainer review is pending. It follows the destination's OSS and neutral-description rules; this is a source-linked discovery request, not an endorsement or security certification.

Scope follow-up: E2B Awesome AI Agents Issue #1468 https://github.com/e2b-dev/awesome-ai-agents/issues/1468 now has a source-backed clarification distinguishing the self-hosted Harness runtime from the separate CLI submission. The directory's scope decision remains pending; this is a review request, not a listing, endorsement, or security certification.

Existing high-visibility review: Slava Awesome AI Agents PR #403 https://github.com/slavakurilyak/awesome-ai-agents/pull/403 already contains a SandBase Harness entry and is clean/mergeable with maintainer review pending. A source and deployment-boundary follow-up was posted; this advances the existing PR rather than creating a duplicate.

Existing agent-platform directory review: Scottcjn Awesome Agents PR #59 https://github.com/Scottcjn/awesome-agents/pull/59 already contains a SandBase Harness entry and is clean/mergeable with maintainer review pending. A source and deployment-boundary verification follow-up was posted; no duplicate PR was created.

MCP directory maintenance: the older duplicate Awesome MCP Servers PR #13188 https://github.com/punkpeye/awesome-mcp-servers/pull/13188 was closed in favor of canonical PR #13240 https://github.com/punkpeye/awesome-mcp-servers/pull/13240, whose `check-submission` passed. The canonical entry remains under maintainer/Glama review; no listing or endorsement is claimed.

DSH index update: Sunrisepeak dsh-index PR #43 https://github.com/Sunrisepeak/dsh-index/pull/43 updates the SandBase Harness descriptor to v0.3.8. Its submitted-revision build and boot checks passed, but the PR is currently dirty and needs a rebase; no index publication is claimed yet.

Another self-hosted sandbox review: Awesome Agent Sandbox PR #2 https://github.com/vivy-yi/awesome-agent-sandbox/pull/2 adds SandBase Harness to its Open Source table. Maintainer review is pending; no endorsement is claimed.

New guide review: Awesome Sandbox PR #27 https://github.com/restyler/awesome-sandbox adds a dedicated SandBase Harness runtime/sandbox case study. GitGuardian is still running and maintainer review is pending; no security certification is claimed.

Evidence-dataset review: AI Agent Sandboxes PR #3 https://github.com/pjlsergeant/ai-sandboxes adds source-linked SandBase Harness metadata to a structured sandbox dataset. Maintainer review is pending; backend limits remain explicit.

Developer discovery: Awesome AI Coding Tools PR #665 https://github.com/ai-for-developers/awesome-ai-coding-tools/pull/665 adds SandBase Harness to MCP Servers and Directories. Review pending; source-linked reference only.

New MCP directory review: Awesome MCP Collection PR #39 https://github.com/JustInCache/awesome-mcp-collection/pull/39 adds SandBase Harness to Development & Version Control. Review pending; source-linked reference only, not an endorsement or security certification.

Additional MCP directory review: Awesome MCP issue #99 https://github.com/abordage/awesome-mcp/issues/99 requests SandBase Harness for Aggregators & Gateways. Review pending; source-linked reference only, not an endorsement or security certification.

New gateway directory review: Awesome MCP Gateways PR #77 https://github.com/e2b-dev/awesome-mcp-gateways/pull/77 adds SandBase Harness to Open-source MCP Gateways. Maintainer review and CLA verification are pending; source-linked reference only, not an endorsement or security certification.

New harness directory review: Awesome AI Harness PR #4 https://github.com/weiwei966/awesome-ai-harness/pull/4 adds SandBase Harness to SDKs & runtimes. Review pending; source-linked reference only, not an endorsement or security certification.

New sandbox directory review: Awesome AI Coding Sandboxes PR #15 https://github.com/fhiltscher/awesome-ai-coding-sandboxes/pull/15 adds SandBase Harness to Adjacent runtimes. Review pending; the entry explicitly preserves the provider-dependent isolation boundary.

Harness directory review: Awesome Agent Harnesses PR #2 https://github.com/bayshier/awesome-agent-harnesses/pull/2 adds SandBase Harness to Platforms & Frameworks. Review pending; source-linked reference only, not an endorsement or security certification.

Agent systems review: Awesome Agent Harness PR #10 https://github.com/zients/awesome-agent-harness/pull/10 adds SandBase Harness to Agent Systems & Harnesses. Review pending; source-linked reference only, not an endorsement or security certification.

AI agent directory review: Awesome AI Agents PR #184 https://github.com/NipunaRanasinghe/awesome-ai-agents/pull/184 adds SandBase Harness to Core Frameworks. Review pending; source-linked reference only, not an endorsement or security certification.

Scope review: E2B Awesome AI Agents Issue #1468 https://github.com/e2b-dev/awesome-ai-agents/issues/1468 asks whether SandBase Harness belongs as a distinct runtime entry from the closed CLI submission. Maintainer scope decision pending; no inclusion or endorsement is claimed.

Runtime directory review: Awesome AI Agents 2026 PR #240 https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026/pull/240 adds SandBase Harness beside the separate CLI entry under Agent Tooling and Infrastructure. Review pending; no endorsement or security certification is claimed.

Link-check follow-up: the failed job reports only the pre-existing `ofekron/better-agent` 404 outside the SandBase diff. A maintainer follow-up records the baseline finding; review remains pending.

SDK/runtime directory review: E2B Awesome AI SDKs PR #344 https://github.com/e2b-dev/awesome-ai-sdks/pull/344 proposes SandBase Harness for its SDKs, frameworks, libraries, and tools list. Review pending; CLA verification remains contributor-owned.

New focused review path: Awesome Agent Harnesses issue #4 https://github.com/NeuraLiying/Awesome-Agent-Harnesses/issues/4 suggests SandBase Harness for Production Harnesses, SDKs & Frameworks. Maintainer review is pending; this is not a listing or endorsement.

New MCP directory submission: https://github.com/chatmcp/mcpso/issues/1#issuecomment-5472364196 includes the canonical repository, v0.3.8 OCI image, MCP server ID, and setup guide. Directory processing is pending; no listing or endorsement is claimed.

New survey review path: https://github.com/HKUST-KnowComp/Awesome-Agent-Harness/issues/8 proposes SandBase Harness as a source-linked runtime resource. Curator scope review is pending; it is not being presented as a research paper, listing, or security certification.

Maintenance update: [Picrew Awesome Agent Harness PR #86](https://github.com/Picrew/awesome-agent-harness/pull/86) was synchronized with the host `main` and is now CLEAN/MERGEABLE. The directory's remaining verification findings are unrelated baseline issues; maintainer review is still pending.

Public listing update: [Awesome Agent Operating Systems PR #13](https://github.com/frankxai/awesome-agent-operating-systems/pull/13) has merged SandBase Harness into Agent Runtimes. The old PR #11 was superseded; this is a directory listing, not an endorsement or security certification.

New high-visibility LLMOps review: [TensorChord Awesome LLMOps PR #785](https://github.com/tensorchord/Awesome-LLMOps/pull/785) adds SandBase Harness to the LLMOps catalog. It is OPEN/MERGEABLE; DCO completion is contributor-owned and review is pending.

The DCO gate for [TensorChord Awesome LLMOps PR #785](https://github.com/tensorchord/Awesome-LLMOps/pull/785) now passes. The PR remains under maintainer review; no listing or endorsement is claimed.
