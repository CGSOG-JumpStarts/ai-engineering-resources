---
name: secure-mcp-review
description: Threat-review an MCP server or agent tool integration for authentication, authorization, data access, prompt injection, side effects, least privilege and audit evidence. Use before enabling a new tool in a Microsoft Foundry agent or coding assistant.
license: MIT
---

# MCP / agent-tool security review

## Input and discovery

Request the server's maintainer/source, exact operations and side effects, base URL, data classes, desired client identity, target permission boundary, deployment environment and rollback path. Never request raw credentials. If a tool schema or contract is unavailable, mark it as a blocker for enabling write actions.

## Procedure

1. Classify each operation: read-only, write, destructive, privileged. Assign required roles and request context.
2. Decide identity: per-user OAuth/Entra passthrough, scoped agent identity, project managed identity or a narrowly scoped key. Shared identities must not silently impersonate end users.
3. Verify the API/tool implementation independently authorizes each request. Prompt instructions do not substitute for authz.
4. Trace data paths: model input, tool arguments, MCP response, logs/traces and downstream storage. Define redaction, retention and tenant boundaries.
5. Test the server against untrusted tool output, injected instructions, suspicious URLs, data exfiltration attempts, excessive payloads, timeouts, retries and unauthorized parameters.
6. Require human confirmation for destructive or high-impact side effects; use idempotency and replay protection where applicable.
7. Provide a allow/hold/block decision per tool, a test matrix and the exact evidence still needed.

## Output

- Tool register: name, operation, classification, principal, scopes, approved destination, audit event, approval requirement.
- Threat table: attack scenario, impact, concrete enforcement point, test and owner.
- Deployment decision: `approved-limited`, `needs-remediation` or `blocked`; this is advice for an authorized human reviewer, not a claim that policy has approved it.

Read [the MCP practices guide](../../04-engineering-guardrails/secure-mcp-practices.md) if operating within the full package. Outside this ZIP, follow the same approach without relying on that optional relative file.
