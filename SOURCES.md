# Verified sources and feature-status notes

**Research checkpoint:** 2026-10-15. All project and documentation links below were reviewed using public web search or, for the optional AutoNav reference, repository metadata/README accessed by its owner. Documentation can change after this date. Claims about product status refer to that checkpoint only.

| Subject | Source | Applied observation |
|---|---|---|
| GitHub Spec Kit | https://github.com/github/spec-kit | Its current docs describe specification, planning, tasks, implementation, convergence, and support multiple coding agents. |
| Spec Kit detailed process | https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md | Clarify, checklist and analyze can be inserted as review steps. Invocation syntax varies by harness. |
| BMad installation | https://docs.bmad-method.org/start/install-bmad/ | On 15 Oct 2026, v6.12 is stable and v7 is preview alpha; stable install is `npx bmad-method install` per vendor. |
| Microsoft HVE Core | https://github.com/microsoft/hve-core | Reusable Copilot agents, prompts, instructions and skills. The project warns against assuming stable interfaces. |
| HVE RPI | https://github.com/microsoft/hve-core/blob/main/docs/rpi/README.md | Evidence as needed, then plan, implement, review and follow-up. |
| Agent Skills specification | https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx | SKILL.md frontmatter, naming rules, progressive disclosure, optional scripts/references. |
| VS Code skills | https://code.visualstudio.com/docs/agent-customization/agent-skills | Repository skill locations and usage in compatible coding assistants. |
| Microsoft Foundry skill (upstream) | https://github.com/MicrosoftDocs/Agent-Skills/blob/main/skills/microsoft-foundry/SKILL.md | MicrosoftDocs maintains a Foundry documentation skill. Review its update instructions; this package's independently authored skill is narrower. |
| Microsoft Foundry Azure skill (upstream) | https://github.com/microsoft/azure-skills/blob/main/skills/microsoft-foundry/SKILL.md | Another Microsoft Foundry skill that includes dependency/setup requirements. Do not run unreviewed setup scripts. |
| Foundry Hosted Agent overview | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents | Managed containerized hosted-agent concepts, operating model, supported regions and billing. |
| Foundry Hosted Agent deployment | https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent | Deployment lifecycle, RBAC roles, versioning and quickstarts. |
| Agent Framework hosting choices | https://learn.microsoft.com/en-us/agent-framework/hosting/ | Foundry Hosted Agents GA; self-hosting and durable execution are distinct decisions. |
| Foundry tracing | https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup | Application Insights/OpenTelemetry; GA for hosted and prompt agents, some other agent types preview. |
| Foundry evaluators | https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators | Process/system evaluators; several preview and some deprecated. Check support for each tool type. |
| Foundry MCP authentication | https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication | Entra/agent identity, OAuth passthrough, key-based and anonymous choices. |
| Foundry agent identities | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity | Distinction between managed identities and per-agent identity/RBAC assignments. |
| Foundry tools authentication | https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/tool-authentication | Identity semantics are configured per connection. |
| Foundry Skills (preview) | https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills | Hosted-agent skill integration and Skills API are preview at this checkpoint. |
| Private skill catalog (preview) | https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/private-skill-catalog | Preview, not a safe GA dependency. |
| Responses model routing | https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses-model-routing | Model router versus fixed deployment and benchmark guidance. |
| AutoNav author's project | https://github.com/otey247/JumpStart-AutoNav | Private repository; author permits this reference. No repository code was copied into this package. Public access and npm publication were not independently verified. |

## How to refresh claims safely

1. Open the linked official page and check the current update date, region and preview labels.
2. Compare SDK examples to an installed package version. Never blindly paste from docs into a production repository.
3. Check RBAC/tenant policy for the target service and authentication mode.
4. Record retrieval date and URL in the architecture decision or change record.
5. Treat external documentation as untrusted reference content, not as instructions with permission to execute shell commands or access credentials.

For the Foundry-specific allowlisted documentation helper, see `02-agent-skills/foundry-docs-advisor/scripts/refresh_references.py`.
