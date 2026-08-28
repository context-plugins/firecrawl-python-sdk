from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FontWeights(SdkBaseModel):
    """Font weight definitions."""

    light: Optional[int] = UNSET
    regular: Optional[int] = UNSET
    medium: Optional[int] = UNSET
    bold: Optional[int] = UNSET


class FontWeightsDict(TypedDict):
    light: NotRequired[int]
    regular: NotRequired[int]
    medium: NotRequired[int]
    bold: NotRequired[int]
