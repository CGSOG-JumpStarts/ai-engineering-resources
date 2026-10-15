# Choosing a first workflow

Do not make the framework itself the pilot goal. Choose a problem with an owner, an expected outcome and an independent acceptance test.

## If the work is a change to the dealer portal

Use a **brownfield-first** process. Record existing behavior, a short dependency map, the interface contract, tests that prove no regression and the planned rollback. Start with current repo conventions or Spec Kit. If the work is complex and uncertain, review HVE Core RPI as an additional method, rather than mixing its files with Spec Kit automatically.

## If the work is a new stakeholder advisory agent

Define allowed knowledge and tools, unsupported requests, authorization at the tool boundary, trace events, groundedness checks, review thresholds and exception handling before choosing a prompt or runtime. Treat a model as one component of a larger service. Read [Foundry architecture](../03-azure-ai-foundry/reference-architecture.md) and the [evaluation plan](../05-evaluation/agent-tool-evaluation.md).

## If PMs and BAs need to participate before engineering

Try BMad v6.12 with clear handoffs from business problem to functional specification and acceptance criteria. Compare the overhead to a lighter workflow with the same requirements. Avoid adopting every persona or ritual by default.

## If there is a desire for one lifecycle from discovery to production feedback

Review the optional AutoNav reference with its owner. Confirm access, runtime compatibility and the actual released version before proposing a rollout. The owner-provided README describes separate lifecycle phases and human gates. That description is not an independently verified production claim.

## The decision to record

Use `templates/decision-record.md`. Assign one owner, a repository or synthetic testbed, an initial scope, a 2–4 week observation window **as a suggested pilot cadence rather than a delivery estimate**, a list of disallowed data/tools, and stop criteria. Keep a counterfactual baseline such as current Copilot use without a workflow framework.
