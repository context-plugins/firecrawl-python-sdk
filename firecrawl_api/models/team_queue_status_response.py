from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TeamQueueStatusResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    jobs_in_queue: Optional[float] = Field(default=UNSET, alias="jobsInQueue")
    """Number of jobs currently in your queue"""

    active_jobs_in_queue: Optional[float] = Field(default=UNSET, alias="activeJobsInQueue")
    """Number of jobs currently active"""

    waiting_jobs_in_queue: Optional[float] = Field(default=UNSET, alias="waitingJobsInQueue")
    """Number of jobs currently waiting"""

    max_concurrency: Optional[float] = Field(default=UNSET, alias="maxConcurrency")
    """Maximum number of concurrent active jobs based on your plan"""

    most_recent_success: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="mostRecentSuccess")
    """Timestamp of the most recent successful job"""


class TeamQueueStatusResponseDict(TypedDict):
    success: NotRequired[bool]
    jobs_in_queue: NotRequired[float]
    active_jobs_in_queue: NotRequired[float]
    waiting_jobs_in_queue: NotRequired[float]
    max_concurrency: NotRequired[float]
    most_recent_success: NotRequired[RFC3339DateTime | None]
