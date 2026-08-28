from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AgentResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    id: Optional[UUID] = UNSET


class AgentResponseDict(TypedDict):
    success: NotRequired[bool]
    id: NotRequired[UUID]
