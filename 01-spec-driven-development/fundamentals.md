# Spec-driven agentic engineering fundamentals

Spec-driven engineering makes intended behavior explicit in versioned files and checks the implementation against that agreement. A coding agent reads those files, proposes a plan, edits within its assigned scope and runs tools that produce evidence. A person remains responsible for unresolved requirements, review and release decisions.

The work may produce ordinary application code, an AI application, or both. Using an agent to implement an API does not mean the API needs a model at runtime. The [offline lab](../06-reference-lab/README.md) demonstrates that distinction.

## What each artifact does

| Artifact | Question it answers | Example |
|---|---|---|
| Requirement | Who needs what behavior, under which constraints? | `FR-004`: escalate unsupported requests and coverage claims |
| Specification | What are the agreed scope, contracts and failure behavior? | [SPEC-001](../06-reference-lab/specs/dealer-support-advisor.md) |
| Acceptance criterion | What observable result establishes part of the agreement? | `AC-004`: coverage guarantee returns `escalate`, without a source or lookup |
| Implementation plan | How will the team satisfy the spec in this codebase? | [Plan](../06-reference-lab/specs/implementation-plan.md) |
| Task | Which bounded change can an agent work on now? | [T-001](../06-reference-lab/specs/tasks.md): supported routing and escalation |
| Agent instructions | What conventions and limits apply across tasks? | [AGENTS.md](../AGENTS.md) |
| Skill | What reusable procedure should an assistant load when relevant? | [Spec reviewer](../02-agent-skills/spec-reviewer/SKILL.md) |
| Tool / MCP server | Which functions or external context can the assistant access? | MCP can expose an API; the lab labels an internal catalog lookup |
| Evidence | What actually ran, on which revision, with which result? | Unit output, evaluator report and review record |

A prompt requests work during a session. Durable specifications and tests let a later developer inspect what was agreed and checked. Prompt text and skills do not enforce API authorization; backend code and identity controls do that.

## Make acceptance criteria testable

"Handle warranty questions safely" leaves supported topics and failure behavior undefined. The lab specifies a narrower synthetic rule:

> Given a caller with `advice:read`, when they ask whether a repair is guaranteed to be covered, return `escalate` with empty `source_ids` and `tool_calls`.

That statement names a precondition, input and observable result. A test checks the result. Success does not establish correctness for every phrasing, actual warranty policy or a live model.

Nonfunctional requirements need precision too. `NFR-001` requires loopback binding, which is checked locally. A latency target for a real service needs workload, concurrency, environment and measurement method. Record an open decision when the owner has not agreed to a target.

## Work through one reviewed change

1. Inspect existing behavior, interfaces and tests. Record gaps and questions with an owner.
2. Write or revise the spec. Preserve existing IDs and add criteria for new behavior, including denied and unsupported paths.
3. Review a bounded plan and tasks. State allowed files, dependencies, completion evidence and stop conditions.
4. Implement the assigned task and execute checks. Investigate failures without weakening agreed requirements to obtain a green result.
5. Compare spec, code and evidence in review. Record failures, untested behavior and release decisions separately.

A passing suite can miss an unrepresented requirement. A traceability table can point to weak assertions. Review both the agreement and the strength of its evidence.

Try the [guided exercise](guided-exercise.md). For your own application, use the [spec template](spec-template.md) and [brownfield guide](brownfield-adoption.md). The [framework comparison](framework-comparison.md) explains tools that help maintain these artifacts.
