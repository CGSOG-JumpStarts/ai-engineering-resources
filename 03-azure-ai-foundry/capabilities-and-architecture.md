# Microsoft Foundry: capabilities and architecture choices

**Research snapshot: 15 October 2026.** "Microsoft Foundry" is the current Microsoft documentation branding; many older links and code samples still say "Azure AI Foundry." Check the selected project's region, setup mode, SDK versions, identity and deployment model before applying a guide.

enterprise is already building stakeholder advisory agents with Foundry. The near-term decision is what Foundry should operate, and what enterprise must build around it for authorization, business data, change control, tests, and support.

## Which runtime owns which responsibility?

| Option | Best fit | Managed by Foundry | Still owned by the application team |
|---|---|---|---|
| **Prompt agent** | Well-bounded advisory interactions defined by instructions + models + tools | Agent runtime, prompt agent lifecycle and its supported tools | Backend tool services, security policy, data integration, evaluation corpus, application UX, approvals |
| **Hosted agent** | Code-based orchestration, custom framework, domain logic, advanced protocols | Containerized agent hosting, sessions, scaling, agent identity, supported endpoint protocols | Code, business actions and APIs, agent policy, tests, operational SLOs, integration permissions |
| **Self-hosted agent** (with Microsoft Agent Framework or another framework) | Existing enterprise runtime, full control over networking, process and delivery | Model/Foundry services the app elects to consume | Compute, lifecycle, HTTP handlers, state, autoscaling, authn/authz, tracing, recoverability |
| **Workflow/durable orchestration** | Multi-step work requiring checkpoints, approvals or recovery | Depends on selected host and durable backend | State transitions, retries, idempotency, compensating actions, human review |

Hosted Agents are generally available as a **service**. Certain Python Agent Framework integration packages are explicitly prerelease. Foundry's skill/toolbox distribution mechanisms include **preview** features. A generally available service does not make every SDK or related feature GA. [Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | [Agent Framework hosting](https://learn.microsoft.com/en-us/agent-framework/hosting/) | [Hosted integration](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) | [Foundry skills](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills).

## Reference architecture for a dealer advisory agent

```text
Dealer portal / internal advisory UI
   │  signed-in user's real identity + request/trace ID
   ▼
enterprise application API / gateway
   │  server-side authz, tenant context, quotas, audit
   ▼
Foundry agent (prompt agent or Hosted agent)
   │  model + allowed tool definitions
   │  read-only question → permitted tool call
   ▼
enterprise-operated tool API or approved MCP gateway
   │  Entra / OAuth / service identity as appropriate
   │  authorization checked again at the system of record
   ▼
Dealer-scoped data services / APIs
   │  scoped retrieval with provenance and freshness
   ▼
Foundry response + request-scoped trace
   ▼
Application displays sourced answer or safe refusal

Observability plane: application logs + correlated OpenTelemetry traces,
Foundry / Application Insights telemetry, evaluation datasets,
latency + token costs + tool errors + safety reviews.
```

This is a **conceptual design**, not an assessment of enterprise's existing environment. No real enterprise architecture or identity system was provided. The sample app in `06-reference-exercise` runs only the read-only tool boundary offline.

## A tool declaration does not implement the business action

Tools require real backend endpoints or functions. For a read-only dealer availability lookup, the implementation must validate the caller's dealer rights, resolve identifiers, query a source of truth, handle stale/missing data, emit audit records, and return typed errors. The model decides whether to call a permitted tool; it does not become the permission authority.

For any **write** action, add explicit authorization, scope checks, idempotency keys, transaction handling, confirmation rules, human approval where needed, compensating behavior, and tests that prove unauthorized or duplicate requests cannot act.

## Identity, tools, and data

- Use Microsoft Entra identities and scoped RBAC at Foundry project/agent and downstream resource boundaries. "Foundry Agent Consumer" is intended for end users who only invoke agents. A hosted agent gets a dedicated agent identity, but that identity alone **does not establish the human caller's dealer entitlements**. [RBAC](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry?view=foundry-classic) | [Hosted deployment](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent)
- Foundry MCP connections support options including keys, Entra-based agent or project identities, OAuth identity passthrough and, for public tools, unauthenticated connections. The choice determines whether downstream services receive user context. Prefer user-scoped identity where per-user permissions matter. [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication).
- MCP tool descriptions and retrieved text are **untrusted content**. Validate parameter schemas; restrict server origins, accepted tools, scopes and side effects; do not pass upstream access tokens through unrelated services. [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | [MCP security considerations](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx).
- Basic and Standard Foundry project configurations differ in where agent data is stored. Check storage, network isolation and retention against enterprise policy. [Agent Service limits and setup](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions) | [Private networking](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks).

## Deployment and lifecycle

A typical hosted-agent lifecycle is: package supported code, establish its project configuration and agent identity, deploy an immutable version, invoke it, monitor traces and failures, update by deploying a new version. The current Hosted Agents documentation supports Azure Developer CLI (`azd`), SDK and REST deployment paths, including a source-code ZIP deployment option for supported languages. Do not assume a hosted agent is merely a prompt plus MCP access. [Official hosted deployment guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent) | [Agent Framework host guide](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent).

For long-running workflows, Microsoft Agent Framework documents checkpointing and a Durable Extension. The choice of state store, approval workflow, timeout semantics, identity and retry behavior must be explicit. [Checkpointing](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | [Hosting overview](https://learn.microsoft.com/en-us/agent-framework/hosting/).

## What to ask before choosing

1. Is the agent purely advisory, or will it perform actions in enterprise systems?
2. Which data is visible to which dealer, support role, and internal team?
3. Are tool calls synchronous, long-running, regulated, or costly?
4. Does enterprise need managed Foundry hosting, or should the agent run within an existing application service?
5. Which region, networking, model, and storage configurations are currently approved?
6. What is the expected process for evaluations, rollbacks, alerts, and version ownership?

A two-path review works well: **improve an existing prompt agent now** while assessing **hosted or self-hosted code** only when the workflow demands it.
