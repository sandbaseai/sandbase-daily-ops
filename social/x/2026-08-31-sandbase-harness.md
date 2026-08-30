# X draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

An agent runtime needs more than a model call: it needs a place for sessions to persist, tools to pass through explicit controls, and runs to leave evidence.

SandBase Harness v0.3.8 is a local-first TypeScript runtime with an MCP bridge, persistent sessions, approvals, audit/replay, and Docker/Kubernetes/worker execution backends.

Try the MCP setup: https://github.com/sandbaseai/sandbase-harness/blob/main/docs/mcp-install.md

Boundary: isolation depends on the selected deployment backend; this is not a universal microVM or kernel-isolation claim.
