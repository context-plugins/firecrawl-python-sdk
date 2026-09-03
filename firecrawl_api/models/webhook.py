from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event1 import Event1OrStr


class Webhook(SdkBaseModel):
    """A webhook specification object."""

    url: str
    """The URL to send the webhook to. This will trigger for batch scrape started (batch_scrape.started), every page
    scraped (batch_scrape.page) and when the batch scrape is completed (batch_scrape.completed or batch_scrape.failed).
    The response will be the same as the ``/scrape`` endpoint."""

    headers: Optional[dict[str, str]] = UNSET
    """Headers to send to the webhook URL."""

    metadata: Optional[Any] = UNSET
    """Custom metadata that will be included in all webhook payloads for this crawl"""

    events: Optional[list[Event1OrStr]] = UNSET
    """Type of events that should be sent to the webhook URL. (default: all)"""


class WebhookDict(TypedDict):
    url: str
    headers: NotRequired[dict[str, str]]
    metadata: NotRequired[Any]
    events: NotRequired[list[Event1OrStr]]
