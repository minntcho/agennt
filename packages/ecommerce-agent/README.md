# ecommerce-agent

## Purpose
Domain-focused practice package for the **ecommerce-agent** workflow.

## Interface
All packages expose the same interface:

```python
from ecommerce_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/ecommerce-agent/src python -c "from ecommerce_agent import run; print(run({'task':'demo'}))"
```
