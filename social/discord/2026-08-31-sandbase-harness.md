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
