from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .period1 import Period1, Period1Dict


class TeamTokenUsageHistoricalResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    periods: Optional[list[Period1]] = UNSET


class TeamTokenUsageHistoricalResponseDict(TypedDict):
    success: NotRequired[bool]
    periods: NotRequired[list[Period1 | Period1Dict]]
