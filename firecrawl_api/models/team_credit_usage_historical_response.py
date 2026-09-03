from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .period import Period, PeriodDict


class TeamCreditUsageHistoricalResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    periods: Optional[list[Period]] = UNSET


class TeamCreditUsageHistoricalResponseDict(TypedDict):
    success: NotRequired[bool]
    periods: NotRequired[list[Period | PeriodDict]]
