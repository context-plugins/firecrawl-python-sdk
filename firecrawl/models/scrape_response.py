from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data1 import Data1, Data1Dict


class ScrapeResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Data1] = UNSET


class ScrapeResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Data1 | Data1Dict]
