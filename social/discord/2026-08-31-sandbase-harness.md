# Discord draft — SandBase Harness v0.3.8

Status: NEEDS REVIEW — operator review and account authorization required

For builders testing a self-owned Agent runtime, SandBase Harness v0.3.8 provides:

- persistent sessions and resumable runtime state;
- an MCP bridge with explicit tool boundaries;
- approvals, credential scoping, audit, and replay;
- Docker, Kubernetes, and worker execution backends.

Start with the [MCP installation guide](https://github.com/sandbaseai/sandbase-harness/blob/main/docs/installation.md) and the [v0.3.8 release](https://github.com/sandbaseai/sandbase-harness/releases/tag/v0.3.8). Isolation is deployment-dependent, so the backends should be evaluated separately; this project does not claim universal microVM or kernel isolation.

Feedback and deployment reports: https://github.com/sandbaseai/sandbase-harness/discussions/116
