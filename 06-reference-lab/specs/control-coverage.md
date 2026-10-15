# Control coverage and limitations

This document distinguishes the sample's automated assertions from manual architecture observations. The contract validator proves **an acceptance criterion maps to an existing test method**; running the test suite proves its current outcome. It cannot establish production authorization, network isolation or compliance.

| Requirement | Evidence | Status in offline lab | Production limitation |
|---|---|---|---|
| FR-001 to FR-003 | AC-001 to AC-003 and supported tests | Executable synthetic assertions | No real policy or data |
| FR-004 | AC-004, AC-010 | Executable negative tests | LLM hallucination not tested |
| FR-005 | AC-005, AC-008, AC-009 | Executable denial tests | No real enterprise RBAC or backend action system |
| FR-006 | AC-006, AC-011 | Executable validation tests | No API gateway or rate limiting |
| FR-007 | AC-001/002/003 source assertions | Executable source ID tests | IDs refer to fictional catalog |
| FR-008 | AC-007 | Executable injected principal check | Hardcoded demo principal; **not authenticated HTTP** |
| NFR-001 | Local binding validation test; `create_server()` rejects non-loopback | Executable local server check | Not a production network policy |
| NFR-002 | Python stdlib imports; no HTTP client in runtime | Manual source inspection | Software bill of materials needed in production |
| NFR-003 | Request ID checked in AC-001 and AC-012; request bodies not logged | Executable fields and source inspection | No real tracing backend |
| NFR-004 | Static synthetic catalog; no persistence code | Manual source inspection | Does not demonstrate retention compliance |
| NFR-005 | `evaluate.py` times in-process decisions | Executable measurements; no defined SLO | Not representative of real traffic/Foundry |

Human reviewers must still inspect the code and recording/retention behavior. A mapping validator cannot detect a misleading or meaningless test assertion.
