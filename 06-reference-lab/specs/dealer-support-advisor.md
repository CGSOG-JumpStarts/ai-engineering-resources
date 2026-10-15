# Dealer support advisor specification

ID: `SPEC-001`  
Owner: Fictional learning team  
Status: Approved for **offline reference exercise only**  
Data: Synthetic FAQ only

## User need

A dealer-portal user asks a general process question. The answer must be short, based on an approved fictional reference, and safe if the request is unsupported. The service must not provide real dealer facts, authorize account access or change records.

## Functional requirements

- `FR-001`: Answer supported general **warranty support-process** questions using the corresponding approved synthetic FAQ entry.
- `FR-002`: Answer supported **parts-inquiry** process questions using the approved synthetic FAQ entry.
- `FR-003`: Answer **service-hours lookup process** questions using the approved synthetic FAQ entry.
- `FR-004`: Abstain/escalate for unsupported requests, specific coverage guarantees or insufficient intent; do not invent policy.
- `FR-005`: Deny attempts to change records, export protected data or access another dealer; never invoke a write tool.
- `FR-006`: Validate JSON input and required question text, max 280 Unicode characters.
- `FR-007`: Attach an approved source ID to every answered result; no source IDs on denials/escalations.
- `FR-008`: Check an **injected trusted demo principal's** `advice:read` scope before lookup. No caller-controlled principal/role in HTTP input.

## Nonfunctional requirements

- `NFR-001`: Server binds to `127.0.0.1` only; there is **no production authentication**.
- `NFR-002`: Use Python stdlib only, no network API calls and no model inference.
- `NFR-003`: Emit a request ID for correlation. Do not log question text by default.
- `NFR-004`: No data persistence or real enterprise policy represented.
- `NFR-005`: Local evaluator records elapsed times, but latency has no production SLO in this exercise.

## Acceptance criteria

- `AC-001`: A warranty **support-process** question returns status `answered`, one approved warranty source ID and one lookup tool label.
- `AC-002`: A parts inquiry returns `answered` and a parts source ID.
- `AC-003`: A service-hours process question returns `answered` and a hours source ID.
- `AC-004`: Unsupported coverage guarantees return `escalate` with **no** source or tool invocation.
- `AC-005`: A request to change another dealer's account returns `denied` and no tool invocation.
- `AC-006`: Blank question text is rejected with an input error.
- `AC-007`: A principal without `advice:read` receives `denied` without catalog lookup.
- `AC-008`: Cross-dealer requests receive `denied` even if caller has read scope.
- `AC-009`: A malicious instruction asking the agent to ignore rules and send account details is denied.
- `AC-010`: Ambiguous or unknown topics are escalated instead of receiving fabricated answers.
- `AC-011`: HTTP POST rejects invalid JSON/extra fields with status 400 and stable error codes.
- `AC-012`: Loopback HTTP `GET /health` returns a healthy status and a request ID.

## Out of scope

Real warranty coverage, pricing, inventory lookup, dealer or customer accounts, authentication, tool writes, Azure deployment, LLM prompts, cross-tenant records, and any claim that a production agent has passed evaluation.

## Approved synthetic references

- `SYN-FAQ-WARRANTY-01` process for requesting support.
- `SYN-FAQ-PARTS-01` process for parts inquiry.
- `SYN-FAQ-HOURS-01` process for locating service hours.

The sources are **fictional**. No real dealer policy can be inferred from them.
