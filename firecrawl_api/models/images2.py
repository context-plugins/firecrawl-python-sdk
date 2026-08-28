from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Images2(SdkBaseModel):
    """Brand images."""

    logo: Optional[str] = UNSET
    """Logo image URL."""

    favicon: Optional[str] = UNSET
    """Favicon URL."""

    og_image: Optional[str] = Field(default=UNSET, alias="ogImage")
    """Open Graph image URL."""


class Images2Dict(TypedDict):
    logo: NotRequired[str]
    favicon: NotRequired[str]
    og_image: NotRequired[str]
