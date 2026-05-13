from __future__ import annotations

from typing import Any, Dict, List


def _brief(input_data: Dict[str, Any]) -> Dict[str, Any]:
    value = input_data.get("market_research_brief", input_data)
    if isinstance(value, dict):
        return value
    return {}


def _pains(brief: Dict[str, Any]) -> List[str]:
    value = brief.get("key_pains", [])
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def run(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Turn a market research brief into launch messaging."""
    brief = _brief(input_data)
    pains = _pains(brief)
    primary_pain = pains[0] if pains else "repetitive ecommerce operations"

    return {
        "package": __name__.split(".")[0],
        "status": "ok",
        "artifact_type": "launch_messaging",
        "artifact_name": "launch_messaging.json",
        "source_artifact": brief.get("artifact_name", "market_research_brief.json"),
        "audience": brief.get("target_customer", "Small online store owners"),
        "positioning": "A lightweight AI operations assistant for small ecommerce sellers.",
        "headline": "Stop losing hours to repetitive ecommerce operations.",
        "subheadline": (
            "Summarize reviews, draft support replies, and spot operational follow-ups "
            "before they pile up."
        ),
        "pain_points_to_echo": pains[:4],
        "cold_email_subjects": [
            "Quick question about your store operations",
            "Do reviews and support messages eat your day?",
            f"Could AI help with {primary_pain}?",
        ],
        "cold_email_draft": (
            "Hi, we are exploring an AI assistant for small ecommerce teams that turns "
            "reviews and customer messages into summaries, reply drafts, and safe next steps. "
            "Would you be open to a short interview about where operations work gets repetitive?"
        ),
        "cta": "Join the beta interview list",
        "promise_guardrails": [
            "Do not claim automatic refunds or inventory actions.",
            "Keep the beta framed as draft-and-review assistance.",
        ],
    }
