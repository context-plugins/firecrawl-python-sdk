from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Scrape1(SdkBaseModel):
    url: Optional[str] = UNSET
    html: Optional[str] = UNSET


class Scrape1Dict(TypedDict):
    url: NotRequired[str]
    html: NotRequired[str]
