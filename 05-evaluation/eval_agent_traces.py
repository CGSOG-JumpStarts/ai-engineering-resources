#!/usr/bin/env python3
"""Deterministic trace scorer for invented fixtures; NOT a live model benchmark.

Run: python 05-evaluation/eval_agent_traces.py [--json]

Never interpret the synthetic tokens/latencies as provider measurements. Pass/fail
compares exact allowed call sequences and expected outcome status, and blocks
forbidden actions regardless of aggregate results.
"""

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).parent


def percentile(values, fraction):
    if not values:
        return None
    ordered = sorted(values)
    rank = (len(ordered) - 1) * fraction
    lower = math.floor(rank)
    upper = math.ceil(rank)
    return round(ordered[lower] + (ordered[upper] - ordered[lower]) * (rank - lower), 1)


def evaluate(golden, runs):
    expected = {item["case_id"]: item for item in golden}
    observed = {item["case_id"]: item for item in runs}
    if len(observed) != len(runs):
        raise ValueError("Duplicate case IDs in runs")
    if set(observed) != set(expected):
        raise ValueError(f"Case mismatch: missing={sorted(set(expected)-set(observed))}; extra={sorted(set(observed)-set(expected))}")
    results = []
    for case_id, reference in expected.items():
        actual = observed[case_id]
        exact_tools = actual["tools"] == reference["expected_tools"]
        exact_status = actual["status"] == reference["expected_status"]
        passed = exact_tools and exact_status
        results.append({
            "case_id": case_id,
            "passed": passed,
            "tool_selection_and_args_passed": exact_tools,
            "outcome_passed": exact_status,
            "blocking_failure": bool(reference["blocking"] and not passed),
        })
    times = [r["latency_ms"] for r in runs]
    return {
        "pass_count": sum(r["passed"] for r in results),
        "case_count": len(results),
        "blocking_failures": [r["case_id"] for r in results if r["blocking_failure"]],
        "p50_latency_ms_fixture": percentile(times, 0.5),
        "p95_latency_ms_fixture": percentile(times, 0.95),
        "input_tokens_fixture": sum(r["input_tokens"] for r in runs),
        "output_tokens_fixture": sum(r["output_tokens"] for r in runs),
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Machine-readable report")
    args = parser.parse_args()
    gold = json.loads((ROOT / "fixtures/golden_cases.json").read_text(encoding="utf-8"))
    candidates = json.loads((ROOT / "fixtures/candidate_traces.json").read_text(encoding="utf-8"))
    report = {item["name"]: evaluate(gold, item["runs"]) for item in candidates["candidates"]}
    if args.json:
        print(json.dumps({"warning": candidates["fixture_notice"], "report": report}, indent=2))
    else:
        print("SYNTHETIC FIXTURE ONLY: no LLMs, Azure services, or actual measurements")
        for name, result in report.items():
            verdict = "BLOCK" if result["blocking_failures"] else ("REVIEW" if result["pass_count"] < result["case_count"] else "PASS")
            print(f"{name}: {result['pass_count']}/{result['case_count']} cases; {verdict}; blocking={result['blocking_failures']}")
            print(f"  Fixture p50={result['p50_latency_ms_fixture']}ms p95={result['p95_latency_ms_fixture']}ms; tokens={result['input_tokens_fixture']} in/{result['output_tokens_fixture']} out")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
