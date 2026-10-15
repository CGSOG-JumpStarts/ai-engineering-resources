# Microsoft Foundry technical resources

The links below go to primary Microsoft documentation. They were researched on **15 October 2026**; this file does not embed copies of mutable vendor docs.

## Build and deploy

| Need | Primary source | Guidance |
|---|---|---|
| Understand available agent types | [Agents in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) | Decide between prompt, voice and hosted agents before choosing code patterns |
| Start with a declarative agent | [Prompt agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent) | Validate model deployment, tool restrictions and user identity |
| Bring your own agent code | [Hosted agent deployment](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent) | Deploy from container image or supported source ZIP; review prerequisites |
| Host Agent Framework code | [Agent Framework Hosted Agents](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) | Check package prerelease notices before pinning dependencies |
| Choose your own runtime | [Agent Framework hosting choices](https://learn.microsoft.com/en-us/agent-framework/hosting/) | Host and protocol selection are separate decisions |
| Plan long-running execution | [Agent Framework checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | Decide durable storage and replay behavior, not only model prompts |

## Secure and operate

| Need | Primary source | Guidance |
|---|---|---|
| Role assignment | [Foundry RBAC](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry?view=foundry-classic) | Verify current project/agent scope and role names before enabling users |
| MCP connections | [MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) | Choose identity passthrough vs service identity based on data permissions |
| Regional and service limits | [Quotas and limits](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions) | Check concurrency, per-agent tools, model quota, project setup |
| Network isolation | [Private networking](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks) | Check actual subnet, private endpoint and ACR behavior in target region/project |
| Version management | [Manage hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-agent) | Immutable agent versions, active version, monitoring and deletion |

## Quality and reusable agent development

| Need | Primary source | Guidance |
|---|---|---|
| Evaluate task and tool behavior | [Foundry agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) | System quality, tool selection, inputs, success, output use; note preview labels |
| Run evaluations in portal | [Evaluate apps and agents](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app) | Use representative data and thresholds; inspect evaluator support |
| Evaluate and optimize hosted agents | [Agent optimizer datasets (preview)](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/create-optimizer-dataset) | Preview; curated tasks and validators first, automatic optimization second |
| Install Microsoft's own coding-agent skill | [Microsoft Foundry Skill](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/use-microsoft-foundry-skill) | Official skill covers deployments, evaluation, traces, troubleshooting |
| Publish skills through Foundry | [Foundry skills and toolboxes (preview)](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills) | Distinguish file-based local skills from hosted skill API/toolbox distribution |
| Define portable skill files | [Agent Skills specification](https://agentskills.io/specification) | `SKILL.md` frontmatter, references and scripts |

## Suggested Microsoft Foundry Skill setup

Microsoft publishes the following installation command for a coding agent that supports skills:

```bash
npx skills add https://github.com/microsoft/azure-skills --skill microsoft-foundry
```

Follow the [official guide](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/use-microsoft-foundry-skill) for supported hosts and configuration. Review external code before installing it; no third-party tool is automatically downloaded by this package.

The **newly authored `foundry-research` skill in this ZIP** is intentionally narrower. It enforces evidence-based technical research, a status matrix, and a decision record for enterprise's context; it does not claim to replace Microsoft's skill or query an Azure tenant.

## Version change procedure

For any live engineering task, capture: documentation URL, retrieval date, resource region, setup mode, SDK language and version, preview/GA statement, deployment model, and the locally tested command. Keep the record with the implementation PR. Do not rely on copied code from an older blog post when official API samples have changed.
