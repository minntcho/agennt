from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "packages" / "sales-marketing-agent" / "src"))
sys.path.insert(0, str(ROOT / "packages" / "ecommerce-agent" / "src"))

from ecommerce_agent import run as ecommerce_run
from research_agent import run as research_run
from sales_marketing_agent import run as marketing_run


FOUNDER_THESIS = """
# Founder Thesis

Small ecommerce sellers spend too much time handling repetitive product
operations: reading reviews, answering customer messages, tracking refunds,
writing product copy, and reacting to operational issues.

An AI assistant could help by turning scattered operational signals into
structured summaries, drafts, warnings, and internal tasks.
"""


def test_founder_thesis_flows_through_three_artifacts() -> None:
    market_research_brief = research_run({"founder_thesis": FOUNDER_THESIS})
    launch_messaging = marketing_run({"market_research_brief": market_research_brief})
    mvp_scope = ecommerce_run(
        {
            "market_research_brief": market_research_brief,
            "launch_messaging": launch_messaging,
        }
    )

    assert market_research_brief["artifact_name"] == "market_research_brief.json"
    assert launch_messaging["source_artifact"] == "market_research_brief.json"
    assert mvp_scope["source_artifacts"] == [
        "market_research_brief.json",
        "launch_messaging.json",
    ]
    assert mvp_scope["included_capabilities"]
