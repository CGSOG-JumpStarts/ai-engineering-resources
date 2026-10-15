# Agent/MCP evaluation implementation checklist

A tool-call evaluation should include four independently observable parts:

1. **The request:** actor or approved test role, dealer scope, intent and allowed tools.
2. **The agent decision:** selected tool, arguments and proposed result, with prompt/model/skill version.
3. **The tool execution:** validated principal, typed inputs, policy outcome, returned data or failure and duration.
4. **The displayed answer:** claims supported by tool return, uncertainty, user action and source references.

Do not let an agent output its own passing score without independent execution evidence. Authorization should be checked at the tool/service boundary, even if a prompt says "only access your dealer".

## Suggested small evaluation record

```json
{
  "case_id": "lookup-allowed-01",
  "principal": "synthetic-dealer-a",
  "expected_calls": [{ "tool": "inventory_lookup", "args": { "dealer_id": "D-A", "sku": "PART-100" } }],
  "forbidden_side_effects": true,
  "expected_status": "available"
}
```

This is an illustrative schema. The runnable fixture scorer has its own explicit JSON format documented in its header.

## Production tracing fields

Capture correlation/request ID, deployment and agent version, model version, tool name, sanitized parameters or parameter hashes, role/identity category, authorization decision, latency, input and output tokens, errors and human approval reference where applicable. Scrub PII, secrets and unapproved source text. Use appropriate retention controls. Trace **why** an action was allowed or rejected without writing credentials to logs.

For Foundry, inspect its Application Insights/OpenTelemetry and evaluation integration from official product docs. [Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | [Hosted Agent observability](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents).

## Regression trigger list

Re-run when model, prompt, tool schema, skill, retrieval index, policy, permissions, SDK/runtime, hosted version, network, or retry configuration changes. Maintain a small set of blocking cross-tenant and write-action tests alongside the broader quality dataset.
