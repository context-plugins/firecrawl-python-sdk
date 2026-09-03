from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Error(SdkBaseModel):
    id: Optional[str] = UNSET
    timestamp: OptionalNullable[str] = UNSET
    """ISO timestamp of failure"""

    url: Optional[str] = UNSET
    """Scraped URL"""

    error: Optional[str] = UNSET
    """Error message"""


class ErrorDict(TypedDict):
    id: NotRequired[str]
    timestamp: NotRequired[str | None]
    url: NotRequired[str]
    error: NotRequired[str]
