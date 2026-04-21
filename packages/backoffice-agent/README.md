# backoffice-agent

## Purpose
Domain-focused practice package for the **backoffice-agent** workflow.

## Interface
All packages expose the same interface:

```python
from backoffice_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/backoffice-agent/src python -c "from backoffice_agent import run; print(run({'task':'demo'}))"
```
