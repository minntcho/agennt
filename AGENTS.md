# AGENTS.md

## 언어 원칙

이 레포의 문서, 설명, PR 제목과 본문, 작업 지시는 한국어를 기본으로 작성합니다.

코드 식별자, 패키지 이름, 파일 이름, 명령어, JSON 필드명처럼 실행 계약에 해당하는 부분은 영어를 유지합니다.

## 프로젝트 방향

이 레포는 도메인별 agent 패턴과 artifact 기반 연결 방식을 연습하기 위한 공간입니다.

처음부터 거대한 중앙 orchestrator나 공통 런타임을 만들기보다, 독립 패키지가 명시적인 artifact를 만들고 다른 패키지가 그 artifact를 읽는 흐름을 우선합니다.

```text
agent -> artifact -> 다음 agent
```

## 작업 방식

- 작은 PR을 선호합니다.
- 각 패키지는 독립적으로 실행 가능해야 합니다.
- 공통 agent 인터페이스인 `run(input_data: dict) -> dict`를 유지합니다.
- 패키지 간 내부 함수를 직접 import해서 연결하기보다 명시적인 artifact를 통해 연결합니다.
- deterministic demo와 실제 agent 동작을 PR 설명에서 구분합니다.

## 로컬 작업 공간

- PR이나 큰 작업 단위마다 별도 git worktree를 사용하는 방식을 권장합니다.
- 생성된 데모 출력은 `workspace/` 아래에 둡니다.
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
