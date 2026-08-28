from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status10 import Status10OrStr


class Session(SdkBaseModel):
    id: Optional[str] = UNSET
    status: Optional[Status10OrStr] = UNSET
    cdp_url: Optional[str] = Field(default=UNSET, alias="cdpUrl")
    live_view_url: Optional[str] = Field(default=UNSET, alias="liveViewUrl")
    interactive_live_view_url: Optional[str] = Field(default=UNSET, alias="interactiveLiveViewUrl")
    """URL to interact with the interact session in real time (click, type, scroll)"""

    stream_web_view: Optional[bool] = Field(default=UNSET, alias="streamWebView")
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    last_activity: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastActivity")


class SessionDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[Status10OrStr]
    cdp_url: NotRequired[str]
    live_view_url: NotRequired[str]
    interactive_live_view_url: NotRequired[str]
    stream_web_view: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
    last_activity: NotRequired[RFC3339DateTime]
