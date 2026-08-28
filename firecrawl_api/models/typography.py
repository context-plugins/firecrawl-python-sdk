from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .font_families import FontFamilies, FontFamiliesDict
from .font_sizes import FontSizes, FontSizesDict
from .font_weights import FontWeights, FontWeightsDict
from .line_heights import LineHeights, LineHeightsDict


class Typography(SdkBaseModel):
    """Detailed typography information."""

    font_families: Optional[FontFamilies] = Field(default=UNSET, alias="fontFamilies")
    """Font families by role."""

    font_sizes: Optional[FontSizes] = Field(default=UNSET, alias="fontSizes")
    """Font sizes for different text levels."""

    font_weights: Optional[FontWeights] = Field(default=UNSET, alias="fontWeights")
    """Font weight definitions."""

    line_heights: Optional[LineHeights] = Field(default=UNSET, alias="lineHeights")
    """Line height values for different text types."""


class TypographyDict(TypedDict):
    font_families: NotRequired[FontFamilies | FontFamiliesDict]
    font_sizes: NotRequired[FontSizes | FontSizesDict]
    font_weights: NotRequired[FontWeights | FontWeightsDict]
    line_heights: NotRequired[LineHeights | LineHeightsDict]
