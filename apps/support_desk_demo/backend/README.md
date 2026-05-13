# support_desk_demo backend

프론트엔드가 붙기 전 단계의 고객 문의 API입니다.

이 백엔드는 agent를 실행하지 않습니다. 고객 문의, 상태, 내부 메모, 응답 초안, agent 제안을 관리하는 제품 백엔드입니다.

agent는 필요할 때 별도 패키지나 별도 명세에서 실행되고, 결과를 `agent_proposal`로 제출합니다. 운영자는 그 제안을 검토한 뒤 `accept`, `reject`, `archive` 중 하나로 처리합니다.

## 실행

```bash
python -m apps.support_desk_demo.backend.server
```

기본 주소는 `http://127.0.0.1:8000`입니다.

## API

```text
GET /health
GET /inquiries
POST /inquiries
GET /inquiries/{id}
PATCH /inquiries/{id}/status
POST /inquiries/{id}/notes
POST /inquiries/{id}/draft-replies
GET /inquiries/{id}/agent-proposals
POST /inquiries/{id}/agent-proposals
GET /agent-proposals
POST /agent-proposals
GET /agent-proposals/{id}
PATCH /agent-proposals/{id}/decision
GET /agent-proposal-contracts
```

## 역할

백엔드는 고객에게 바로 답변하지 않습니다. 환불 승인, 보상 약속, 정책 예외 판단도 하지 않습니다.

대신 사람이 고객 문의를 처리하는 데 필요한 기본 업무 흐름을 제공합니다.

```text
문의 생성
-> 상태 변경
-> 내부 메모 작성
-> 응답 초안 저장
-> agent 제안 수신
-> 사람이 제안 검토
```

## Agent proposal

agent는 백엔드 상태를 직접 바꾸지 않고 다음 형태의 제안을 제출합니다.

```json
{
  "source_agent": "cs-agent",
  "proposal_type": "support_intake",
  "title": "환불 문의 응대 전 확인 항목",
  "summary": "환불 승인 전에 주문, 상품 상태, 환불 정책을 확인해야 합니다.",
  "payload": {
    "needed_context": ["주문 번호", "스토어 환불 정책"],
    "do_not_auto_handle": ["환불 승인"]
  }
}
```

`POST /inquiries/{id}/agent-proposals`로 제출하면 백엔드가 `target_type`과 `target_id`를 문의에 맞게 붙입니다.

지원하는 agent별 제안 타입은 `GET /agent-proposal-contracts`에서 확인합니다.
