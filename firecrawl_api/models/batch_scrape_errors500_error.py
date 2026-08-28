from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BatchScrapeErrors500Error(SdkBaseModel):
    error: Optional[str] = UNSET


class BatchScrapeErrors500ErrorDict(TypedDict):
    error: NotRequired[str]
