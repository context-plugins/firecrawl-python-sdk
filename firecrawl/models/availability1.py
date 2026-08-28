from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Availability1(SdkBaseModel):
    """The availability of the item."""

    in_stock: bool = Field(alias="inStock")
    """Whether the item is available."""

    text: OptionalNullable[str] = UNSET
    """Human-readable availability text."""


class Availability1Dict(TypedDict):
    in_stock: bool
    text: NotRequired[str | None]
