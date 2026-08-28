from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.status1 import Status1OrStr
from .monitor_notification import MonitorNotification, MonitorNotificationDict
from .monitor_summary import MonitorSummary, MonitorSummaryDict
from .monitor_webhook import MonitorWebhook, MonitorWebhookDict
from .schedule import Schedule, ScheduleDict
from .unions.monitor_target import MonitorTarget, MonitorTargetDict


class Monitor(SdkBaseModel):
    id: Optional[UUID] = UNSET
    name: Optional[str] = UNSET
    status: Optional[Status1OrStr] = UNSET
    schedule: Optional[Schedule] = UNSET
    next_run_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="nextRunAt")
    last_run_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="lastRunAt")
    current_check_id: OptionalNullable[UUID] = Field(default=UNSET, alias="currentCheckId")
    targets: Optional[list[MonitorTarget]] = UNSET
    webhook: Optional[MonitorWebhook] = UNSET
    """Webhook destination for monitor page and check completion events."""

    notification: Optional[MonitorNotification] = UNSET
    retention_days: Optional[int] = Field(default=UNSET, alias="retentionDays")
    estimated_credits_per_month: OptionalNullable[int] = Field(default=UNSET, alias="estimatedCreditsPerMonth")
    """Upper-bound monthly credit estimate. When judging is enabled, actual usage may be lower because judge credits are
    only charged for changed pages that are judged."""

    last_check_summary: Optional[MonitorSummary] = Field(default=UNSET, alias="lastCheckSummary")
    goal: OptionalNullable[str] = UNSET
    judge_enabled: Optional[bool] = Field(default=UNSET, alias="judgeEnabled")
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")


class MonitorDict(TypedDict):
    id: NotRequired[UUID]
    name: NotRequired[str]
    status: NotRequired[Status1OrStr]
    schedule: NotRequired[Schedule | ScheduleDict]
    next_run_at: NotRequired[RFC3339DateTime | None]
    last_run_at: NotRequired[RFC3339DateTime | None]
    current_check_id: NotRequired[UUID | None]
    targets: NotRequired[list[MonitorTarget | MonitorTargetDict]]
    webhook: NotRequired[MonitorWebhook | MonitorWebhookDict]
    notification: NotRequired[MonitorNotification | MonitorNotificationDict]
    retention_days: NotRequired[int]
    estimated_credits_per_month: NotRequired[int | None]
    last_check_summary: NotRequired[MonitorSummary | MonitorSummaryDict]
    goal: NotRequired[str | None]
    judge_enabled: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
