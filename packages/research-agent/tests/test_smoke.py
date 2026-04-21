from research_agent import run


def test_smoke() -> None:
    result = run({"task": "smoke"})
    assert result["status"] == "ok"
