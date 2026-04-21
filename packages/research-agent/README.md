# research-agent

## Purpose
Domain-focused practice package for the **research-agent** workflow.

## Interface
All packages expose the same interface:

```python
from research_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/research-agent/src python -c "from research_agent import run; print(run({'task':'demo'}))"
```
