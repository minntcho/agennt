from __future__ import annotations

from typing import Any, Dict, Iterable, List


def _as_text(input_data: Dict[str, Any]) -> str:
    for key in ("founder_thesis", "founder_thesis_md", "thesis", "task"):
        value = input_data.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return "Small ecommerce sellers need help with repetitive operations."


def _contains_any(text: str, needles: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(needle in lowered for needle in needles)


def _unique(items: Iterable[str]) -> List[str]:
    seen = set()
    result: List[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def run(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Turn a founder thesis into the first market research artifact."""
    thesis = _as_text(input_data)
    pains = [
        "customer support overload",
        "manual review analysis",
        "refund and return tracking",
        "product copy workload",
        "operational issue triage",
    ]

    if _contains_any(thesis, ("inventory", "stock")):
        pains.append("unclear inventory decisions")
    if _contains_any(thesis, ("csv", "upload", "import")):
        pains.append("fragile data import workflows")

    return {
        "package": __name__.split(".")[0],
        "status": "ok",
        "artifact_type": "market_research_brief",
        "artifact_name": "market_research_brief.json",
        "source_artifact": input_data.get("source_artifact", "founder_thesis.md"),
        "problem": "Small ecommerce sellers spend too much time on repetitive product operations.",
        "target_customer": "Small online store owners with 1-10 employees",
        "key_pains": _unique(pains),
        "opportunity": (
            "AI can turn scattered review, support, refund, copy, and operations signals "
            "into structured summaries and safe next-step drafts."
        ),
        "evidence": [
            "The founder thesis names repeated review, support, refund, and copy work.",
            "The workflow has inspectable text outputs, so it is safer for an early MVP than automatic actions.",
        ],
        "follow_up_questions": [
            "Which workflow is painful enough for sellers to pay for first?",
            "Which input channel should the first beta support: reviews, support messages, or both?",
            "What human review step is required before any customer-facing draft is sent?",
        ],
    }
