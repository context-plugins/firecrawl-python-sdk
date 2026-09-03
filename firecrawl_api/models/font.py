from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Font(SdkBaseModel):
    family: Optional[str] = UNSET
    """Font family name."""


class FontDict(TypedDict):
    family: NotRequired[str]
