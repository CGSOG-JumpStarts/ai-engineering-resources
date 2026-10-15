# Prompts to start a bounded engineering change

These prompts assume a repo-aware coding tool with normal review and test access. Adapt names and permissions to the selected repo.

## Clarify requirements before planning

> Read `AGENTS.md` and the existing public API and test conventions. Review this feature request: [sanitized text]. List ambiguous business rules, impacted roles and data, negative cases, and requirements that need an owner decision. Draft only a feature spec using `01-spec-driven-development/spec-template.md`. Do not implement or modify unrelated files. Do not infer enterprise policies.

## Produce a reviewable implementation plan

> Using the approved feature spec, inspect the affected code paths and tests. Produce a bounded implementation plan mapped to FR/NFR IDs and identify data/permission boundaries, failure modes, test cases, and rollback options. Do not edit code until the plan and decisions are approved.

## Implement with verification

> Implement only approved tasks [IDs], preserve existing public contracts, and add failing tests for each acceptance criterion first where feasible. Stop for approval before external calls, new permissions, migrations, data exfiltration, or destructive operations. Report code changes, executed tests, failures, and remaining risks.

## Foundry documentation research

> Use the `foundry-research` skill to research the current supported Foundry options for a read-only dealer advisor. Use official primary documentation. Separate GA service capability from preview integration packages. Cite every claim and record the retrieval date. Describe identity, tool contracts, audit, networking, supported regions and evaluation plan before recommending deployment.
