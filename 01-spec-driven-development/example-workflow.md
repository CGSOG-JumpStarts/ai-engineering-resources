# Worked spec-to-implementation example

**Scenario:** a dealer submits a portal support question about parts, warranty or store hours. The application recommends the appropriate next step based on a small approved, fictional catalog. It must not invent warranty coverage or expose dealer-specific data. This is a synthetic learning scenario, not enterprise policy.

## Step 1: Capture intent

Problem: developers want a consistent way to route common requests without introducing unsupported policy statements. Users need a short answer and a named reference. Security reviewers need a clear refusal for unsupported or unauthorized requests.

Open `06-reference-lab/specs/dealer-support-advisor.md` and identify the functional requirements, security rules and acceptance criteria. No actual dealer records are included.

## Step 2: Plan one change

Ask a coding assistant:

> Read the current specification and existing source files. Propose only the smallest change required to meet AC-004 (unsupported policy questions must be escalated, not answered). List files to change, risks, tests and assumptions. Do not modify code until the plan is approved.

Write the result into `06-reference-lab/specs/implementation-plan.md` or a separate dated change plan. Do not overwrite agreed scope without a human decision.

## Step 3: Implementation under a bounded contract

> Implement only the approved task T-001. Respect `AGENTS.md` and the dealer-support spec. Preserve existing API contracts and tests. Add or update a test for every affected acceptance criterion. Do not call external APIs or invent policies.

Run the unit tests and the contract validator. The sample lab is already implemented. Use the [guided exercise](guided-exercise.md) to practice a bounded spec/test change; introduce new behavior only after its spec and task are reviewed.

## Step 4: Convergence / independent review

Ask a second developer or an independent assistant to identify spec clauses that code does not satisfy. Verify every claimed result with a concrete test. Run `python scripts/validate_contracts.py`, then `python scripts/evaluate.py`. Human approval is still needed for scope, sensitive behavior and a release decision.

## Step 5: Foundry translation

Only after the deterministic lab meets its acceptance criteria, decide whether a foundation model adds value for natural-language intake, document extraction or explanation. Keep authorization and transactional actions outside model text. Map approved knowledge and tool calls to the Foundry architecture and record quality, tool-call success, p95 latency and true usage cost.

## An anti-pattern

'Build a helpful dealer agent using all available tools' does not identify a safe set of actions, authorized data, expected results, error paths or a way to prove success. A well-written spec is the operational contract for evaluation and review.
