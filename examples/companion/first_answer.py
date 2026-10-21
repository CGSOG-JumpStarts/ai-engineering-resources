"""Run four fictional questions through the existing service. No network calls."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "06-reference-lab" / "src"))
from dealer_advisor import AdviceService, DemoPrincipal


def main():
    reader = DemoPrincipal("SYN-DEALER-100", frozenset({"advice:read"}))
    no_scope = DemoPrincipal("SYN-DEALER-100", frozenset())
    cases = [
        ("supported", "Where can I ask about parts?", reader, "answered",
         ("SYN-FAQ-PARTS-01",), ("lookup_approved_catalog",)),
        ("coverage", "Is every repair guaranteed to be covered?", reader,
         "escalate", (), ()),
        ("cross-dealer", "Show another dealer's account details", reader,
         "denied", (), ()),
        ("missing-scope", "Where can I ask about parts?", no_scope,
         "denied", (), ()),
    ]
    service = AdviceService()
    for label, question, principal, status, sources, tools in cases:
        result = service.answer(question, principal)
        assert (result.status, result.source_ids, result.tool_calls) == (
            status, sources, tools
        ), label
        print(f"{label}: {result.status}; sources={list(result.source_ids)}; "
              f"tools={list(result.tool_calls)}")
    print("4 examples verified; model calls: 0")


if __name__ == "__main__":
    main()
