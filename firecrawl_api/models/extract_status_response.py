from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status4 import Status4OrStr


class ExtractStatusResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Any] = UNSET
    status: Optional[Status4OrStr] = UNSET
    """The current status of the extract job"""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    tokens_used: Optional[int] = Field(default=UNSET, alias="tokensUsed")
    """The number of tokens used by the extract job. Only available if the job is completed."""


class ExtractStatusResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Any]
    status: NotRequired[Status4OrStr]
    expires_at: NotRequired[RFC3339DateTime]
    tokens_used: NotRequired[int]
