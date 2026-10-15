# Implementation plan

Approved source: [SPEC-001](dealer-support-advisor.md) (synthetic). Owner: sample developer. This plan documents the included implementation and is available for a modification exercise.

## Design

- Use `DemoPrincipal` injected by the local handler. Never accept a user-supplied role or dealer ID as proof of authorization.
- A deterministic classifier checks prohibited actions/policy claims *before* supported intents.
- Read-only synthetic `catalog` is the single approved answer source.
- Return structured response (`status`, `answer`, `source_ids`, `tool_calls`, `request_id`).
- Implement a loopback-only HTTP server with strict request parsing and a static local UI.
- Record golden-case outcomes and map AC IDs to test method names.

## Security rationale

This is a **nonproduction** example. A hardcoded lab principal makes the HTTP path testable; it is not a valid identity layer and must be replaced with a real authenticating proxy/service before connecting actual dealer data.

## Verification

| Task | Requirement | Verification |
|---|---|---|
| T-001 | FR-001 to FR-004 | Unit and golden intent tests |
| T-002 | FR-005, FR-008 | Denied authorization and prohibited-action tests |
| T-003 | FR-006, FR-007 | Validation and cited source tests |
| T-004 | NFR-001 to NFR-003 | Local HTTP integration tests, loopback binding and request ID checks |
| T-005 | All AC IDs | `validate_contracts.py`, `evaluate.py`, CI suite |

Before any actual Foundry extension: create a separate ADR for model necessity, explicit API/tool contracts, Entra identity, tenant data separation, telemetry data capture, fail-safe behavior and deployment/rollback.
