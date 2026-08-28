from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .monitor_check import MonitorCheck, MonitorCheckDict


class MonitorRunResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    id: Optional[UUID] = UNSET
    data: Optional[MonitorCheck] = UNSET


class MonitorRunResponseDict(TypedDict):
    success: NotRequired[bool]
    id: NotRequired[UUID]
    data: NotRequired[MonitorCheck | MonitorCheckDict]
