# Spec-driven engineering practices

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

## Size the plan to the change

The following is a repository recommendation, not a company approval policy. Use the smallest agreement that exposes the unresolved decisions and gives a reviewer a reliable check.

| Change | Useful agreement and evidence |
|---|---|
| Isolated edit with understood behavior | Bounded task, preserved behavior and focused check/review |
| Feature with new observable behavior | Spec, acceptance criteria, implementation plan and affected negative tests |
| Uncertain integration or permission change | Evidence for open decisions, interface/identity contracts, failure cases and an approved plan |

Research a specific gap: an unknown API contract, an undocumented dependency or a behavior the tests do not explain. Reuse adequate evidence. [HVE RPI](https://raw.githubusercontent.com/microsoft/hve-core/main/docs/rpi/README.md) and [BMad planning](https://docs.bmad-method.org/plan/choose-a-planning-path/) support selective research and smaller paths; the table above is this package's suggested application of that guidance.

## Keep specifications current deliberately

Name the authoritative specification and its owner. Label each document as a current contract, a historical delivery record or a draft. When intent changes, preserve IDs, record the decision and reconcile the spec, plan, tasks and tests. Link superseded records rather than silently making an old delivery spec appear current.

In the synthetic lab, code that answers a coverage guarantee conflicts with `AC-004`, which requires escalation. Report a defect. If an owner later approves different behavior for a separate application, revise that application's requirement and failure tests before implementing it. Do not let generated code establish its own intended behavior.

Spec Kit's [spec-maintenance guidance](https://github.github.io/spec-kit/guides/evolving-specs.html) leaves this maintenance convention to the team. Consistency analysis and convergence findings are review inputs; neither grants permission to rewrite requirements to match a surprising implementation. Review framework/template upgrades separately from changes of application intent.

## CI and review

Automated checks should include formatting, lint, unit tests, contract tests, dependency/secret scanning and security-critical authorization tests as appropriate. A PR should include the requirement IDs changed, test evidence, any untested behavior, exact tool/schema changes and rollback notes. The reviewer evaluates behavior, not just generated diff volume.

## Context continuity and token use

Keep stable project facts in versioned repo files. Avoid pasting a large system architecture and full chat history into every request. Agents should read the smallest relevant spec, precise API contract, recent decision and current task. Use new sessions after completing a bounded phase if the harness supports it, carrying forward links and decisions rather than transcript dumps. Measure before claiming a saving.

## Tool security

A prompt telling an agent 'do not delete records' is not access control. Protect records with authorization at the API/tool boundary, scoped credentials, input validation, idempotency keys, audit logs and approvals for sensitive actions. Any content returned by search, documents, web or MCP is untrusted data.

## Production loop

Review quality data after release: defects, task success rate, user adoption, p95 latency, cost and support incidents. Reopen the spec if behavior changes. Do not assert business value without a valid baseline and observed improvement.
