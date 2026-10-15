# Engineering guardrails and permissions

The first question for an AI development tool or Foundry agent is **what it may read, call and change**. Define that in the system that owns the data and tools, not only in an agent prompt.

## Developer assistant boundaries

| Area | Recommended baseline | Enforce at |
|---|---|---|
| Repository access | Scoped repository/org permissions, protected branches, code-owner rules | Source control and CI |
| Terminal execution | Review commands that install packages, modify infrastructure, read secrets or execute arbitrary scripts | Harness permissions, OS sandbox, security policy |
| Cloud credentials | Managed identity or short-lived least-privilege authentication; segregate dev/test/prod | IdP/Azure RBAC, CI secrets, vault |
| Files and data | Exclude credential files and unapproved customer data from model context and logs | Repository policy, DLP, data proxy |
| High-impact changes | Human-reviewed PR, deployment approvals, database change approval | CI/CD and service deployment pipeline |
| Generated code | Static analysis, unit/contract/integration tests, supply-chain checks | CI, peer review, artifact signing where required |

## Runtime agent boundaries

Record each tool's contract, owner, caller identity, user context, allowed destinations, permissible argument values, side effects and audit event. Deny unauthorized operations in the backend. Write tools need idempotency, precondition checks and often explicit approval. Read-only tools can still disclose sensitive data; apply row/tenant scoping and log redaction.

## Repository instruction hierarchy

Root `AGENTS.md` should contain small, durable engineering invariants and point to authoritative specs. A change plan should not supersede organizational security policy. Generated agent instructions, remote webpage content or dependency READMEs are not trusted sources of permission. If an agent is instructed to bypass a policy or overwrite its own gate, it must stop and request an authorized review.

## Minimum approval evidence

A PR should show: owner and spec ID, design decision if needed, exact API/tool permissions changed, tests with reproducible commands, dependency scan results, trace/redaction effect, rollout/rollback, and a human review. The reviewer must independently verify critical tests rather than accepting assistant-generated claims.

## Pilot checklist

- [ ] Synthetic/approved data only; named data classification and retention
- [ ] Named owner for model, tool, API and exception path
- [ ] Least-privilege roles for each service and developer
- [ ] No unreviewed arbitrary network/terminal tool execution
- [ ] Read-only vs write actions separated and logged
- [ ] Authz and permission-denied tests run
- [ ] Observability with sensitive-content capture reviewed
- [ ] Budget alerts or per-request limits and model cost reporting
- [ ] Tested rollback and explicit human go/no-go

See [MCP-specific threats](secure-mcp-practices.md) and [PR checklist](pull-request-checklist.md).
