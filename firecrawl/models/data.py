from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.status2 import Status2OrStr
from .enums.trigger import TriggerOrStr
from .monitor_check_page import MonitorCheckPage, MonitorCheckPageDict
from .monitor_summary import MonitorSummary, MonitorSummaryDict


class Data(SdkBaseModel):
    id: Optional[UUID] = UNSET
    monitor_id: Optional[UUID] = Field(default=UNSET, alias="monitorId")
    status: Optional[Status2OrStr] = UNSET
    trigger: Optional[TriggerOrStr] = UNSET
    scheduled_for: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="scheduledFor")
    started_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="startedAt")
    finished_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="finishedAt")
    estimated_credits: OptionalNullable[int] = Field(default=UNSET, alias="estimatedCredits")
    """Upper-bound credits reserved for this check before Firecrawl knows how many pages changed and require judging."""

    reserved_credits: OptionalNullable[int] = Field(default=UNSET, alias="reservedCredits")
    actual_credits: OptionalNullable[int] = Field(default=UNSET, alias="actualCredits")
    """Final credits charged for this check after scrapes, crawls, and any changed-page judge calls complete."""

    billing_status: Optional[str] = Field(default=UNSET, alias="billingStatus")
    summary: Optional[MonitorSummary] = UNSET
    target_results: OptionalNullable[str] = Field(default=UNSET, alias="targetResults")
    notification_status: OptionalNullable[Any] = Field(default=UNSET, alias="notificationStatus")
    error: OptionalNullable[str] = UNSET
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    pages: Optional[list[MonitorCheckPage]] = UNSET
    next: OptionalNullable[str] = UNSET
    """URL to fetch the next page of monitor check page results, if any."""


class DataDict(TypedDict):
    id: NotRequired[UUID]
    monitor_id: NotRequired[UUID]
    status: NotRequired[Status2OrStr]
    trigger: NotRequired[TriggerOrStr]
    scheduled_for: NotRequired[RFC3339DateTime | None]
    started_at: NotRequired[RFC3339DateTime | None]
    finished_at: NotRequired[RFC3339DateTime | None]
    estimated_credits: NotRequired[int | None]
    reserved_credits: NotRequired[int | None]
    actual_credits: NotRequired[int | None]
    billing_status: NotRequired[str]
    summary: NotRequired[MonitorSummary | MonitorSummaryDict]
    target_results: NotRequired[str | None]
    notification_status: NotRequired[Any | None]
    error: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    pages: NotRequired[list[MonitorCheckPage | MonitorCheckPageDict]]
    next: NotRequired[str | None]
