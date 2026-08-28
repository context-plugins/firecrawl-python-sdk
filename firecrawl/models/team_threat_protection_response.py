from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data9 import Data9, Data9Dict


class TeamThreatProtectionResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Data9] = UNSET


class TeamThreatProtectionResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Data9 | Data9Dict]
