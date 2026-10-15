# Introducing spec-driven development into an existing application

This approach is designed for a dealer-facing portal with ongoing feature work, production dependencies and developers already using Copilot/Cursor.

## Inventory first

Capture the current entry points, routes/API contracts, build pipeline, test suite, data classification, auth/roles, logging, deployment gates, and the current release process. Record owner and source locations. Do not treat a coding agent's repository summary as authoritative without checking key files.

## Pick a vertical slice

Choose an additive feature or behavior correction with few downstream dependencies. Write the current behavior as a test before adding new behavior. Decide how to handle current callers, migration/backfill, feature flags, analytics changes and rollback. No uncontrolled schema changes in the pilot.

## Put minimal instructions at repository root

Start with `AGENTS.md` pointing to conventions and the accepted spec. Use path-scoped agent instructions where your coding assistant supports them. Keep security and access policy in CI, runtime identity and tool controls. Do not allow an AI process to edit its own approval or policy files without authorized review.

## Pilot design

Two developers or small working groups should implement equivalent scoped changes using a common evaluation rubric. Capture model/harness version, context files read, token/cost records if available, test failures, retries, review minutes and results. Compare to the current baseline and keep controls for task complexity.

## Expand only with evidence

Adopt a reusable template or skill when it reliably reduces ambiguity or review burden. Establish change ownership for template updates and deprecation, documented version compatibility, rollback and onboarding. Identify the person who will maintain the framework when upstream changes arrive.
