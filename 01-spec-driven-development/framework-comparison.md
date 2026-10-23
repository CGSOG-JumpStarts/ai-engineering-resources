# Spec-driven development framework comparison

**Checked:** 21 October 2026. These are not substitutes for code review, security controls, an SDLC, or CI validation. Choose by workflow, maintenance requirements and team fit rather than popularity.

| Option | Best fit | What it contributes | Considerations | First trial |
|---|---|---|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Developers using Copilot, Cursor or other coding agents who want durable feature specs | Constitution; specify, clarify, plan, tasks, analyze, implement and converge steps; reusable templates | Adds documents and review work; prompts are not an enforcement boundary; verify exact harness command syntax against installed version | One scoped change with spec, plan, tasks and convergence |
| [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) | Teams needing more structured requirements, UX, product and engineering collaboration | Roles and workflows from discovery to implementation; richer elicitation | More process surface than a single engineer may want; **v6.12 stable, v7 preview alpha** at research date | Use v6.12 for a planned feature with product/BA input |
| [Microsoft HVE Core](https://github.com/microsoft/hve-core) | GitHub Copilot-oriented teams exploring repeatable research, planning, implementation and review | RPI task identity, evidence and review phases; reusable prompts, instructions, skills | Repository explicitly says the project is opinionated and rapidly changing; pin a known revision for experiments | RPI on a bounded integration change |
| **Jump Start AutoNav** (optional author reference) | A separate discussion of lifecycle coordination and human review gates | Request a demonstration from its owner | Access, released version and distribution rights are unverified in this update; no code is bundled | Consider only after a reviewed, accessible distribution is available |
| Existing repo conventions plus focused skills | Teams with mature CI, reviews and agreed engineering standards | Minimal disruption; small version-controlled templates and automated checks | Requires the team to create governance/traceability; no prebuilt lifecycle coordinator | Apply spec template, acceptance tests and a review skill to one PR |

## Release observations, not installation results

On October 21, the public [Spec Kit releases](https://github.com/github/spec-kit/releases) listed **v1.2.2** (October 19) as Latest. [BMad releases](https://github.com/bmad-code-org/BMAD-METHOD/releases) listed **v6.12.4** (October 14); its [installation page](https://docs.bmad-method.org/start/install-bmad/) still labeled v7 preview alpha and v6.12 stable. An elapsed release ETA is not evidence of general availability. These are documentation observations; no package or coding-assistant integration was installed for this update.

Spec Kit also documents separate bug-fixing and idea-assessment paths. A feature specification is appropriate when intended behavior needs definition; a diagnosed defect can use a bounded repair task. Choose the entry point before creating documents. See [proportional planning](recommended-practices.md#size-the-plan-to-the-change).

## Suggested first evaluation

Begin with **Spec Kit or existing repo conventions plus the included skills** for a small portal change. Use BMad when product-definition and UX work require more structure. Inspect HVE Core's RPI method if Copilot workflow orchestration is the immediate question. AutoNav can be demonstrated as an optional lifecycle reference by its owner, after access and packaging have been cleared.

Do not install multiple workflow frameworks into the same pilot repository on day one. Competing prompt files, task paths and instruction priority can create contradictory agent behavior and make results impossible to attribute.

## Comparison criteria for a real pilot

Score each option from recorded evidence on:

1. **Spec fidelity:** Were all approved functional and nonfunctional criteria implemented without scope drift?
2. **Review burden:** Minutes of human review/rework per accepted change; record actual effort.
3. **Context continuity:** Can a second developer resume from repository files in a fresh session?
4. **Security:** Can access permissions be enforced outside of prompts?
5. **Efficiency:** Cost, input/output tokens, retries and successful changes per dollar, using captured usage data.
6. **Portability and upgrade:** Ability to swap coding assistants or upgrade without breaking repo conventions.
7. **Evidence:** Explicit test, CI, reviewer and production measures linked to requirement IDs.

## Status caveat

Spec Kit and HVE Core change frequently. BMad installation guidance inspected on 21 October 2026 still identifies v6.12 as stable. Refer to [SOURCES.md](../SOURCES.md) rather than assuming command names, statuses or package versions remain unchanged.
