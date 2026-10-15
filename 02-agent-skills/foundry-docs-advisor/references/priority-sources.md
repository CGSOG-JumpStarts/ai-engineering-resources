# Foundry source index

Use a narrow set of official documentation pages for the task. Research checkpoint: **2026-10-15**. 'Preview' means specifically labelled as preview at this checkpoint, not a guarantee of current availability.

## Runtime and lifecycle

- [Agent Framework hosting overview](https://learn.microsoft.com/en-us/agent-framework/hosting/) — Foundry Hosted Agents vs self-hosting vs Durable extension. Documented hosted GA.
- [Hosted Agent overview](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) — managed container and region/resource operating model.
- [Deploy a Hosted Agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent) — prerequisites, versions, RBAC, deployment techniques. Always verify project type and target region.

## Security and tools

- [MCP tool authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) — key, Entra, OAuth passthrough and anonymous modes.
- [Toolbox authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/tool-authentication) — who each connection represents.
- [Agent identity](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) — per-agent identity and role assignments.

## Quality, cost and visibility

- [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) — system and process metrics, tool-type limitations, mixed preview/GA status.
- [Tracing setup](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) — server-side traces with linked Application Insights; review data/privacy options before enabling content capture.
- [Responses API model routing](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses-model-routing) — router and fixed-model benchmark patterns.

## Skills (preview)

- [Use skills in Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills) — skills APIs/toolbox integration described as preview.
- [Private skill catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/private-skill-catalog) — preview.
- [Microsoft-maintained Foundry docs skill](https://github.com/MicrosoftDocs/Agent-Skills/blob/main/skills/microsoft-foundry/SKILL.md) — example of a periodically maintained docs skill.

## Keeping an answer honest

A docs fetch tells you what Microsoft documents, not what your tenant is configured to use. Verify permissions, allowed region, subscription, policy, model deployment and actual installed packages with authorized operations. A stale cached snapshot must not override the current live page.
