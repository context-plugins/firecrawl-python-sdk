from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .monitor_check import MonitorCheck, MonitorCheckDict


class MonitorCheckListResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[list[MonitorCheck]] = UNSET


class MonitorCheckListResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[list[MonitorCheck | MonitorCheckDict]]
