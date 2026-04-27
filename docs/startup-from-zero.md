# Startup From Zero: Ecommerce AI Ops

## Concept

This scenario starts from a founder's problem hypothesis, not from a finished agent architecture.

The company does not exist in order to use agents. The company begins because a founder notices a real operational problem, then agents become useful as the company creates research, messaging, product operations, support, internal tasks, incidents, security reviews, and evaluation artifacts.

The scenario is:

```text
founder problem hypothesis
-> market validation
-> launch messaging
-> MVP scope
-> first customer inquiry
-> beta onboarding
-> operational incident
-> security review
-> experiment evaluation
```

## Company premise

A founder wants to build an AI operations assistant for small ecommerce sellers.

The initial thesis:

```text
Small ecommerce sellers spend too much time handling repetitive product operations: reading reviews, answering customer messages, tracking refunds, writing product copy, and reacting to operational issues.

An AI assistant could help by turning scattered operational signals into structured summaries, drafts, warnings, and internal tasks.
```

The company starts with a thesis, not a product.

## First artifact: founder thesis

File idea:

```text
founder_thesis.md
```

Example:

```md
# Founder Thesis

## Problem

Small ecommerce sellers waste too much time handling repetitive product operations.

## Target Customer

Small online store owners with 1-10 employees.

## Hypothesis

If we provide an AI assistant that summarizes reviews, drafts support replies, and suggests operational actions, sellers can save time and reduce support mistakes.

## Initial Product Idea

An AI-powered ecommerce operations assistant.
```

This thesis becomes the root input for the first agent tasks.

---

## Stage 1: Validate the problem

### Client request

```text
We think small ecommerce sellers struggle with repetitive operations.
Research whether this problem is real, what pains are common, and what questions we should investigate next.
```

### Agent

```text
research-agent
```

### Output artifact

```text
market_research_brief.json
```

### Expected output shape

```json
{
  "problem": "Small ecommerce sellers struggle with repetitive operational tasks.",
  "target_customer": "Small online store owners",
  "key_pains": [
    "customer support overload",
    "manual review analysis",
    "refund and return handling",
    "unclear inventory decisions",
    "marketing copy workload"
  ],
  "opportunity": "AI can assist by turning scattered signals into operational recommendations.",
  "follow_up_questions": [
    "Which pain is urgent enough to pay for?",
    "Which workflow should be automated first?"
  ]
}
```

### Learning target

Practice turning a broad founder thesis into a structured research brief.

---

## Stage 2: Create the first market-facing message

### Client request

```text
Use the research brief to create landing page copy and cold email drafts.
The product is not finished yet. The goal is to get interviews and beta signups.
```

### Agent

```text
sales-marketing-agent
```

### Output artifact

```text
launch_messaging.json
```

### Expected output shape

```json
{
  "headline": "Stop drowning in repetitive ecommerce operations.",
  "subheadline": "Use AI to summarize reviews, draft support replies, and spot operational issues before they pile up.",
  "cold_email_subjects": [
    "Quick question about your store operations",
    "Do customer messages and reviews eat your day?"
  ],
  "cta": "Join the beta"
}
```

### Learning target

Practice converting research output into useful messaging without pretending the product is already mature.

---

## Stage 3: Choose the MVP scope

### Client request

```text
We cannot build everything at once.
Given review analysis, support reply drafting, inventory warnings, and product copy generation, recommend the first MVP scope.
```

### Agent

```text
ecommerce-agent
```

### Output artifact

```text
mvp_scope.json
```

### Expected output shape

```json
{
  "recommended_mvp": "review_and_support_signal_summary",
  "why": [
    "reviews and support messages are common repetitive inputs",
    "outputs are easy to inspect",
    "low risk compared to automatic refunds or inventory actions"
  ],
  "excluded_for_now": [
    "automatic refund approval",
    "automatic inventory ordering",
    "direct ad campaign execution"
  ]
}
```

### Learning target

Practice scope control: the first product should solve one painful workflow before pretending to be a full operating system.

---

## Stage 4: Handle the first customer inquiry

### Client request

```text
A store owner saw the beta page and asked whether the tool can help with reviews and refund questions.
Classify the inquiry and draft a response. Since this may be an early lead, flag whether the founder should review it personally.
```

### Agent

```text
cs-agent
```

### Output artifact

```text
lead_support_reply.json
```

### Expected output shape

