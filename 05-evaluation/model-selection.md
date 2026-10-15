# Model selection for advisory agents

Use the **smallest-cost model or routing strategy that meets observed outcome and security requirements** under your application workload. No single provider benchmark guarantees performance on dealer questions and MCP tools.

## Experimental design

1. Freeze 30–100 representative **approved or synthetic** cases when available, including rare and costly failures. Small early pilots can use fewer cases but must disclose confidence limits.
2. Hold system prompt, tool schemas, retrieval corpus, permissions, temperature, service configuration and evaluation rules constant.
3. Compare a fixed model with a smaller fixed model and, where supported, Foundry model routing; repeat stochastic cases.
4. Capture actual model deployment/version, region, input/output tokens, cached tokens (if reported), tool calls/retries, wall-clock latency, and invoice/pricing basis.
5. Separately score deterministic assertions (exact tool, allowed params, permission checks) and judged qualities (helpfulness, grounding, tone), with human spot checks.
6. Apply non-negotiable constraints before computing weighted performance. A single unauthorized write or data disclosure blocks rollout pending remediation.

## Suggested scorecard calculations

- Task success = accepted cases / eligible cases; record denied/unsupported cases as their own expected successful outcomes if correctly handled.
- Tool selection accuracy = cases with correct approved tool choice / cases requiring a tool.
- Tool invocation success = successful tool calls / attempted tool calls, and tool failure propagation rate separately.
- Unsupported claim rate = cases with unsupported factual claims / answers containing claims.
- Mean billed cost per accepted case = total billed cost / accepted cases (not total cases).
- p50/p95 end-to-end latency from caller's perspective; record sample count and concurrency.

Do not average away permission failures. Record the *worst-case failure classes* and whether a human intervention was required.

Microsoft's [Responses model routing docs](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses-model-routing) explain fixed versus router deployment strategies. Model availability, quotas and pricing vary by region and date.
