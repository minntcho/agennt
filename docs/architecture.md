# Architecture

## 목표

이 레포는 도메인별 agent 패턴과 artifact 기반 연결 방식을 연습하기 위한 훈련장입니다.

목표는 모든 패키지를 하나의 공통 런타임으로 합치는 것이 아닙니다. 또한 `Startup From Zero: Ecommerce AI Ops` 하나만 구현하는 것도 아닙니다.

여러 문제 케이스를 `scenarios/*` 아래에 두고, 각 scenario가 독립 agent 패키지들을 조합해 artifact chain을 만드는 구조를 지향합니다.

```text
scenario + 독립 agent 패키지 + 공유 artifact 흐름 = agent ecosystem 연습
```

## 핵심 단위

### `scenarios/*`

문제 케이스, 세계관, 입력 artifact, 실행 흐름, 기대 출력 형태를 담는 위치입니다.

scenario는 어떤 agent를 어떤 순서로 사용할지 정하지만, agent 구현을 소유하지 않습니다.

### `packages/*`

도메인별 agent 패키지입니다. 패키지는 특정 scenario에 종속되지 않고 독립적으로 실행 가능해야 합니다.

공통 인터페이스는 다음 형태를 유지합니다.

```python
run(input_data: dict) -> dict
```

### `workspace/*`

scenario 실행 결과를 저장하는 로컬 작업 공간입니다. 생성된 artifact는 기본적으로 커밋하지 않습니다.

### `shared/*`

공유 schema, prompt, artifact IO helper, utility helper를 둘 수 있는 위치입니다.

## 실험 범위

`scenarios/*`와 `workspace/*`는 케이스별 실험 자유도가 높은 공간입니다. 새 문제 케이스, 입력 artifact, 실행 흐름, 기대 출력, 로컬 실행 결과는 이 범위에서 과감하게 시도할 수 있습니다.

`packages/*`와 `shared/*`는 여러 scenario가 함께 쓰는 재사용 영역입니다. 이 영역을 바꿀 때는 공통 인터페이스, artifact 계약, 기존 scenario에 미치는 영향을 확인합니다.

## 도메인 패키지

- `research-agent`: 넓은 주제를 구조화된 리서치 브리프로 바꿉니다.
- `sales-marketing-agent`: 리서치, 제품, 고객 맥락을 바탕으로 캠페인 카피와 세일즈 초안을 만듭니다.
- `ecommerce-agent`: 상품, 리뷰, 주문, 재고 신호를 분석합니다.
- `cs-agent`: 고객 메시지를 분류하고 응답 초안을 만듭니다.
- `backoffice-agent`: 운영 요청을 내부 업무 항목으로 구조화합니다.
- `devops-agent`: 로그, 장애, 배포 이슈를 triage합니다.
- `security-assist-agent`: 방어적 보안 이벤트를 검토하고 안전한 점검 항목을 제안합니다.
- `eval-benchmark`: 실험 산출물을 단순 지표로 비교합니다.

## 연결 모델

agent들은 직접 서로를 호출하기보다, 명시적인 artifact를 통해 연결됩니다.

```text
scenario 입력
-> agent A 실행
-> artifact 작성
-> agent B가 artifact를 입력으로 받음
-> agent B가 새 artifact 작성
```

중요한 기준은 다음입니다.

```text
scenario가 agent를 조합한다.
agent가 scenario를 소유하지 않는다.
```

예를 들어 `research-agent`는 이커머스 스타트업 scenario에서도 쓰일 수 있고, 다른 문제 검증 scenario에서도 쓰일 수 있어야 합니다.

## 권장 디렉토리 구조

```text
scenarios/
  startup-ecommerce-ai-ops/
    README.md
    founder_thesis.md
    scenario.json
    expected/

packages/
  research-agent/
  sales-marketing-agent/
  ecommerce-agent/

workspace/
  artifacts/
    startup-ecommerce-ai-ops/
```

자세한 scenario 구조는 `docs/scenario-structure.md`를 따릅니다.

## 규칙

1. 각 패키지는 독립 실행 가능해야 합니다.
2. agent 인터페이스는 `run(input_data: dict) -> dict`로 표준화합니다.
3. 모든 패키지는 smoke test를 가집니다.
4. 재사용될 가능성이 있는 패키지 출력은 명시적인 artifact 형태로 만듭니다.
5. 패키지는 서로의 내부 함수를 직접 import해서 호출하는 방식에 의존하지 않습니다.
6. 새 문제 케이스는 `scenarios/*` 아래에 추가합니다.
7. scenario 통합 테스트는 특정 패키지 내부보다 scenario 또는 루트 테스트 위치에 둡니다.

## 첫 예시 scenario

첫 예시 scenario는 `Startup From Zero: Ecommerce AI Ops`입니다.

이 scenario는 작은 이커머스 셀러를 위한 AI 운영 보조 SaaS를 가정하고, 창업자 문제 가설에서 시장 조사, 출시 메시지, MVP 범위, 고객 문의, 운영 업무, 장애 대응, 보안 점검, 평가 artifact로 확장됩니다.

이 scenario는 레포 전체의 고정 세계관이 아니라, 앞으로 추가될 여러 문제 케이스 중 첫 예시입니다.
