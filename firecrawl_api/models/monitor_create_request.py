from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .monitor_notification import MonitorNotification, MonitorNotificationDict
from .monitor_schedule import MonitorSchedule, MonitorScheduleDict
from .monitor_webhook import MonitorWebhook, MonitorWebhookDict
from .unions.monitor_target import MonitorTarget, MonitorTargetDict


class MonitorCreateRequest(SdkBaseModel):
    name: str
    schedule: MonitorSchedule
    """Schedule for monitor checks. Provide either ``cron`` or ``text``."""

    webhook: Optional[MonitorWebhook] = UNSET
    """Webhook destination for monitor page and check completion events."""

    notification: Optional[MonitorNotification] = UNSET
    targets: list[MonitorTarget]
    retention_days: Optional[int] = Field(default=UNSET, alias="retentionDays")
    goal: OptionalNullable[str] = UNSET
    """Plain-language goal used to judge whether changed pages are meaningful. If provided and ``judgeEnabled`` is
    omitted, judging is enabled automatically. Required (non-empty) when any target is a ``search`` target, unless
    ``judgeEnabled`` is ``false``."""

    judge_enabled: Optional[bool] = Field(default=UNSET, alias="judgeEnabled")
    """Whether to judge changed pages against ``goal``. Requires a non-empty ``goal`` to run."""


class MonitorCreateRequestDict(TypedDict):
    name: str
    schedule: MonitorSchedule | MonitorScheduleDict
    webhook: NotRequired[MonitorWebhook | MonitorWebhookDict]
    notification: NotRequired[MonitorNotification | MonitorNotificationDict]
    targets: list[MonitorTarget | MonitorTargetDict]
    retention_days: NotRequired[int]
    goal: NotRequired[str | None]
    judge_enabled: NotRequired[bool]
