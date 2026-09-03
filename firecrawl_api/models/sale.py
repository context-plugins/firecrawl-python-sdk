from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .original_price import OriginalPrice, OriginalPriceDict


class Sale(SdkBaseModel):
    """Sale/discount information for the variant, present when the variant is discounted."""

    original_price: OriginalPrice = Field(alias="originalPrice")
    """The original (pre-discount) price of the variant."""


class SaleDict(TypedDict):
    original_price: OriginalPrice | OriginalPriceDict
