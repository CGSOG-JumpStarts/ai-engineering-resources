"""Offline tests for safe docs source selection and HTML cleaning."""
import importlib.util
from pathlib import Path
import unittest
P = Path(__file__).resolve().parents[1] / 'scripts' / 'refresh_references.py'
spec = importlib.util.spec_from_file_location('docs_refresh_helper',P)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RefreshSafetyTests(unittest.TestCase):
    def test_allowlist(self):
        module.validate_url('https://learn.microsoft.com/en-us/agent-framework/hosting/')
        for url in ('http://learn.microsoft.com/en-us/agent-framework/hosting/',
                    'https://evil.example/en-us/foo',
                    'https://learn.microsoft.com.evil.example/en-us/foo',
                    'https://learn.microsoft.com/other/foo',
                    'https://fake:secret@learn.microsoft.com/en-us/foo'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                module.validate_url(url)

    def test_html_does_not_include_script(self):
        parser = module.TextFromHTML()
        parser.feed('<main><h1>Hosted agents</h1><p>Use supported service.</p><script>StealToken()</script><p>Check status.</p></main>')
        cleaned=parser.result()
        self.assertIn('Hosted agents',cleaned)
        self.assertIn('Check status',cleaned)
        self.assertNotIn('StealToken',cleaned)
