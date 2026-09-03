from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FontFamilies(SdkBaseModel):
    """Font families by role."""

    primary: Optional[str] = UNSET
    """Primary font family."""

    heading: Optional[str] = UNSET
    """Heading font family."""

    code: Optional[str] = UNSET
    """Code/monospace font family."""


class FontFamiliesDict(TypedDict):
    primary: NotRequired[str]
    heading: NotRequired[str]
    code: NotRequired[str]
