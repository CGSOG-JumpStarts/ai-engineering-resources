---
name: agent-tool-evaluation
description: Design and review reproducible evaluations for AI agent tool selection, parameter accuracy, authorization, answer groundedness, failure handling, latency and spend. Use when comparing models or introducing MCP tools and when an agent must prove that it respects a read-only or cross-tenant boundary.
---

# Agent and MCP tool evaluation

## Procedure

1. Inventory allowed tools, schemas, data classifications, identity propagation, side effects, costs and failure modes.
2. Define tasks and an expected outcome before testing. Include ordinary successful, ambiguous, forbidden, missing-data, tool-failure and malicious-instruction examples.
3. Separate **system outcome** (correct, grounded result) from **process** (tool selected, args valid, policy enforced, call succeeded, response used correctly). See `05-evaluation/`.
4. Record candidate configuration: exact model/version, prompt and skill versions, tool schema hash, host, concurrency, region, input/output tokens, cost and request latency where measured.
5. Apply deterministic checks for schemas, policy denials, forbidden side effects and golden tool sequences. Only use an LLM judge when the rubric requires semantic evaluation; calibrate judges against human-reviewed cases.
6. Prefer side-by-side runs over the **same** scenario set, with repeat samples and confidence intervals if stochastic. Report no numeric improvement without measurements.
7. Provide a go/no-go report with failure cases and remediation. Any denied cross-tenant action or unauthorized write is a blocking defect regardless of aggregate score.

## Available local example

Use `python 05-evaluation/eval_agent_traces.py` from the repository root to compare two **invented fixture traces**. The example is a deterministic scorer and is **not a Foundry evaluator or measured model benchmark**.

## Output

Evaluation matrix (task, expected tool call, actual call, policy result, answer judgment), summary by candidate, p50/p95 latency, token/spend inputs where available, critical failures, data-set limits, and release recommendation.
