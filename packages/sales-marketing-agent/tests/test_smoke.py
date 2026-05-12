from sales_marketing_agent import run


def test_smoke() -> None:
    result = run(
        {
            "market_research_brief": {
                "artifact_name": "market_research_brief.json",
                "target_customer": "Small online store owners with 1-10 employees",
                "key_pains": ["customer support overload", "manual review analysis"],
            }
        }
    )

    assert result["status"] == "ok"
    assert result["artifact_type"] == "launch_messaging"
    assert result["artifact_name"] == "launch_messaging.json"
    assert result["source_artifact"] == "market_research_brief.json"
    assert result["cold_email_subjects"]
