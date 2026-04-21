# security-assist-agent

## Purpose
Domain-focused practice package for the **security-assist-agent** workflow.

## Interface
All packages expose the same interface:

```python
from security_assist_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/security-assist-agent/src python -c "from security_assist_agent import run; print(run({'task':'demo'}))"
```
