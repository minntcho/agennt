from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .models import (
    JsonDict,
    PROPOSAL_TYPES_BY_AGENT,
    validate_agent_proposal,
    validate_inquiry_status,
    validate_proposal_status,
)

DATA_DIR = Path(__file__).with_name("data")
INQUIRIES_PATH = DATA_DIR / "inquiries.json"
AGENT_PROPOSALS_PATH = DATA_DIR / "agent_proposals.json"


class InquiryNotFoundError(LookupError):
    """Raised when an inquiry id is not in the demo store."""


class AgentProposalNotFoundError(LookupError):
    """Raised when an agent proposal id is not in the demo store."""


class SupportDeskStore:
    def __init__(
        self,
        inquiries: list[JsonDict],
        agent_proposals: list[JsonDict] | None = None,
        internal_notes: list[JsonDict] | None = None,
        draft_replies: list[JsonDict] | None = None,
    ) -> None:
        self.inquiries = {str(inquiry["id"]): dict(inquiry) for inquiry in inquiries}
        self.agent_proposals = {
            str(proposal["id"]): dict(proposal)
            for proposal in (agent_proposals or [])
        }
        self.internal_notes = list(internal_notes or [])
        self.draft_replies = list(draft_replies or [])
        self._next_note_number = len(self.internal_notes) + 1
        self._next_reply_number = len(self.draft_replies) + 1
        self._next_inquiry_number = len(self.inquiries) + 1
        self._next_proposal_number = len(self.agent_proposals) + 1

    @classmethod
    def from_seed_files(cls) -> "SupportDeskStore":
        return cls(
            inquiries=load_json_list(INQUIRIES_PATH),
            agent_proposals=load_json_list(AGENT_PROPOSALS_PATH),
        )

    def list_inquiries(self) -> list[JsonDict]:
        return [self.to_inquiry_summary(inquiry) for inquiry in self.inquiries.values()]

    def create_inquiry(self, data: JsonDict) -> JsonDict:
        required_fields = ["customer_name", "channel", "subject", "message"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            raise ValueError(f"missing inquiry fields: {', '.join(missing_fields)}")

        inquiry_id = data.get("id") or self.next_id("inq", self._next_inquiry_number)
        self._next_inquiry_number += 1
        inquiry = {
            "id": str(inquiry_id),
            "customer_name": data["customer_name"],
            "channel": data["channel"],
            "subject": data["subject"],
            "message": data["message"],
            "order_id": data.get("order_id"),
            "product_name": data.get("product_name"),
            "status": data.get("status", "new"),
            "received_at": data.get("received_at", now_iso()),
            "tags": data.get("tags", []),
            "customer_sentiment": data.get("customer_sentiment", "unknown"),
        }
        validate_inquiry_status(str(inquiry["status"]))
        self.inquiries[str(inquiry_id)] = inquiry
        return inquiry

    def get_inquiry(self, inquiry_id: str) -> JsonDict:
        try:
            inquiry = self.inquiries[inquiry_id]
        except KeyError as exc:
            raise InquiryNotFoundError(inquiry_id) from exc

        return {
            **inquiry,
            "internal_notes": self.list_internal_notes(inquiry_id),
            "draft_replies": self.list_draft_replies(inquiry_id),
            "agent_proposals": self.list_agent_proposals(
                target_type="inquiry",
                target_id=inquiry_id,
            ),
        }

    def update_inquiry_status(self, inquiry_id: str, status: str) -> JsonDict:
        validate_inquiry_status(status)
        inquiry = self.require_inquiry(inquiry_id)
        inquiry["status"] = status
        inquiry["updated_at"] = now_iso()
        return inquiry

    def add_internal_note(self, inquiry_id: str, data: JsonDict) -> JsonDict:
        self.require_inquiry(inquiry_id)
        if not data.get("body"):
            raise ValueError("missing note body")

        note = {
            "id": self.next_id("note", self._next_note_number),
            "inquiry_id": inquiry_id,
            "author": data.get("author", "operator"),
            "body": data["body"],
            "created_at": now_iso(),
        }
        self._next_note_number += 1
        self.internal_notes.append(note)
        return note

    def add_draft_reply(self, inquiry_id: str, data: JsonDict) -> JsonDict:
        self.require_inquiry(inquiry_id)
        if not data.get("body"):
            raise ValueError("missing reply body")

        draft_reply = {
            "id": self.next_id("reply", self._next_reply_number),
            "inquiry_id": inquiry_id,
            "author": data.get("author", "operator"),
            "body": data["body"],
            "source_proposal_id": data.get("source_proposal_id"),
            "created_at": now_iso(),
        }
        self._next_reply_number += 1
        self.draft_replies.append(draft_reply)
        return draft_reply

    def list_internal_notes(self, inquiry_id: str) -> list[JsonDict]:
        return [
            note for note in self.internal_notes if note.get("inquiry_id") == inquiry_id
        ]

    def list_draft_replies(self, inquiry_id: str) -> list[JsonDict]:
        return [
            reply for reply in self.draft_replies if reply.get("inquiry_id") == inquiry_id
        ]

    def list_agent_proposals(
        self,
        target_type: str | None = None,
        target_id: str | None = None,
        status: str | None = None,
    ) -> list[JsonDict]:
        proposals = list(self.agent_proposals.values())
        if target_type is not None:
            proposals = [
                proposal
                for proposal in proposals
                if proposal.get("target_type") == target_type
            ]
        if target_id is not None:
            proposals = [
                proposal for proposal in proposals if proposal.get("target_id") == target_id
            ]
        if status is not None:
            validate_proposal_status(status)
            proposals = [
                proposal for proposal in proposals if proposal.get("status") == status
            ]
        return proposals

    def add_agent_proposal(self, data: JsonDict) -> JsonDict:
        proposal = {
            "id": data.get("id") or self.next_id("prop", self._next_proposal_number),
            "source_agent": data.get("source_agent"),
            "proposal_type": data.get("proposal_type"),
            "target_type": data.get("target_type"),
            "target_id": data.get("target_id"),
            "title": data.get("title"),
            "summary": data.get("summary"),
            "payload": data.get("payload"),
            "status": data.get("status", "pending"),
            "created_at": data.get("created_at", now_iso()),
        }
        validate_agent_proposal(proposal)
        validate_proposal_status(str(proposal["status"]))
        if proposal["target_type"] == "inquiry":
            self.require_inquiry(str(proposal["target_id"]))

        self._next_proposal_number += 1
        self.agent_proposals[str(proposal["id"])] = proposal
        return proposal

    def get_agent_proposal(self, proposal_id: str) -> JsonDict:
        try:
            return self.agent_proposals[proposal_id]
        except KeyError as exc:
            raise AgentProposalNotFoundError(proposal_id) from exc

    def decide_agent_proposal(self, proposal_id: str, data: JsonDict) -> JsonDict:
        proposal = self.get_agent_proposal(proposal_id)
        decision = str(data.get("decision", ""))
        status_by_decision = {
            "accept": "accepted",
            "reject": "rejected",
            "archive": "archived",
        }
        if decision not in status_by_decision:
            raise ValueError("decision must be one of: accept, reject, archive")

        proposal["status"] = status_by_decision[decision]
        proposal["decided_at"] = now_iso()
        proposal["decided_by"] = data.get("decided_by", "operator")
        proposal["decision_reason"] = data.get("reason")
        return proposal

    def proposal_contracts(self) -> JsonDict:
        return {
            "proposal_statuses": ["pending", "accepted", "rejected", "archived"],
            "proposal_types_by_agent": {
                source_agent: sorted(proposal_types)
                for source_agent, proposal_types in PROPOSAL_TYPES_BY_AGENT.items()
            },
        }

    def require_inquiry(self, inquiry_id: str) -> JsonDict:
        try:
            return self.inquiries[inquiry_id]
        except KeyError as exc:
            raise InquiryNotFoundError(inquiry_id) from exc

    def to_inquiry_summary(self, inquiry: JsonDict) -> JsonDict:
        inquiry_id = str(inquiry["id"])
        return {
            "id": inquiry.get("id"),
            "customer_name": inquiry.get("customer_name"),
            "channel": inquiry.get("channel"),
            "subject": inquiry.get("subject"),
            "status": inquiry.get("status"),
            "received_at": inquiry.get("received_at"),
            "customer_sentiment": inquiry.get("customer_sentiment"),
            "pending_agent_proposals": len(
                self.list_agent_proposals(
                    target_type="inquiry",
                    target_id=inquiry_id,
                    status="pending",
                )
            ),
        }

    def next_id(self, prefix: str, number: int) -> str:
        return f"{prefix}-{number:04d}"


def load_json_list(path: Path) -> list[JsonDict]:
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
