# Ecosystem Architecture

## Purpose

`agennt` is a practice repository for learning agent design through a connected but lightweight operating simulation.

The repository should stay useful for independent experiments. Each package can be run and tested by itself. At the same time, the packages become more interesting when their outputs become inputs for other packages.

The design target is:

```text
small company / service operations simulated through independent agents
```

## Core rule

Agents communicate through artifacts.

```text
agent -> artifact -> next agent
```

Do not make package-to-package imports the main coordination mechanism. A package should not need to know another package's internal implementation to reuse its result.

## Why artifacts

Artifacts keep the exercises modular while still making them feel connected.

They make it possible to practice:

- task decomposition
- structured outputs
- evidence and source tracking
- workflow chaining
- evaluation across packages
- scenario-based learning

## Package roles

### `research-agent`

Produces research briefs from broad topics.

Example artifact:

```text
market_brief.json
```

Downstream users:

- `sales-marketing-agent` can use findings and customer pains.
- `ecommerce-agent` can use market or competitor context.
- `eval-benchmark` can score brief quality.

### `sales-marketing-agent`

Produces sales emails, campaign copy, landing page drafts, or positioning notes.

Example artifact:

```text
campaign_copy.json
```

Downstream users:

- `ecommerce-agent` can use product copy.
- `cs-agent` can align support messaging with current positioning.
- `eval-benchmark` can compare variants.

### `ecommerce-agent`

Analyzes product, review, sales, inventory, and order signals.

Example artifact:

```text
product_ops_summary.json
```

Downstream users:

- `cs-agent` can use common complaints.
- `backoffice-agent` can use restock or refund signals.
- `sales-marketing-agent` can use review-derived strengths.

### `cs-agent`

Classifies support messages and drafts customer responses.

Example artifact:

```text
support_case_summary.json
```

Downstream users:

- `backoffice-agent` can create internal tickets.
- `ecommerce-agent` can learn recurring product issues.
- `eval-benchmark` can score classification and reply quality.

### `backoffice-agent`

Turns operational requests into structured internal work items.

Example artifact:

```text
internal_task_ticket.json
```

Downstream users:

- `eval-benchmark` can score completeness.
- Future workflow tools can inspect missing fields and approvals.

### `devops-agent`

Triage logs, incidents, deployment issues, and safe next checks.

Example artifact:

```text
incident_triage.json
```

Downstream users:

- `cs-agent` can draft customer notices.
- `backoffice-agent` can open follow-up tasks.
- `eval-benchmark` can compare diagnosis quality.

### `security-assist-agent`

Reviews defensive security events and suggests safe checks.

Example artifact:

```text
security_triage.json
```

Downstream users:

- `backoffice-agent` can create internal review checklists.
- `devops-agent` can correlate operational and security signals.
- `eval-benchmark` can score risk classification.

### `eval-benchmark`

Collects and compares experiment results.

Example artifact:

```text
benchmark_report.json
```

Downstream users:

- Humans reviewing what changed across versions.
- Future automation that compares score, latency, cost, and failure modes.

## Suggested workspace shape

A later iteration can add a local workspace for scenario inputs and generated outputs.

```text
workspace/
├─ scenarios/
│  └─ ecommerce_saas_launch.json
├─ inputs/
├─ artifacts/
│  ├─ research/
│  ├─ sales_marketing/
│  ├─ ecommerce/
│  ├─ cs/
│  ├─ backoffice/
│  ├─ devops/
│  ├─ security/
│  └─ eval/
└─ events/
```

This workspace is not required for the earliest package exercises, but it gives the repository a clear growth path.

## First connected scenario

A good first scenario is an ecommerce SaaS launch.

```text
1. `research-agent` writes a market brief.
2. `sales-marketing-agent` turns the brief into campaign copy.
3. `ecommerce-agent` analyzes product/review/sales signals.
4. `cs-agent` handles customer questions or complaints.
5. `backoffice-agent` turns support cases into internal tasks.
6. `devops-agent` triages a checkout or API incident.
7. `security-assist-agent` reviews suspicious login events.
8. `eval-benchmark` compares outputs across packages.
```

The point is not to build a large production orchestrator first. The point is to make each package more fun to practice by placing it in a shared world.

## Non-goals for now

- No central monolithic runtime.
- No mandatory multi-agent orchestration.
- No package-to-package internal coupling.
- No real production system side effects.
- No automatic external actions without explicit later design.
