from __future__ import annotations

from typing import Any

JsonDict = dict[str, Any]

INQUIRY_STATUSES = {
    "new",
    "triage",
    "needs_info",
    "ready_to_reply",
    "resolved",
    "closed",
}

PROPOSAL_STATUSES = {
    "pending",
    "accepted",
    "rejected",
    "archived",
}

PROPOSAL_TYPES_BY_AGENT = {
    "cs-agent": {
        "support_intake",
        "reply_draft",
        "inquiry_triage",
    },
    "research-agent": {
        "market_research",
        "customer_segment_note",
    },
    "sales-marketing-agent": {
        "launch_messaging",
        "campaign_copy",
    },
    "ecommerce-agent": {
        "mvp_scope",
        "product_signal",
        "returns_policy_note",
    },
    "backoffice-agent": {
        "internal_task",
        "onboarding_checklist",
    },
    "devops-agent": {
        "incident_triage",
        "operational_checklist",
    },
    "security-assist-agent": {
        "security_review",
        "access_risk_note",
    },
    "eval-benchmark": {
        "evaluation_report",
    },
}

PROPOSAL_TYPES = {
    proposal_type
    for proposal_types in PROPOSAL_TYPES_BY_AGENT.values()
    for proposal_type in proposal_types
}

TARGET_TYPES = {
    "inquiry",
    "workspace",
    "scenario",
}


def validate_inquiry_status(status: str) -> None:
    if status not in INQUIRY_STATUSES:
        raise ValueError(f"unknown inquiry status: {status}")


def validate_proposal_status(status: str) -> None:
    if status not in PROPOSAL_STATUSES:
        raise ValueError(f"unknown proposal status: {status}")


def validate_agent_proposal(proposal: JsonDict) -> None:
    required_fields = [
        "source_agent",
        "proposal_type",
        "target_type",
        "target_id",
        "title",
        "summary",
        "payload",
    ]
    missing_fields = [
        field
        for field in required_fields
        if field not in proposal or proposal[field] in (None, "")
    ]
    if missing_fields:
        raise ValueError(f"missing proposal fields: {', '.join(missing_fields)}")

    source_agent = str(proposal["source_agent"])
    proposal_type = str(proposal["proposal_type"])
    target_type = str(proposal["target_type"])

    if source_agent not in PROPOSAL_TYPES_BY_AGENT:
        raise ValueError(f"unknown source agent: {source_agent}")
    if proposal_type not in PROPOSAL_TYPES_BY_AGENT[source_agent]:
        raise ValueError(
            f"{source_agent} cannot submit proposal type: {proposal_type}"
        )
    if target_type not in TARGET_TYPES:
        raise ValueError(f"unknown proposal target type: {target_type}")
    if not isinstance(proposal["payload"], dict):
        raise ValueError("proposal payload must be an object")
