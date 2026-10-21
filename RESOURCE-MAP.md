# Resource map

This map covers the technical questions the package supports. Exercises use synthetic examples. Suggested artifacts are review aids, not company policy or evidence of completed work.

For sequential reading, start with [the code companion](GUIDE.md). It follows a single application from request to evidence. Use the table below as a reference index after the walkthrough, and the [companion source index](examples/companion/README.md) to find complete runnable examples.

| Question | Read | Try or produce |
|---|---|---|
| What does spec-driven engineering involve? | [Fundamentals](01-spec-driven-development/fundamentals.md) | Trace one acceptance criterion to its executed test |
| Which workflow should we try? | [Comparison](01-spec-driven-development/framework-comparison.md), [setup](01-spec-driven-development/tools-quickstart.md) | Record one workflow's version and selection reason |
| How do we write actionable requirements? | [Practices](01-spec-driven-development/recommended-practices.md), [spec template](01-spec-driven-development/spec-template.md) | Functional/nonfunctional requirements, negative cases and open questions |
| How does an agent implement a reviewed change? | [Example](01-spec-driven-development/example-workflow.md), [exercise](01-spec-driven-development/guided-exercise.md), [prompts](01-spec-driven-development/example-prompts.md) | Spec, bounded plan/task, test evidence and reviewer decision |
| How do we start in an existing codebase? | [Brownfield guide](01-spec-driven-development/brownfield-adoption.md) | Current-behavior evidence and regression/rollback plan |
| Which skills can we reuse? | [Catalog](02-agent-skills/README.md), [skill checks](02-agent-skills/skills-tests.md) | Review and trial one skill against expected behavior |
| How do we check current Foundry guidance? | [Docs adviser](02-agent-skills/foundry-docs-advisor/README.md), [sources](SOURCES.md) | Dated official references, feature status and environment questions |
| What runs in a hosted container or our own service? | [Foundry guide](03-azure-ai-foundry/platform-guide.md), [architecture](03-azure-ai-foundry/reference-architecture.md) | [Hosting decision record](03-azure-ai-foundry/adr-hosting-template.md) |
| What must remain outside model instructions? | [Instructions](04-engineering-guardrails/agent-instructions.md), [MCP security](04-engineering-guardrails/secure-mcp-practices.md), [data handling](04-engineering-guardrails/data-handling.md) | Tool/identity/permission matrix and backend denial tests |
| How do we reduce repeated context and token use? | [Context guidance](04-engineering-guardrails/context-and-token-efficiency.md) | [Session handoff](04-engineering-guardrails/session-handoff-template.md) and measured cost per accepted change |
| How do we compare models and tool behavior? | [Evaluation](05-evaluation/README.md), [model selection](05-evaluation/model-selection.md) | Fixed cases, actual traces and a [scorecard](05-evaluation/scorecard-template.md) |

Use [Start here](START-HERE.md) for a short sequence and the [October 2026 update](reports/October%202026%20engineering%20update.md) for the reasoning behind the newer guidance. A team can review these resources independently; no workshop or commercial engagement is assumed.
