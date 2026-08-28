from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BatchScrape402Error1(SdkBaseModel):
    error: Optional[str] = UNSET


class BatchScrape402Error1Dict(TypedDict):
    error: NotRequired[str]
