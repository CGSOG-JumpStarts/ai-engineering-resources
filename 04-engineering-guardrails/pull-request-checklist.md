# PR review checklist for AI-assisted changes

**Request/feature:** ______   **Owner:** ______   **Spec revision/commit:** ______

- [ ] Change corresponds to approved requirement IDs; out-of-scope changes explained.
- [ ] Human-readable behavior and error cases are correct for users.
- [ ] No invented APIs, schema fields, policy statements or success claims.
- [ ] API contracts remain compatible, or the migration is documented.
- [ ] Access is checked server-side; denied/cross-tenant cases tested.
- [ ] Side-effecting tool calls use correct auth, approval and idempotency rules.
- [ ] Test commands actually executed; reviewer can reproduce; skipped tests disclosed.
- [ ] Secrets/dependency scanning completed with material findings resolved.
- [ ] Logs/traces don't contain sensitive data; retention and telemetry reviewed.
- [ ] Cost/latency implications and new external model/tool calls identified.
- [ ] Rollback/feature flag and on-call ownership documented.
- [ ] A human reviewer has inspected critical generated code and evidence.

## Review disposition

Decision: Approve | Request changes | Hold  
Reviewer and time: ______  
Evidence links and open risks: ______
