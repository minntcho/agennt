from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_SRCS = [
    ROOT / "packages" / "research-agent" / "src",
    ROOT / "packages" / "sales-marketing-agent" / "src",
    ROOT / "packages" / "ecommerce-agent" / "src",
]

for package_src in PACKAGE_SRCS:
    sys.path.insert(0, str(package_src))

from ecommerce_agent import run as ecommerce_run
from research_agent import run as research_run
from sales_marketing_agent import run as marketing_run


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_demo(founder_thesis_path: Path, output_dir: Path) -> Dict[str, Path]:
    founder_thesis = founder_thesis_path.read_text(encoding="utf-8")

    market_research_brief = research_run(
        {
            "source_artifact": founder_thesis_path.name,
            "founder_thesis": founder_thesis,
        }
    )
    launch_messaging = marketing_run({"market_research_brief": market_research_brief})
    mvp_scope = ecommerce_run(
        {
            "market_research_brief": market_research_brief,
            "launch_messaging": launch_messaging,
        }
    )

    outputs = {
        "market_research_brief": output_dir / "market_research_brief.json",
        "launch_messaging": output_dir / "launch_messaging.json",
        "mvp_scope": output_dir / "mvp_scope.json",
    }
    _write_json(outputs["market_research_brief"], market_research_brief)
    _write_json(outputs["launch_messaging"], launch_messaging)
    _write_json(outputs["mvp_scope"], mvp_scope)
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the first startup artifact chain.")
    parser.add_argument(
        "--founder-thesis",
        type=Path,
        default=ROOT / "examples" / "startup-from-zero" / "founder_thesis.md",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "workspace" / "artifacts" / "startup-demo",
    )
    args = parser.parse_args()

    outputs = run_demo(args.founder_thesis, args.output_dir)
    for name, path in outputs.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
