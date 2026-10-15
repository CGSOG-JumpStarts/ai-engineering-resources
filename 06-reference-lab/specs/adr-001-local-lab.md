# ADR-001: stdlib-only synthetic reference lab

Date: 2026-10-15  
Status: Accepted for learning package

## Context

This company-agnostic learning package needs a repeatable exercise for development practices before any cloud connection. It assumes no production contracts, company data or live integration.

## Decision

Ship a Python standard-library-only service with an exact fictional FAQ and deterministic rules. Include unit/API tests, golden evaluation and spec traceability. Bind only to localhost and do not persist questions. Runtime identity is a fixed demo principal that cannot be confused with production security.

## Alternatives

- A live Foundry agent would require tenant, billing, cloud permissions, model selection, API contracts and data approvals; none are assumed.
- A FastAPI app would provide more production-shaped routing but require installation and supply chain; unnecessary for offline training.

## Reversal condition

When used in a real system, replace every sample identity/catalog/server element with reviewed production components. Do not use this application or its default content directly in a dealer portal.
