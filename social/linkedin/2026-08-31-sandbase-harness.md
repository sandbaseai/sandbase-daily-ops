# LinkedIn draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

When an Agent moves from a chat window into an engineering workflow, the hard question is no longer only which model to call. Platform teams also need to know where sessions live, which tools may run, what needs approval, and how to reconstruct a failed run.

SandBase Harness v0.3.8 is the open-source, local-first runtime for that layer. It provides persistent sessions, an MCP bridge, explicit approvals, credential scoping, audit/replay records, and replaceable Docker, Kubernetes, and worker execution backends.

This makes it useful for teams evaluating self-owned Agent infrastructure: start locally, connect an MCP client, and inspect the session and tool boundaries before deciding how to deploy it.

The important qualification is deployment-specific: Docker, Kubernetes, and worker backends do not provide identical isolation properties. SandBase Harness does not claim universal microVM or kernel isolation.

Read the installation guide and source-backed release details: https://github.com/sandbaseai/sandbase-harness/blob/main/docs/mcp-install.md
