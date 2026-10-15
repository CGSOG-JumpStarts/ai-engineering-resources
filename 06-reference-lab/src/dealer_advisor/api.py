"""Local loopback HTTP wrapper with strict JSON input and static file allowlist."""
from __future__ import annotations
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from uuid import uuid4
from .advisor import AdviceService, DemoPrincipal, InputError

LAB_ROOT = Path(__file__).resolve().parents[2]
STATIC = {
    "/": (LAB_ROOT / "web" / "index.html", "text/html; charset=utf-8"),
    "/app.js": (LAB_ROOT / "web" / "app.js", "text/javascript; charset=utf-8"),
    "/styles.css": (LAB_ROOT / "web" / "styles.css", "text/css; charset=utf-8"),
}
MAX_BODY_BYTES = 4096


def make_handler(service: AdviceService | None = None):
    service = service or AdviceService()
    # Lab-only trusted principal injected by host. No role or dealer ID is taken from requests.
    demo_principal = DemoPrincipal("SYN-DEALER-100", frozenset({"advice:read"}))

    class Handler(BaseHTTPRequestHandler):
        server_version = "DealerLab/1.0"
        sys_version = ""

        def log_message(self, format, *args):  # noqa: A002
            # Intentionally do not log request bodies, questions, or any source text.
            return

        def _headers(self, status: int, mimetype: str, length: int):
            self.send_response(status)
            self.send_header("Content-Type", mimetype)
            self.send_header("Content-Length", str(length))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; form-action 'self'; base-uri 'none'")
            self.end_headers()

        def _send(self, status: int, payload: dict):
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self._headers(status, "application/json; charset=utf-8", len(data))
            self.wfile.write(data)

        def do_GET(self):  # noqa: N802
            # Only static paths and a health endpoint can be read.
            if self.path == "/health":
                self._send(200, {"status": "healthy", "mode": "offline-synthetic", "request_id": uuid4().hex})
                return
            if self.path not in STATIC:
                self._send(404, {"error": "not_found", "request_id": uuid4().hex})
                return
            path, mime = STATIC[self.path]
            data = path.read_bytes()
            self._headers(200, mime, len(data))
            self.wfile.write(data)

        def do_POST(self):  # noqa: N802
            if self.path != "/v1/advice":
                self._send(404, {"error": "not_found", "request_id": uuid4().hex})
                return
            mime = self.headers.get("Content-Type", "").split(";", 1)[0].lower().strip()
            if mime != "application/json":
                self._send(415, {"error": "unsupported_media_type", "request_id": uuid4().hex})
                return
            try:
                length = int(self.headers.get("Content-Length", "-1"))
            except ValueError:
                length = -1
            if length < 0 or length > MAX_BODY_BYTES:
                self._send(413 if length > MAX_BODY_BYTES else 400, {"error": "invalid_body_length", "request_id": uuid4().hex})
                return
            try:
                request = json.loads(self.rfile.read(length).decode("utf-8"))
            except (UnicodeError, json.JSONDecodeError):
                self._send(400, {"error": "invalid_json", "request_id": uuid4().hex})
                return
            if not isinstance(request, dict) or set(request) != {"question"}:
                self._send(400, {"error": "invalid_fields", "request_id": uuid4().hex})
                return
            try:
                answer = service.answer(request["question"], demo_principal)
            except InputError as ex:
                self._send(400, {"error": ex.code, "request_id": uuid4().hex})
                return
            self._send(200, answer.as_dict())

    return Handler


def create_server(host: str = "127.0.0.1", port: int = 8765) -> ThreadingHTTPServer:
    if host != "127.0.0.1":
        raise ValueError("Lab server is restricted to 127.0.0.1")
    httpd = ThreadingHTTPServer((host, port), make_handler())
    httpd.daemon_threads = True
    return httpd
