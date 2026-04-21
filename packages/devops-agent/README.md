# devops-agent

## Purpose
Domain-focused practice package for the **devops-agent** workflow.

## Interface
All packages expose the same interface:

```python
from devops_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/devops-agent/src python -c "from devops_agent import run; print(run({'task':'demo'}))"
```
