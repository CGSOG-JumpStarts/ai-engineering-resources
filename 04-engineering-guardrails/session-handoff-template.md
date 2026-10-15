# Session handoff template

Save a short record with the task or PR when a session ends or another developer takes over. Link artifacts instead of repeating transcripts. Remove inapplicable fields and exclude secrets/customer data.

```text
Task / owner:
Repository revision and branch:
Working-tree changes to preserve:
Approved spec path + revision:
Requirement / acceptance / task IDs:
Current state: planned | in progress | ready for review | blocked

Relevant files, interfaces and decisions:
Decisions made, with owner or approval reference:
Changes completed:

Checks actually executed:
- Command, working directory, interpreter/tool version:
- Result, counts and evidence location:

Checks not executed and why:
Known failures or uncertainties:
Current permissions and disallowed actions/data:
Next bounded action and acceptance evidence:
Decision needed, from whom:
```

The next session should verify the revision and working-tree state, read the spec and inspect evidence before continuing. A handoff's "passed" statement does not replace test output, CI results or a reviewer decision.

For token comparisons, record provider usage across the whole accepted change, including failed attempts and review. Label missing usage as unknown; do not infer tokens from transcript length. See [context guidance](context-and-token-efficiency.md).
