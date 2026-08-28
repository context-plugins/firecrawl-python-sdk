from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InteractResponse2(SdkBaseModel):
    success: Optional[bool] = UNSET
    session_duration_ms: Optional[int] = Field(default=UNSET, alias="sessionDurationMs")
    """Total session duration in milliseconds"""

    credits_billed: Optional[float] = Field(default=UNSET, alias="creditsBilled")
    """Number of credits billed for the session"""


class InteractResponse2Dict(TypedDict):
    success: NotRequired[bool]
    session_duration_ms: NotRequired[int]
    credits_billed: NotRequired[float]
