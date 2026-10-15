import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from dealer_advisor import AdviceService, DemoPrincipal

P = DemoPrincipal("SYN-DEALER-100", frozenset({"advice:read"}))

class SupportedTests(unittest.TestCase):
    def setUp(self):
        self.service = AdviceService()

    def test_ac_001_warranty_source(self):
        r = self.service.answer("How do I start a warranty support request?", P)
        self.assertEqual(r.status, "answered")
        self.assertEqual(r.source_ids, ("SYN-FAQ-WARRANTY-01",))
        self.assertEqual(r.tool_calls, ("lookup_approved_catalog",))
        self.assertIn("fictional", r.answer.lower())
        self.assertTrue(r.request_id)

    def test_ac_002_parts_source(self):
        r = self.service.answer("Where can I ask about parts availability?", P)
        self.assertEqual(r.status, "answered")
        self.assertEqual(r.source_ids, ("SYN-FAQ-PARTS-01",))

    def test_ac_003_hours_source(self):
        r = self.service.answer("How do I find dealer service hours?", P)
        self.assertEqual(r.status, "answered")
        self.assertEqual(r.source_ids, ("SYN-FAQ-HOURS-01",))

    def test_sources_never_mixed(self):
        r = self.service.answer("Can I find parts?", P)
        self.assertEqual(len(r.source_ids), 1)
        self.assertNotIn("WARRANTY", r.source_ids[0])
