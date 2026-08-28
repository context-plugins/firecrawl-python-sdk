from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OriginalPrice(SdkBaseModel):
    """The original (pre-discount) price of the variant."""

    amount: float
    """The numeric price amount."""

    currency: Optional[str] = UNSET
    """The ISO 4217 currency code (e.g. 'USD')."""

    formatted: Optional[str] = UNSET
    """The price formatted for display (e.g. '$249.99')."""


class OriginalPriceDict(TypedDict):
    amount: float
    currency: NotRequired[str]
    formatted: NotRequired[str]
