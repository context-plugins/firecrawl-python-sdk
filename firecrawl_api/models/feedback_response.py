from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FeedbackResponse(SdkBaseModel):
    success: bool
    feedback_id: UUID = Field(alias="feedbackId")
    credits_refunded: float = Field(alias="creditsRefunded")
    already_submitted: Optional[bool] = Field(default=UNSET, alias="alreadySubmitted")
    daily_cap_reached: Optional[bool] = Field(default=UNSET, alias="dailyCapReached")
    credits_refunded_today: Optional[float] = Field(default=UNSET, alias="creditsRefundedToday")
    daily_refund_cap: Optional[float] = Field(default=UNSET, alias="dailyRefundCap")
    warning: Optional[str] = UNSET


class FeedbackResponseDict(TypedDict):
    success: bool
    feedback_id: UUID
    credits_refunded: float
    already_submitted: NotRequired[bool]
    daily_cap_reached: NotRequired[bool]
    credits_refunded_today: NotRequired[float]
    daily_refund_cap: NotRequired[float]
    warning: NotRequired[str]
