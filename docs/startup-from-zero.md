# Startup From Zero: Ecommerce AI Ops

## 컨셉

이 시나리오는 완성된 agent 아키텍처에서 출발하지 않습니다. 출발점은 창업자의 문제 가설입니다.

회사는 agent를 쓰기 위해 존재하지 않습니다. 회사는 창업자가 실제 운영 문제를 발견하면서 시작됩니다. 이후 리서치, 메시징, 제품 운영, 고객 지원, 내부 업무, 장애 대응, 보안 점검, 평가 artifact가 생기고, 그 과정에서 agent들이 유용해집니다.

전체 흐름은 다음입니다.

```text
창업자 문제 가설
-> 시장 검증
-> 출시 메시지
-> MVP 범위
-> 첫 고객 문의
-> 베타 온보딩
-> 운영 장애
-> 보안 점검
-> 실험 평가
```

## 회사 전제

창업자는 작은 이커머스 셀러를 위한 AI 운영 보조 SaaS를 만들고 싶어합니다.

초기 가설은 다음입니다.

```text
작은 이커머스 셀러들은 리뷰 읽기, 고객 메시지 응답, 환불 추적, 상품 카피 작성, 운영 이슈 대응 같은 반복 업무에 너무 많은 시간을 쓴다.

AI assistant는 흩어진 운영 신호를 구조화된 요약, 초안, 경고, 내부 업무로 바꿔 이 문제를 줄일 수 있다.
```

이 회사는 제품이 아니라 thesis에서 시작합니다.

## 첫 artifact: founder thesis

파일 아이디어:

```text
founder_thesis.md
```

예시:

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

이 thesis가 첫 agent 작업의 루트 입력이 됩니다.

---

## Stage 1: 문제가 실제인지 검증하기

### Client request

```text
우리는 작은 이커머스 셀러들이 반복 운영 업무에 시달린다고 보고 있다.
이 문제가 실제로 존재하는지, 어떤 pain이 흔한지, 다음에 조사해야 할 질문이 무엇인지 조사해줘.
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

넓은 창업자 가설을 구조화된 research brief로 바꾸는 연습입니다.

---

## Stage 2: 첫 시장-facing 메시지 만들기

### Client request

```text
research brief를 바탕으로 landing page copy와 cold email draft를 만들어줘.
제품은 아직 완성되지 않았고, 목표는 인터뷰와 베타 신청을 받는 것이다.
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

리서치 결과를 제품이 성숙한 척하지 않는 유용한 메시지로 바꾸는 연습입니다.

---

## Stage 3: MVP 범위 정하기

### Client request

```text
우리는 모든 기능을 한 번에 만들 수 없다.
리뷰 분석, 고객 응답 초안, 재고 경고, 상품 카피 생성 중에서 첫 MVP 범위를 추천해줘.
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

범위 통제 연습입니다. 첫 제품은 전체 운영체제인 척하기보다, 하나의 아픈 workflow를 먼저 해결해야 합니다.

---

## Stage 4: 첫 고객 문의 처리하기

### Client request

```text
한 스토어 운영자가 베타 페이지를 보고, 이 도구가 리뷰와 환불 문의에 도움을 줄 수 있는지 물었다.
문의 유형을 분류하고 응답 초안을 만들어줘. 초기 리드일 수 있으니 창업자가 직접 검토해야 하는지도 표시해줘.
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

고객 메시지 분류, 응답 초안 작성, escalation 판단을 연습합니다.

---

## Stage 5: 베타 온보딩 업무 만들기

### Client request

```text
첫 베타 고객이 관심을 보였다.
고객의 store data를 처리하기 전에 어떤 정보가 필요한지 내부 onboarding ticket으로 정리해줘.
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

고객 관심을 구조화된 내부 업무로 바꾸는 연습입니다.

---

## Stage 6: 첫 운영 장애 triage하기

### Client request

```text
베타 고객이 review CSV를 업로드했는데 분석 결과가 나오지 않았다.
장애 설명과 로그를 바탕으로 가능한 원인과 안전한 다음 점검 항목을 제안해줘.
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

위험한 production action으로 바로 뛰지 않고 장애를 triage하는 연습입니다.

---

## Stage 7: 초기 보안 우려 점검하기

### Client request

```text
이제 베타 고객 데이터가 생겼다.
관리자 로그인 실패가 반복된 기록을 검토하고, 우리가 수행해야 할 방어적 점검 항목을 정리해줘.
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

방어적 보안 triage와 안전한 점검 계획을 연습합니다.

---

## Stage 8: 시뮬레이션 평가하기

### Client request

```text
이번 startup scenario에서 나온 산출물들을 검토해줘.
무엇이 잘 됐고, 무엇이 약했으며, 각 agent가 다음 iteration에서 무엇을 개선해야 하는지 평가해줘.
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

각 연습을 고립된 과제로 끝내지 않고, agent 산출물을 실험 artifact로 비교하는 연습입니다.

---

## 전체 artifact chain

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

## 설계 원칙

회사 이야기가 agent 작업을 이끌어야 합니다.

이렇게 시작하지 않습니다.

```text
agent를 만들어야 하니까 가짜 문제를 찾는다.
```

이렇게 시작합니다.

```text
창업자에게 문제 가설이 있다.
회사가 생기면서 일이 생긴다.
agent가 그 일을 돕는다.
```

이 방식은 연습을 더 구체적이고, 순차적이고, 확장 가능하게 만듭니다.

## 이 시나리오의 non-goals

- 실제 고객 데이터 없음.
- 실제 외부 side effect 없음.
- 자동 환불, 자동 배포, 자동 보안 조치 없음.
- 첫 버전에서 중앙 orchestrator는 필수가 아님.
- 모든 패키지를 구현해야만 학습을 시작할 수 있다는 가정 없음.

첫 구현은 `founder_thesis`와 `research-agent`만으로 시작할 수 있습니다.
