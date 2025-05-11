from datetime import datetime

from pydantic import BaseModel, Field

class EventBase(BaseModel):
    """이벤트 기본 스키마"""
    title: str = Field(..., description="이벤트 제목", min_length=1, max_length=255)
    organizer: str = Field(..., description="이벤트 주최자", min_length=1, max_length=255)
    month: int = Field(..., description="이벤트 월")
    registration_period: str = Field(..., description="이벤트 등록 기간")
    link: str = Field(..., description="이벤트 링크")
    category_json: list[str] = Field(..., description="이벤트 카테고리")


class EventResponse(EventBase):
    """이벤트 응답 스키마"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 