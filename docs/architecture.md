# Architecture

## Goal

Use this repository as a training ground for domain-oriented agent patterns.

The repository is not meant to collapse every package into one shared runtime. Each package should remain a focused practice unit. The larger direction is to model a small connected operating ecosystem where independent agents produce artifacts that later agents can read.

In short:

```text
independent agent packages + shared artifact flow = agent ecosystem practice
```

## Domain packages

- `research-agent`: turns broad topics into structured research briefs.
- `sales-marketing-agent`: turns research, product, or customer context into campaign copy and sales drafts.
- `ecommerce-agent`: analyzes product, review, order, and inventory signals.
- `cs-agent`: classifies customer messages and drafts support responses.
- `backoffice-agent`: converts operational requests into structured internal work items.
- `devops-agent`: triages logs, incidents, and deployment issues.
- `security-assist-agent`: reviews defensive security events and suggests safe checks.
- `eval-benchmark`: compares experiment outputs using simple metrics.

## Ecosystem model

Agents should be connected through explicit artifacts rather than direct package-to-package calls.

Preferred flow:

```text
agent A runs
-> writes an artifact
-> agent B receives that artifact as input
-> agent B writes a new artifact
```

Examples:

- `research-agent` creates a market brief; `sales-marketing-agent` uses it to draft campaign copy.
- `ecommerce-agent` extracts common product complaints; `cs-agent` uses them to improve support classification.
- `cs-agent` identifies a refund case; `backoffice-agent` turns it into an internal review ticket.
- `devops-agent` summarizes a checkout incident; `cs-agent` creates a customer-facing notice.
- `security-assist-agent` finds account-risk signals; `backoffice-agent` turns them into an internal checklist.
- All package outputs can later feed `eval-benchmark`.

## Conventions

1. Each package is independently runnable.
2. The agent interface is standardized as `run(input_data: dict) -> dict`.
3. Every package ships a smoke test.
4. Package outputs should be shaped as explicit artifacts when they are meant to be reused.
5. Packages should not directly import and call each other as their primary coordination mechanism.
6. `eval-benchmark` provides a simple metrics schema to compare experiments.

## Learning direction

Start with one concrete scenario and let the packages affect each other through saved outputs.

A useful first scenario is:

```text
research brief
-> campaign copy
-> ecommerce signals
-> customer support cases
-> backoffice tasks
-> incident/security triage
-> benchmark report
```

This keeps the repository fun to practice with while preserving package independence.
