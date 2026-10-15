---
name: spec-driven-delivery
description: Turn a bounded engineering change into a reviewable specification, implementation plan, atomic tasks, acceptance tests and decision log. Use before asking a coding agent to implement business features, APIs, migrations or agent tools, especially when permissions and nonfunctional requirements matter.
---

# Spec-driven delivery

## Procedure

1. Read nearest `AGENTS.md` and related interfaces/tests. Summarize the existing system's **verified** behavior and constraints. Treat source code as evidence, not license to invent business rules.
2. Clarify actor, objective, scope exclusions, business rules and edge cases. Use templates from `01-spec-driven-development/` to create requirement IDs (`FR-`, `NFR-`) and measurable acceptance criteria.
3. Identify sensitive inputs, caller identity, tenant/data entitlement, backend tool contracts, write effects, retries, stale data and failure modes.
4. Produce a plan with impact by module, dependencies, rollback, test mapping and human decisions. Stop for approval before changes with data, permission, schema, cost or deployment implications.
5. Split the approved plan into independently testable tasks. Implementation must not quietly extend scope. Keep deterministic controls in code and tests.
6. Run available validation and tests. Report **actual executed commands** and results, mapped to requirement IDs; missing tests are unfinished work, not an acceptable substitute for evidence.
7. Update the spec and dated decisions for legitimate changes. Preserve rejected options and design tradeoffs rather than rewriting requirements after the fact.

## Outputs

- Feature `spec.md` with stable FR/NFR IDs and actor/authorization matrix
- `plan.md` with files, data contracts, risks and rollback
- `tasks.md` with acceptance evidence
- Traceability from requirement IDs to concrete test names
- Dated ADR when a choice affects multiple features

Use `references/review-checklist.md` at the end. See `06-reference-exercise/dealer-advisor/specs/` for a filled example.
