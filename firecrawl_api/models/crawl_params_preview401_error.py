from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CrawlParamsPreview401Error(SdkBaseModel):
    success: Optional[bool] = UNSET
    error: Optional[str] = UNSET


class CrawlParamsPreview401ErrorDict(TypedDict):
    success: NotRequired[bool]
    error: NotRequired[str]
