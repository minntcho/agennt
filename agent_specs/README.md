# agent_specs

`agent_specs/*`는 제품 백엔드와 분리된 agent 제안 명세를 두는 위치입니다.

백엔드는 고객 문의, 상태, 메모, 응답 초안 같은 제품 데이터를 책임집니다. agent는 그 데이터를 직접 바꾸지 않고, 백엔드가 받을 수 있는 제안을 만듭니다.

```text
backend data
-> agent input
-> agent proposal
-> operator decision
-> backend state change
```

agent 구현은 `packages/*`에 둘 수 있지만, 어떤 제안을 언제 제출해야 하는지는 이 디렉토리에서 먼저 문서화합니다.
