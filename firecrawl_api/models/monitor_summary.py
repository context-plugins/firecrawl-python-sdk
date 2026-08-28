from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MonitorSummary(SdkBaseModel):
    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    same: Optional[int] = UNSET
    changed: Optional[int] = UNSET
    new: Optional[int] = UNSET
    removed: Optional[int] = UNSET
    error: Optional[int] = UNSET


class MonitorSummaryDict(TypedDict):
    total_pages: NotRequired[int]
    same: NotRequired[int]
    changed: NotRequired[int]
    new: NotRequired[int]
    removed: NotRequired[int]
    error: NotRequired[int]
