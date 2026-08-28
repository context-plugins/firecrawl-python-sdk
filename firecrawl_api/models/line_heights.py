from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LineHeights(SdkBaseModel):
    """Line height values for different text types."""

    heading: Optional[str] = UNSET
    body: Optional[str] = UNSET


class LineHeightsDict(TypedDict):
    heading: NotRequired[str]
    body: NotRequired[str]
