from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Schedule(SdkBaseModel):
    cron: Optional[str] = UNSET
    timezone: Optional[str] = UNSET


class ScheduleDict(TypedDict):
    cron: NotRequired[str]
    timezone: NotRequired[str]
