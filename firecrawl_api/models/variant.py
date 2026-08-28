from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .availability import Availability, AvailabilityDict
from .images3 import Images3, Images3Dict
from .price import Price, PriceDict
from .sale import Sale, SaleDict


class Variant(SdkBaseModel):
    id: Optional[str] = UNSET
    """The variant identifier."""

    sku: Optional[str] = UNSET
    """The variant SKU."""

    title: Optional[str] = UNSET
    """The variant title."""

    values: Optional[dict[str, str]] = UNSET
    """The variant option values (e.g. { "color": "Black" })."""

    price: Optional[Price] = UNSET
    """The current price of the variant."""

    sale: Optional[Sale] = UNSET
    """Sale/discount information for the variant, present when the variant is discounted."""

    availability: Availability
    """The availability of the variant. Always present on a variant."""

    images: Optional[list[Images3]] = UNSET
    """Variant images."""


class VariantDict(TypedDict):
    id: NotRequired[str]
    sku: NotRequired[str]
    title: NotRequired[str]
    values: NotRequired[dict[str, str]]
    price: NotRequired[Price | PriceDict]
    sale: NotRequired[Sale | SaleDict]
    availability: Availability | AvailabilityDict
    images: NotRequired[list[Images3 | Images3Dict]]
