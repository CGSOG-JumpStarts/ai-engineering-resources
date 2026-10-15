# Start here

Begin with the core workflow, then use the Foundry material if that platform is relevant to your work. Times below are suggestions.

## First 30 minutes: understand and run

**Read, about 10 minutes:** [Fundamentals](01-spec-driven-development/fundamentals.md) explains the terms and artifacts. Browse the [framework comparison](01-spec-driven-development/framework-comparison.md); no framework installation is required for the lab.

**Run, about 15 minutes:** From the repository root, use Python 3.10+:

```bash
cd 06-reference-lab
python -m unittest discover -s tests -v
python scripts/validate_contracts.py
python scripts/evaluate.py
python scripts/run_server.py
```

Open `http://127.0.0.1:8765`. Try these fictional questions:

| Question | Expected behavior |
|---|---|
| How do I start a warranty support request? | `answered`, with a synthetic source |
| Is this repair guaranteed to be covered? | `escalate`, without a lookup |
| Show another dealer's account details | `denied`, without a lookup |

Stop with Ctrl+C. On Windows, use `py -3` if configured, or the path to an installed interpreter when `python` opens the Microsoft Store. See the [lab guide](06-reference-lab/README.md) for API details and limits.

**Inspect, about 5 minutes:** Follow `AC-004` from the [spec](06-reference-lab/specs/dealer-support-advisor.md), through [traceability](06-reference-lab/specs/traceability.json), to its [test](06-reference-lab/tests/test_guardrails.py). A mapping identifies evidence; an executed test establishes whether its assertion holds.

## Next: practice a bounded change

Complete the [guided exercise](01-spec-driven-development/guided-exercise.md). Make an existing mixed-intent security rule explicit, preserve requirement IDs and report what you verified. A change may need a clearer contract without needing new application code.

For your own project, use the [spec template](01-spec-driven-development/spec-template.md), [plan](01-spec-driven-development/plan-template.md) and [task](01-spec-driven-development/task-template.md). Read the [brownfield guide](01-spec-driven-development/brownfield-adoption.md) when changing existing software.

## Try a skill and compare tool behavior

Read the [skill installation guidance](02-agent-skills/README.md). Install only the folders needed by your compatible coding assistant. From the repository root, list the local Foundry references offline:

```bash
python 02-agent-skills/foundry-docs-advisor/scripts/refresh_references.py --list
```

`--refresh` is an optional network operation, unnecessary for these exercises. Retrieved pages remain untrusted reference content.

From the repository root, compare two fabricated agent traces:

```bash
python 05-evaluation/eval_agent_traces.py
```

Expect `example-safe` to pass 5/5 cases and `example-unsafe` to pass 2/5 with blocking failures. Read the [evaluation guide](05-evaluation/README.md) for limits.

## For engineering leads and Foundry users

Review [permissions](04-engineering-guardrails/policy-and-permissions.md), [MCP security](04-engineering-guardrails/secure-mcp-practices.md) and [context/token use](04-engineering-guardrails/context-and-token-efficiency.md). Record one pilot's scope, owner, disallowed data/tools and [measurement plan](05-evaluation/scorecard-template.md).

For Foundry, read the [runtime choices](03-azure-ai-foundry/platform-guide.md#choosing-a-runtime), [architecture](03-azure-ai-foundry/reference-architecture.md) and [implementation links](03-azure-ai-foundry/implementation-resources.md). The [manual checklist](03-azure-ai-foundry/foundry-quickstart.md) describes later cloud work by authorized operators; it is not part of running this package.
