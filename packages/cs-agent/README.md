# cs-agent

## Purpose
Domain-focused practice package for the **cs-agent** workflow.

## Interface
All packages expose the same interface:

```python
from cs_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/cs-agent/src python -c "from cs_agent import run; print(run({'task':'demo'}))"
```
