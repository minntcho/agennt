# agennt

`agennt`는 agent 시스템을 **문제 케이스별 scenario**와 **도메인별 독립 패키지**로 연습하기 위한 레포입니다.

## 언어 원칙

이 레포의 문서, 설명, PR 제목과 본문, 작업 지시는 한국어를 기본으로 작성합니다.

코드 식별자, 패키지 이름, 파일 이름, 명령어, JSON 필드명처럼 실행 계약에 해당하는 부분은 영어를 유지합니다.

## 방향

`agennt`는 하나의 거대한 공통 런타임을 먼저 만드는 레포가 아닙니다. 또한 특정 스타트업 사례 하나만 구현하는 레포도 아닙니다.

여러 문제 케이스를 `scenarios/*` 아래에 두고, 각 scenario가 재사용 가능한 `packages/*` agent들을 조합해 artifact chain을 만드는 것이 목표입니다.

핵심 규칙은 다음입니다.

```text
scenario -> agent -> artifact -> 다음 agent
```

즉, agent끼리 서로 내부 함수를 직접 import해서 호출하는 방식보다, 명시적인 산출물을 남기고 그 산출물을 다음 agent가 읽는 방식을 우선합니다.

## 첫 예시 scenario

첫 예시 케이스는 **Startup From Zero: Ecommerce AI Ops**입니다.

완성된 agent 구조에서 시작하지 않고, 가상의 클라이언트 요청서에서 시작합니다. 요청서 안에는 창업자의 문제 가설과 아직 검증되지 않은 불확실성이 함께 들어 있습니다.

작은 이커머스 셀러들이 반복 운영 업무에 시달린다는 문제를 발견하고, 이를 해결하는 AI 운영 보조 SaaS를 만든다고 가정합니다.

이 회사가 생기면서 agent들이 맡을 일이 차례로 발생합니다.

```text
클라이언트 요청서
-> 시장 조사
-> 출시 메시지
-> MVP 범위 설정
-> 첫 고객 문의
-> 베타 온보딩
-> CSV 업로드 장애
-> 보안 점검
-> 실험 평가
```

전체 시나리오 설명은 `docs/startup-from-zero.md`에 있고, scenario 디렉토리 설계는 `docs/scenario-structure.md`에 정리되어 있습니다.

첫 scenario 디렉토리는 `scenarios/startup-ecommerce-ai-ops/`에 있습니다.

## 구조

- `apps/*`: agent가 붙을 실제 제품 표면을 두는 위치입니다.
- `agent_specs/*`: 제품 백엔드와 분리된 agent 제안 명세를 두는 위치입니다.
- `scenarios/*`: 문제 케이스별 입력, 실행 흐름, 기대 artifact를 두는 위치입니다.
- `packages/*`: 도메인별 agent 패키지. 공통 인터페이스는 `run(input_data) -> dict`입니다.
- `workspace/*`: scenario 실행 결과 artifact를 저장하는 로컬 작업 공간입니다. 생성물은 기본적으로 커밋하지 않습니다.
- `shared/*`: 공유 schema, prompt, utility helper를 두는 위치입니다.
- `docs/architecture.md`: 전체 아키텍처와 기본 규칙입니다.
- `docs/ecosystem-architecture.md`: artifact 기반 agent 생태계 방향입니다.
- `docs/scenario-structure.md`: 문제 케이스별 scenario 구조입니다.
- `docs/startup-from-zero.md`: 첫 예시 scenario의 상세 설명입니다.

## Quick start

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
make run PKG=cs-agent
make support-desk-api
```
