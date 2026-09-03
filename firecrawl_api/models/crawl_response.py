from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CrawlResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    id: Optional[str] = UNSET
    url: Optional[str] = UNSET


class CrawlResponseDict(TypedDict):
    success: NotRequired[bool]
    id: NotRequired[str]
    url: NotRequired[str]
