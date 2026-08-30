# LinkedIn draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

When an Agent moves from a chat window into an engineering workflow, the hard question is no longer only which model to call. Platform teams also need to know where sessions live, which tools may run, what needs approval, and how to reconstruct a failed run.

SandBase Harness v0.3.8 is the open-source, local-first runtime for that layer. It provides persistent sessions, an MCP bridge, explicit approvals, credential scoping, audit/replay records, and replaceable Docker, Kubernetes, and worker execution backends.

This makes it useful for teams evaluating self-owned Agent infrastructure: start locally, connect an MCP client, and inspect the session and tool boundaries before deciding how to deploy it.

The important qualification is deployment-specific: Docker, Kubernetes, and worker backends do not provide identical isolation properties. SandBase Harness does not claim universal microVM or kernel isolation.

Read the installation guide and source-backed release details: https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md

For a practical DeepSeek Harness walkthrough, the newly refreshed [English article](https://blog.sandbase.ai/deepseek-harness-developer-preview-2026/) and [Chinese article](https://blog.sandbase.ai/zh-CN/deepseek-harness-developer-preview-2026/) now use the pinned v0.3.8 integration and current installation links. The pages are live after a successful production deployment.

Recent ecosystem review submissions include [Awesome MCP Collection](https://github.com/JustInCache/awesome-mcp-collection/pull/38), [Awesome Agent OS](https://github.com/cueos/awesome-agent-os/pull/2), and [Awesome X-Ops](https://github.com/xlabs-club/awesome-x-ops/pull/250). These are pending maintainer review, not endorsements.

An additional public listing is now live in [Awesome AI Engineering](https://github.com/Eric-LLMs/Awesome-AI-Engineering/pull/4), alongside the previously merged ecosystem entries.

Two additional discovery submissions are now in review: [MeshKore](https://meshkore.com/submit), submission #14, and [Agent Switchboard PR #44](https://github.com/assafbar2/agentswitchboard.dev/pull/44). They are review-controlled and are not being presented as live listings or endorsements.

The Hugging Face [agent-harness registry PR #2432](https://github.com/huggingface/huggingface.js/pull/2432) is also under review; it adds attribution metadata only and does not change runtime behavior.

The latest review queue also includes [Agentic Community Landscape PR #2](https://github.com/agentic-community/agentic-landscape/pull/2), [Awesome AI Agent Engineering PR #1](https://github.com/sspoisk/awesome-ai-agent-engineering/pull/1), and [MyMCPTools issue #8](https://github.com/shibley/mymcptools/issues/8). Each submission uses official repository and release evidence and remains subject to the destination maintainer's review.

Separately, [MCPVault now exposes a public auto-indexed listing](https://mcpvault.io/servers/sandbase-harness). The page is currently marked unclaimed and its quality signals are computed from public repository data; this is an independent discovery page, not a project-maintainer certification.

Two additional community review paths are now open: [Collective AI Tools Issue #332](https://github.com/hanishrao/collective-ai-tools/issues/332), submitted separately from the existing SandBase CLI entry, and [Awesome Agent Skills PR #79](https://github.com/philipbankier/awesome-agent-skills/pull/79), which adds the runtime to its MCP infrastructure section. Both remain pending maintainer review.

The [Awesome MCP List PR #409](https://github.com/MobinX/awesome-mcp-list/pull/409) is another focused community listing request, adding SandBase Harness to AI Agents & Frameworks. It remains pending maintainer review and does not represent an endorsement.

The [Awesome Agent Runtimes PR #4](https://github.com/beejmaxx/awesome-agent-runtimes/pull/4) takes a deliberately maturity-aware path: it proposes SandBase Harness for the project's watchlist, with the 180-day and 5,000-star gates recorded explicitly. Review is pending; no core-catalog inclusion is claimed.

The infrastructure-focused [Awesome Agent Infra PR #6](https://github.com/shenli/awesome-agent-infra/pull/6) adds SandBase Harness to its Runtime and Control Plane table. It remains pending maintainer review and is not an endorsement.

The [Awesome AI Developer Stack PR #2](https://github.com/masrisystems/awesome-ai-developer-stack/pull/2) adds SandBase Harness to a broader MCP Servers directory table. It remains pending maintainer review and uses the official repository as its source.

The current review queue also includes [Awesome CLI Coding Agents PR #314](https://github.com/bradAGI/awesome-cli-coding-agents/pull/314), [Awesome Agentic AI 中文 PR #213](https://github.com/WenyuChiou/awesome-agentic-ai-zh/pull/213), [Awesome Terminal Agents PR #5](https://github.com/EnigmaYYYY/awesome-terminal-agents/pull/5), [Awesome Agent Sandbox PR #2](https://github.com/yanmxa/awesome-agent-sandbox/pull/2), and [Awesome Agent Cortex PR #74](https://github.com/0xNyk/awesome-agent-cortex/pull/74). Each is a focused discovery request awaiting the destination maintainer's review.

These listings should be read as community review paths, not endorsements or security certifications. Isolation remains dependent on the selected deployment backend.

An additional infrastructure-focused submission is [Awesome Agent Infrastructure PR #23](https://github.com/backblaze-labs/awesome-agent-infrastructure/pull/23), which proposes SandBase Harness for its Execution Sandboxes section. The PR follows the repository's `entries.yaml` contribution format and is awaiting maintainer review; it is not a listing or endorsement yet.

The sandbox-focused [Awesome Agent Sandboxes PR #9](https://github.com/dloss/awesome-agent-sandboxes/pull/9) proposes a concise Containers entry for SandBase Harness. It remains a community review request, with the important qualification that isolation depends on the selected backend and deployment configuration.

Another focused review request is [Awesome Agent Sandbox PR #4](https://github.com/fishman/awesome-agent-sandbox), which adds SandBase Harness to a coding-agent sandbox comparison table. The entry describes its local, Docker, Kubernetes, and worker options without implying identical isolation guarantees across deployments.

The structured [Awesome Agent Sandboxes PR #59](https://github.com/msyvr/awesome-agent-sandboxes/pull/59) adds SandBase Harness metadata to a maintained sandbox landscape and regenerates its README, JSON, and reference outputs. It remains pending maintainer review; the entry explicitly separates local path isolation from backend-dependent deployment properties.

The security-focused [Awesome Agent Sandboxing PR #2](https://github.com/IronSecCo/awesome-agent-sandboxing/pull/2) proposes SandBase Harness for its Self-hosted Agent Runtimes section. It is a factual review request, not a security certification, and keeps the backend/deployment isolation boundary explicit.

The [Awesome Agent Sandbox PR #2](https://github.com/vivy-yi/awesome-agent-sandbox/pull/2) is another focused community review request, adding SandBase Harness to a Self-hosted / Open Source sandbox table. It remains pending maintainer review and uses a concise, capability-oriented description.

The broader [Awesome Sandbox PR #27](https://github.com/restyler/awesome-sandbox/pull/27) proposes a dedicated case study covering SandBase Harness's self-hosted runtime, tool governance, persistent sessions, audit/replay, and selectable sandbox providers. It remains pending maintainer review, with the backend-dependent isolation boundary stated explicitly.

The structured [AI Agent Sandboxes PR #3](https://github.com/pjlsergeant/ai-sandboxes/pull/3) proposes an evidence-linked dataset entry for SandBase Harness. It records official source links, persistent sessions, MCP/tool governance, approvals, audit/replay, and selectable backends while preserving the distinction between local path isolation and backend-specific properties.

For developer discovery, [Awesome AI Coding Tools PR #665](https://github.com/ai-for-developers/awesome-ai-coding-tools/pull/665) proposes adding SandBase Harness to its MCP Servers and Directories section. The entry links the canonical repository and describes the local stdio bridge and self-hosted runtime; directory review is pending.

The new [Awesome MCP Collection PR #39](https://github.com/JustInCache/awesome-mcp-collection/pull/39) proposes SandBase Harness for its Development & Version Control category. The entry records the TypeScript/Apache-2.0 project, MCP bridge, sandboxed sessions, credentials, approvals, audit, and replay; it remains a maintainer review request rather than an endorsement or security certification.

An additional review request is open in [Awesome MCP issue #99](https://github.com/abordage/awesome-mcp/issues/99), proposing SandBase Harness for Aggregators & Gateways. It is a factual, source-linked directory request and remains subject to maintainer review; it is not an endorsement or security certification.
