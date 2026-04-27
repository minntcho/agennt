# Ecosystem Architecture

## 목적

`agennt`는 연결된 작은 운영 시뮬레이션을 통해 agent 설계를 연습하는 레포입니다.

각 패키지는 독립적으로 실행되고 테스트될 수 있어야 합니다. 동시에 패키지들이 만든 산출물이 다른 패키지의 입력이 될 때, 연습은 훨씬 더 재미있고 실제 업무에 가까워집니다.

설계 목표는 다음입니다.

```text
작은 회사 / 서비스 운영을 독립 agent들로 시뮬레이션하기
```

## 핵심 규칙

agent들은 artifact를 통해 소통합니다.

```text
agent -> artifact -> 다음 agent
```

패키지 간 내부 import를 주요 연결 방식으로 삼지 않습니다. 어떤 패키지가 다른 패키지의 결과를 재사용하려면, 그 패키지의 내부 구현을 알아야 하는 것이 아니라 명시적인 산출물을 읽으면 되어야 합니다.

## 왜 artifact인가

artifact는 연습을 모듈화하면서도 서로 연결된 느낌을 줍니다.

이를 통해 다음을 연습할 수 있습니다.

- 작업 분해
- 구조화된 출력
- 근거와 출처 추적
- workflow chaining
- 패키지 간 평가
- 시나리오 기반 학습

## 패키지 역할

### `research-agent`

넓은 주제에서 리서치 브리프를 만듭니다.

예시 artifact:

```text
market_brief.json
```

후속 사용:

- `sales-marketing-agent`가 발견한 pain point와 시장 신호를 사용할 수 있습니다.
- `ecommerce-agent`가 시장/경쟁 맥락을 사용할 수 있습니다.
- `eval-benchmark`가 브리프 품질을 평가할 수 있습니다.

### `sales-marketing-agent`

세일즈 이메일, 캠페인 카피, 랜딩 페이지 초안, 포지셔닝 문구를 만듭니다.

예시 artifact:

```text
campaign_copy.json
```

후속 사용:

- `ecommerce-agent`가 제품 카피를 사용할 수 있습니다.
- `cs-agent`가 현재 포지셔닝에 맞춰 고객 응답 톤을 맞출 수 있습니다.
- `eval-benchmark`가 여러 variant를 비교할 수 있습니다.

### `ecommerce-agent`

상품, 리뷰, 판매, 재고, 주문 신호를 분석합니다.

예시 artifact:

```text
product_ops_summary.json
```

후속 사용:

- `cs-agent`가 반복 불만을 사용할 수 있습니다.
- `backoffice-agent`가 재고/환불 관련 신호를 내부 업무로 바꿀 수 있습니다.
- `sales-marketing-agent`가 리뷰에서 나온 장점을 마케팅 재료로 사용할 수 있습니다.

### `cs-agent`

고객 메시지를 분류하고 응답 초안을 만듭니다.

예시 artifact:

```text
support_case_summary.json
```

후속 사용:

- `backoffice-agent`가 내부 처리 티켓을 만들 수 있습니다.
- `ecommerce-agent`가 반복 상품 이슈를 학습할 수 있습니다.
- `eval-benchmark`가 분류와 응답 품질을 평가할 수 있습니다.

### `backoffice-agent`

운영 요청을 구조화된 내부 업무 항목으로 바꿉니다.

예시 artifact:

```text
internal_task_ticket.json
```

후속 사용:

- `eval-benchmark`가 완성도를 평가할 수 있습니다.
- 나중의 workflow 도구가 누락 필드와 승인 항목을 점검할 수 있습니다.

### `devops-agent`

로그, 장애, 배포 이슈, 안전한 다음 점검 항목을 triage합니다.

예시 artifact:

```text
incident_triage.json
```

후속 사용:

- `cs-agent`가 고객 안내문을 만들 수 있습니다.
- `backoffice-agent`가 후속 업무를 열 수 있습니다.
- `eval-benchmark`가 진단 품질을 비교할 수 있습니다.

### `security-assist-agent`

방어적 보안 이벤트를 검토하고 안전한 점검 항목을 제안합니다.

예시 artifact:

```text
security_triage.json
```

후속 사용:

- `backoffice-agent`가 내부 보안 점검 체크리스트를 만들 수 있습니다.
- `devops-agent`가 운영 신호와 보안 신호를 함께 볼 수 있습니다.
- `eval-benchmark`가 위험도 분류를 평가할 수 있습니다.

### `eval-benchmark`

실험 결과를 수집하고 비교합니다.

예시 artifact:

```text
benchmark_report.json
```

후속 사용:

- 사람이 버전별 개선점을 검토할 수 있습니다.
- 나중에 score, latency, cost, failure mode를 비교하는 자동화에 사용할 수 있습니다.

## 제안 workspace 구조

나중에 scenario 입력과 생성된 출력을 저장하기 위한 local workspace를 둘 수 있습니다.

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

이 workspace는 가장 초기 연습에 필수는 아니지만, 레포가 어디로 자랄지 보여주는 성장 경로가 됩니다.

## 첫 연결 시나리오

첫 시나리오는 `Startup From Zero: Ecommerce AI Ops`입니다.

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

목표는 처음부터 거대한 production orchestrator를 만드는 것이 아닙니다. 각 패키지를 하나의 공유 세계 안에 놓아서 연습을 더 재미있게 만드는 것입니다.

자세한 내용은 `docs/startup-from-zero.md`에 있습니다.

## 현재 non-goals

- 중앙 집중형 monolithic runtime 없음.
- 필수 multi-agent orchestration 없음.
- 패키지 간 내부 결합 없음.
- 실제 production side effect 없음.
- 명시적인 후속 설계 없는 자동 외부 action 없음.
