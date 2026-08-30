# X draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

An agent runtime needs more than a model call: it needs a place for sessions to persist, tools to pass through explicit controls, and runs to leave evidence.

SandBase Harness v0.3.8 is a local-first TypeScript runtime with an MCP bridge, persistent sessions, approvals, audit/replay, and Docker/Kubernetes/worker execution backends.

Try the MCP setup: https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md

DeepSeek Harness walkthrough: https://blog.sandbase.ai/deepseek-harness-developer-preview-2026/

Now publicly listed in Awesome AI Engineering: https://github.com/Eric-LLMs/Awesome-AI-Engineering/pull/4

New directory submissions are under review: MeshKore (#14) https://meshkore.com/submit and Agent Switchboard PR #44 https://github.com/assafbar2/agentswitchboard.dev/pull/44

Hugging Face agent-harness registry PR: https://github.com/huggingface/huggingface.js/pull/2432 (review pending)

Boundary: isolation depends on the selected deployment backend; this is not a universal microVM or kernel-isolation claim.
