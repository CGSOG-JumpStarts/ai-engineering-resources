# Companion examples

Read [the guide](../../GUIDE.md) alongside these programs. Python 3.10+ and its standard library are sufficient. Run commands from the repository root. The programs resolve repository paths from their own files, so no package installation or `PYTHONPATH` setting is needed.

## Learning contract

These examples exercise the existing synthetic lab. They do not alter its approved spec, application source or acceptance IDs. The mixed-intent exercise provides a worked test solution for existing denial behavior; proposed `AC-013` remains a learner change, not a newly approved baseline criterion.

| Program | Expected behavior |
|---|---|
| `first_answer.py` | Shows answered, escalated, denied and missing-scope results; verifies their source/tool fields |
| `trace_contract.py` | Locates AC-004, its FR-004 link and mapped test; prints the actual test source, without claiming to run it |
| `mixed_intent_lab.py` | Runs 3 tests, including mixed-intent denial, scope denial and a supported-only control; prohibited paths must not read the catalog |
| `evaluate_traces.py` | Uses the existing scorer; verifies safe 5/5 and unsafe 2/5 with two blocking cases; prints individual failures |
| `http_roundtrip.py` | Starts a temporary loopback-only server, verifies 3 requests and shuts it down; needs local socket access |

All data is fictional. There are no model calls, external API/MCP requests, credentials or cloud resources. The HTTP program uses `127.0.0.1` and an operating-system-selected temporary port. It never accepts a remote server address. Programs do not write files. Python may create its normal gitignored bytecode cache.

## Run the examples

```bash
python examples/companion/run_all.py
```

This runs the first four programs. Each exits nonzero if its assertions fail. The fixture comparison deliberately contains an unsafe candidate; the example succeeds when it detects the documented failures.

Include the HTTP walkthrough when local sockets are permitted:

```bash
python examples/companion/run_all.py --http
```

Use `py -3` or your installed interpreter path if `python` is not configured. `--http` changes only this runner's example selection. It does not change any operating-system permission. A socket permission error should be reported, not worked around by widening the server binding.

## Find the source behind a chapter

| Guide chapter | Companion | Existing application/evidence |
|---|---|---|
| [1. A first answer](../../GUIDE.md#1-a-first-answer) | [first_answer.py](first_answer.py) | [advisor](../../06-reference-lab/src/dealer_advisor/advisor.py), [catalog](../../06-reference-lab/src/dealer_advisor/catalog.py) |
| [2. Read the contract](../../GUIDE.md#2-read-the-contract) | [trace_contract.py](trace_contract.py) | [spec](../../06-reference-lab/specs/dealer-support-advisor.md), [mapping](../../06-reference-lab/specs/traceability.json) |
| [3. Make a bounded change](../../GUIDE.md#3-make-a-bounded-change) | [mixed_intent_lab.py](mixed_intent_lab.py) | [learning exercise](../../01-spec-driven-development/guided-exercise.md), [guardrail tests](../../06-reference-lab/tests/test_guardrails.py) |
| [4. Cross the HTTP boundary](../../GUIDE.md#4-cross-the-http-boundary) | [http_roundtrip.py](http_roundtrip.py) | [HTTP wrapper](../../06-reference-lab/src/dealer_advisor/api.py) |
| [5. Read evaluation evidence](../../GUIDE.md#5-read-evaluation-evidence) | [evaluate_traces.py](evaluate_traces.py) | [scorer](../../05-evaluation/eval_agent_traces.py), [fixtures](../../05-evaluation/fixtures/candidate_traces.json) |

These examples do not establish production authentication, general natural-language coverage, live model quality or Foundry/MCP compatibility. Their purpose is to make each local claim inspectable and executable.
