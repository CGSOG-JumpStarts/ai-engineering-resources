# Experiment scorecard template

Experiment ID: ______  
Owner: ______  
Run date: ______  
Baseline configuration: model ______ / harness ______ / tools ______ / testset SHA ______  
Candidate configuration: ______

| Metric | Baseline | Candidate | Evidence/source | Gate | Decision |
|---|---:|---:|---|---|---|
| Eligible cases | | | | | |
| Accepted cases | | | | | |
| Task success rate | | | | | |
| Unauthorized tool calls | | | | 0 | |
| Unsupported claims | | | | Explicit agreed limit | |
| Tool selection accuracy | | | | | |
| Tool call success | | | | | |
| p50 elapsed ms | | | | | |
| p95 elapsed ms | | | | | |
| Input tokens / output tokens | | | | | |
| Billed or estimated total cost | | | | Label type | |
| Cost per accepted case | | | | | |
| Human review minutes | | | | | |
| Known regression count | | | | 0 critical | |

## Calculation and caveats

Define success outcomes before running the candidates. For required denial/escalation cases, correct refusal is a success. Use the same inputs in both groups. Label cost as *billed*, *estimated from pricing*, or *not captured*. If sample sizes differ, compare rates with denominators and examine confidence intervals. Never conclude value from a speculative baseline.

## Decision

`Proceed | Revise and retest | Insufficient evidence | Stop`

Business owner and security owner sign-off: ______  
Outstanding issue IDs: ______  
Rollback or fallback: ______
