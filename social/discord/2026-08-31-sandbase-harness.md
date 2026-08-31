# Discord draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

For builders testing a self-owned Agent runtime, SandBase Harness v0.3.8 provides:

- persistent sessions and resumable runtime state;
- an MCP bridge with explicit tool boundaries;
- approvals, credential scoping, audit, and replay;
- Docker, Kubernetes, and worker execution backends.

Start with the [MCP installation guide](https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md) and the [v0.3.8 release](https://github.com/sandbaseai/sandbase-harness/releases/tag/v0.3.8). Isolation is deployment-dependent, so the backends should be evaluated separately; this project does not claim universal microVM or kernel isolation.

Feedback and deployment reports: https://github.com/sandbaseai/sandbase-harness/discussions/116

DeepSeek Harness walkthroughs are now live in [English](https://blog.sandbase.ai/deepseek-harness-developer-preview-2026/) and [中文](https://blog.sandbase.ai/zh-CN/deepseek-harness-developer-preview-2026/), both refreshed for the pinned SandBase Harness v0.3.8 integration.

Discovery updates (all pending external review): [Awesome MCP Collection](https://github.com/JustInCache/awesome-mcp-collection/pull/38), [Awesome Agent OS](https://github.com/cueos/awesome-agent-os/pull/2), and [Awesome X-Ops](https://github.com/xlabs-club/awesome-x-ops/pull/250). Inclusion requests are not endorsements or security certifications.

One more public listing is confirmed in [Awesome AI Engineering](https://github.com/Eric-LLMs/Awesome-AI-Engineering/pull/4); it is an independent catalog entry, not a certification.

New directory submissions awaiting review: [MeshKore #14](https://meshkore.com/submit) and [Agent Switchboard PR #44](https://github.com/assafbar2/agentswitchboard.dev/pull/44). These are discovery submissions only, not endorsements or security certifications.

Hugging Face agent-harness registry: [PR #2432](https://github.com/huggingface/huggingface.js/pull/2432), pending review and limited to attribution metadata.

Additional pending review paths: [Agentic Community Landscape PR #2](https://github.com/agentic-community/agentic-landscape/pull/2), [Awesome AI Agent Engineering PR #1](https://github.com/sspoisk/awesome-ai-agent-engineering/pull/1), and [MyMCPTools issue #8](https://github.com/shibley/mymcptools/issues/8). These are independent directory submissions, not endorsements or security certifications.

Public discovery update: [MCPVault lists SandBase Harness](https://mcpvault.io/servers/sandbase-harness) as an auto-indexed, unclaimed entry. Its automated quality signals are not a maintainer review or security certification.

Two more community review paths: [Collective AI Tools #332](https://github.com/hanishrao/collective-ai-tools/issues/332) and [Awesome Agent Skills PR #79](https://github.com/philipbankier/awesome-agent-skills/pull/79). Both are pending maintainer review and are not endorsements or security certifications.

Another pending directory request: [Awesome MCP List PR #409](https://github.com/MobinX/awesome-mcp-list/pull/409), adding SandBase Harness to AI Agents & Frameworks. It is a review request only.

Maturity-aware review path: [Awesome Agent Runtimes PR #4](https://github.com/beejmaxx/awesome-agent-runtimes/pull/4) proposes SandBase Harness for its watchlist, not the active core catalog. Review is pending.

Infrastructure review path: [Awesome Agent Infra PR #6](https://github.com/shenli/awesome-agent-infra/pull/6), adding SandBase Harness to Runtime and Control Plane. Review is pending.

Another pending directory request: [Awesome AI Developer Stack PR #2](https://github.com/masrisystems/awesome-ai-developer-stack/pull/2), adding SandBase Harness to its MCP Servers table. This is a review request only.

More pending review paths: [Awesome CLI Coding Agents PR #314](https://github.com/bradAGI/awesome-cli-coding-agents/pull/314), [Awesome Agentic AI 中文 PR #213](https://github.com/WenyuChiou/awesome-agentic-ai-zh/pull/213), [Awesome Terminal Agents PR #5](https://github.com/EnigmaYYYY/awesome-terminal-agents/pull/5), [Awesome Agent Sandbox PR #2](https://github.com/yanmxa/awesome-agent-sandbox/pull/2), and [Awesome Agent Cortex PR #74](https://github.com/0xNyk/awesome-agent-cortex/pull/74). These are discovery submissions only, not endorsements or security certifications.

Isolation depends on the selected deployment backend; no universal microVM or kernel-isolation claim is made.

New infrastructure review path: [Awesome Agent Infrastructure PR #23](https://github.com/backblaze-labs/awesome-agent-infrastructure/pull/23), proposing SandBase Harness for Execution Sandboxes. Maintainer review is pending; this is not an endorsement or security certification.

Another pending sandbox submission: [Awesome Agent Sandboxes PR #9](https://github.com/dloss/awesome-agent-sandboxes/pull/9), adding SandBase Harness to Containers. This is a review request only; isolation depends on the selected backend and deployment configuration.

Another pending sandbox review: [Awesome Agent Sandbox PR #4](https://github.com/fishman/awesome-agent-sandbox), adding SandBase Harness to Container Sandboxes and its comparison table. Review only; no endorsement or security certification is claimed.

Structured catalog review: [Awesome Agent Sandboxes PR #59](https://github.com/msyvr/awesome-agent-sandboxes/pull/59), adding SandBase Harness metadata and regenerated catalog outputs. Maintainer review is pending; isolation depends on the selected backend and deployment configuration.

Security-focused runtime review: [Awesome Agent Sandboxing PR #2](https://github.com/IronSecCo/awesome-agent-sandboxing/pull/2), adding SandBase Harness to Self-hosted Agent Runtimes. Review is pending; it is not a security certification.

Another pending self-hosted sandbox review: [Awesome Agent Sandbox PR #2](https://github.com/vivy-yi/awesome-agent-sandbox/pull/2), adding SandBase Harness to the Open Source table. Review only; no endorsement is claimed.

New guide review: [Awesome Sandbox PR #27](https://github.com/restyler/awesome-sandbox/pull/27), adding a dedicated SandBase Harness runtime/sandbox case study. Maintainer review is pending; this is not a security certification.

Evidence-dataset review: [AI Agent Sandboxes PR #3](https://github.com/pjlsergeant/ai-sandboxes/pull/3), adding source-linked SandBase Harness metadata to a structured sandbox dataset. Maintainer review is pending; this is not an endorsement or security certification.

Developer discovery update: [Awesome AI Coding Tools PR #665](https://github.com/ai-for-developers/awesome-ai-coding-tools/pull/665) adds SandBase Harness to MCP Servers and Directories. Maintainer review is pending; the entry is a factual source-linked reference, not an endorsement.

New MCP directory review: [Awesome MCP Collection PR #39](https://github.com/JustInCache/awesome-mcp-collection/pull/39) adds SandBase Harness to Development & Version Control. Maintainer review is pending; this is a source-linked reference, not an endorsement or security certification.

Additional MCP directory review: [Awesome MCP issue #99](https://github.com/abordage/awesome-mcp/issues/99) requests SandBase Harness for Aggregators & Gateways. Maintainer review is pending; this is a source-linked reference, not an endorsement or security certification.

New gateway directory review: [Awesome MCP Gateways PR #77](https://github.com/e2b-dev/awesome-mcp-gateways/pull/77) adds SandBase Harness to Open-source MCP Gateways. Maintainer review and CLA verification are pending; this is not an endorsement or security certification.

New harness directory review: [Awesome AI Harness PR #4](https://github.com/weiwei966/awesome-ai-harness/pull/4) adds SandBase Harness to SDKs & runtimes. Maintainer review is pending; this is not an endorsement or security certification.

New sandbox directory review: [Awesome AI Coding Sandboxes PR #15](https://github.com/fhiltscher/awesome-ai-coding-sandboxes/pull/15) adds SandBase Harness to Adjacent runtimes. Maintainer review is pending; the entry preserves the provider-dependent isolation boundary.

Harness directory review: [Awesome Agent Harnesses PR #2](https://github.com/bayshier/awesome-agent-harnesses/pull/2) adds SandBase Harness to Platforms & Frameworks. Maintainer review is pending; this is not an endorsement or security certification.

Agent systems review: [Awesome Agent Harness PR #10](https://github.com/zients/awesome-agent-harness/pull/10) adds SandBase Harness to Agent Systems & Harnesses. Maintainer review is pending; model-provider and backend/deployment requirements remain explicit.

AI agent directory review: [Awesome AI Agents PR #184](https://github.com/NipunaRanasinghe/awesome-ai-agents/pull/184) adds SandBase Harness to Core Frameworks. Maintainer review is pending; this is not an endorsement or security certification.

Scope review: [E2B Awesome AI Agents Issue #1468](https://github.com/e2b-dev/awesome-ai-agents/issues/1468) asks whether SandBase Harness belongs as a distinct runtime entry from the closed CLI submission. Maintainer decision is pending; no inclusion or endorsement is claimed.

Runtime directory review: [Awesome AI Agents 2026 PR #240](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026/pull/240) adds SandBase Harness beside the separate CLI entry under Agent Tooling and Infrastructure. Maintainer review is pending; this is not an endorsement or security certification.

SDK/runtime directory review: [E2B Awesome AI SDKs PR #344](https://github.com/e2b-dev/awesome-ai-sdks/pull/344) proposes SandBase Harness for its SDKs, frameworks, libraries, and tools list. Maintainer review and CLA verification are pending.

New review path: [Awesome Agent Harnesses issue #4](https://github.com/NeuraLiying/Awesome-Agent-Harnesses/issues/4) suggests SandBase Harness for Production Harnesses, SDKs & Frameworks. Maintainer review is pending; no listing, endorsement, or security certification is claimed.

New MCP directory submission: [mcp.so intake comment](https://github.com/chatmcp/mcpso/issues/1#issuecomment-5472364196) provides the canonical repository, MCP server ID, v0.3.8 OCI image, and setup guide. Processing is pending; no listing or endorsement is claimed.

New survey scope review: [HKUST-KnowComp Awesome Agent Harness issue #8](https://github.com/HKUST-KnowComp/Awesome-Agent-Harness/issues/8) proposes SandBase Harness as a source-linked runtime resource. Curator review is pending; no research-paper, listing, endorsement, or security-certification claim is made.

Maintenance update: [Picrew Awesome Agent Harness PR #86](https://github.com/Picrew/awesome-agent-harness/pull/86) is synchronized with upstream `main` and now CLEAN/MERGEABLE. Review remains pending; unrelated baseline verifier findings are documented.

Public listing update: [Awesome Agent Operating Systems PR #13](https://github.com/frankxai/awesome-agent-operating-systems/pull/13) merged SandBase Harness into Agent Runtimes. The old PR #11 was superseded; no endorsement or security certification is claimed.

New LLMOps review: [TensorChord Awesome LLMOps PR #785](https://github.com/tensorchord/Awesome-LLMOps/pull/785) adds SandBase Harness to the catalog. It is OPEN/MERGEABLE; DCO completion is contributor-owned and maintainer review is pending.
