# Microsoft Foundry: capabilities and runtime choices

**Rechecked: 2026-10-21.** Use this guide to compare Foundry options for an advisory-agent application. It assumes no particular company architecture or existing deployment.

## What Foundry adds

Foundry provides a model/agent development environment with managed agent hosting options, tool integrations, identity, tracing and evaluation capabilities. Actual options depend on project type, region, permission model and feature lifecycle. Some capabilities are preview. The user-facing dealer portal, system-of-record permissions, application API, incident handling and operations still need explicit implementation.

## Choose the execution behavior first

This package recommends choosing the control structure before hosting. Use deterministic code for known rules. A bounded model call can handle one extraction, classification or summary. An agent loop is useful when the next permitted tool/action depends on intermediate results. An explicit workflow is useful when ordering, approval and recovery must follow a defined business contract. These choices can coexist in one application; they are not mandatory adoption stages.

For a synthetic support case, summarizing an approved FAQ needs no autonomous action loop. A case-creation workflow needs a validated target, permitted write, idempotency and recovery even if a model drafts the description. Define those responsibilities before choosing a container or SDK. Foundry's [agent overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) and [hosting guide](https://learn.microsoft.com/en-us/agent-framework/hosting/) describe different service and hosting paths.

## Choosing a runtime

| Decision | Option | When it fits | Responsibility |
|---|---|---|---|
| Managed hosting | **Foundry Hosted Agents** | Code-defined agents where the managed container/service lifecycle is acceptable | Foundry manages hosted infrastructure; your team owns agent code, tools, identity design, tests and user experience |
| Application-managed hosting | **Self-host an Agent Framework app** | Existing runtime controls, custom networking, BFF or enterprise services required | Your team manages hosting, scaling, auth boundary, endpoints and deployment. Check the exact SDK package's release status. |
| Durable workflow | **Durable extension / orchestration runtime** | Long-running operations, checkpoints, waits and compensating actions | Your team owns workflow states, durable storage, retries, idempotency and approval policy; see current Agent Framework hosting docs |
| Bounded LLM call | **Model via a normal app API** | Classification, summarization or retrieval with no autonomous multi-tool loop | Ordinary API, validation, telemetry and retries; often the simplest option |

Do **not** infer that choosing Agent Framework deploys APIs, provisions downstream systems, defines business actions, or creates durable workflows automatically. The framework composes model and tool calls; infrastructure and transactional semantics still require engineering.

**Current status:** Microsoft documents Foundry Hosted Agents as **generally available**. Some package surfaces, Skills APIs and optional integration types have different lifecycle labels. [Hosting overview](https://learn.microsoft.com/en-us/agent-framework/hosting/), [Hosted Agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents), [deployment guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent).

## State and recovery are separate contracts

| State | Recovery question |
|---|---|
| Conversation history | Can the assistant recover the relevant intent and constraints? |
| Hosted-session files/state | What survives a session/process restart, and who can access it? |
| Business workflow progress | Which action committed, which approval remains valid, and what is safe to retry? |

A surviving conversation does not prove that a timed-out write failed. Reconcile backend state before retrying; record idempotency keys and approval identities. [Durable execution](https://learn.microsoft.com/en-us/agent-framework/hosting/durable-extension) and [workflow checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) provide mechanisms, while the application still defines transactional behavior and storage controls.

## Choosing tool identity

- Use **per-user identity/passthrough** where a dealer-facing action must preserve a caller's authorization.
- Use **agent identity** for agent-specific service access where supported; grant only the scopes/actions the agent needs.
- Use **project managed identity** for deliberate shared service identity use cases, and document how end-user access is checked separately.
- Treat shared API keys as last-resort secrets with vault, rotation, scopes and audit controls.
- Limit anonymous tools to explicitly public resources.

The precise supported methods depend on tool type. See [tool auth](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/tool-authentication), [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) and [agent identity](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity).

### Confirm the agent object model

Microsoft's [identity concepts](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) and [migration guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications) describe legacy Agent Applications and a newer agent model. Their creation/publishing identity behavior differs. Record the actual resource/API path, agent identity, endpoint and role bindings instead of assuming one universal publishing rule. Recreating an agent can change the identity; verify downstream role assignments after migration. The migration examples include preview surfaces, so do not infer universal tenant availability.

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
