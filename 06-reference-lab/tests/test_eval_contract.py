from pathlib import Path
import json
import unittest

LAB = Path(__file__).resolve().parents[1]
class EvaluationContractTests(unittest.TestCase):
    def test_golden_cases_valid(self):
        cases = json.loads((LAB/'evaluation/cases.json').read_text())
        self.assertGreaterEqual(len(cases), 10)
        ids = [x['id'] for x in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertIn(case['expected_status'], ['answered','denied','escalate','error'])
            self.assertIn('question', case)
            if case['expected_status'] == 'answered':
                self.assertTrue(case.get('expected_source'))
            else:
                self.assertFalse(case.get('expected_source'))
