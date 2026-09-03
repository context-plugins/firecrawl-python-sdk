from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Images4(SdkBaseModel):
    url: str
    """Image URL."""

    alt: OptionalNullable[str] = UNSET
    """Alternative text for the image."""


class Images4Dict(TypedDict):
    url: str
    alt: NotRequired[str | None]
