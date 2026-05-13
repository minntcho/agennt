from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

for package_src in sorted((ROOT / "packages").glob("*/src")):
    sys.path.insert(0, str(package_src))
