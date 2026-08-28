from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .profile1 import Profile1, Profile1Dict


class InteractRequest(SdkBaseModel):
    ttl: Optional[int] = UNSET
    """Total time-to-live in seconds for the interact session"""

    activity_ttl: Optional[int] = Field(default=UNSET, alias="activityTtl")
    """Time in seconds before the session is destroyed due to inactivity"""

    stream_web_view: Optional[bool] = Field(default=UNSET, alias="streamWebView")
    """Whether to stream a live view of the browser"""

    profile: Optional[Profile1] = UNSET
    """Enable persistent storage across interact sessions. Data saved in one session can be loaded in a later session
    using the same name."""


class InteractRequestDict(TypedDict):
    ttl: NotRequired[int]
    activity_ttl: NotRequired[int]
    stream_web_view: NotRequired[bool]
    profile: NotRequired[Profile1 | Profile1Dict]
