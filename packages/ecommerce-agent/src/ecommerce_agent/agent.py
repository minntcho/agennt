from __future__ import annotations

from typing import Any, Dict, List


DEFAULT_FEATURES = [
    "review analysis",
    "support reply drafting",
    "inventory warnings",
    "product copy generation",
]


def _dict_input(input_data: Dict[str, Any], key: str) -> Dict[str, Any]:
    value = input_data.get(key, {})
    return value if isinstance(value, dict) else {}


def _features(input_data: Dict[str, Any]) -> List[str]:
    value = input_data.get("feature_options", DEFAULT_FEATURES)
    if isinstance(value, list):
        return [str(item) for item in value]
    return DEFAULT_FEATURES


def run(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Use upstream artifacts to recommend the first ecommerce MVP scope."""
    brief = _dict_input(input_data, "market_research_brief")
    messaging = _dict_input(input_data, "launch_messaging")
    features = _features(input_data)

    recommended = "review_and_support_signal_summary"
    excluded = [feature for feature in features if feature not in {"review analysis", "support reply drafting"}]

    return {
        "package": __name__.split(".")[0],
        "status": "ok",
        "artifact_type": "mvp_scope",
        "artifact_name": "mvp_scope.json",
        "source_artifacts": [
            brief.get("artifact_name", "market_research_brief.json"),
            messaging.get("artifact_name", "launch_messaging.json"),
        ],
        "recommended_mvp": recommended,
        "included_capabilities": [
            "summarize recurring review themes",
            "classify support message intent",
            "draft customer-safe reply suggestions",
            "flag cases that need founder review",
        ],
        "why": [
            "Reviews and support messages are common repetitive inputs in the research brief.",
            "The outputs are drafts and summaries, so users can inspect them before acting.",
            "The launch messaging can promise assistance without implying risky automation.",
        ],
        "excluded_for_now": excluded
        or ["automatic refund approval", "automatic inventory ordering", "direct ad campaign execution"],
        "success_signals": [
            "seller saves time triaging reviews and messages",
            "draft replies require fewer edits over time",
            "founder can identify which workflow deserves deeper automation next",
        ],
    }
