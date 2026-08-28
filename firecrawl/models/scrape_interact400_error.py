from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScrapeInteract400Error(SdkBaseModel):
    success: Optional[bool] = UNSET
    error: Optional[str] = UNSET


class ScrapeInteract400ErrorDict(TypedDict):
    success: NotRequired[bool]
    error: NotRequired[str]
