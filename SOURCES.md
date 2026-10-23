# Sources and feature-status notes

## October 21, 2026 update

The following primary sources were inspected for the [October research update](reports/October%202026%20engineering%20update.md). Release tags and feature labels are observations from public pages, not tested installations or archived proof of every earlier October revision. Other entries in the historical index below were not automatically revalidated. No authenticated repositories, Azure tenants or enterprise systems were accessed.

| Source | Observation or use in this update |
|---|---|
| [Spec Kit releases](https://github.com/github/spec-kit/releases), [quickstart](https://github.github.io/spec-kit/quickstart.html), [installation](https://github.github.io/spec-kit/installation.html) | Latest listed release v1.2.2, October 19; separate terminal setup and chat skills; record active feature and installed integration |
| [Spec maintenance](https://github.github.io/spec-kit/guides/evolving-specs.html), [existing projects](https://github.github.io/spec-kit/guides/existing-projects.html) | Team chooses artifact-aging convention; review managed-file updates separately from feature intent |
| [BMad installation](https://docs.bmad-method.org/start/install-bmad/), [releases](https://github.com/bmad-code-org/BMAD-METHOD/releases) | Page still labels v6.12 stable/v7 preview alpha; releases list v6.12.4, October 14. Earlier ETA is not release evidence |
| [HVE RPI](https://raw.githubusercontent.com/microsoft/hve-core/main/docs/rpi/README.md), [BMad planning](https://docs.bmad-method.org/plan/choose-a-planning-path/) | Select research/planning for actual evidence or decision gaps; smaller work can take a smaller path |
| [Agent Skills](https://agentskills.io/specification), [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) | Progressive loading and host-specific discovery/behavior; metadata compatibility does not establish execution parity |
| [Context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | Compaction risks and provider-native cache/usage semantics; no universal saving inferred |
| [Agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | January 9, 2026 guidance distinguishes trials, trajectories and outcomes; repeated success is distinct from best-of-several success |
| [Hosting choices](https://learn.microsoft.com/en-us/agent-framework/hosting/), [Foundry integration](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent), [deployment](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent) | Hosted Agents GA; package-specific prerelease labels remain separate; no SDK/region qualification performed |
| [Durable execution](https://learn.microsoft.com/en-us/agent-framework/hosting/durable-extension), [checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | Recovery mechanisms require explicit application state, retry and storage contracts |
| [Identity concepts](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity), [identity migration](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications) | Legacy/new agent models coexist in guidance; confirm actual object model and role assignments rather than assume one publishing identity rule |
| [Foundry MCP authentication](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication), [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), [MCP security](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | User-context flow, audience validation, approval/state binding and local-code boundaries. `latest` resolved to MCP 2026-07-28; implementation support untested |
| [Foundry Skills](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills), [private catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/private-skill-catalog) | Both remain preview at inspection; skill/project/catalog permissions are separate concerns |
| [Tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup), [evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) | Verify agent/tool support and lifecycle per feature; telemetry access/content and evaluator suitability require integration checks |

Some Microsoft Learn responses displayed authorization banners while returning readable article bodies. The research used those bodies without signing in. Contradictory identity wording and untested tenant/SDK/region behavior remain explicit unknowns. Frameworks and mutable docs were not independently exercised. The [research notes](research_notes/October%202026%20engineering%20update/workflows.md), [practice notes](research_notes/October%202026%20engineering%20update/practices.md) and [Foundry/MCP notes](research_notes/October%202026%20engineering%20update/foundry-mcp.md) separate source observations from editorial recommendations.

## Historical reading index: October 15, 2026

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

## Historical recheck scope: October 15

Public pages inspected on 2026-10-15:

- Spec Kit README: spec/plan/task/implement/converge workflow and CLI setup. Its documented prerequisite is Python 3.11+; the offline lab separately supports Python 3.10+.
- BMad installation: v6.12 stable and v7 preview alpha at inspection time. Installation commands were read, not executed.
- HVE Core README: RPI workflow and the warning that interfaces may change. Its licensing section notes MIT coverage and exceptions for some derived skill content; review the relevant license and notices before reuse.
- Foundry hosted-agent overview, deployment guide and Agent Framework hosting overview: managed container hosting versus self-hosting. The hosting overview explicitly states Hosted Agents are generally available; package lifecycle and feature restrictions still need separate checks.
- Foundry Skills API and private skill catalog: preview guidance. The Skills API page requires a preview feature header.
- Official Microsoft Foundry Skill guide, agent evaluator catalog, Agent Skills specification, VS Code skill guide and MCP authorization tutorial: implementation and review references.

No external installers, model calls, documentation-refresh network helper or deployment commands were run. Public documentation checks do not establish tenant configuration, regional availability, installed SDK compatibility, measured quality or licensing permission for a particular redistribution.

For protocol authorization guidance, use the [official MCP tutorial](https://modelcontextprotocol.io/docs/tutorials/security/authorization). It is a protocol reference, not evidence that a particular MCP server implements the controls.
