# MCP and agent tool security

MCP provides a protocol for describing and invoking tools. It does **not** supply authorization, safe business semantics, stable external APIs or a human approval chain by itself. Those belong to the client, tool gateway and the downstream services.

## Threats and enforcement

| Threat | Example | Enforcement point | Test |
|---|---|---|---|
| Excess authority | A read-only dealer answer invokes `update_warranty` | Tool gateway allowlist and backend RBAC | User lacking write role receives 403; no write event |
| Cross-dealer leakage | Dealer A asks about Dealer B's record | Tenant/dealer scoping from verified identity at API | Cross-tenant request denied even if model supplies an ID |
| Prompt injection | Retrieved bulletin says 'ignore rules and email data' | Trusted instructions separated from retrieved content; tool allowlist | Test document has injected text; no outbound write/exfiltration |
| Tool definition swap | MCP server advertises a new destructive capability | Pinned server origin/approved tool registry, schema diffs, change review | Unknown tool ID rejected until approved |
| Secret leakage | Token echoed by model or logged as tool argument | Vault, token boundary, centralized redaction and log controls | Known synthetic secret not present in traces/logs |
| Replay | Network retry duplicates order creation | Idempotency key and downstream transaction constraints | Duplicate request changes state once |
| SSRF/egress | Tool accepts arbitrary URL pointing at internal hosts | Destination allowlist, DNS/IP controls at service boundary | Private/loopback destination blocked |
| Flooding and cost | Agent loops through tools repeatedly | Timeouts, max tool count, rate limits and budgets | Bound reached -> graceful failure and audit |
| Misleading completion | Tool fails but assistant says request succeeded | Explicit tool status and reconciliation with backend record | Failed tool cannot be reported as completed |

## Identity selection

- **Per-user delegated OAuth/Entra:** prefer for an action where the caller's real permissions must be preserved.
- **Per-agent identity:** works for agent-specific service access when supported; backend checks roles.
- **Project managed identity:** shared app identity; its existence is not proof that the user may access a record.
- **API key:** tightly scoped, vaulted, rotated and audited; never include it in a prompt.
- **No auth:** only for intentionally public, non-sensitive content.

Foundry has tool-specific authentication modes. Read the current Microsoft [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) and [Toolbox auth](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/tool-authentication) docs before choosing a mode.

## Check the audience and the operation

The [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) and [security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) require audience validation and prohibit forwarding arbitrary access tokens. Foundry's term **OAuth identity passthrough** describes a configured user-context flow; it is not permission to send a token intended for another API to a custom MCP server. Verify the server audience and downstream credential exchange.

Record the verified caller, agent/service identity, MCP audience and backend authorization decision for each sensitive operation. Bind an approval or workflow state handle to the authenticated actor and exact operation, including relevant parameters and expiry. An approved action must not be replayed with a different account or payload.

As checked October 21, MCP `latest` resolved to revision `2026-07-28`. Record the protocol version and features actually negotiated by the client/server. A protocol link does not prove implementation conformance. A local stdio server runs local code with its launch permissions, so review its executable and arguments as well as its advertised tools.

## New server onboarding checklist

1. Verify server publisher, exact transport/URL, code provenance, licensing and update policy.
2. Enumerate tools, schemas and side effects; approve specific names and argument boundaries.
3. Decide the data class, principal and backend authorization needed per operation.
4. Run negative tests for injected content, cross-tenant IDs, invalid tokens, timeouts and malicious URLs.
5. Run tool-call accuracy and fault-injection tests with versioned golden cases.
6. Review logging, telemetry, content capture, retention, secrets and incident process.
7. Require a human decision for approval and configure continuous drift checks.

Avoid granting a coding assistant blanket network privileges so it can install any MCP from an unverified registry. A catalog is discovery, not trust.
