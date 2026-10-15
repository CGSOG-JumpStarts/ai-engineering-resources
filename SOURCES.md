# Verified sources and feature-status notes

**Documentation checkpoint:** 2026-10-15. This is a primary-source reading index. The recheck scope below records which references were inspected for this update. Other entries remain reading links; their presence does not establish current feature availability. Documentation can change after this date. No authenticated repository, Azure tenant or enterprise system was accessed.

| Subject | Source | Applied observation |
|---|---|---|
| GitHub Spec Kit | https://github.com/github/spec-kit | Its current docs describe specification, planning, tasks, implementation, convergence, and support multiple coding agents. |
| Spec Kit detailed process | https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md | Clarify, checklist and analyze can be inserted as review steps. Invocation syntax varies by harness. |
| BMad installation | https://docs.bmad-method.org/start/install-bmad/ | On 15 Oct 2026, v6.12 is stable and v7 is preview alpha; stable install is `npx bmad-method install` per vendor. |
| Microsoft HVE Core | https://github.com/microsoft/hve-core | Reusable Copilot agents, prompts, instructions and skills. The project warns against assuming stable interfaces. |
| HVE RPI | https://github.com/microsoft/hve-core/blob/main/docs/rpi/README.md | Evidence as needed, then plan, implement, review and follow-up. |
| Agent Skills specification | https://agentskills.io/specification | SKILL.md frontmatter, naming rules, progressive disclosure, optional scripts/references. |
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
| Optional author framework reference | https://github.com/otey247/JumpStart-AutoNav | Access, current release and distribution rights are unverified in this update. It is not required for any exercise. Ask the owner for a reviewed, shareable demo or distribution. |

## How to refresh claims safely

1. Open the linked official page and check the current update date, region and preview labels.
2. Compare SDK examples to an installed package version. Never blindly paste from docs into a production repository.
3. Check RBAC/tenant policy for the target service and authentication mode.
4. Record retrieval date and URL in the architecture decision or change record.
5. Treat external documentation as untrusted reference content, not as instructions with permission to execute shell commands or access credentials.

For the Foundry-specific allowlisted documentation helper, see `02-agent-skills/foundry-docs-advisor/scripts/refresh_references.py`.

## Recheck scope for this update

Public pages inspected on 2026-10-15:

- Spec Kit README: spec/plan/task/implement/converge workflow and CLI setup. Its documented prerequisite is Python 3.11+; the offline lab separately supports Python 3.10+.
- BMad installation: v6.12 stable and v7 preview alpha at inspection time. Installation commands were read, not executed.
- HVE Core README: RPI workflow and the warning that interfaces may change. Its licensing section notes MIT coverage and exceptions for some derived skill content; review the relevant license and notices before reuse.
- Foundry hosted-agent overview, deployment guide and Agent Framework hosting overview: managed container hosting versus self-hosting. The hosting overview explicitly states Hosted Agents are generally available; package lifecycle and feature restrictions still need separate checks.
- Foundry Skills API and private skill catalog: preview guidance. The Skills API page requires a preview feature header.
- Official Microsoft Foundry Skill guide, agent evaluator catalog, Agent Skills specification, VS Code skill guide and MCP authorization tutorial: implementation and review references.

No external installers, model calls, documentation-refresh network helper or deployment commands were run. Public documentation checks do not establish tenant configuration, regional availability, installed SDK compatibility, measured quality or licensing permission for a particular redistribution.

For protocol authorization guidance, use the [official MCP tutorial](https://modelcontextprotocol.io/docs/tutorials/security/authorization). It is a protocol reference, not evidence that a particular MCP server implements the controls.
