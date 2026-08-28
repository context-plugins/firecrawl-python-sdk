from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.model1 import Model1OrStr
from .enums.status9 import Status9OrStr


class AgentResponse1(SdkBaseModel):
    success: Optional[bool] = UNSET
    status: Optional[Status9OrStr] = UNSET
    data: Optional[Any] = UNSET
    """The extracted data (only present when status is completed)"""

    model: Optional[Model1OrStr] = UNSET
    """Model preset used for the agent run"""

    error: Optional[str] = UNSET
    """Error message (only present when status is failed)"""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    credits_used: Optional[float] = Field(default=UNSET, alias="creditsUsed")


class AgentResponse1Dict(TypedDict):
    success: NotRequired[bool]
    status: NotRequired[Status9OrStr]
    data: NotRequired[Any]
    model: NotRequired[Model1OrStr]
    error: NotRequired[str]
    expires_at: NotRequired[RFC3339DateTime]
    credits_used: NotRequired[float]
