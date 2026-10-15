# Context and token efficiency practices

The enterprise team mentioned lowering token usage. Token counts, cost and accuracy can conflict; optimize **cost per accepted outcome**, not tokens alone.

## Concrete defaults

1. Keep short global instructions in `AGENTS.md`; use scoped files for service-specific conventions.
2. Load one approved feature spec, the relevant code contract and a bounded implementation plan, instead of the full project narrative in each turn.
3. Store architecture decisions and test artifacts in files so a new session can reconstruct context without transcript replay.
4. Minimize tool outputs. Prefer file paths, line ranges and relevant search matches over dumping hundreds of files.
5. Separate discovery/research from implementation and review; record findings once with stable links.
6. Put full examples/schema references in on-demand skills rather than always-on instruction files.
7. Before multiple agent runs, specify exact task boundaries and avoid duplicating the same research across workers.
8. Use deterministic code for validation, access checks, formatting, fixtures and simple routing rather than repeated model calls.
9. Consider a smaller model or router only after it meets the fixed golden-case quality and security thresholds.
10. Log actual provider input/output tokens, retries, inference latency, model name/version and billed/estimated cost separately.

## Suggested experiment design

Run 20 or more representative tasks **if available**, with a fixed rubric and comparable task complexity. Compare:

- Accepted changes / runs, reviewed defects / change, human review minutes, production regressions.
- Input tokens and output tokens separately, plus external tool call volume and retry count.
- Cost per accepted change, p50/p95 wall-clock time and 'no evidence' frequency.

Control for model, harness and context window; otherwise improvements cannot be attributed to the instruction changes. Stated reductions are hypotheses until measured.

## Example session handoff (edit for the real repo)

```text
Feature: FR-014 dealer-portal FAQ routing
Approved spec: specs/feature-faq-routing.md at commit <SHA>
Current task: T-004, add unsupported-request path
Relevant API: src/portal/advice_service.py
Known decision: ADR-012, read-only tool policy
Tests to run: tests/test_advice_service.py
Blocked on: reviewer answer for AC-008
No new cloud permissions or real customer data approved.
```
