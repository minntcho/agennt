from eval_benchmark import summarize


def test_summarize() -> None:
    result = summarize(score=0.9, cost_usd=0.01, latency_ms=400)
    assert result["score"] == 0.9
