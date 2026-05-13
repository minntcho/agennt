from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import urlparse

from .intake import build_support_intake_brief
from .repository import InquiryNotFoundError, get_inquiry, list_inquiries

Response = tuple[int, dict[str, Any]]


def make_response(method: str, raw_path: str) -> Response:
    path = urlparse(raw_path).path.rstrip("/") or "/"

    if method == "GET" and path == "/health":
        return 200, {"status": "ok"}

    if method == "GET" and path == "/inquiries":
        return 200, {"inquiries": list_inquiries()}

    parts = path.strip("/").split("/")
    if len(parts) >= 2 and parts[0] == "inquiries":
        inquiry_id = parts[1]
        try:
            inquiry = get_inquiry(inquiry_id)
        except InquiryNotFoundError:
            return 404, {"error": "inquiry_not_found", "inquiry_id": inquiry_id}

        if method == "GET" and len(parts) == 2:
            return 200, {"inquiry": inquiry}

        if method == "POST" and parts == ["inquiries", inquiry_id, "intake"]:
            return 200, {"support_intake_brief": build_support_intake_brief(inquiry)}

    return 404, {"error": "not_found"}


class SupportDeskRequestHandler(BaseHTTPRequestHandler):
    server_version = "SupportDeskDemo/0.1"

    def do_GET(self) -> None:
        self.respond(*make_response("GET", self.path))

    def do_POST(self) -> None:
        self.read_body()
        self.respond(*make_response("POST", self.path))

    def read_body(self) -> bytes:
        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length == 0:
            return b""
        return self.rfile.read(content_length)

    def respond(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None:
        return


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    server = ThreadingHTTPServer((host, port), SupportDeskRequestHandler)
    print(f"support desk backend listening on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run(port=int(os.environ.get("PORT", "8000")))
