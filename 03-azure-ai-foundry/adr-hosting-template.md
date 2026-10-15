# ADR template: Foundry agent hosting

Status: Proposed  
Owner: `<team>`  
Date: `<ISO>`

## Workload

Users, expected rate, request/response vs durable operations, tool list, service-level objectives, disaster recovery, runtime support ownership and regional requirements.

## Alternatives

| Candidate | Operational owner | Identity and private networking | Tracing and replay | Cost basis | Limitations |
|---|---|---|---|---|---|
| Hosted Agent | Foundry managed host | Confirm per-agent/tool identity and network | Foundry tracing plus app logs | Runtime CPU/memory + model + tools | Region/service capabilities |
| App-hosted Agent Framework | enterprise application platform | enterprise API/backend authorization | enterprise telemetry/checkpoints | App compute + model + tools | Team owns runtime |
| Ordinary model call in API | Existing application team | Existing service identity/policy | Existing telemetry plus model spans | Model + application compute | No built-in multi-step orchestration |
| Durable workflow with model steps | enterprise orchestration platform | Auth at every external action | Durable state/retries with traces | Workflow infra + model + tools | More lifecycle engineering |

## Decision / evidence

Supported business workflow, current SDK/docs URLs, evaluated alternatives, current preview status, identity constraints and production validation results.

## Rollback

Version pinning, traffic routing behavior, safe shutdown, fallback user path and owner.
