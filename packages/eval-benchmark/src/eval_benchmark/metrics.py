from __future__ import annotations

from typing import Dict


def summarize(score: float, cost_usd: float, latency_ms: int) -> Dict[str, float]:
    """Simple shared benchmark output shape for practice runs."""
    return {
        "score": score,
        "cost_usd": cost_usd,
        "latency_ms": float(latency_ms),
    }
