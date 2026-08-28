from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BatchScrape500Error(SdkBaseModel):
    error: Optional[str] = UNSET


class BatchScrape500ErrorDict(TypedDict):
    error: NotRequired[str]
