# Checklist for assessing an existing Foundry agent

**Function and value**

- [ ] Identify target user and one measurable job the agent should complete.
- [ ] Document approved knowledge sources and fresh/stale information rules.
- [ ] Classify the agent as advisory/read-only or action-capable.
- [ ] Define acceptable abstentions, sources, and escalation behavior.

**Architecture and ownership**

- [ ] Record agent type, host, project, region, model deployment and API version.
- [ ] Identify owners for prompt, code, tools, source data, IAM, and monitoring.
- [ ] Distinguish external tools already implemented from desired future actions.
- [ ] Record state/session, failure recovery, compatibility and version rollback strategy.

**Identity and security**

- [ ] Identify the caller's actual identity source and data permissions.
- [ ] Verify downstream authorization independently of instructions to the LLM.
- [ ] Inventory approved MCP servers, allowed methods, parameter schemas and audiences.
- [ ] Validate secret handling and policies for tools that write, transmit, or delete data.
- [ ] Decide whether Basic/Standard storage and network choices meet data policy.

**Quality and operations**

- [ ] Establish a golden dataset with positive, negative, ambiguous, stale and cross-tenant cases.
- [ ] Baseline task completion, groundedness, tool success, latency and costs.
- [ ] Trace request, model, tool calls, errors, approval and user-visible result together.
- [ ] Define release gate, error budget/latency objective and alert owner.
- [ ] Retest after every model, prompt, tool, skill or retrieval change.

**Do not claim this checklist is complete** for enterprise until the team confirms its architecture, business requirements, security approvals, and operational objectives.
