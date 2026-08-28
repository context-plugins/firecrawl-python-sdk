from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data6 import Data6, Data6Dict


class TeamTokenUsageResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Data6] = UNSET


class TeamTokenUsageResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Data6 | Data6Dict]
