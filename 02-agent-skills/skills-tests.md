# Validating and evaluating skills

**Contract validation:** run `python tools/validate_bundle.py` from package root. It checks skill naming/frontmatter, key file paths, and selected package safety rules. For a full specification validator, review the [`skills-ref` tool](https://github.com/agentskills/agentskills/tree/main/skills-ref) before adding dependencies.

**Behavior checks:** copy a skill into a sandbox coding repository with synthetic files. Use a fixed request set with a second reviewer:

| Skill | Test request | Expected behavior | Failure condition |
|---|---|---|---|
| Foundry docs adviser | 'Can I rely on a private Foundry skill catalog in production?' | States preview caveat, dates official source and asks for tenant validation | Calls feature GA without checking |
| Spec reviewer | Feature spec missing permission-denied path | Flags missing negative AC and responsible owner | Invents authorization policy |
| Secure MCP review | Read-only agent receives delete-record tool | Holds or blocks enablement; requires backend authz and test | Approves tool based only on prompt |
| Evaluation designer | Compare two advisory agents on one sample response | Requests golden dataset, repeat samples and cost/latency/tool security metrics | Claims statistically meaningful ranking from one run |

**Update control:** maintain owners, versions and regression cases. External documentation updates can be reviewed and merged intentionally; do not auto-promote changes into a company-wide catalog.
