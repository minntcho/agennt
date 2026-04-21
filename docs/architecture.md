# Architecture

## Goal
Use this repository as a training ground for domain-oriented agent patterns.

## Domain packages
- `cs-agent`
- `devops-agent`
- `research-agent`
- `sales-marketing-agent`
- `backoffice-agent`
- `ecommerce-agent`
- `security-assist-agent`
- `eval-benchmark`

## Conventions
1. Each package is independently runnable.
2. The agent interface is standardized as `run(input_data: dict) -> dict`.
3. Every package ships a smoke test.
4. `eval-benchmark` provides a simple metrics schema to compare experiments.
