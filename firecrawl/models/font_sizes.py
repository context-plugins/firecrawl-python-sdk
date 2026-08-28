from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FontSizes(SdkBaseModel):
    """Font sizes for different text levels."""

    h1: Optional[str] = UNSET
    h2: Optional[str] = UNSET
    h3: Optional[str] = UNSET
    body: Optional[str] = UNSET


class FontSizesDict(TypedDict):
    h1: NotRequired[str]
    h2: NotRequired[str]
    h3: NotRequired[str]
    body: NotRequired[str]
