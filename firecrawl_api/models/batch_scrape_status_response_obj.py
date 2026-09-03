from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .data2 import Data2, Data2Dict


class BatchScrapeStatusResponseObj(SdkBaseModel):
    status: Optional[str] = UNSET
    """The current status of the batch scrape. Can be ``scraping``, ``completed``, or ``failed``."""

    total: Optional[int] = UNSET
    """The total number of pages that were attempted to be scraped."""

    completed: Optional[int] = UNSET
    """The number of pages that have been successfully scraped."""

    credits_used: Optional[int] = Field(default=UNSET, alias="creditsUsed")
    """The number of credits used for the batch scrape."""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """The date and time when the batch scrape will expire."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date and time when the batch scrape was started."""

    completed_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="completedAt")
    """The date and time when the batch scrape finished. Present only when the batch scrape is in a terminal state
    (``completed``, ``failed``, or ``cancelled``)."""

    duration: Optional[float] = UNSET
    """Batch scrape duration in seconds. For terminal batch scrapes, this is the elapsed time from ``createdAt`` to
    ``completedAt``. For in-progress batch scrapes, it is the elapsed time from ``createdAt`` to now."""

    next: OptionalNullable[str] = UNSET
    """The URL to retrieve the next 10MB of data. Returned if the batch scrape is not completed or if the response is
    larger than 10MB."""

    data: Optional[list[Data2]] = UNSET
    """The data of the batch scrape."""


class BatchScrapeStatusResponseObjDict(TypedDict):
    status: NotRequired[str]
    total: NotRequired[int]
    completed: NotRequired[int]
    credits_used: NotRequired[int]
    expires_at: NotRequired[RFC3339DateTime]
    created_at: NotRequired[RFC3339DateTime]
    completed_at: NotRequired[RFC3339DateTime]
    duration: NotRequired[float]
    next: NotRequired[str | None]
    data: NotRequired[list[Data2 | Data2Dict]]
