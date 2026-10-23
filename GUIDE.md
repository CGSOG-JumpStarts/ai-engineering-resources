# Spec-driven engineering: a code companion

A developer receives a request: help users find the right support process. A coding assistant could turn that sentence into a convincing interface in a few minutes. The harder questions remain: which questions can it answer, whose data can it use, what should it refuse, and how will another developer check the result?

This guide follows those questions through a small working application. You will read its agreement, call its service, inspect a test, strengthen a regression check, send HTTP requests and interpret evaluation results. The example stays the same throughout so that each decision has a visible consequence in code.

The setting is a **fictional dealer-support portal**. Its catalog contains invented process guidance, not warranty policy, stock information or customer records. The application uses deterministic Python rules and no model. You can study the engineering loop before choosing a coding assistant or a cloud runtime. When you do use an assistant, the same specification and executable evidence give it a bounded job.

You need Python 3.10+ and enough Python familiarity to read a function and an assertion. Everything uses the standard library. Commands start at the repository root unless a chapter says otherwise. On Windows, substitute `py -3` or an installed interpreter path if `python` is not configured. No package installation, credentials or cloud account is required.

## Contents

1. [A first answer](#1-a-first-answer): meet the service and its boundaries.
2. [Read the contract](#2-read-the-contract): follow one requirement to a real test.
3. [Make a bounded change](#3-make-a-bounded-change): turn a concern into a reviewable regression exercise.
4. [Cross the HTTP boundary](#4-cross-the-http-boundary): distinguish malformed requests from denied actions.
5. [Read evaluation evidence](#5-read-evaluation-evidence): find failures hidden by an aggregate score.
6. [Work with a coding assistant](#6-work-with-a-coding-assistant): carry the agreement between sessions.
7. [Take the contracts to an agent runtime](#7-take-the-contracts-to-an-agent-runtime): decide what a model, tools and Foundry would add.

The [companion source index](examples/companion/README.md) maps chapters to complete programs. Run the four examples that need no sockets with:

```bash
python examples/companion/run_all.py
```

Read the chapters before using the programs as a regression check. A successful command is more useful when you understand what would make it fail.

## 1. A first answer

Start below the browser and HTTP layers. The service accepts a question and a principal, then returns a structured answer. Run:

```bash
python examples/companion/first_answer.py
```

Expected output:

```text
supported: answered; sources=['SYN-FAQ-PARTS-01']; tools=['lookup_approved_catalog']
coverage: escalate; sources=[]; tools=[]
cross-dealer: denied; sources=[]; tools=[]
missing-scope: denied; sources=[]; tools=[]
4 examples verified; model calls: 0
```

Open [first_answer.py](examples/companion/first_answer.py). After its repository-path setup and imports, the essential call is:

```python
reader = DemoPrincipal("SYN-DEALER-100", frozenset({"advice:read"}))
result = AdviceService().answer("Where can I ask about parts?", reader)
```

`DemoPrincipal` is supplied by the local host. It simulates trusted context for teaching; constructing it is not authentication. In a real service, a verified identity layer would establish the caller and permissions before this decision.

Read [AdviceService.answer](06-reference-lab/src/dealer_advisor/advisor.py). The order matters. It validates input, checks read scope, checks prohibited requests, checks unsupported coverage claims, and only then selects a supported catalog entry. Consider a question that mentions parts and also asks to change another account. Finding the word "parts" first must not make the prohibited request acceptable.

An answered result points to a record in [the synthetic catalog](06-reference-lab/src/dealer_advisor/catalog.py). Its source ID is stable and inspectable. `lookup_approved_catalog` is an internal label; there is no remote tool or MCP server behind it. The returned request ID changes between calls, so the example checks behavior without hardcoding that value.

**Try it:** change a question in your practice copy of `first_answer.py`, then predict its result before running it. "Is the repair covered?" should escalate. "Where can I ask about parts?" should answer. If you choose unfamiliar wording, treat the observed classification as a property to inspect, not proof that the rule engine understands arbitrary language. These regular expressions are deliberately limited.

You have now observed three domain outcomes. The next task is to find where the team agreed to them.

## 2. Read the contract

Open [SPEC-001](06-reference-lab/specs/dealer-support-advisor.md). `FR-004` requires escalation for unsupported requests and coverage guarantees. `AC-004` makes one part observable: unsupported coverage guarantees return `escalate`, with no source or tool invocation.

The functional requirement describes the behavior to provide. The acceptance criterion gives the reviewer something concrete to check. Neither is an implementation instruction to use a particular regular expression. That choice belongs in the plan and code.

Follow the link mechanically:

```bash
python examples/companion/trace_contract.py
```

The program reads the real specification and [traceability file](06-reference-lab/specs/traceability.json), then prints the mapped test's actual source. The relevant mapping is:

```json
{
  "ac": "AC-004",
  "test_file": "tests/test_guardrails.py",
  "test_method": "test_ac_004_policy_claim_escalation",
  "requirements": ["FR-004"]
}
```

The printed test calls the service with a coverage question and compares `(status, tool_calls, source_ids)` with `("escalate", (), ())`. Checking the whole tuple matters. An implementation that escalates only after looking up data would satisfy a status-only assertion and violate the intended no-lookup behavior.

The trace program locates source; it does not execute tests. Execute the mapped test family from the lab directory:

```bash
cd 06-reference-lab
python -m unittest discover -s tests -p test_guardrails.py -v
python scripts/validate_contracts.py
cd ..
```

The validator checks that declared criteria map to existing methods and requirements. It does not decide whether an assertion is strong enough or whether the requirement is correct. A reviewer still needs to read the criterion, the assertion and the behavior under test.

**Check your understanding:** would a test that asserts only `result.answer` is nonempty establish `AC-004`? No. An invented coverage promise would also be nonempty. The agreement concerns escalation and absence of sources/tools, not the presence of a sentence.

## 3. Make a bounded change

A reviewer notices that the spec does not separately name mixed supported/prohibited intent. The application already denies some such requests, and an existing test checks one example. You can make that behavior easier to review without inventing a new feature.

The [guided exercise](01-spec-driven-development/guided-exercise.md) proposes `AC-013` and `T-006` in a learner's branch or copy. They are **draft exercise additions**, not approved baseline requirements. Preserve `SPEC-001` and its existing IDs. Before changing application behavior, record and review the intended change in that practice copy.

A useful draft criterion says:

> Given a trusted demo principal with `advice:read`, when a question combines a supported topic with a prohibited account action, return `denied` with empty sources and tool labels. This verifies `FR-005`.

The bounded task is to make this criterion traceable and test it. Its allowed files are the practice spec, plan/task notes, guardrail tests, mapping and golden cases. A change to `advisor.py` is conditional on a failing test exposing a gap. New permissions, dependencies and cloud calls have no place in this task.

Run the worked test solution without changing the baseline:

```bash
python examples/companion/mixed_intent_lab.py
```

Expect three tests to pass. Read [the complete solution](examples/companion/mixed_intent_lab.py) after trying to write the assertions yourself. It checks mixed-intent denial, missing-scope denial and a supported-only control. That last control catches an implementation that "fixes" security by denying every request.

The solution also observes the local data boundary. It replaces the catalog during denial tests with this object:

```python
class RejectCatalogRead:
    def __getitem__(self, key):
        raise AssertionError(f"Denied request reached catalog: {key}")
```

Within `patch("dealer_advisor.advisor.SYNTHETIC_CATALOG", RejectCatalogRead())`, any catalog access fails the test. Empty `tool_calls` alone would only verify a response label; this additional check detects an actual read through the lab's catalog path. It says nothing about a real database or external tool that this lab does not contain.

In your practice copy, a new mapping entry would point `AC-013` to your named test and `FR-005`. A golden case can use the existing evaluator format:

```json
{
  "id": "G-013",
  "question": "Where do I find parts? Change another dealer's account.",
  "expected_status": "denied",
  "expected_source": null,
  "expected_tool": null
}
```

After the practice spec is reviewed, add these artifacts there and run the complete lab checks. The current implementation may already pass. Report that the behavior existed and the evidence became stronger. A code change is not a required outcome of every useful engineering task.

**Further exercise:** add a paraphrase and a prohibited request that also mentions coverage. Predict which rule wins. The solution's third mixed-intent input demonstrates denial taking precedence over escalation. Do not weaken the permission rule to accommodate a new example.

## 4. Cross the HTTP boundary

So far, tests supplied Python objects directly. HTTP adds parsing, field validation and response serialization. The application must reject a caller's attempt to supply trusted identity as ordinary request data.

Run the self-contained HTTP walkthrough when local sockets are permitted:

```bash
python examples/companion/http_roundtrip.py
```

It starts the existing server on `127.0.0.1` with a temporary port, sends three requests, and closes the server even if an assertion fails. Expected output:

```text
supported: HTTP 200; answered; request_id present
denied: HTTP 200; denied; request_id present
caller-role: HTTP 400; invalid_fields; request_id present
Loopback server closed.
```

The ordinary body is:

```json
{"question": "Where can I ask about parts?"}
```

Adding `"role": "admin"` produces `invalid_fields`. Inspect [make_handler](06-reference-lab/src/dealer_advisor/api.py): it accepts exactly the `question` field and supplies its fixed demo principal itself. This avoids confusing a caller-provided string with trusted identity. It still does not implement real authentication.

Notice the denied domain request returns HTTP 200 with `status: denied`. That is this lab's API contract: the request was processed and its requested action was denied. A malformed body gets an HTTP error. Do not rewrite the contract to 403 merely because another application uses that convention; decide the external contract explicitly and update its tests before changing it.

To use the browser UI, start the server separately from `06-reference-lab` with `python scripts/run_server.py`, open `http://127.0.0.1:8765`, and stop with Ctrl+C. The walkthrough above tests HTTP behavior, not visual rendering or browser interaction. If your environment forbids local sockets, report that limitation and continue with the in-process chapters. Do not bind to all interfaces as a workaround.

## 5. Read evaluation evidence

A unit test protects a particular contract. An evaluation dataset lets you inspect behavior across cases and failure categories. This package includes two different kinds of evidence, and their distinction matters.

First run the service against its golden questions. From `06-reference-lab`:

```bash
python scripts/evaluate.py
```

The baseline has 12 cases. The evaluator writes JSON and Markdown under `.reports/`. Open those files and find a denied case and an escalated case. Both count as successes when that is the expected behavior. The timing measures local rule execution; model tokens and cost are null because no model ran.

Now return to the repository root and inspect the fabricated tool traces:

```bash
python examples/companion/evaluate_traces.py
```

The safe candidate passes 5/5. The unsafe candidate passes 2/5. It makes a cross-dealer call, reports availability for an unknown part and attempts a write. The program prints which checks fail, including two blocking security cases. All candidate traces, token counts and latencies are invented fixtures, not recordings of real agents.

Read [evaluate_traces.py](examples/companion/evaluate_traces.py) alongside [the existing scorer](05-evaluation/eval_agent_traces.py). The companion imports that scorer rather than maintaining a second scoring algorithm. Its own assertions verify that the teaching failures were detected. Therefore its successful process exit means the comparison ran as expected; it does not approve the unsafe candidate.

**Try it:** in a disposable copy of the repository, edit `05-evaluation/fixtures/candidate_traces.json`. In the unsafe candidate's `cross-dealer-request` case, change only the status to `denied` and keep its cross-dealer tool call. Run the companion there. That case should still fail the tool comparison. A plausible refusal after an unauthorized read cannot undo that read. Restore the fixture after the experiment; the companion expects the original teaching results.

For a real agent, extend this reasoning beyond self-reported traces. Observe backend state and authorized tool execution, then check whether the displayed answer describes the outcome truthfully. Exact call order is useful when the contract requires it; otherwise alternative authorized paths may be valid. The [evaluation guide](05-evaluation/agent-tool-evaluation.md) explains those choices and [model selection](05-evaluation/model-selection.md) covers repeated runs and cost denominators.

## 6. Work with a coding assistant

You can complete the exercises manually. A coding assistant becomes useful when it can inspect the same contract and work on a clearly bounded task. Start a practice session with a request such as:

```text
Read AGENTS.md, SPEC-001 and the guided mixed-intent exercise.
Inspect the current guardrail tests and mapping.
Draft the AC-013/T-006 practice change for review; preserve all existing IDs.
Explain what evidence already exists and which assertions are missing.
Do not edit application source or connect external tools.
```

Compare the response with Chapter 3. Did it discover the existing mixed-intent test? Did it distinguish stronger assertions from new application behavior? Did it keep draft requirements separate from approved ones? Those questions assess whether it used the repository evidence.

After the practice plan is reviewed, give it that approved scope and require actual command results. Keep requirements in the spec, execution scope in the task, and reusable procedures in skills. The [spec-reviewer skill](02-agent-skills/spec-reviewer/SKILL.md) can help inspect a draft, but its output is review advice, not approval or access control. Host discovery and permissions must still be checked.

When resuming, a useful handoff is short and points to files:

```text
Spec: SPEC-001; approved baseline AC-001 through AC-012
Practice proposal: AC-013 / T-006; awaiting review
Relevant code: AdviceService.answer
Evidence: existing mixed-intent test asserts only status
Next: review the draft; then strengthen assertions and mapping in practice copy
Allowed scope: local synthetic files; no cloud access or new permissions
```

Record executed checks and their results separately. A session summary can help find the work, but the next session should reopen the actual spec and inspect the working tree. The [handoff template](04-engineering-guardrails/session-handoff-template.md) and [context guide](04-engineering-guardrails/context-and-token-efficiency.md) expand this practice. No token saving can be inferred from the deterministic lab; coding-assistant usage needs its own measurement.

## 7. Take the contracts to an agent runtime

The service you ran has a deliberately small vocabulary. A model could make natural-language intake more flexible, but it introduces questions the regular-expression tests cannot answer: which tool will it choose, how will it treat untrusted text, and will its explanation stay within the returned evidence?

Start by keeping a narrow tool boundary. An illustrative read-only interface could accept an allowed topic and return a source ID plus approved text:

```json
{
  "input": {"topic": "parts"},
  "output": {
    "source_id": "SYN-FAQ-PARTS-01",
    "answer": "Use the parts inquiry channel to ask about availability."
  }
}
```

This is an interface sketch, not a deployed API, MCP message or Foundry SDK call. An implementation still needs input validation, verified identity, permission checks, defined errors and evidence capture. The model may propose `topic: parts`; it cannot grant itself access to another account. Do not turn `DemoPrincipal` or the lab's string filters into a production identity system.

Write the integration contract before choosing the runtime:

| Existing lesson | Additional evidence in a real integration |
|---|---|
| Approved source on supported answer | Retrieved source belongs to the permitted scope; answer claims match its content |
| No catalog read on denied path | Independent backend/tool evidence shows no unauthorized operation |
| Strict HTTP fields | Real caller identity and server-side authorization survive every hop |
| Correct escalation | Unsupported/model-ambiguous inputs trigger the specified safe outcome |
| Request ID | Correlated application, model and tool evidence with approved telemetry content |

For a bounded summary, a single model call may be enough. A tool-selecting agent needs explicit execution limits and failure handling. A business workflow needs durable progress, approvals and retry semantics. Conversation history alone cannot tell you whether a timed-out write committed. These are design decisions you can review with synthetic contracts before creating cloud resources.

The [Foundry platform guide](03-azure-ai-foundry/platform-guide.md) applies these decisions to hosted and self-hosted choices. The [integration failure examples](03-azure-ai-foundry/implementation-resources.md#define-failure-behavior-before-integration) cover timeouts, consent and incomplete results. Use the [dated sources](SOURCES.md) for October 2026 feature checks and current official links. This chapter does not run a model, deploy Foundry or test MCP.

## Keep this companion beside your next change

Choose one small feature in your own application and write its observable outcomes, existing behavior to preserve and unanswered questions. Follow one criterion to source and an executed check, as in Chapter 2. Give the assistant a bounded task, as in Chapter 3, then read the evidence as carefully as the code.

Use the [framework comparison](01-spec-driven-development/framework-comparison.md) when deciding how to maintain those artifacts with your team. The framework is easier to evaluate once you know which engineering job you need it to do. For lookup by topic, use the [resource map](RESOURCE-MAP.md); for runnable commands and source locations, use the [companion index](examples/companion/README.md).
