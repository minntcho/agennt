from __future__ import annotations

from typing import Any

Inquiry = dict[str, Any]
IntakeBrief = dict[str, Any]

REFUND_TERMS = ("refund", "return", "exchange", "환불", "반품", "교환")
SHIPPING_TERMS = ("shipping", "delivery", "배송", "택배", "집하", "송장")
REVIEW_TERMS = ("review", "quality", "리뷰", "불만", "하자", "품질")
PRODUCT_TERMS = ("product", "size", "detail", "상품", "사이즈", "상세", "설명")

DEFAULT_DO_NOT_AUTO_HANDLE = [
    "환불 승인",
    "보상 약속",
    "정책 예외 안내",
    "고객에게 확정 답변 발송",
]

NEEDED_CONTEXT_BY_TYPE = {
    "refund_request": [
        "주문 번호",
        "구매 상품명",
        "배송 완료일",
        "반품 가능 기간",
        "상품 사용 여부",
        "스토어 환불 정책",
    ],
    "shipping_issue": [
        "주문 번호",
        "송장 번호",
        "배송사",
        "마지막 배송 상태",
        "예상 배송 지연 공지 여부",
    ],
    "review_complaint": [
        "리뷰 원문",
        "구매 상품명",
        "동일 이슈 반복 여부",
        "상품 상세 페이지 고지 내용",
        "고객에게 추가 확인이 필요한 내용",
    ],
    "product_question": [
        "문의 상품명",
        "상품 상세 페이지 내용",
        "재고 상태",
        "고객이 혼동한 표현",
    ],
    "general_support": [
        "고객 문의 원문",
        "관련 주문 번호",
        "관련 상품명",
        "스토어 정책",
    ],
}


def build_support_intake_brief(inquiry: Inquiry) -> IntakeBrief:
    inquiry_type = classify_inquiry(inquiry)
    risk_flags = detect_risk_flags(inquiry, inquiry_type)

    return {
        "inquiry_id": inquiry.get("id"),
        "inquiry_type": inquiry_type,
        "customer_problem": summarize_customer_problem(inquiry),
        "needed_context": NEEDED_CONTEXT_BY_TYPE[inquiry_type],
        "risk_flags": risk_flags,
        "recommended_next_step": recommend_next_step(inquiry_type, risk_flags),
        "human_review_required": True,
        "do_not_auto_handle": DEFAULT_DO_NOT_AUTO_HANDLE,
        "source": "deterministic-support-intake-v0",
    }


def classify_inquiry(inquiry: Inquiry) -> str:
    text = searchable_text(inquiry)

    if contains_any(text, REFUND_TERMS):
        return "refund_request"
    if contains_any(text, SHIPPING_TERMS):
        return "shipping_issue"
    if contains_any(text, REVIEW_TERMS):
        return "review_complaint"
    if contains_any(text, PRODUCT_TERMS):
        return "product_question"
    return "general_support"


def detect_risk_flags(inquiry: Inquiry, inquiry_type: str) -> list[str]:
    flags: list[str] = []
    text = searchable_text(inquiry)

    if inquiry_type == "refund_request":
        flags.append("환불 정책 확인 필요")
    if "frustrated" in text or "불만" in text or "화" in text:
        flags.append("고객 감정 악화 가능성")
    if "택" in text or "사용" in text:
        flags.append("상품 상태 확인 필요")
    if inquiry_type == "review_complaint":
        flags.append("상품 품질 신호일 수 있음")

    return flags or ["사람 검토 필요"]


def recommend_next_step(inquiry_type: str, risk_flags: list[str]) -> str:
    if inquiry_type == "refund_request":
        return "환불 정책과 상품 상태를 확인한 뒤 사람이 직접 응답합니다."
    if inquiry_type == "shipping_issue":
        return "배송 상태와 지연 공지를 확인한 뒤 예상 안내 문구를 준비합니다."
    if inquiry_type == "review_complaint":
        return "동일 품질 이슈 반복 여부를 확인하고 필요한 경우 상품 담당자가 검토합니다."
    if "고객 감정 악화 가능성" in risk_flags:
        return "고객 감정을 먼저 안정시키는 응답 방향을 사람이 검토합니다."
    return "누락 정보를 확인한 뒤 사람이 응답 방향을 결정합니다."


def summarize_customer_problem(inquiry: Inquiry) -> str:
    subject = str(inquiry.get("subject") or "문의 제목 없음")
    product_name = str(inquiry.get("product_name") or "상품 미확인")
    return f"{product_name}: {subject}"


def searchable_text(inquiry: Inquiry) -> str:
    values = [
        inquiry.get("subject", ""),
        inquiry.get("message", ""),
        inquiry.get("customer_sentiment", ""),
        " ".join(str(tag) for tag in inquiry.get("tags", [])),
    ]
    return " ".join(str(value).lower() for value in values)


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term.lower() in text for term in terms)
