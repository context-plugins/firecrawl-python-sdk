from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Crawl500Error1(SdkBaseModel):
    error: Optional[str] = UNSET


class Crawl500Error1Dict(TypedDict):
    error: NotRequired[str]
