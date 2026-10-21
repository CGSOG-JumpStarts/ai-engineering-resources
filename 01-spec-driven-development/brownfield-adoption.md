# Introducing spec-driven development into an existing application

Use this approach for an existing application with current callers, operational dependencies and established engineering practices. The dealer-support domain in this package is only a fictional example.

## Inventory first

Capture the current entry points, routes/API contracts, build pipeline, test suite, data classification, auth/roles, logging, deployment gates, and the current release process. Record owner and source locations. Do not treat a coding agent's repository summary as authoritative without checking key files.

## Pick a vertical slice

Choose an additive feature or behavior correction with few downstream dependencies. Write the current behavior as a test before adding new behavior. Decide how to handle current callers, migration/backfill, feature flags, analytics changes and rollback. No uncontrolled schema changes in the pilot.

## Write a preservation list for the selected slice

A full-system specification is unnecessary for a bounded change. Identify what the affected slice must preserve and point to its current evidence:

| Preserve | Record before implementation |
|---|---|
| Public request/response contract | Source location, current schema and compatibility tests |
| Authorization and data scope | Principal source, enforcement point and denial tests |
| Error behavior | Error codes, timeout/retry semantics and client expectations |
| Stored state and rollout constraints | Migration/backfill assumptions, feature flag and rollback boundary |

Give each unresolved question an owner and say whether it blocks implementation. For example, a missing owner decision about cross-account access blocks a new lookup; it does not authorize the agent to infer a rule. A characterization test records current behavior, including an existing defect, so mark what is preserved versus deliberately corrected.

The [Spec Kit existing-project guide](https://github.github.io/spec-kit/guides/existing-projects.html) discusses a reviewable baseline and bounded next change. Inspect initialization diffs before accepting replacement of framework-managed files. Existing maintained repo context can be reused after verifying it against the affected code.

## Put minimal instructions at repository root

Start with `AGENTS.md` pointing to conventions and the accepted spec. Use path-scoped agent instructions where your coding assistant supports them. Keep security and access policy in CI, runtime identity and tool controls. Do not allow an AI process to edit its own approval or policy files without authorized review.

## Pilot design

Two developers or small working groups should implement equivalent scoped changes using a common evaluation rubric. Capture model/harness version, context files read, token/cost records if available, test failures, retries, review minutes and results. Compare to the current baseline and keep controls for task complexity.

## Expand only with evidence

Adopt a reusable template or skill when it reliably reduces ambiguity or review burden. Establish change ownership for template updates and deprecation, documented version compatibility, rollback and onboarding. Identify the person who will maintain the framework when upstream changes arrive.
