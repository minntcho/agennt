# Ecosystem Architecture

## 목적

`agennt`는 연결된 작은 운영 시뮬레이션을 통해 agent 설계를 연습하는 레포입니다.

이 생태계의 중심은 특정 agent나 중앙 orchestrator가 아니라 `scenario`입니다. scenario는 하나의 문제 케이스를 설명하고, 여러 독립 agent 패키지가 만든 artifact를 이어 붙여 학습 가능한 흐름으로 만듭니다.

```text
작은 문제 케이스를 독립 agent들과 artifact 흐름으로 시뮬레이션하기
```

## 왜 scenario인가

회사나 서비스는 agent를 쓰기 위해 존재하지 않습니다. 먼저 문제 케이스가 있고, 그 문제를 풀기 위한 일이 생기며, 그 일을 돕기 위해 agent가 사용됩니다.

따라서 새 세계관이나 문제는 agent 패키지 내부에 박지 않고 `scenarios/*` 아래에 둡니다.

```text
문제 케이스 -> scenario -> agent 조합 -> artifact chain
```

이 구조를 통해 다음을 연습할 수 있습니다.

- 문제 정의
- 작업 분해
- 구조화된 출력
- 근거와 출처 추적
- workflow chaining
- 패키지 간 평가
- scenario 기반 학습

## 핵심 규칙

agent들은 artifact를 통해 소통합니다.

```text
agent -> artifact -> 다음 agent
```

패키지 간 내부 import를 주요 연결 방식으로 삼지 않습니다. 어떤 패키지가 다른 패키지의 결과를 재사용하려면, 그 패키지의 내부 구현을 알아야 하는 것이 아니라 명시적인 산출물을 읽으면 되어야 합니다.

## scenario와 package의 관계

```text
scenarios/*  = 문제 케이스와 실행 흐름
packages/*   = 재사용 가능한 도메인 agent
workspace/*  = 실행 결과 artifact
shared/*     = 공통 schema, prompt, utility
```

scenario는 agent를 조합합니다. agent는 scenario를 소유하지 않습니다.

예를 들어 `research-agent`는 이커머스 SaaS 문제 검증에도 쓰이고, 다른 시장 검증 scenario에도 쓰일 수 있어야 합니다.

## 제안 scenario 구조

```text
scenarios/
  startup-ecommerce-ai-ops/
    README.md
    founder_thesis.md
    scenario.json
    expected/
      market_research_brief.json
      launch_messaging.json
      mvp_scope.json
```

`scenario.json`은 처음부터 복잡한 orchestrator 설정일 필요가 없습니다. 어떤 입력을 어떤 agent가 읽고 어떤 artifact를 남기는지 설명하는 작은 실행 계획이면 충분합니다.

## 제안 workspace 구조

생성된 출력은 레포의 소스가 아니라 실행 결과입니다. 따라서 기본적으로 `workspace/` 아래에 둡니다.

```text
workspace/
├─ artifacts/
│  └─ startup-ecommerce-ai-ops/
│     ├─ market_research_brief.json
│     ├─ launch_messaging.json
│     └─ mvp_scope.json
└─ events/
```

## 패키지 역할

- `research-agent`: 넓은 주제에서 리서치 브리프를 만듭니다.
- `sales-marketing-agent`: 세일즈 이메일, 캠페인 카피, 랜딩 페이지 초안, 포지셔닝 문구를 만듭니다.
- `ecommerce-agent`: 상품, 리뷰, 판매, 재고, 주문 신호를 분석합니다.
- `cs-agent`: 고객 메시지를 분류하고 응답 초안을 만듭니다.
- `backoffice-agent`: 운영 요청을 구조화된 내부 업무 항목으로 바꿉니다.
- `devops-agent`: 로그, 장애, 배포 이슈, 안전한 다음 점검 항목을 triage합니다.
- `security-assist-agent`: 방어적 보안 이벤트를 검토하고 안전한 점검 항목을 제안합니다.
- `eval-benchmark`: 실험 결과를 수집하고 비교합니다.

## 첫 예시 scenario

첫 예시 scenario는 `Startup From Zero: Ecommerce AI Ops`입니다.

```text
1. 창업자가 문제 가설을 쓴다.
2. `research-agent`가 시장 조사 브리프를 만든다.
3. `sales-marketing-agent`가 출시 메시지를 만든다.
4. `ecommerce-agent`가 MVP 범위와 운영 신호를 정리한다.
5. `cs-agent`가 첫 고객 문의를 분류하고 응답 초안을 만든다.
6. `backoffice-agent`가 베타 온보딩 업무를 만든다.
7. `devops-agent`가 CSV 업로드 장애를 triage한다.
8. `security-assist-agent`가 초기 보안 이슈를 점검한다.
9. `eval-benchmark`가 각 산출물을 비교한다.
```

목표는 처음부터 거대한 production orchestrator를 만드는 것이 아닙니다. 각 scenario를 하나의 공유 세계 안에 놓아서 연습을 더 구체적이고 확장 가능하게 만드는 것입니다.

자세한 scenario 디렉토리 설계는 `docs/scenario-structure.md`에 있습니다.

## 현재 non-goals

- 중앙 집중형 monolithic runtime 없음.
- 필수 multi-agent orchestration 없음.
- 패키지 간 내부 결합 없음.
- 실제 production side effect 없음.
- 명시적인 후속 설계 없는 자동 외부 action 없음.
- 단일 startup scenario에만 종속된 레포 구조 없음.
