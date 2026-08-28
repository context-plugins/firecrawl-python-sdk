from __future__ import annotations

from typing import Any

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event import EventOrStr


class MonitorWebhook(SdkBaseModel):
    """Webhook destination for monitor page and check completion events."""

    url: AnyUrl
    """The URL to send monitor webhooks to."""

    headers: Optional[dict[str, str]] = UNSET
    """Headers to send to the webhook URL."""

    metadata: Optional[Any] = UNSET
    """Custom metadata included in webhook payloads."""

    events: Optional[list[EventOrStr]] = UNSET
    """Monitor webhook events to receive. Defaults to all monitor events."""


class MonitorWebhookDict(TypedDict):
    url: AnyUrl
    headers: NotRequired[dict[str, str]]
    metadata: NotRequired[Any]
    events: NotRequired[list[EventOrStr]]
