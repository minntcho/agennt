from apps.support_desk_demo.backend.repository import SupportDeskStore
from apps.support_desk_demo.backend.server import make_response


def test_list_inquiries_endpoint_returns_summaries() -> None:
    store = make_store()

    status, payload = make_response("GET", "/inquiries", store=store)

    assert status == 200
    assert len(payload["inquiries"]) == 1
    assert "message" not in payload["inquiries"][0]
    assert payload["inquiries"][0]["pending_agent_proposals"] == 0


def test_create_inquiry_endpoint() -> None:
    store = make_store()

    status, payload = make_response(
        "POST",
        "/inquiries",
        {
            "customer_name": "New Customer",
            "channel": "email",
            "subject": "배송 문의",
            "message": "배송이 언제 시작되나요?",
        },
        store=store,
    )

    assert status == 201
    assert payload["inquiry"]["id"].startswith("inq-")
    assert payload["inquiry"]["status"] == "new"


def test_update_inquiry_status_endpoint() -> None:
    store = make_store()

    status, payload = make_response(
        "PATCH",
        "/inquiries/inq-test/status",
        {"status": "triage"},
        store=store,
    )

    assert status == 200
    assert payload["inquiry"]["status"] == "triage"


def test_agent_proposal_lifecycle_for_inquiry() -> None:
    store = make_store()

    created_status, created_payload = make_response(
        "POST",
        "/inquiries/inq-test/agent-proposals",
        {
            "source_agent": "cs-agent",
            "proposal_type": "support_intake",
            "title": "응대 전 확인 항목",
            "summary": "환불 정책을 먼저 확인해야 합니다.",
            "payload": {
                "needed_context": ["주문 번호", "스토어 환불 정책"],
                "do_not_auto_handle": ["환불 승인"],
            },
        },
        store=store,
    )

    assert created_status == 201
    proposal = created_payload["agent_proposal"]
    assert proposal["target_type"] == "inquiry"
    assert proposal["target_id"] == "inq-test"
    assert proposal["status"] == "pending"

    decided_status, decided_payload = make_response(
        "PATCH",
        f"/agent-proposals/{proposal['id']}/decision",
        {"decision": "accept", "decided_by": "operator"},
        store=store,
    )

    assert decided_status == 200
    assert decided_payload["agent_proposal"]["status"] == "accepted"


def test_rejects_agent_proposal_type_outside_agent_contract() -> None:
    store = make_store()

    status, payload = make_response(
        "POST",
        "/inquiries/inq-test/agent-proposals",
        {
            "source_agent": "cs-agent",
            "proposal_type": "security_review",
            "title": "잘못된 제안",
            "summary": "cs-agent가 보안 검토를 제출하면 안 됩니다.",
            "payload": {"risk": "unknown"},
        },
        store=store,
    )

    assert status == 400
    assert payload["error"] == "bad_request"


def test_adds_operator_note_and_draft_reply() -> None:
    store = make_store()

    note_status, note_payload = make_response(
        "POST",
        "/inquiries/inq-test/notes",
        {"author": "operator", "body": "환불 정책 확인 필요"},
        store=store,
    )
    reply_status, reply_payload = make_response(
        "POST",
        "/inquiries/inq-test/draft-replies",
        {"author": "operator", "body": "확인 후 안내드리겠습니다."},
        store=store,
    )

    assert note_status == 201
    assert note_payload["internal_note"]["inquiry_id"] == "inq-test"
    assert reply_status == 201
    assert reply_payload["draft_reply"]["inquiry_id"] == "inq-test"


def test_agent_proposal_contract_endpoint() -> None:
    status, payload = make_response("GET", "/agent-proposal-contracts", store=make_store())

    assert status == 200
    assert "cs-agent" in payload["proposal_types_by_agent"]
    assert "support_intake" in payload["proposal_types_by_agent"]["cs-agent"]
    assert "security_review" in payload["proposal_types_by_agent"]["security-assist-agent"]


def make_store() -> SupportDeskStore:
    return SupportDeskStore(
        inquiries=[
            {
                "id": "inq-test",
                "customer_name": "Test Customer",
                "channel": "email",
                "subject": "환불 문의",
                "message": "환불 가능한가요?",
                "order_id": "ORD-TEST",
                "product_name": "linen shirt",
                "status": "new",
                "received_at": "2026-05-13T12:00:00+09:00",
                "tags": ["refund"],
                "customer_sentiment": "frustrated",
            }
        ],
        agent_proposals=[],
    )
