from apps.support_desk_demo.backend.intake import build_support_intake_brief, classify_inquiry
from apps.support_desk_demo.backend.server import make_response


def test_classifies_refund_request() -> None:
    inquiry = {
        "id": "inq-test",
        "subject": "환불 가능한가요?",
        "message": "사이즈가 맞지 않아 반품하고 싶습니다.",
        "product_name": "linen shirt",
        "tags": ["refund"],
    }

    assert classify_inquiry(inquiry) == "refund_request"


def test_builds_intake_brief_without_auto_handling() -> None:
    inquiry = {
        "id": "inq-test",
        "subject": "환불 가능한가요?",
        "message": "택은 제거했지만 환불 가능한지 궁금합니다.",
        "product_name": "linen shirt",
        "tags": ["refund"],
        "customer_sentiment": "frustrated",
    }

    brief = build_support_intake_brief(inquiry)

    assert brief["inquiry_type"] == "refund_request"
    assert brief["human_review_required"] is True
    assert "스토어 환불 정책" in brief["needed_context"]
    assert "환불 승인" in brief["do_not_auto_handle"]
    assert "환불 정책 확인 필요" in brief["risk_flags"]


def test_list_inquiries_endpoint() -> None:
    status, payload = make_response("GET", "/inquiries")

    assert status == 200
    assert len(payload["inquiries"]) >= 1
    assert "message" not in payload["inquiries"][0]


def test_intake_endpoint_returns_support_intake_brief() -> None:
    status, payload = make_response("POST", "/inquiries/inq-1001/intake")

    assert status == 200
    brief = payload["support_intake_brief"]
    assert brief["inquiry_id"] == "inq-1001"
    assert brief["inquiry_type"] == "refund_request"
    assert brief["source"] == "deterministic-support-intake-v0"


def test_unknown_inquiry_returns_404() -> None:
    status, payload = make_response("GET", "/inquiries/missing")

    assert status == 404
    assert payload == {"error": "inquiry_not_found", "inquiry_id": "missing"}
