from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status7 import Status7OrStr


class BatchScrapeResponse(SdkBaseModel):
    status: Optional[Status7OrStr] = UNSET


class BatchScrapeResponseDict(TypedDict):
    status: NotRequired[Status7OrStr]
