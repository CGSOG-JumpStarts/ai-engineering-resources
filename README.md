# Spec-driven agentic engineering resources

A company-agnostic code companion for developers, engineering leads and architects getting started with AI-assisted software development. Follow a fictional support advisor from a request through its specification, implementation, tests, HTTP API and evaluation. Microsoft Foundry is an optional platform-specific track; the core workflow and offline exercises require no cloud account or model API key.

## Start here

Read [Spec-driven engineering: a code companion](GUIDE.md). Its seven connected chapters include code walkthroughs, expected outputs, exercises and a worked test solution. The [companion index](examples/companion/README.md) links each chapter to runnable programs and the existing implementation.

```bash
python examples/companion/run_all.py
```

This runs four programs with Python 3.10+ and no network access. Add `--http` to include a temporary localhost server and three API requests. See [Start here](START-HERE.md) for the shorter route and [the lab guide](06-reference-lab/README.md) to run the browser UI.

After the walkthrough, compare [Spec Kit, BMad, HVE Core and a template-based approach](01-spec-driven-development/framework-comparison.md), or review the [four reusable skills](02-agent-skills/README.md) for your own project.

The [resource map](RESOURCE-MAP.md) connects common questions to readings, exercises and review artifacts. The [October 2026 research update](reports/October%202026%20engineering%20update.md) explains the latest additions: proportional planning, spec maintenance, context/cache boundaries, independent outcome checks and Foundry identity/recovery decisions.

## Included

| Folder | Resources |
|---|---|
| [Spec-driven development](01-spec-driven-development/fundamentals.md) | Fundamentals, framework comparison, brownfield adoption, prompts, spec/plan/task templates and a worked exercise |
| [Agent skills](02-agent-skills/README.md) | Original skills for spec review, Foundry research, MCP security review and evaluation design |
| [Microsoft Foundry](03-azure-ai-foundry/platform-guide.md) | Capabilities, hosted/container and self-hosted choices, identity, integration, observability and official implementation links |
| [Engineering guardrails](04-engineering-guardrails/agent-instructions.md) | Agent instructions, data handling, MCP permissions, context/token use and review guidance |
| [Evaluation](05-evaluation/README.md) | Model selection, tool accuracy, reliability, latency/cost measures, scorecard and a runnable synthetic trace comparison |
| [Reference lab](06-reference-lab/README.md) | Python standard-library app, local API/UI, synthetic spec, traceability, unit tests and golden-case evaluator |

## First team experiment

Choose a small change in an existing application or an advisory-agent workflow. Use synthetic data, agree on acceptance criteria, and record the current process as a baseline. Compare review effort, defects, requirement coverage, actual tool/token use and cost through the accepted change. [Pilot guidance](04-engineering-guardrails/adoption-plan.md) and the [scorecard](05-evaluation/scorecard-template.md) provide a place to record evidence.

The lab uses a fictional dealer-support domain as a concrete example. It contains no company policies or customer data. Its routing is deterministic and makes no model calls. Passing its checks demonstrates the local exercise's contracts; model quality, live MCP integration and cloud deployment require separate tests.

## Sources and maintenance

[Source notes](SOURCES.md) record public references and dated feature-status checks. The [validation record](VALIDATION.md) lists checks executed for this update and remaining limits. Commands, SDKs, model availability and preview labels can change. Review upstream source and licenses before installing tools or copying material. This package links to third-party projects and does not bundle their source code.

Microsoft's newer documentation uses **Microsoft Foundry**; older resources use **Azure AI Foundry**. Verify the selected feature, SDK, region and identity configuration against current documentation before implementation. No credentials, Azure accounts or enterprise systems are needed to review this repository.
