# scenarios

문제 케이스별 scenario를 두는 위치입니다.

각 scenario는 하나의 문제, 세계관, 입력 artifact, 실행 흐름, 기대 출력 artifact를 설명합니다.

새 케이스는 `packages/`에 직접 박지 않고 이 디렉토리 아래에 추가합니다.

```text
scenarios/<scenario-name>/
  README.md
  scenario.json
  입력 artifact
  expected/
```
