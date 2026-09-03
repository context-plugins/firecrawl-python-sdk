from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MonitorSchedule(SdkBaseModel):
    """Schedule for monitor checks. Provide either ``cron`` or ``text``."""

    cron: Optional[str] = UNSET
    """Five-field cron expression. Minimum interval is 5 minutes."""

    text: Optional[str] = UNSET
    """Natural language schedule. Supported examples include ``every 30 minutes``, ``every 15 minutes starting at :07``,
    ``hourly``, ``every 2 hours``, ``daily``, ``daily at 9:00``, ``daily at 9am``, ``daily at 5:30 PM``, and
    ``weekly``."""

    timezone: Optional[str] = UNSET
    """IANA timezone for the schedule."""


class MonitorScheduleDict(TypedDict):
    cron: NotRequired[str]
    text: NotRequired[str]
    timezone: NotRequired[str]
