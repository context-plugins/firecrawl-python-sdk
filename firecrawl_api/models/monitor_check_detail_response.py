from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .data import Data, DataDict


class MonitorCheckDetailResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    next: OptionalNullable[str] = UNSET
    """URL to fetch the next page of monitor check page results, if any."""

    data: Optional[Data] = UNSET


class MonitorCheckDetailResponseDict(TypedDict):
    success: NotRequired[bool]
    next: NotRequired[str | None]
    data: NotRequired[Data | DataDict]
