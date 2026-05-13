# support_desk_proposals

`support_desk_demo` 백엔드가 받을 수 있는 agent 제안 명세입니다.

agent는 백엔드 상태를 직접 변경하지 않습니다. 대신 `agent_proposal`을 만들고, 운영자가 그 제안을 검토합니다.

## 공통 형태

```json
{
  "source_agent": "cs-agent",
  "proposal_type": "support_intake",
  "target_type": "inquiry",
  "target_id": "inq-1001",
  "title": "환불 문의 응대 전 확인 항목",
  "summary": "환불 승인 전에 주문, 상품 상태, 환불 정책을 확인해야 합니다.",
  "payload": {
    "needed_context": ["주문 번호", "스토어 환불 정책"],
    "do_not_auto_handle": ["환불 승인"]
  }
}
```

`target_type`과 `target_id`는 `POST /agent-proposals`로 직접 제출할 때 필요합니다.

특정 문의에 붙이는 제안은 `POST /inquiries/{id}/agent-proposals`를 사용할 수 있습니다. 이때 백엔드가 `target_type: inquiry`, `target_id: {id}`를 채웁니다.

## 패키지별 제안 타입

| package | proposal_type | 의미 |
| --- | --- | --- |
| `cs-agent` | `support_intake` | 고객 응대 전에 확인해야 할 정보와 위험 신호 |
| `cs-agent` | `reply_draft` | 사람이 검토할 응답 초안 |
| `cs-agent` | `inquiry_triage` | 문의 유형, 긴급도, 라우팅 제안 |
| `research-agent` | `market_research` | 고객군, pain, 검증 질문에 대한 조사 요약 |
| `research-agent` | `customer_segment_note` | 문의나 리드에서 발견한 고객군 메모 |
| `sales-marketing-agent` | `launch_messaging` | 베타 모집, 랜딩 카피, 이메일 메시지 제안 |
| `sales-marketing-agent` | `campaign_copy` | 고객군별 캠페인 문구 제안 |
| `ecommerce-agent` | `mvp_scope` | 제품 범위와 제외 범위 제안 |
| `ecommerce-agent` | `product_signal` | 리뷰나 문의에서 발견한 상품/운영 신호 |
| `ecommerce-agent` | `returns_policy_note` | 환불/반품 정책 검토 메모 |
| `backoffice-agent` | `internal_task` | 사람이 처리할 내부 업무 제안 |
| `backoffice-agent` | `onboarding_checklist` | 베타 고객 온보딩 체크리스트 |
| `devops-agent` | `incident_triage` | 장애 가능성, 안전한 확인 순서 |
| `devops-agent` | `operational_checklist` | 운영 점검 체크리스트 |
| `security-assist-agent` | `security_review` | 보안 위험 신호와 방어적 점검 항목 |
| `security-assist-agent` | `access_risk_note` | 권한, 로그인, 데이터 접근 관련 위험 메모 |
| `eval-benchmark` | `evaluation_report` | agent 제안이나 시나리오 실행 결과 평가 |

## 원칙

- agent 제안은 기본적으로 `pending` 상태로 저장합니다.
- agent 제안은 고객에게 바로 노출하지 않습니다.
- 환불 승인, 보상 약속, 정책 예외, 보안 조치, 배포 조치는 사람이 결정합니다.
- 백엔드는 agent output의 원문을 `payload`에 보존하되, 상태 변경은 운영자의 decision 이후에만 수행합니다.
