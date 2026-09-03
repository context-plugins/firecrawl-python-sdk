from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .monitor import Monitor, MonitorDict


class MonitorListResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[list[Monitor]] = UNSET


class MonitorListResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[list[Monitor | MonitorDict]]
