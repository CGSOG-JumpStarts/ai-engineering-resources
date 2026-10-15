# Evaluation resources

Use independent evidence to assess task outcomes, tool decisions and backend behavior. A correct refusal can be a successful outcome. An authorization or disclosure failure must remain visible even when other cases pass.

- [Model comparison](model-selection.md): controlled experiments, repeated runs and actual-cost reporting.
- [Agent/tool evaluation](agent-tool-evaluation.md): expected calls, denied actions, retries and grounded answers.
- [Tool checklist](tool-evaluation.md): trace fields and the execution evidence to capture.
- [Scorecard](scorecard-template.md) and [matrix](evaluation-matrix.csv): editable planning aids, containing no measured agent results.

## Run two offline examples

**Executed application cases:** from `06-reference-lab`, run:

```bash
python scripts/evaluate.py
```

This executes the deterministic Python service against `evaluation/cases.json` and writes `.reports/evaluation-report.json` and `.md`. Its elapsed times are local rule-execution measurements. It makes no model or MCP calls.

**Fabricated agent traces:** from the repository root, run:

```bash
python 05-evaluation/eval_agent_traces.py
python 05-evaluation/eval_agent_traces.py --json
```

The scorer compares `fixtures/candidate_traces.json` with `fixtures/golden_cases.json`. It checks exact tool sequences and argument values, expected statuses and blocking-case failures. Expected output:

```text
example-safe: 5/5 cases; PASS; blocking=[]
example-unsafe: 2/5 cases; BLOCK; blocking=['cross-dealer-request', 'request-to-place-order']
```

The unsafe example accesses another dealer and attempts a write; it also invents availability for an unknown part. These are deliberately fabricated failures. All token and latency values in these traces are invented. No model ranking, cost saving or actual system security can be inferred.

The scorer exits zero after printing either candidate's verdict, including `BLOCK`. It is a teaching comparison, not a CI release gate. Do not use its process exit status as proof that an agent passed evaluation.

## Move from examples to an actual benchmark

Write expected behavior independently of candidate output and freeze case/model/prompt/tool versions. Capture sanitized traces from approved runs, including downstream authorization and side-effect evidence. Check required failures and refusals alongside successful tool calls. Use the [scorecard](scorecard-template.md) to record sample counts, repeated-run outcomes, measured latency and billed or explicitly estimated cost.

This fixture scorer does not validate arbitrary input schemas, verify trace authenticity, observe downstream effects, assess response grounding or exercise an MCP transport/authentication handshake. Those require separate tests. Add timeouts, malformed results, retries, tool loops and duplicate-action cases when the real integration supports them. Calibrate any model-based judging against human reviews and retain a holdout set for final comparisons.
