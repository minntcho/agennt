# sales-marketing-agent

## 목적

`sales-marketing-agent` workflow를 연습하기 위한 도메인 중심 패키지입니다.

## 인터페이스

모든 패키지는 같은 인터페이스를 노출합니다.

```python
from sales_marketing_agent import run

result = run({"task": "example"})
```

## 실행

```bash
PYTHONPATH=packages/sales-marketing-agent/src python -c "from sales_marketing_agent import run; print(run({'task':'demo'}))"
```
