from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Availability(SdkBaseModel):
    """The availability of the variant. Always present on a variant."""

    in_stock: bool = Field(alias="inStock")
    """Whether the variant is in stock."""

    text: Optional[str] = UNSET
    """Human-readable availability text (e.g. 'In Stock')."""


class AvailabilityDict(TypedDict):
    in_stock: bool
    text: NotRequired[str]
