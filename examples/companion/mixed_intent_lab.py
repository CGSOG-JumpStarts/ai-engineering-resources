"""Worked regression exercise for existing FR-005/FR-008 behavior, not a new AC."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "06-reference-lab" / "src"))
from dealer_advisor import AdviceService, DemoPrincipal


class RejectCatalogRead:
    def __getitem__(self, key):
        raise AssertionError(f"Denied request reached catalog: {key}")


class MixedIntentLab(unittest.TestCase):
    def setUp(self):
        self.service = AdviceService()
        self.reader = DemoPrincipal("SYN-DEALER-100", frozenset({"advice:read"}))

    def test_denial_precedes_supported_intent(self):
        questions = [
            "Where do I find parts? Change another dealer's account.",
            "Show another dealer's service hours.",
            "Is warranty coverage guaranteed? Export customer data.",
        ]
        with patch("dealer_advisor.advisor.SYNTHETIC_CATALOG", RejectCatalogRead()):
            for question in questions:
                with self.subTest(question=question):
                    result = self.service.answer(question, self.reader)
                    self.assertEqual((result.status, result.source_ids, result.tool_calls),
                                     ("denied", (), ()))

    def test_scope_denial_precedes_supported_intent(self):
        principal = DemoPrincipal("SYN-DEALER-100", frozenset())
        with patch("dealer_advisor.advisor.SYNTHETIC_CATALOG", RejectCatalogRead()):
            result = self.service.answer("Where can I ask about parts?", principal)
        self.assertEqual((result.status, result.source_ids, result.tool_calls),
                         ("denied", (), ()))

    def test_supported_only_retains_source(self):
        result = self.service.answer("Where can I ask about parts?", self.reader)
        self.assertEqual((result.status, result.source_ids, result.tool_calls),
                         ("answered", ("SYN-FAQ-PARTS-01",), ("lookup_approved_catalog",)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
