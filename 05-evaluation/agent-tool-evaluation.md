# Evaluating an agent with tools

AI tool correctness is an end-to-end property: the user intended something, an agent selected a tool, parameters were validated, a backend authorized and performed (or rejected) the operation, and the final answer accurately represented that result.

## Minimum test families

| Family | Expected evidence |
|---|---|
| Happy path | Allowed tool selection and grounded response; correct source ID |
| Unsupported intent | No invented policy answer; human escalation path |
| Missing/ambiguous parameters | Clarifying request or valid safe default, never guessed target account |
| Permission denied | No downstream data/action, meaningful failure to user, audit event |
| Malicious retrieved content | Embedded instructions ignored; only original user intent/tool policy applies |
| Tool timeout or 503 | Bounded retry where safe, failure communicated, no fake success |
| Duplicate request | Idempotent action or safe rejection |
| Cross-tenant attempt | Identity-derived tenant context prevents record lookup |
| Excessive tool loop | Max steps/latency/budget bound enforced |
| Cost/regression | All actual calls metered and compared to baseline |

## Metric record

For each run, record `case_id`, testset version, prompt/model/tool version, actor role, expected outcome, actual outcome, selected tool, tool args schema, tool status, final response evidence ID, milliseconds, input/output tokens, cost and human reviewer disposition. Protect any trace containing user data.

## Evaluator choice

Use deterministic tests for exact schema, authorization, calls, errors and state transitions. LLM-as-judge can assess subtler response qualities, but requires calibration against human judgments and can be inconsistent. The Foundry [agent evaluator catalog](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) distinguishes task/system and tool/process evaluators, identifies preview features and limits some evaluators for some tool types. Verify availability at deployment time.

## Suggested pass gates for a new pilot

These are **illustrative thresholds for discussion**, not enterprise's pre-approved service requirements:

- 100% of tested unauthorized writes blocked; zero disclosed cross-dealer records.
- 100% of unsupported policy questions abstained/escalated in the critical golden set.
- At least 95% of low-risk positive cases accepted across an adequately sized sample.
- No material p95 latency regression without business owner acceptance.
- Full explanation of sample counts, missing evaluations, real costs and trace retention.

For the offline simulator's actual gates, see its `specs/dealer-support-advisor.md` and `scripts/evaluate.py`. Those gates apply only to synthetic deterministic behavior.
