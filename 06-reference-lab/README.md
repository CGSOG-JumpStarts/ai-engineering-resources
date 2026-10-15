# Dealer-support advisor: local spec-driven exercise

A working, **fictional** support-answer application showing how approved specs, tasks, deterministic behavior, tests and evaluation evidence fit together. This is a teaching reference, **not** a enterprise dealer policy catalog or a production AI agent.

## What it does

- Answers common *synthetic* warranty support, parts-inquiry and service-hours process questions from a fictional approved FAQ catalog, returning a stable source ID.
- Escalates unsupported questions, including coverage-guarantee requests, rather than inventing policy.
- Blocks attempted account changes, data export and cross-dealer access; backend only supports read-only catalog lookup.
- Validates request structure and length.
- Includes a local browser UI, read-only catalog module, versioned specification, acceptance tests, contract coverage and a deterministic evaluator.

There are **no LLM/model calls, Azure resources, external MCP servers, API keys or real dealer records**. The fixed `DemoPrincipal` in the HTTP handler is a lab-only simulation and must **not** be reused as authentication in an actual deployment. Use a real identity provider and backend authorization for production.

## Requirements

Python **3.10+** with standard library only. Supported on Windows, macOS and Linux. The server binds **127.0.0.1**; it never listens on all interfaces.

## Run and verify

From `06-reference-lab`:

```bash
python -m unittest discover -s tests -v
python scripts/validate_contracts.py
python scripts/evaluate.py
python scripts/run_server.py
```

On Windows use `py -3` instead of `python` if that is how Python is installed. Open `http://127.0.0.1:8765`, ask a sample question and inspect the source ID shown. Stop with Ctrl+C.

Evaluator outputs are written to `.reports/` as `evaluation-report.json` and `evaluation-report.md`. The sample should pass its fixed golden cases, but that proves **this rule-based lab's contracts**, not model quality.

## Try the API

```bash
curl -sS -X POST http://127.0.0.1:8765/v1/advice \
  -H 'Content-Type: application/json' \
  -d '{"question":"How do I start a warranty support request?"}'
```

Expected fields: `status`, `answer`, `source_ids`, `tool_calls`, `request_id`. Source IDs are invented and begin with `SYN-`.

## The spec-driven review loop

1. Read `specs/dealer-support-advisor.md`, then `specs/implementation-plan.md` and `specs/tasks.md`.
2. Inspect `specs/traceability.json` to see which test verifies each acceptance criterion.
3. Change one **approved** requirement, e.g. clarify how a mixed intent should be treated. Add a new AC and new test *before* changing the service code.
4. Implement only the bounded planned task. Re-run tests, contract validator and evaluation.
5. Have a second engineer compare code to spec and review unauthorized/unsupported paths.
6. Document the observed difference in the [scorecard](../05-evaluation/scorecard-template.md).

## Teaching boundaries

- A real implementation must use Entra/OIDC, validated caller scope, actual approved sources, platform logging, privacy review, rate limits, operational SLOs and CI/CD. The local lab does not include them.
- Do not use this lab to decide warranty eligibility, inventory, repair advice or actual dealer status.
- Do not claim 'model token savings' from this lab; tokens and provider cost are **not applicable** because no model is called.
- `evaluation-report.json` reports deterministic test pass rate and elapsed time only. No real Foundry performance/effectiveness is inferred.

## Files

- `src/dealer_advisor/`: domain logic, catalog and local HTTP server.
- `web/`: plain local UI with no external assets.
- `scripts/run_server.py`: loopback-only server.
- `scripts/validate_contracts.py`: checks AC-to-tests mapping.
- `scripts/evaluate.py`: executes golden cases and emits JSON/Markdown.
- `tests/`: unit and local HTTP integration tests.
- `evaluation/cases.json`: golden input/output cases.

See the [broader architecture](../03-azure-ai-foundry/reference-architecture.md) before attaching any actual model or tool.
