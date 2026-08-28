from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.status import StatusOrStr
from .monitor_notification import MonitorNotification, MonitorNotificationDict
from .monitor_schedule import MonitorSchedule, MonitorScheduleDict
from .monitor_webhook import MonitorWebhook, MonitorWebhookDict
from .unions.monitor_target import MonitorTarget, MonitorTargetDict


class MonitorUpdateRequest(SdkBaseModel):
    """Partial monitor update payload. Include at least one field."""

    name: Optional[str] = UNSET
    schedule: Optional[MonitorSchedule] = UNSET
    """Schedule for monitor checks. Provide either ``cron`` or ``text``."""

    webhook: Optional[MonitorWebhook] = UNSET
    """Webhook destination for monitor page and check completion events."""

    notification: Optional[MonitorNotification] = UNSET
    targets: Optional[list[MonitorTarget]] = UNSET
    retention_days: Optional[int] = Field(default=UNSET, alias="retentionDays")
    goal: OptionalNullable[str] = UNSET
    """Plain-language goal used to judge whether changed pages are meaningful. If provided and ``judgeEnabled`` is
    omitted, judging is enabled automatically. Required (non-empty) when any target is a ``search`` target, unless
    ``judgeEnabled`` is ``false``."""

    judge_enabled: Optional[bool] = Field(default=UNSET, alias="judgeEnabled")
    """Whether to judge changed pages against ``goal``. Requires a non-empty ``goal`` to run."""

    status: Optional[StatusOrStr] = UNSET


class MonitorUpdateRequestDict(TypedDict):
    name: NotRequired[str]
    schedule: NotRequired[MonitorSchedule | MonitorScheduleDict]
    webhook: NotRequired[MonitorWebhook | MonitorWebhookDict]
    notification: NotRequired[MonitorNotification | MonitorNotificationDict]
    targets: NotRequired[list[MonitorTarget | MonitorTargetDict]]
    retention_days: NotRequired[int]
    goal: NotRequired[str | None]
    judge_enabled: NotRequired[bool]
    status: NotRequired[StatusOrStr]
