# sales-marketing-agent

## Purpose
Domain-focused practice package for the **sales-marketing-agent** workflow.

## Interface
All packages expose the same interface:

```python
from sales_marketing_agent import run

result = run({"task": "example"})
```

## Run
```bash
PYTHONPATH=packages/sales-marketing-agent/src python -c "from sales_marketing_agent import run; print(run({'task':'demo'}))"
```
