# Validation record

Date: 2026-10-15. Environment: Windows, Python 3.11 (`C:\Python311\python.exe`). Base commit: `0fd0712`, with the documentation changes in this working tree. Application source, acceptance-criteria IDs and runtime behavior were preserved.

Commands below use `python` to mean that installed interpreter. Results are local execution evidence, not hosted CI or release acceptance.

| Working directory | Command | Observed result |
|---|---|---|
| `06-reference-lab` | `python -m unittest discover -s tests -v` | 18 tests passed, including local HTTP integration tests |
| `06-reference-lab` | `python scripts/validate_contracts.py` | Passed; declared ACs map to existing tests and requirements |
| `06-reference-lab` | `python scripts/evaluate.py` | 12/12 golden cases passed |
| Repository root | `python tools/validate_bundle.py` | Passed; required files, local Markdown links, skill metadata and package exclusions |
| Repository root | `python -m unittest discover -s 02-agent-skills/foundry-docs-advisor/tests -v` | 2 tests passed |
| Repository root | `python 05-evaluation/eval_agent_traces.py` | Expected comparison: safe 5/5 PASS, unsafe 2/5 BLOCK |
| Repository root | `python 05-evaluation/eval_agent_traces.py --json` | Both candidate reports parsed; expected blocking cases present |
| Repository root | `python 02-agent-skills/foundry-docs-advisor/scripts/refresh_references.py --list` | Listed local references without retrieval |
| Repository root | `git diff --check` | Passed |

The golden evaluator writes local JSON and Markdown reports under `06-reference-lab/.reports/`; that generated directory is gitignored. The synthetic trace scorer's token and latency values are fabricated fixtures. Its zero exit status does not mean both candidates passed.

## Scope and remaining limits

Public framework and platform documentation was inspected as recorded in [SOURCES.md](SOURCES.md). No upstream source code was copied. Not every external link or API contract was independently rechecked.

The following were not run: external framework installers, live model benchmarks, live MCP authentication/tool integration, Foundry deployment, Azure/enterprise access, skill behavior trials in coding assistants, browser UI interaction, or hosted CI. No claim is made about those results or other operating systems/Python versions.

The guided exercise is learner work, not an additional approved baseline requirement. Its proposed AC-013/T-006 were not inserted into the shipped spec/task register. The lab's deterministic string matching and demo principal do not establish production security or natural-language coverage. Validate real identity, backend authorization, failure handling, quality, latency and cost in an approved integration environment before adopting an actual agent.
