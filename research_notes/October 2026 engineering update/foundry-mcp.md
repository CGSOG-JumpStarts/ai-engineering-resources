# Microsoft Foundry, Agent Framework and MCP

Research checked 2026-10-21 against public primary documentation. No credentials, cloud resources, private repositories, enterprise systems, installers or live integrations were accessed. Microsoft Learn responses showed an authorization banner but returned readable article bodies; the findings below use those bodies and do not imply authenticated access. This is documentation research, not environment validation.

## Which execution model fits, and what status is actually verified?

### Takeaway

Separate the need for an agent loop from hosting, protocol and durable execution choices. Hosted Agents GA does not establish GA for every integration package or adjacent feature.

### Cited Findings

- Foundry supports configured prompt agents, code-defined hosted agents and using the Responses API from application code running elsewhere. The platform overview therefore supports a bounded model call without requiring an agent resource. [Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)
- The hosting overview explicitly labels Foundry Hosted Agents generally available, while Python self-hosting packages remain prerelease. It separates infrastructure ownership from client protocol. Foundry operates the hosted container/scaling/session lifecycle; self-hosting leaves routes, identity, authorization, storage, deployment and scaling with the application team. [Hosting overview, updated 2026-10-16](https://learn.microsoft.com/en-us/agent-framework/hosting/)
- The integration guide independently labels `agent-framework-foundry-hosting` prerelease. Hosted sessions persist files/state, but local development does not receive the platform's user/call context and must supply its own controls. [Agent Framework hosting integration](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent)
- Deployment can use azd, language SDKs or REST; a supported source ZIP path lets the platform build the container. This does not remove responsibility for application dependencies and behavior. [Hosted deployment guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent)
- Durable Extension supports Azure Functions and bring-your-own-compute paths using Durable Task infrastructure. It persists execution, recovers work and supports waiting for external input. Workflow checkpoints capture state between supersteps; storage access/integrity remain application concerns. [Durable Extension, updated 2026-10-16](https://learn.microsoft.com/en-us/agent-framework/hosting/durable-extension), [checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints)

### Inferences

- Add an editorial decision sequence to `platform-guide.md`: deterministic code for known rules; a bounded model call for one extraction/classification/summarization task; an agent loop when tool choice/next action varies; an explicit workflow when ordering/approval/recovery must be controlled. Choose host and protocol afterward. These are recommendations, not Microsoft-mandated stages.
- Explain three different states: conversation history, hosted-session files and business workflow progress. A surviving conversation does not prove a partially completed business action is safe to retry. For a synthetic approval workflow, record timeout, approval identity, idempotency and post-restart behavior.

### Gaps

- No package installs, deployed region tests, quota checks or runtime compatibility checks. Do not recommend concrete dependency pins from article examples alone.

## Which identity and skill boundaries need clearer explanation?

### Takeaway

The docs describe multiple agent object models at once. Record the actual identity and endpoint model before assigning permissions; user-scoped access and agent service authority remain different questions.

### Cited Findings

- The identity-concepts article describes legacy in-development agents sharing a project agent identity and published Agent Applications receiving separate identities. It explicitly directs readers to a newer object-model migration guide. [Identity concepts](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)
- The migration guide says new-model agents receive an individual identity and stable endpoint at creation. Legacy applications remain supported; recreating/migrating an agent changes its identity, and prior downstream RBAC does not transfer. Its sample inspection request uses a preview API/feature header, so this is not evidence that every feature or tenant rollout is GA. [Migration guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications)
- Foundry MCP auth distinguishes shared credentials/agent or project identity from OAuth identity passthrough that retains user context. Its OAuth guidance prohibits sending known-Microsoft-audience tokens to untrusted custom MCP endpoints and requires a custom server audience under the application's control. [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication)
- Foundry Skills remains preview. Skill versions are immutable; skills may be delivered via a toolbox or downloaded into a hosted/local project. Toolbox skills must share the Foundry project and discovery requires MCP Resources support. [Foundry Skills, updated 2026-10-15](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills)
- The private skill catalog remains public preview and uses Azure API Center. API Center catalog access and Foundry project access require separate permissions. [Private catalog, updated 2026-09-14](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/private-skill-catalog)

### Inferences

- Add an object-model compatibility note in `platform-guide.md` and implementation links. Avoid universal claims that identity always changes on publish or every agent always has an isolated identity. Confirm the specific resource/API path and role bindings.
- Expand `skills-in-foundry.md` with three separate decisions: developer skill discovery, runtime skill loading/version promotion and downstream tool authorization. A skill update may change behavior without a code release, so evaluate the skill version with the agent/tool versions before promotion.

### Gaps

- The public identity and migration guides have different wording and property names, and no tenant was inspected. Keep the distinction explicit rather than guessing one universal identity contract. Exact SDK/property compatibility and regional rollout remain unresolved.

## What should MCP security and evaluation add beyond a successful answer?

### Takeaway

Check the principal, tool execution and resulting state independently. Authentication, a convincing answer and an evaluator score are different evidence.

### Cited Findings

- MCP `latest` redirected to revision `2026-07-28` at inspection. Its HTTP authorization specification requires audience-bound token validation; stdio uses a different credential boundary. Optional extensions are independently versioned. [Specification](https://modelcontextprotocol.io/specification/2026-07-28), [authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- MCP security guidance prohibits raw token forwarding, requires state handles be checked against authenticated principals, and treats local server launch commands as local code execution requiring consent and restricted privileges. Foundry's term OAuth identity passthrough must not be read as permission to forward arbitrary API tokens. [MCP security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- Foundry tracing is GA for prompt/hosted agents; workflow/external agent coverage is preview. Server-side traces follow connection of Application Insights; application code may need client instrumentation. Traces can include inputs, outputs and tool arguments, with retention/billing tied to telemetry configuration. [Tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup)
- Foundry evaluators distinguish system outcomes and process/tool behavior. Several evaluators are preview; Quality Grader is deprecated. MCP/functions/file search are supported, while the article limits certain tool/grounding evaluators for other tool types. Check the exact supported-input matrix. [Evaluator catalog, updated 2026-09-30](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)

### Inferences

- Add a compact failure-contract table to the integration guide: expired consent -> request consent without claiming tool success; timeout after a write -> reconcile state/idempotency before retry; interrupted stream -> report incomplete; wrong tenant -> backend denial; trace contains secrets -> redact before telemetry; incompatible evaluator/tool type -> deterministic integration evidence plus a supported judge.
- Add a trust-boundary diagram or table naming caller identity, agent identity, MCP audience and backend authorization. Transport compatibility does not implement business entitlements. Bind approvals and state handles to the verified actor and operation.

### Gaps

- None of the source checks proves a selected MCP implementation conforms to revision 2026-07-28, that audience exchange is correct, that tracing redacts data, or that a real agent meets accuracy/cost targets. Record negotiated protocol and test the actual boundary separately.
