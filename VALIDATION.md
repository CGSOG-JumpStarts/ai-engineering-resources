# Validation record

## Code companion walkthrough: October 21, 2026

Added [GUIDE.md](GUIDE.md) and the [companion programs](examples/companion/README.md). The guide follows the existing implementation through questions, contracts, regression tests, HTTP and evaluation. Baseline application source, approved specifications, acceptance IDs and skill instructions were preserved. The earlier research edits remain in the working tree.

Local environment: Windows, Python 3.11.0 (`C:\Python311\python.exe`). Results below were obtained after the executable examples and navigation changes.

| Working directory | Command | Observed result |
|---|---|---|
| Repository root | `python examples/companion/run_all.py` | Four programs completed without sockets; all assertions and 3 companion tests passed |
| Repository root | `python examples/companion/run_all.py --http` | Five programs completed, including 3 successful HTTP assertions and server cleanup; localhost access was permitted for this run |
| `06-reference-lab` | `python -m unittest discover -s tests -v` | All 18 passed, including HTTP integration tests, with localhost access |
| `06-reference-lab` | `python scripts/validate_contracts.py` | Passed |
| `06-reference-lab` | `python scripts/evaluate.py` | 12/12 golden cases passed |
| Repository root | `python tools/validate_bundle.py` | Passed, including new guide/example paths and local Markdown links |
| Repository root | `python -m unittest discover -s 02-agent-skills/foundry-docs-advisor/tests -v` | 2 passed |
| Repository root | `git diff --check` | Passed |

The documented first-answer and HTTP output blocks match these runs. The trace companion detected the intended unsafe candidate rather than approving it. The existing CI workflow now includes the five companion programs; hosted CI was not run here. Browser interaction, live coding-assistant skill behavior, model calls, MCP integration and Foundry deployment were not tested. The Foundry chapter is an integration-design walkthrough, not executable cloud code or a fresh feature-status recheck.

## October 21, 2026 research update

Environment: Windows, Python 3.11.0 (`C:\Python311\python.exe`). Base commit: `f200a95`. This update changes documentation and research records; application source, runtime behavior, specs, acceptance IDs and skills were preserved.

The runtime checks below ran before these documentation-only edits. The final bundle audit and `git diff --check` passed after the edits.

| Check | Observed result |
|---|---|
| Lab `python -m unittest discover -s tests -v` | Initial sandbox run had 4 HTTP errors (`WinError 10013`, socket access denied); the other 14 passed. A permitted loopback-access rerun passed all 18 in 0.665s |
| Lab `python scripts/validate_contracts.py` | Passed |
| Lab `python scripts/evaluate.py` | 12/12 golden cases passed |
| Root `python tools/validate_bundle.py` | Passed before edits |
| Root documentation-helper unit discovery | 2 tests passed |
| Root `python 05-evaluation/eval_agent_traces.py` | Expected safe 5/5 PASS and unsafe 2/5 BLOCK |

Public-source research is documented in [SOURCES.md](SOURCES.md). No installer, live model/MCP/Foundry test, Azure/enterprise access, coding-assistant skill behavior trial, browser interaction or hosted CI ran. The sandbox failure and successful rerun are separate observations; no tests were weakened to avoid the socket boundary.

## Historical validation: October 15, 2026

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
