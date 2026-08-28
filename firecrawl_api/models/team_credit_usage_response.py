from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data5 import Data5, Data5Dict


class TeamCreditUsageResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Data5] = UNSET


class TeamCreditUsageResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Data5 | Data5Dict]
