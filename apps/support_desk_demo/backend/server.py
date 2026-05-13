from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlparse

from .repository import (
    AgentProposalNotFoundError,
    InquiryNotFoundError,
    SupportDeskStore,
)

JsonDict = dict[str, Any]
Response = tuple[int, JsonDict]

STORE = SupportDeskStore.from_seed_files()


def make_response(
    method: str,
    raw_path: str,
    body: JsonDict | None = None,
    store: SupportDeskStore | None = None,
) -> Response:
    active_store = store or STORE
    parsed_url = urlparse(raw_path)
    path = parsed_url.path.rstrip("/") or "/"
    query = parse_qs(parsed_url.query)
    payload = body or {}

    try:
        return route_request(method, path, query, payload, active_store)
    except InquiryNotFoundError as exc:
        return 404, {"error": "inquiry_not_found", "inquiry_id": str(exc)}
    except AgentProposalNotFoundError as exc:
        return 404, {"error": "agent_proposal_not_found", "proposal_id": str(exc)}
    except ValueError as exc:
        return 400, {"error": "bad_request", "message": str(exc)}


def route_request(
    method: str,
    path: str,
    query: dict[str, list[str]],
    payload: JsonDict,
    store: SupportDeskStore,
) -> Response:
    if method == "GET" and path == "/health":
        return 200, {"status": "ok"}

    if method == "GET" and path == "/agent-proposal-contracts":
        return 200, store.proposal_contracts()

    if path == "/inquiries":
        if method == "GET":
            return 200, {"inquiries": store.list_inquiries()}
        if method == "POST":
            return 201, {"inquiry": store.create_inquiry(payload)}

    if path == "/agent-proposals":
        if method == "GET":
            return 200, {
                "agent_proposals": store.list_agent_proposals(
                    status=first_query_value(query, "status")
                )
            }
        if method == "POST":
            return 201, {"agent_proposal": store.add_agent_proposal(payload)}

    parts = path.strip("/").split("/")

    if len(parts) >= 2 and parts[0] == "agent-proposals":
        proposal_id = parts[1]
        if method == "GET" and len(parts) == 2:
            return 200, {"agent_proposal": store.get_agent_proposal(proposal_id)}
        if method == "PATCH" and parts == ["agent-proposals", proposal_id, "decision"]:
            return 200, {
                "agent_proposal": store.decide_agent_proposal(proposal_id, payload)
            }

    if len(parts) >= 2 and parts[0] == "inquiries":
        inquiry_id = parts[1]

        if method == "GET" and len(parts) == 2:
            return 200, {"inquiry": store.get_inquiry(inquiry_id)}

        if method == "PATCH" and parts == ["inquiries", inquiry_id, "status"]:
            return 200, {
                "inquiry": store.update_inquiry_status(
                    inquiry_id,
                    str(payload.get("status", "")),
                )
            }

        if method == "POST" and parts == ["inquiries", inquiry_id, "notes"]:
            return 201, {"internal_note": store.add_internal_note(inquiry_id, payload)}

        if method == "POST" and parts == ["inquiries", inquiry_id, "draft-replies"]:
            return 201, {"draft_reply": store.add_draft_reply(inquiry_id, payload)}

        if parts == ["inquiries", inquiry_id, "agent-proposals"]:
            if method == "GET":
                return 200, {
                    "agent_proposals": store.list_agent_proposals(
                        target_type="inquiry",
                        target_id=inquiry_id,
                        status=first_query_value(query, "status"),
                    )
                }
            if method == "POST":
                proposal = {
                    **payload,
                    "target_type": "inquiry",
                    "target_id": inquiry_id,
                }
                return 201, {"agent_proposal": store.add_agent_proposal(proposal)}

    return 404, {"error": "not_found"}


class SupportDeskRequestHandler(BaseHTTPRequestHandler):
    server_version = "SupportDeskDemo/0.2"

    def do_GET(self) -> None:
        self.respond(*make_response("GET", self.path))

    def do_POST(self) -> None:
        try:
            body = self.read_json_body()
        except ValueError as exc:
            self.respond(400, {"error": "bad_request", "message": str(exc)})
            return
        self.respond(*make_response("POST", self.path, body))

    def do_PATCH(self) -> None:
        try:
            body = self.read_json_body()
        except ValueError as exc:
            self.respond(400, {"error": "bad_request", "message": str(exc)})
            return
        self.respond(*make_response("PATCH", self.path, body))

    def read_json_body(self) -> JsonDict:
        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length == 0:
            return {}

        raw_body = self.rfile.read(content_length).decode("utf-8")
        try:
            decoded = json.loads(raw_body)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid json body: {exc.msg}") from exc
        if not isinstance(decoded, dict):
            raise ValueError("json body must be an object")
        return decoded

    def respond(self, status: int, payload: JsonDict) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None:
        return


def first_query_value(query: dict[str, list[str]], key: str) -> str | None:
    values = query.get(key)
    if not values:
        return None
    return values[0]


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    server = ThreadingHTTPServer((host, port), SupportDeskRequestHandler)
    print(f"support desk backend listening on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run(port=int(os.environ.get("PORT", "8000")))
