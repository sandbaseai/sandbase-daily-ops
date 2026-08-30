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
