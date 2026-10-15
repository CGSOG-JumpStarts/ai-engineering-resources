# Reusable engineering skills

Four **original**, portable skill packages are included. Each contains a `SKILL.md` with Agent Skills-compliant `name` and `description` frontmatter. They work by giving a compatible coding assistant a reviewed procedure; they do not grant access to tools, documents or cloud resources.

| Skill | Use when | Outputs |
|---|---|---|
| `foundry-docs-advisor` | Foundry architecture, feature availability, RBAC, SDK or agent troubleshooting | Verified source index, dated source notes, options, preview caveats and next checks |
| `spec-reviewer` | Reviewing a feature spec before implementation | Requirement gaps, ambiguous AC, missing negative tests and approval questions |
| `secure-mcp-review` | Connecting a new MCP server, hosted agent or action tool | Threat assessment, auth/approval matrix and acceptance checks |
| `agent-evaluation-designer` | Comparing agents/models/prompts or tool changes | Reproducible golden cases, metrics, thresholds and failure taxonomy |

## Add to a project

Copy **only the skill folder(s) you need** to the repo's `.agents/skills/` directory. Compatible VS Code/Copilot installations also support `.github/skills/`; consult the installed tool's current documentation before assuming another harness discovers the same locations. The repository root `AGENTS.md` is a different file: it gives broader project instructions.

```text
my-project/
  AGENTS.md
  .agents/skills/
    foundry-docs-advisor/SKILL.md
    spec-reviewer/SKILL.md
```

Review bundled scripts, licenses and references before enabling external network access. Copying a skill does **not** import its scripts into the runtime's trusted execution path. Do not distribute customer-only content inside a shared skill without access controls.

## Foundry docs refresh

`foundry-docs-advisor/scripts/refresh_references.py` is a conservative, optional helper. Listing local sources is offline. `--refresh` explicitly fetches **only** the allowlisted HTTPS Microsoft Learn URLs in `references/upstream.json`, saves a timestamped text snapshot to `.cache/`, and can produce a short provenance manifest. The output is reference material, not trusted instructions. There is no scheduled background job and the refresh is not proof of a product feature's availability.

## Related Microsoft skills

Microsoft also publishes Foundry skills in [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills/tree/main/skills/microsoft-foundry) and [microsoft/azure-skills](https://github.com/microsoft/azure-skills/tree/main/skills/microsoft-foundry). These are **links**, not vendored dependencies. Some upstream skills run dependency-installation scripts; inspect those separately before adopting them in a managed environment.

See the [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) and [VS Code skill discovery guide](https://code.visualstudio.com/docs/agent-customization/agent-skills).
