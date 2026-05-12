from ecommerce_agent import run


def test_smoke() -> None:
    result = run(
        {
            "market_research_brief": {"artifact_name": "market_research_brief.json"},
            "launch_messaging": {"artifact_name": "launch_messaging.json"},
            "feature_options": [
                "review analysis",
                "support reply drafting",
                "inventory warnings",
                "product copy generation",
            ],
        }
    )

    assert result["status"] == "ok"
    assert result["artifact_type"] == "mvp_scope"
    assert result["artifact_name"] == "mvp_scope.json"
    assert result["recommended_mvp"] == "review_and_support_signal_summary"
    assert "market_research_brief.json" in result["source_artifacts"]
