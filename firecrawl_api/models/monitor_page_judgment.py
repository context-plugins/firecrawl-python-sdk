from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.confidence import ConfidenceOrStr
from .meaningful_change import MeaningfulChange, MeaningfulChangeDict


class MonitorPageJudgment(SdkBaseModel):
    meaningful: Optional[bool] = UNSET
    """Whether the changed page is meaningful for the monitor goal."""

    confidence: Optional[ConfidenceOrStr] = UNSET
    reason: Optional[str] = UNSET
    meaningful_changes: Optional[list[MeaningfulChange]] = Field(default=UNSET, alias="meaningfulChanges")
    """Goal-relevant changes selected by the judge from the page diff."""


class MonitorPageJudgmentDict(TypedDict):
    meaningful: NotRequired[bool]
    confidence: NotRequired[ConfidenceOrStr]
    reason: NotRequired[str]
    meaningful_changes: NotRequired[list[MeaningfulChange | MeaningfulChangeDict]]
