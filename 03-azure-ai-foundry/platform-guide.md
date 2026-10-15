# Microsoft Foundry: capabilities and runtime choices

**Research checkpoint: 2026-10-15.** Use this guide to compare Foundry options for an advisory-agent application. It assumes no particular company architecture or existing deployment.

## What Foundry adds

Foundry provides a model/agent development environment with managed agent hosting options, tool integrations, identity, tracing and evaluation capabilities. Actual options depend on project type, region, permission model and feature lifecycle. Some capabilities are preview. The user-facing dealer portal, system-of-record permissions, application API, incident handling and operations still need explicit implementation.

## Choosing a runtime

| Decision | Option | When it fits | Responsibility |
|---|---|---|---|
| Managed hosting | **Foundry Hosted Agents** | Code-defined agents where the managed container/service lifecycle is acceptable | Foundry manages hosted infrastructure; your team owns agent code, tools, identity design, tests and user experience |
| Application-managed hosting | **Self-host an Agent Framework app** | Existing runtime controls, custom networking, BFF or enterprise services required | Your team manages hosting, scaling, auth boundary, endpoints and deployment. Check the exact SDK package's release status. |
| Durable workflow | **Durable extension / orchestration runtime** | Long-running operations, checkpoints, waits and compensating actions | Your team owns workflow states, durable storage, retries, idempotency and approval policy; see current Agent Framework hosting docs |
| Bounded LLM call | **Model via a normal app API** | Classification, summarization or retrieval with no autonomous multi-tool loop | Ordinary API, validation, telemetry and retries; often the simplest option |

Do **not** infer that choosing Agent Framework deploys APIs, provisions downstream systems, defines business actions, or creates durable workflows automatically. The framework composes model and tool calls; infrastructure and transactional semantics still require engineering.

**Current status:** Microsoft documents Foundry Hosted Agents as **generally available**. Some package surfaces, Skills APIs and optional integration types have different lifecycle labels. [Hosting overview](https://learn.microsoft.com/en-us/agent-framework/hosting/), [Hosted Agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents), [deployment guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent).

## Choosing tool identity

- Use **per-user identity/passthrough** where a dealer-facing action must preserve a caller's authorization.
- Use **agent identity** for agent-specific service access where supported; grant only the scopes/actions the agent needs.
- Use **project managed identity** for deliberate shared service identity use cases, and document how end-user access is checked separately.
- Treat shared API keys as last-resort secrets with vault, rotation, scopes and audit controls.
- Limit anonymous tools to explicitly public resources.

The precise supported methods depend on tool type. See [tool auth](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/tool-authentication), [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) and [agent identity](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity).

## Observability and evaluation

Attach Application Insights to the Foundry project, configure tracing and data privacy, then review actual spans/events. Microsoft documents GA tracing for prompt and hosted agents, with other integration coverage varying. Track correlation IDs from dealer portal through gateway, agent and downstream tool calls. Redact secrets and dealer data before telemetry capture; configure retention and access.

Agent evaluation should combine **system outcomes** (did the request succeed? was advice grounded?) with **process outcomes** (which tool was called? were parameters authorized? did the API succeed?). Microsoft's built-in Foundry evaluators cover several such metrics, with preview labels and tool-type restrictions that must be checked case by case. [Tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup), [evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators).

## Questions to confirm for your application

1. Foundry project type and deployment region? Hosted or application-hosted agent today?
2. Which tools does each agent call, and does tool access represent an individual stakeholder or service principal?
3. What are approved knowledge sources and what happens when a question has no approved answer?
4. Where are traces recorded; can logs capture sensitive prompts or retrieved content?
5. How are accuracy, tool-call success, latency, cost and negative cases measured before a release?
6. What action requires an approval and which system enforces that approval?

For an implementation path, see [the quickstart](foundry-quickstart.md) and [reference architecture](reference-architecture.md).
