# First 30 minutes with the package

## Engineering lead: review

**10 minutes:** Read [framework comparison](01-spec-driven-development/framework-comparison.md) and [selection guide](01-spec-driven-development/selection-guide.md). Write down whether the first pilot is a feature in the existing dealer portal or a new advisory-agent workflow.

**10 minutes:** Review the [Foundry hosting decision](03-azure-ai-foundry/platform-guide.md#choosing-a-runtime) and [MCP identity model](04-engineering-guardrails/secure-mcp-practices.md). List the tools the current advisory agents can use and which actions need a person to approve.

**10 minutes:** Agree on one measurable pilot and the [evaluation scorecard](05-evaluation/scorecard-template.md).

## Developer: try a complete local slice

From this ZIP's top-level folder:

```bash
cd 06-reference-lab
python -m unittest discover -s tests -v
python scripts/validate_contracts.py
python scripts/evaluate.py
python scripts/run_server.py
```

Open `http://127.0.0.1:8765` and submit a fictional dealer question. Stop the server with Ctrl+C. Full details, Windows commands and acceptance criteria are in the [lab guide](06-reference-lab/README.md).

## Try the portable skills

Install only the skill folders you want into a repository's `.agents/skills/` or, for compatible Copilot environments, `.github/skills/`. Review the skill code before execution. For a read-only listing of verified Foundry docs in this package:

```bash
python 02-agent-skills/foundry-docs-advisor/scripts/refresh_references.py --list
```

An explicit `--refresh` performs network retrieval from the allowlisted Microsoft Learn pages, when the local environment permits it. The skill itself contains reference links and instructions that work without refreshing content.

## Bring to the next discussion

- Current stack and portal architecture, with confidential details withheld from an external workshop until approved.
- One scoped dealer-portal requirement or advisory-agent workflow.
- Existing AI development tools and approved license/policy boundaries.
- Azure project type, region, agent hosting approach and current evaluation/tracing setup.
- Current baseline: defects, review time, token use, cost, latency or at least a plan to capture them.

No workshop or commercial engagement is implied by this package. It can be reviewed independently.