```json
{
  "category": "product_inquiry",
  "intent": "beta_interest",
  "draft_reply": "Yes, the beta is designed for stores with recurring review and support workloads...",
  "needs_human_review": true,
  "reason": "Potential first customer; founder should personally respond."
}
```

### Learning target

Practice customer-message classification, reply drafting, and escalation judgement.

---

## Stage 5: Create beta onboarding work

### Client request

```text
The first beta customer is interested.
Create an internal onboarding ticket that lists what information we need before we can process their store data.
```

### Agent

```text
backoffice-agent
```

### Output artifact

```text
beta_onboarding_ticket.json
```

### Expected output shape

```json
{
  "task_type": "beta_onboarding",
  "customer": "Example Store",
  "missing_fields": [
    "store_url",
    "monthly_order_volume",
    "support_channel",
    "review_data_format"
  ],
  "checklist": [
    "confirm beta terms",
    "collect sample reviews",
    "collect sample support messages",
    "schedule onboarding call"
  ]
}
```

### Learning target

Practice converting customer interest into structured internal work.

---

## Stage 6: Triage the first operational incident

### Client request

```text
A beta customer uploaded a review CSV, but the analysis result did not appear.
Given the incident description and logs, identify likely causes and safe next checks.
```

### Agent

```text
devops-agent
```

### Output artifact

```text
csv_import_incident_triage.json
```

### Expected output shape

```json
{
  "incident": "CSV import failed for beta customer",
  "suspected_causes": [
    "unexpected column names",
    "encoding issue",
    "empty required field",
    "timeout during parsing"
  ],
  "safe_checks": [
    "inspect uploaded CSV headers",
    "check parser logs",
    "reproduce with sample file",
    "verify file encoding"
  ],
  "unsafe_actions": [
    "delete customer upload without backup",
    "change parser behavior without test case"
  ]
}
```

### Learning target

Practice incident triage without jumping directly to risky production actions.

---

## Stage 7: Review early security concerns

### Client request

```text
Now that beta customer data exists, review suspicious admin login failures and identify defensive checks we should perform.
```

### Agent

```text
security-assist-agent
```

### Output artifact

```text
security_review_ticket.json
```

### Expected output shape

```json
{
  "risk_level": "medium",
  "signals": [
    "multiple failed admin logins",
    "customer data access policy not documented"
  ],
  "recommended_checks": [
    "review admin login history",
    "confirm MFA status",
    "document data access roles",
    "check whether beta data is isolated"
  ],
  "needs_human_review": true
}
```

### Learning target

Practice defensive security triage and safe review planning.

---

## Stage 8: Evaluate the simulation

### Client request

```text
Review the outputs from this startup scenario.
Score what worked, what was weak, and what each agent should improve in the next iteration.
```

### Agent

```text
eval-benchmark
```

### Output artifact

```text
startup_simulation_eval.json
```

### Expected output shape

```json
{
  "scenario": "ecommerce_ai_ops_startup",
  "agent_outputs": [
    {
      "agent": "research-agent",
      "score": 0.82,
      "strength": "clear pain points",
      "weakness": "limited competitor detail"
    },
    {
      "agent": "cs-agent",
      "score": 0.76,
      "strength": "good classification",
      "weakness": "reply too generic"
    }
  ],
  "next_iteration": [
    "make research-agent cite source snippets",
    "make cs-agent separate beta lead from normal support",
    "make backoffice-agent produce stricter missing-field tickets"
  ]
}
```

### Learning target

Practice comparing agent outputs as experiment artifacts instead of treating each exercise as isolated.

---

## Full artifact chain

```text
founder_thesis.md
-> market_research_brief.json
-> launch_messaging.json
-> mvp_scope.json
-> lead_support_reply.json
-> beta_onboarding_ticket.json
-> csv_import_incident_triage.json
-> security_review_ticket.json
-> startup_simulation_eval.json
```

## Design principle

The company story should drive the agent tasks.

Do not start from:

```text
I need to build an agent, so I need a fake problem.
```

Start from:

```text
A founder has a problem hypothesis. The company creates work. Agents help handle that work.
```

This keeps the practice grounded, sequential, and easier to expand.

## Non-goals for this scenario

- No real customer data.
- No real external side effects.
- No automatic refunds, deployments, or security actions.
- No central orchestrator required for the first version.
- No assumption that all packages must be implemented before learning can start.

The first implementation can begin with only the founder thesis and `research-agent`.
