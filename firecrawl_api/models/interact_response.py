from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class InteractResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    id: Optional[str] = UNSET
    """The unique session identifier"""

    cdp_url: Optional[str] = Field(default=UNSET, alias="cdpUrl")
    """WebSocket URL for Chrome DevTools Protocol access"""

    live_view_url: Optional[str] = Field(default=UNSET, alias="liveViewUrl")
    """URL to view the interact session in real time"""

    interactive_live_view_url: Optional[str] = Field(default=UNSET, alias="interactiveLiveViewUrl")
    """URL to interact with the interact session in real time (click, type, scroll)"""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """When the session will expire based on TTL"""


class InteractResponseDict(TypedDict):
    success: NotRequired[bool]
    id: NotRequired[str]
    cdp_url: NotRequired[str]
    live_view_url: NotRequired[str]
    interactive_live_view_url: NotRequired[str]
    expires_at: NotRequired[RFC3339DateTime]
