from research_agent import run


FOUNDER_THESIS = """
# Founder Thesis

Small ecommerce sellers spend too much time reading reviews, answering customer
messages, tracking refunds, and writing product copy.
"""


def test_smoke() -> None:
    result = run({"founder_thesis": FOUNDER_THESIS})

    assert result["status"] == "ok"
    assert result["artifact_type"] == "market_research_brief"
    assert result["artifact_name"] == "market_research_brief.json"
    assert "customer support overload" in result["key_pains"]
    assert result["follow_up_questions"]
