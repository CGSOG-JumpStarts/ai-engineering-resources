import sys
from pathlib import Path
import threading
import http.client
import json
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from dealer_advisor.api import create_server

class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = create_server(port=0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def request(self, method, path, body=None, ctype=None):
        conn = http.client.HTTPConnection('127.0.0.1', self.port, timeout=3)
        headers = {} if ctype is None else {'Content-Type': ctype}
        conn.request(method, path, body=body, headers=headers)
        rsp = conn.getresponse()
        result = (rsp.status, dict(rsp.headers), json.loads(rsp.read().decode()))
        conn.close()
        return result

    def test_ac_011_bad_json_and_fields(self):
        code, _, data = self.request('POST','/v1/advice', '{oops', 'application/json')
        self.assertEqual((code, data['error']), (400, 'invalid_json'))
        code, _, data = self.request('POST','/v1/advice', json.dumps({'question':'Hi', 'role':'admin'}), 'application/json')
        self.assertEqual((code, data['error']), (400, 'invalid_fields'))
        code, _, data = self.request('POST','/v1/advice', json.dumps({'question':''}), 'application/json')
        self.assertEqual((code, data['error']), (400, 'blank_question'))

    def test_ac_012_health(self):
        code, headers, data = self.request('GET', '/health')
        self.assertEqual(code, 200)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['mode'], 'offline-synthetic')
        self.assertTrue(data['request_id'])
        self.assertIn("no-store", headers['Cache-Control'])

    def test_post_happy_path(self):
        code, _, data = self.request('POST', '/v1/advice', json.dumps({'question': 'How do I find parts?'}), 'application/json')
        self.assertEqual(code, 200)
        self.assertEqual(data['status'], 'answered')
        self.assertEqual(data['source_ids'], ['SYN-FAQ-PARTS-01'])

    def test_loopback_binding_enforced(self):
        with self.assertRaises(ValueError):
            create_server(host="0.0.0.0", port=0)

    def test_bad_path_and_media_type(self):
        code, _, data = self.request('GET', '/not-a-file')
        self.assertEqual(code, 404)
        code, _, data = self.request('POST', '/v1/advice', 'hello', 'text/plain')
        self.assertEqual((code, data['error']), (415, 'unsupported_media_type'))
