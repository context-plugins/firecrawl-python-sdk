from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CrawlActive429Error(SdkBaseModel):
    success: Optional[bool] = UNSET
    error: Optional[str] = UNSET


class CrawlActive429ErrorDict(TypedDict):
    success: NotRequired[bool]
    error: NotRequired[str]
