# startup-ecommerce-ai-ops

`Startup From Zero: Ecommerce AI Ops`의 첫 scenario 디렉토리입니다.

이 scenario는 작은 이커머스 셀러를 위한 AI 운영 보조 SaaS를 가정하고, 가상의 외부 클라이언트 요청서에서 출발해 agent artifact chain을 연습합니다.

클라이언트 요청서는 창업자의 문제 가설, 아직 검증되지 않은 불확실성, 원하는 산출물을 함께 담습니다. 이렇게 해야 레포 내부 규칙이 아니라 외부 요구가 agent 작업을 끌고 갑니다.

## 흐름

```text
client_request.md
-> market_research_brief.json
-> launch_messaging.json
-> mvp_scope.json
```

## 파일

- `client_request.md`: scenario의 시작 입력 artifact입니다. 의뢰자 상황, 창업자 문제 가설, 불확실성, 원하는 산출물을 담습니다.
- `scenario.json`: 어떤 agent가 어떤 artifact를 읽고 쓰는지 설명하는 실행 계획입니다.
- `expected/`: deterministic demo나 테스트에서 참고할 기대 artifact를 둘 수 있는 위치입니다.

이 디렉토리는 첫 예시 케이스일 뿐, 레포 전체의 고정 세계관은 아닙니다.
