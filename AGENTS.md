# AGENTS.md

## 언어 원칙

이 레포의 문서, 설명, PR 제목과 본문, 작업 지시는 한국어를 기본으로 작성합니다.

코드 식별자, 패키지 이름, 파일 이름, 명령어, JSON 필드명처럼 실행 계약에 해당하는 부분은 영어를 유지합니다.

## 프로젝트 방향

이 레포는 도메인별 agent 패턴과 artifact 기반 연결 방식을 연습하기 위한 공간입니다.

특정 스타트업 케이스 하나에 종속되지 않고, 여러 문제 케이스를 `scenarios/*` 아래에 추가할 수 있어야 합니다.

처음부터 거대한 중앙 orchestrator나 공통 런타임을 만들기보다, scenario가 독립 agent 패키지를 조합하고, 각 패키지가 명시적인 artifact를 만들며, 다음 패키지가 그 artifact를 읽는 흐름을 우선합니다.

```text
scenario -> agent -> artifact -> 다음 agent
```

## Scenario 원칙

- 새 문제 케이스는 `packages/`가 아니라 `scenarios/<scenario-name>/` 아래에 둡니다.
- `packages/*`는 특정 scenario 전용 구현이 아니라 재사용 가능한 도메인 agent로 유지합니다.
- scenario는 입력 artifact, 실행 순서, 기대 출력 artifact를 설명합니다.
- scenario 통합 테스트는 특정 agent 패키지 내부보다 `tests/scenarios/` 또는 `scenarios/<scenario-name>/tests/`에 두는 것을 선호합니다.
- deterministic demo와 실제 agent 동작을 PR 설명에서 구분합니다.

## 작업 방식

- 작은 PR을 선호합니다.
- 각 패키지는 독립적으로 실행 가능해야 합니다.
- 공통 agent 인터페이스인 `run(input_data: dict) -> dict`를 유지합니다.
- 패키지 간 내부 함수를 직접 import해서 연결하기보다 명시적인 artifact를 통해 연결합니다.

## 로컬 작업 공간

- PR이나 큰 작업 단위마다 별도 git worktree를 사용하는 방식을 권장합니다.
- 생성된 demo와 scenario 출력은 `workspace/` 아래에 둡니다.
- `workspace/` 아래 생성물은 기본적으로 커밋하지 않습니다.

## 테스트

개발 의존성 설치:

```bash
python -m pip install -r requirements-dev.txt
```

테스트 실행:

```bash
python -m pytest -q
```
