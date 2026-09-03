from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event1 import Event1OrStr


class Webhook1(SdkBaseModel):
    """A webhook specification object."""

    url: str
    """The URL to send the webhook to. This will trigger for crawl started (crawl.started), every page crawled
    (crawl.page) and when the crawl is completed (crawl.completed or crawl.failed). The response will be the same as the
    ``/scrape`` endpoint."""

    headers: Optional[dict[str, str]] = UNSET
    """Headers to send to the webhook URL."""

    metadata: Optional[Any] = UNSET
    """Custom metadata that will be included in all webhook payloads for this crawl"""

    events: Optional[list[Event1OrStr]] = UNSET
    """Type of events that should be sent to the webhook URL. (default: all)"""


class Webhook1Dict(TypedDict):
    url: str
    headers: NotRequired[dict[str, str]]
    metadata: NotRequired[Any]
    events: NotRequired[list[Event1OrStr]]
