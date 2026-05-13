from __future__ import annotations

import json
from pathlib import Path
from typing import Any

Inquiry = dict[str, Any]

DATA_PATH = Path(__file__).with_name("data") / "inquiries.json"


class InquiryNotFoundError(LookupError):
    """Raised when an inquiry id is not in the demo dataset."""


def load_inquiries(path: Path | None = None) -> list[Inquiry]:
    data_path = path or DATA_PATH
    return json.loads(data_path.read_text(encoding="utf-8"))


def list_inquiries() -> list[Inquiry]:
    return [to_summary(inquiry) for inquiry in load_inquiries()]


def get_inquiry(inquiry_id: str) -> Inquiry:
    for inquiry in load_inquiries():
        if inquiry.get("id") == inquiry_id:
            return inquiry
    raise InquiryNotFoundError(inquiry_id)


def to_summary(inquiry: Inquiry) -> Inquiry:
    return {
        "id": inquiry.get("id"),
        "customer_name": inquiry.get("customer_name"),
        "channel": inquiry.get("channel"),
        "subject": inquiry.get("subject"),
        "status": inquiry.get("status"),
        "received_at": inquiry.get("received_at"),
        "customer_sentiment": inquiry.get("customer_sentiment"),
    }
