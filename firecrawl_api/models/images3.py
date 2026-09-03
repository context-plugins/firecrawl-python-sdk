from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Images3(SdkBaseModel):
    url: str
    """Image URL."""

    alt: Optional[str] = UNSET
    """Alternative text for the image."""


class Images3Dict(TypedDict):
    url: str
    alt: NotRequired[str]
