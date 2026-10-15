# Introducing consistent AI development practices

## Select a real pilot without risking live dealer data

Name an engineering lead and an application owner, then identify an additive or low-risk feature with synthetic fixtures. Measure the existing build/review process as a baseline. Both developers and analysts should agree on acceptance criteria before generating code.

## Try one technique at a time

Start with durable feature specs and the spec review skill. Next add the one selected framework, then tool/identity review if MCP is part of the job. Comparing many frameworks concurrently in the same repo obscures causality.

## Minimum sample evidence

| Signal | Source |
|---|---|
| Implemented requirements / missing acceptance tests | Spec-to-test traceability file plus CI |
| Change acceptance and rework | PR timeline and reviewer notes |
| Duration and interruptions | Harness logs, tickets and human time tracking |
| Tokens and cost | Provider telemetry/invoice plus model name |
| Foundry tool accuracy/reliability | Evaluation cases and correlated tool traces |
| Access violations | Negative tests plus service-side authorization events |
| User value | Product analytics or stakeholder outcome tied to baseline |

## Standardize only reviewed assets

Assign an owner to each shared `SKILL.md`, instruction file and template. Record purpose, version, dependencies, security classification and regression cases. Require pull-request review before marketplace publication or wide rollout. Upstream releases are inputs to a change review, not automatic updates to every engineering workspace.

## When to request a hands-on workshop

A workshop becomes useful when the team has one real scenario, confirmed attendance, a data-safe test environment, and a decision they want to validate. The package is suitable for review without committing to a workshop.
