"""Explain failures in the existing fabricated traces; no provider measurements."""
import json
from pathlib import Path
import sys

EVAL = Path(__file__).resolve().parents[2] / "05-evaluation"
sys.path.insert(0, str(EVAL))
from eval_agent_traces import evaluate


def main():
    golden = json.loads((EVAL / "fixtures" / "golden_cases.json").read_text(encoding="utf-8"))
    fixtures = json.loads((EVAL / "fixtures" / "candidate_traces.json").read_text(encoding="utf-8"))
    expected = {
        "example-safe": (5, []),
        "example-unsafe": (2, ["cross-dealer-request", "request-to-place-order"]),
    }
    names = [candidate["name"] for candidate in fixtures["candidates"]]
    assert len(names) == len(expected) and set(names) == set(expected)
    print("Fabricated traces; token and latency fields are not measurements.")
    for candidate in fixtures["candidates"]:
        report = evaluate(golden, candidate["runs"])
        assert (report["pass_count"], report["blocking_failures"]) == expected[candidate["name"]]
        verdict = "BLOCK" if report["blocking_failures"] else "PASS"
        print(f"{candidate['name']}: {report['pass_count']}/{report['case_count']} {verdict}")
        for result in report["results"]:
            if not result["passed"]:
                print(f"  {result['case_id']}: tool_match={result['tool_selection_and_args_passed']}; "
                      f"status_match={result['outcome_passed']}; blocking={result['blocking_failure']}")


if __name__ == "__main__":
    main()
