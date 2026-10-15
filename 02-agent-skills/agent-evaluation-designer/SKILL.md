---
name: agent-evaluation-designer
description: Design repeatable model and agent evaluations covering task outcomes, tool calls, permissions, groundedness, cost, latency, failure recovery and regressions. Use when comparing Microsoft Foundry deployments or modifying agent tools and prompts.
license: MIT
---

# Agent evaluation designer

1. Define the task, intended user, environment, success criteria, risk tier and required approvals. Freeze the same input cases across models.
2. Construct a versioned evaluation set with at least one positive, negative, ambiguous, tool-error and injection/authorization scenario per sensitive workflow. Use synthetic or approved redacted data.
3. Record **expected tool names and arguments** where deterministic, and a justified set of acceptable outcomes where several actions are valid. Do not use LLM judgment for facts that can be asserted in code.
4. Measure task success, tool selection/parameter accuracy, tool call success, grounding/unsupported claims, p50/p95 latency, request/retry count, and actual input/output tokens and cost when model calls are made.
5. Report numerator, denominator and environment for every rate, and distinguish estimated cost from billed usage. Run repeated samples for stochastic models; compare model/harness versions and concurrency.
6. Require zero known unauthorized writes. Define noncompensable security failures separately from average quality scores.
7. Review failures by category, propose one bounded change, rerun the fixed golden set and run a regression check before approving rollout.

## Output

Return an evaluation case table (ID, intent, synthetic input, expected outcome, expected tools, expected permissions, evidence) and a scorecard (samples, pass/fail counts, latency percentiles, tokens, cost, reproducibility, unresolved gaps). Include a decision: proceed, more evidence, or stop.

The local sample in `05-evaluation/evaluation-matrix.csv` and `06-reference-lab/` uses deterministic cases only. Microsoft Foundry's live evaluators vary by tool type and feature status; see official documentation before naming an evaluator as required in a production pipeline.
