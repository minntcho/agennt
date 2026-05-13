# Scenario Structure

## 목적

`scenario`는 하나의 문제 케이스를 담는 단위입니다.

이 레포는 특정 스타트업 사례 하나를 구현하는 레포가 아니라, 여러 문제 케이스가 공통 agent 패키지를 조합해 artifact chain을 만드는 방식을 연습하는 레포입니다.

```text
scenario -> agent package -> artifact -> 다음 agent package
```

## 핵심 원칙

- 새 문제 케이스는 `packages/`에 직접 박지 않고 `scenarios/<scenario-name>/` 아래에 둡니다.
- `packages/*`는 재사용 가능한 도메인 agent입니다.
- `scenario`는 어떤 agent를 어떤 순서로 실행하고, 어떤 artifact를 입출력으로 사용할지 정의합니다.
- 실행 결과는 레포에 커밋하지 않고 `workspace/artifacts/<scenario-name>/` 아래에 생성합니다.
- 첫 구현은 deterministic demo여도 괜찮지만, PR 설명에서 실제 agent 동작과 구분합니다.

## 권장 디렉토리 구조

```text
scenarios/
  startup-ecommerce-ai-ops/
    README.md
    founder_thesis.md
    scenario.json
    expected/
      market_research_brief.json
      launch_messaging.json
      mvp_scope.json

packages/
  research-agent/
  sales-marketing-agent/
  ecommerce-agent/
  cs-agent/

workspace/
  artifacts/
    startup-ecommerce-ai-ops/
      market_research_brief.json
      launch_messaging.json
      mvp_scope.json
```

## `scenario.json` 초안

처음에는 복잡한 orchestrator 대신, 사람이 읽기 쉬운 실행 계획 정도면 충분합니다.

```json
{
  "name": "startup-ecommerce-ai-ops",
  "entry_artifact": "founder_thesis.md",
  "steps": [
    {
      "agent": "research-agent",
      "input": "founder_thesis.md",
      "output": "market_research_brief.json"
    },
    {
      "agent": "sales-marketing-agent",
      "input": "market_research_brief.json",
      "output": "launch_messaging.json"
    },
    {
      "agent": "ecommerce-agent",
      "input": [
        "market_research_brief.json",
        "launch_messaging.json"
      ],
      "output": "mvp_scope.json"
    }
  ]
}
```

## 테스트 위치

패키지 하나만 검증하는 테스트는 해당 패키지의 `tests/`에 둡니다.

여러 agent를 연결하는 scenario 테스트는 특정 패키지에 넣지 않고, 루트의 `tests/scenarios/` 또는 해당 `scenarios/<scenario-name>/tests/` 아래에 둡니다.

## 첫 예시 scenario

현재 첫 예시 케이스는 `Startup From Zero: Ecommerce AI Ops`입니다.

이 케이스는 작은 이커머스 셀러를 위한 AI 운영 보조 SaaS를 가정하고, 창업자 문제 가설에서 시작해 시장 조사, 출시 메시지, MVP 범위, 고객 문의, 운영 업무, 장애 대응, 보안 점검, 평가 artifact로 확장됩니다.

중요한 점은 이 케이스가 레포 전체의 고정 세계관이 아니라, `scenarios/*` 아래에 들어갈 첫 예시라는 것입니다.
