from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Scrape500Error21(SdkBaseModel):
    success: Optional[bool] = UNSET
    error: Optional[str] = UNSET


class Scrape500Error21Dict(TypedDict):
    success: NotRequired[bool]
    error: NotRequired[str]
