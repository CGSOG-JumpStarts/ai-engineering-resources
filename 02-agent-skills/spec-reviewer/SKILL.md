---
name: spec-reviewer
description: Review functional and nonfunctional feature specifications, acceptance criteria, task traceability and implementation readiness before an AI coding session. Use for PRDs, user stories, brownfield changes and spec-driven development handoffs.
license: MIT
---

# Specification reviewer

## Input

Read the approved or draft spec, related API schema, implementation plan, affected test names and repo conventions. If one is absent, mark it **not supplied** rather than fabricating it.

## Review procedure

1. Extract every stable requirement ID, acceptance criterion, actor, trigger, expected behavior, error condition and dependency.
2. Check that behaviors can be independently observed and tested; identify unclear words such as 'fast', 'secure' or 'intuitive' without measures.
3. Check *negative* cases: permissions denied, unsupported requests, dependency timeouts, invalid input, empty outputs, idempotent retries and version compatibility.
4. Check nonfunctional scope: authn/authz, privacy, retention, tracing, performance under defined load, accessible UX where relevant, deployment/rollback.
5. Map criteria to planned tasks and test IDs. Identify uncovered IDs rather than inventing test pass/fail results.
6. Return the smallest set of **blocking** questions that prevent a safe implementation, followed by nonblocking improvements. Do not rewrite the spec's business decisions without approval.

## Output

| ID | Severity | Source clause | Finding and risk | Proposed change | Owner |
|---|---|---|---|---|---|

Then report: `ready`, `ready-with-notes` or `blocked`, the requirement-to-test matrix, evidence paths and unknowns. A 'ready' result is only a document-review judgment. Tests and human approval remain mandatory.

## Guardrail

Do not mark a requirement implemented simply because a task is checked. Only verified test evidence, review and observed outcomes support that claim.
