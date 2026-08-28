from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .session import Session, SessionDict


class InteractResponse1(SdkBaseModel):
    success: Optional[bool] = UNSET
    sessions: Optional[list[Session]] = UNSET


class InteractResponse1Dict(TypedDict):
    success: NotRequired[bool]
    sessions: NotRequired[list[Session | SessionDict]]
