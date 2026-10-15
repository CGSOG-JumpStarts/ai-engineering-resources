# Data handling in AI-assisted engineering

## Data classes

Classify: public documentation, synthetic test data, approved internal non-sensitive data, sensitive internal/customer data, credentials/regulated data. The included lab contains **synthetic only**. Use real dealer information solely in environments with explicit authorization, vendor data-processing coverage and a privacy/security review.

## Data flow questions

For each model and tool request, identify input sources, recipient/service endpoint, storage region, potential logging and telemetry capture, retention, deletion, and who may retrieve a trace. Confirm what persists in agent threads and what is transmitted to third-party MCP operators.

## Controls

- Strip unnecessary names, IDs, email, phone, account information, free-text attachments and tokens before model input.
- Enforce per-caller data access in the API, not by asking the model to remember a dealer ID.
- Scrub PII and secrets from logs/traces; configure sampling and retention intentionally. Scrubbing structured fields is preferable to hoping a model will mask free-text spans.
- Keep secrets in managed stores, use short-lived identities where supported and prevent inclusion in prompt templates and skill snapshots.
- Track approved data sources by version/freshness; report absent source evidence instead of inventing a policy answer.
- Preserve audit evidence of sensitive tool invocations and human approvals in access-controlled storage.
- Define model/vendor incident escalation and endpoint disablement procedures.

## Foundry-specific review

Foundry tracing can contain prompt/tool content depending on configuration. Verify the official [tracing setup and security guidance](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup), Azure role assignments, Application Insights/Log Analytics readers, retention and ingestion filters before turning it on for real traffic.
