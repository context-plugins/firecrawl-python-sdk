from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data4 import Data4, Data4Dict


class CrawlParamsPreviewResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Data4] = UNSET


class CrawlParamsPreviewResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Data4 | Data4Dict]
