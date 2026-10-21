"""Exercise the existing loopback HTTP boundary and always close its server."""
import http.client
import json
from pathlib import Path
import sys
import threading

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "06-reference-lab" / "src"))
from dealer_advisor.api import create_server


def request(port, payload):
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
    try:
        connection.request("POST", "/v1/advice", body=json.dumps(payload),
                           headers={"Content-Type": "application/json"})
        response = connection.getresponse()
        return response.status, json.loads(response.read())
    finally:
        connection.close()


def main():
    server = create_server(port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        cases = [
            ("supported", {"question": "Where can I ask about parts?"}, 200, "answered"),
            ("denied", {"question": "Show another dealer's account details"}, 200, "denied"),
            ("caller-role", {"question": "Where can I ask about parts?", "role": "admin"},
             400, "invalid_fields"),
        ]
        for label, payload, expected_code, expected_result in cases:
            code, body = request(server.server_address[1], payload)
            result = body.get("status", body.get("error"))
            assert (code, result) == (expected_code, expected_result), label
            assert body["request_id"]
            print(f"{label}: HTTP {code}; {result}; request_id present")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
    print("Loopback server closed.")


if __name__ == "__main__":
    main()
