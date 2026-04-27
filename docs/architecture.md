# Architecture

## 목표

이 레포는 도메인별 agent 패턴을 연습하기 위한 훈련장입니다.

목표는 모든 패키지를 하나의 공통 런타임으로 합치는 것이 아닙니다. 각 패키지는 독립적인 연습 단위로 유지하되, 더 큰 방향에서는 독립 agent들이 artifact를 만들고, 다른 agent가 그 artifact를 읽는 작은 운영 생태계를 모델링합니다.

요약하면 다음과 같습니다.

```text
독립 agent 패키지 + 공유 artifact 흐름 = agent ecosystem 연습
```

## 도메인 패키지

- `research-agent`: 넓은 주제를 구조화된 리서치 브리프로 바꿉니다.
- `sales-marketing-agent`: 리서치, 제품, 고객 맥락을 바탕으로 캠페인 카피와 세일즈 초안을 만듭니다.
- `ecommerce-agent`: 상품, 리뷰, 주문, 재고 신호를 분석합니다.
- `cs-agent`: 고객 메시지를 분류하고 응답 초안을 만듭니다.
- `backoffice-agent`: 운영 요청을 내부 업무 항목으로 구조화합니다.
- `devops-agent`: 로그, 장애, 배포 이슈를 triage합니다.
- `security-assist-agent`: 방어적 보안 이벤트를 검토하고 안전한 점검 항목을 제안합니다.
- `eval-benchmark`: 실험 산출물을 단순 지표로 비교합니다.

## 생태계 모델

agent들은 직접 서로를 호출하기보다, 명시적인 artifact를 통해 연결됩니다.

선호 흐름은 다음입니다.

```text
agent A 실행
-> artifact 작성
-> agent B가 그 artifact를 입력으로 받음
-> agent B가 새 artifact 작성
```

예시:

- `research-agent`가 시장 조사 브리프를 만들고, `sales-marketing-agent`가 이를 사용해 캠페인 카피를 만듭니다.
- `ecommerce-agent`가 상품 불만 신호를 추출하고, `cs-agent`가 이를 고객문의 분류에 활용합니다.
- `cs-agent`가 환불 케이스를 식별하고, `backoffice-agent`가 이를 내부 검토 티켓으로 바꿉니다.
- `devops-agent`가 checkout 장애를 요약하고, `cs-agent`가 고객 안내문을 만듭니다.
- `security-assist-agent`가 계정 위험 신호를 찾고, `backoffice-agent`가 내부 점검 체크리스트를 만듭니다.
- 모든 패키지 산출물은 나중에 `eval-benchmark`의 입력이 될 수 있습니다.

## 규칙

1. 각 패키지는 독립 실행 가능해야 합니다.
2. agent 인터페이스는 `run(input_data: dict) -> dict`로 표준화합니다.
3. 모든 패키지는 smoke test를 가집니다.
4. 재사용될 가능성이 있는 패키지 출력은 명시적인 artifact 형태로 만듭니다.
5. 패키지는 서로의 내부 함수를 직접 import해서 호출하는 방식에 의존하지 않습니다.
6. `eval-benchmark`는 실험을 비교하기 위한 단순 metrics schema를 제공합니다.

## 학습 방향

하나의 구체적인 시나리오에서 시작하고, 패키지들이 저장된 산출물을 통해 서로 영향을 주도록 만듭니다.

첫 시나리오는 다음 흐름이 좋습니다.

```text
창업자 문제 가설
-> 시장 조사 브리프
-> 출시 메시지
-> MVP 범위
-> 고객 문의 대응
-> 내부 운영 티켓
-> 장애/보안 triage
-> 평가 리포트
```

이 방식은 패키지 독립성을 유지하면서도, 연습을 하나의 이야기처럼 이어지게 만듭니다.
