from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FeedbackErrorResponse(SdkBaseModel):
    success: bool
    error: str
    feedback_error_code: Optional[str] = Field(default=UNSET, alias="feedbackErrorCode")
    details: Optional[list[Any]] = UNSET


class FeedbackErrorResponseDict(TypedDict):
    success: bool
    error: str
    feedback_error_code: NotRequired[str]
    details: NotRequired[list[Any]]
