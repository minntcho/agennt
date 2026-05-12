# agennt

`agennt`는 agent 시스템을 **도메인별 독립 패키지**로 연습하기 위한 레포입니다.

## 방향

`agennt`는 하나의 거대한 공통 런타임을 먼저 만드는 레포가 아닙니다.

각 패키지는 독립적으로 실행 가능한 연습 단위로 유지하되, 패키지들이 만든 산출물이 서로의 입력이 되는 작은 **agent 생태계**로 키우는 것이 목표입니다.

핵심 규칙은 다음입니다.

```text
agent -> artifact -> 다른 agent가 artifact를 읽음
```

즉, agent끼리 서로 내부 함수를 직접 import해서 호출하는 방식보다, 명시적인 산출물을 남기고 그 산출물을 다음 agent가 읽는 방식을 우선합니다.

## 첫 시나리오

첫 세계관은 **Startup From Zero: Ecommerce AI Ops**입니다.

완성된 agent 구조에서 시작하지 않고, 창업자의 문제 가설에서 시작합니다. 작은 이커머스 셀러들이 반복 운영 업무에 시달린다는 문제를 발견하고, 이를 해결하는 AI 운영 보조 SaaS를 만든다고 가정합니다.

이 회사가 생기면서 agent들이 맡을 일이 차례로 발생합니다.

```text
창업자 문제 가설
-> 시장 조사
-> 출시 메시지
-> MVP 범위 설정
-> 첫 고객 문의
-> 베타 온보딩
-> CSV 업로드 장애
-> 보안 점검
-> 실험 평가
```

전체 시나리오는 `docs/startup-from-zero.md`에 정리되어 있습니다.

## 구조

- `packages/*`: 도메인별 agent 패키지. 공통 인터페이스는 `run(input_data) -> dict`입니다.
- `shared/*`: 공유 schema, prompt, utility helper를 두는 위치입니다.
- `docs/architecture.md`: 전체 아키텍처와 기본 규칙입니다.
- `docs/ecosystem-architecture.md`: artifact 기반 agent 생태계 방향입니다.
- `docs/startup-from-zero.md`: 첫 클라이언트/창업자 주도 시나리오입니다.
- `examples/startup-from-zero/founder_thesis.md`: 3단계 데모의 시작 입력입니다.

## Quick start

```bash
make test
make run PKG=cs-agent
make demo-startup
```

`make demo-startup`은 `founder_thesis.md`를 읽고 다음 artifact를 만듭니다.

```text
market_research_brief.json
-> launch_messaging.json
-> mvp_scope.json
```
