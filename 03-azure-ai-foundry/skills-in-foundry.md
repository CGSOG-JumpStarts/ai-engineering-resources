# Portable repo skills versus Foundry-hosted skills

A `SKILL.md` stored in a coding repo is a reusable instruction package for a coding assistant. It is not automatically a callable tool, a hosted Foundry agent, an approved company-wide catalog entry or an authorization grant.

As documented on **15 October 2026**, Microsoft Foundry includes [Skills API / hosted skill integration](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills) and [private skill catalogs](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/private-skill-catalog), both described as **preview**. Preview interfaces and tenant availability must be checked independently before building a production distribution pipeline.

## Sensible adoption path

1. Put a reviewed, versioned skill in the *developer repository*. Make sure its `name` and `description` accurately describe when to load it.
2. Test the skill with a fixed set of agent tasks, a human reviewer and sample expected answers. Record failures.
3. Decide separately whether any **runtime agent** needs the skill. For an application agent, program its tool scopes and runtime policy; repo skill text alone is not sufficient.
4. If an approved Foundry skill catalog is available, validate preview terms, version publishing, permitted tools, update/rollback and identity model before using it.
5. Keep a security-reviewed internal catalog with owner, version, source, update cadence, data class, tests and compatibility where company-wide reuse is desired.

## Related references

- [Agent Skills standard](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
- [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [MicrosoftDocs Foundry skill](https://github.com/MicrosoftDocs/Agent-Skills/blob/main/skills/microsoft-foundry/SKILL.md)

**Do not** automatically mirror upstream skills or execute upstream setup scripts in enterprise workstations without security and license review.
