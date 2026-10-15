# enterprise | AI-assisted engineering field guide

**Spec-driven development, reusable agent skills and Microsoft Foundry**  
Audience: Engineering leads, dealer-portal developers, solution architects and AI platform owners.

This is a technical handoff to help your team compare approaches, establish engineering standards, and try a working example. It is not a enterprise system design, production agent, or a recommendation to migrate an existing application without review.

## Start here

1. Read [START-HERE.md](START-HERE.md) for the short review path and first exercises.
2. Read the [framework comparison](01-spec-driven-development/framework-comparison.md) and [public tool setup guide](01-spec-driven-development/tools-quickstart.md). Choose **one** primary workflow for a small pilot rather than installing several overlapping orchestrators.
3. Walk through [the example](01-spec-driven-development/example-workflow.md), then run the [offline dealer-support lab](06-reference-lab/README.md). It needs Python 3.10+ and no Azure access or LLM API key.
4. Browse the [portable agent skills](02-agent-skills/README.md). Start with the Foundry docs adviser when comparing features or designing Foundry integrations.
5. Use the [Foundry architecture guide](03-azure-ai-foundry/platform-guide.md), [security baseline](04-engineering-guardrails/policy-and-permissions.md), and [evaluation scorecard](05-evaluation/scorecard-template.md) as review material.

## Included

| Folder | Contents | Why review it |
|---|---|---|
| `01-spec-driven-development` | Framework comparison, brownfield guide, examples, specification templates | Establish a common approach for Copilot/Cursor teams |
| `02-agent-skills` | Four original portable skills, reference index and on-demand documentation refresh helper | Reuse the same review and Foundry practices across developers |
| `03-azure-ai-foundry` | Hosted vs self-hosted decision, tool identity, deployment, tracing, skills and reference architecture | Extend an existing advisory-agent project with deliberate runtime choices |
| `04-engineering-guardrails` | Repo instructions, MCP controls, data handling, token context, PR checklist | Set boundaries before granting agents tools or production access |
| `05-evaluation` | Model and tool benchmarks, reusable evaluation matrix and scorecard | Compare outcomes, cost, latency and reliability with evidence |
| `06-reference-lab` | Runnable dealer-support exercise with versioned specs, a minimal API, local tests and evaluator | Try the entire review loop without cloud credentials |

## Recommended first experiment

Select one **small, low-risk dealer-portal workflow**, replace its data with synthetic examples, agree on acceptance criteria, and have two developers complete the same scoped change with one selected process. Compare review effort, defects, scope coverage, tool usage, token use, and maintainability. A baseline should come from recorded runs, not estimates made before execution.

The included offline lab uses fictional dealer records and rule-based decisions. It deliberately does not call a foundation model. Its objective is to demonstrate **durable specifications, approval gates and measurable tests**, not to imply that a rule engine substitutes for a production AI advisor.

## Framework posture

- **GitHub Spec Kit:** a straightforward starting process for developers already using coding agents. Current documentation includes specify, plan, tasks, implement, and converge.
- **BMad Method:** structured product, UX and engineering workflows. As checked 15 October 2026, **v6.12 is the stable choice; v7 is preview alpha**.
- **Microsoft HVE Core:** useful RPI (Research/Plan/Implement/Review) patterns for GitHub Copilot; its repository cautions that the project is rapidly evolving.
- **Jump Start AutoNav:** an optional, broader lifecycle reference described by its author, including human gates and post-release learning. Treat access and package availability as **unverified for enterprise** until a shareable distribution is confirmed. No code from that private repository is bundled here.

See [selection guidance](01-spec-driven-development/selection-guide.md) and [source notes](SOURCES.md).

## Foundry terminology and version caution

Microsoft is using **Microsoft Foundry** in newer documentation; some older resources use **Azure AI Foundry**. This field guide uses *Foundry* for both where appropriate. Hosting features, SDKs, preview labels and RBAC role names evolve rapidly. Do not assume a capability is generally available because it appears in a how-to article. The live docs linked in each section are authoritative at deployment time.

Specifically, Foundry Hosted Agents are documented as generally available; **private skill catalogs and certain skills features remain preview**. Validate target region, policy, quota and tenant permissions before rollout.

## Privacy and provenance

This ZIP contains original sample text/code and references to public third-party resources. It does not include customer credentials, internal project data or vendor source-code copies. Public links may require additional authentication, may change, and are not embedded dependencies. A referenced AutoNav repository is private; request access or a reviewed public distribution from its owner before sharing that specific material outside its approved audience.

Source verification and feature status: [SOURCES.md](SOURCES.md). This repository intentionally does not install or deploy anything to enterprise or Azure.
