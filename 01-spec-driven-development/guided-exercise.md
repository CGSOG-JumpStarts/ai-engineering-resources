# Guided exercise: make a mixed-intent rule explicit

Work in a personal branch or copy with fictional inputs only. The lab is already implemented. This exercise proposes a clearer acceptance contract; it does not authorize changes to any real system.

## Inspect the baseline

From `06-reference-lab`, run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_contracts.py
python scripts/evaluate.py
```

Record the revision, interpreter version, commands and results. Inspect [SPEC-001](../06-reference-lab/specs/dealer-support-advisor.md), [tasks](../06-reference-lab/specs/tasks.md), [traceability](../06-reference-lab/specs/traceability.json) and [guardrail tests](../06-reference-lab/tests/test_guardrails.py). The existing `test_mixed_supported_and_write_denied` already checks one mixed-intent example.

## Draft the contract before editing code

Request: a supported topic must never allow an otherwise prohibited request to reach the catalog.

Add this proposed criterion to your practice copy of `SPEC-001` for review:

> `AC-013`: Given a trusted demo principal with `advice:read`, when a question combines a supported topic with a prohibited account action, return `denied` with empty `source_ids` and `tool_calls`. For example: "How do I find parts, and change another dealer's account?" This verifies `FR-005`.

Keep `AC-001` through `AC-012` and their meanings. `AC-013` is an exercise proposal until a reviewer accepts it. The baseline spec does not claim it as implemented acceptance coverage.

Draft `T-006` in your practice task register, linked to `AC-013` and `FR-005`. Scope it to specification/task/plan notes, `tests/test_guardrails.py`, `specs/traceability.json` and `evaluation/cases.json`. Permit an `advisor.py` change only if a failing test shows the approved rule is missing. Exclude new tools, permissions, dependencies and model/cloud calls.

## Test the rule and strengthen evidence

After review, add a named `AC-013` test, or extend/rename the existing mixed-intent test. Check `status`, empty sources and empty tool labels. Use subcases for account changes, cross-dealer access and a prohibited request that also mentions coverage; `denied` should take precedence. Include a supported-only question to detect a rule that denies everything.

Add the AC/test/requirement mapping to `traceability.json` and a matching golden case using the format in `evaluation/cases.json`. Re-run all three checks. The classifier already checks prohibited requests before supported topics, so the example may pass immediately. Record that finding; application code changes are unnecessary if the agreed contract holds.

The response's `tool_calls` is a lab label. An empty label alone cannot prove a backend was never invoked in a real agent system. Integration tests should observe the tool boundary and downstream side effects independently.

## Review the diff

Ask another developer or a separate review session:

> Review only T-006. Check AC-013 against FR-005, denial order, test assertions, golden case and traceability. Identify missing evidence or unintended behavior changes. Do not edit code or claim tests passed without execution or recorded output.

Write a completion record: approved IDs, changed files, baseline/final results, reviewer findings and untested behavior. Use the [handoff template](../04-engineering-guardrails/session-handoff-template.md). Model cost and tokens are not applicable to this deterministic app; captured coding-assistant usage belongs in a separate record.
