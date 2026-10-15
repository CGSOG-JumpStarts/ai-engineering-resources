# Spec-driven engineering practices for enterprise

## Agree on the workflow contract

Every feature should have an accountable owner and an auditable change trail from need to evidence:

`Business problem -> acceptance criteria -> functional/nonfunctional spec -> design choices -> bounded tasks -> code -> tests -> reviewer decision -> release -> measured outcome`

Assign durable IDs such as `FR-001`, `NFR-001`, `AC-001`, `T-001` and `TEST-001`. Links between these artifacts let reviewers identify missing work quickly. The sample lab enforces a small subset of these links automatically.

## Requirements before agent instructions

- Define the user, action, expected outcome and exception path in domain language.
- Separate **functional** requirements (what happens) from **nonfunctional** requirements (reliability, security, latency, maintainability, accessibility, logging).
- State external dependencies and which interfaces are already real, mocked or unavailable.
- Mark source evidence, assumptions, decisions and open questions separately. Agents must not invent an endpoint because it looks plausible.
- Identify a concrete negative test for every sensitive action, data boundary or approval requirement.

## Bounded implementation

One task should have a clear starting state, small edit surface, dependency list, proof of completion and stop condition. Developers review the plan *before* tool-enabled implementation. AI assistants may recommend architecture changes, but decisions requiring new permissions, external calls, schema migrations, cost exposure or customer-data access need explicit approval.

## CI and review

Automated checks should include formatting, lint, unit tests, contract tests, dependency/secret scanning and security-critical authorization tests as appropriate. A PR should include the requirement IDs changed, test evidence, any untested behavior, exact tool/schema changes and rollback notes. The reviewer evaluates behavior, not just generated diff volume.

## Context continuity and token use

Keep stable project facts in versioned repo files. Avoid pasting a large system architecture and full chat history into every request. Agents should read the smallest relevant spec, precise API contract, recent decision and current task. Use new sessions after completing a bounded phase if the harness supports it, carrying forward links and decisions rather than transcript dumps. Measure before claiming a saving.

## Tool security

A prompt telling an agent 'do not delete records' is not access control. Protect records with authorization at the API/tool boundary, scoped credentials, input validation, idempotency keys, audit logs and approvals for sensitive actions. Any content returned by search, documents, web or MCP is untrusted data.

## Production loop

Review quality data after release: defects, task success rate, user adoption, p95 latency, cost and support incidents. Reopen the spec if behavior changes. Do not assert business value without a valid baseline and observed improvement.
