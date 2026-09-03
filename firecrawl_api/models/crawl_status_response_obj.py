from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .data2 import Data2, Data2Dict


class CrawlStatusResponseObj(SdkBaseModel):
    status: Optional[str] = UNSET
    """The current status of the crawl. Can be ``scraping``, ``completed``, or ``failed``."""

    total: Optional[int] = UNSET
    """The total number of pages that were attempted to be crawled."""

    completed: Optional[int] = UNSET
    """The number of pages that have been successfully crawled."""

    credits_used: Optional[int] = Field(default=UNSET, alias="creditsUsed")
    """The number of credits used for the crawl."""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """The date and time when the crawl will expire."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date and time when the crawl was started."""

    completed_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="completedAt")
    """The date and time when the crawl finished. Present only when the crawl is in a terminal state (``completed``,
    ``failed``, or ``cancelled``)."""

    duration: Optional[float] = UNSET
    """Crawl duration in seconds. For terminal crawls, this is the elapsed time from ``createdAt`` to ``completedAt``.
    For in-progress crawls, it is the elapsed time from ``createdAt`` to now."""

    next: OptionalNullable[str] = UNSET
    """The URL to retrieve the next 10MB of data. Returned if the crawl is not completed or if the response is larger
    than 10MB."""

    data: Optional[list[Data2]] = UNSET
    """The data of the crawl."""


class CrawlStatusResponseObjDict(TypedDict):
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
