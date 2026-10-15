# Foundry docs adviser, portable skill

Read [SKILL.md](SKILL.md) for the workflow and [priority source index](references/priority-sources.md) for direct Microsoft links. Both work offline as dated reference materials.

To list approved URLs (does **not** fetch the network):

```bash
python scripts/refresh_references.py --list
```

To refresh a local **untrusted** text snapshot of each allowlisted Microsoft Learn page, with explicit permission:

```bash
python scripts/refresh_references.py --refresh
```

The script uses the Python standard library, enforces HTTPS `learn.microsoft.com/en-us/...`, size/time limits, redirect checks, per-URL SHA-256 hashes and a timestamped `.cache/manifest.json`. It never executes content or authenticates to Azure. Snapshot extraction is a convenience and may miss tables, warnings or interactive elements; use the **live official page** for final capability and preview status confirmation. The helper does not run automatically.

Optional context: Microsoft itself publishes a [Foundry skill](https://github.com/MicrosoftDocs/Agent-Skills/blob/main/skills/microsoft-foundry/SKILL.md), which can be evaluated separately in an approved environment.
