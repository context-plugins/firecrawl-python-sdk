from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .monitor import Monitor, MonitorDict


class MonitorResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Monitor] = UNSET


class MonitorResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Monitor | MonitorDict]
