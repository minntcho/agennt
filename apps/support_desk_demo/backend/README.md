# support_desk_demo backend

프론트엔드가 붙기 전 단계의 작은 고객 문의 API입니다.

이 백엔드는 agent 자체가 아니라 agent가 붙을 자리를 만듭니다. 현재 `POST /inquiries/{id}/intake`는 LLM 호출 없이 deterministic 함수로 `support_intake_brief`를 만듭니다.

## 실행

```bash
python -m apps.support_desk_demo.backend.server
```

기본 주소는 `http://127.0.0.1:8000`입니다.

## API

```text
GET /health
GET /inquiries
GET /inquiries/{id}
POST /inquiries/{id}/intake
```

## 역할

`intake` 결과는 고객에게 바로 답변하지 않습니다. 환불 승인, 보상 약속, 정책 예외 판단도 하지 않습니다.

대신 사람이 응대하기 전에 확인해야 할 정보, 문의 유형, 위험 신호, 다음 확인 작업을 정리합니다.
