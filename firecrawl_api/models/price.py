from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price(SdkBaseModel):
    """The current price of the variant."""

    amount: float
    """The numeric price amount."""

    currency: Optional[str] = UNSET
    """The ISO 4217 currency code (e.g. 'USD')."""

    formatted: Optional[str] = UNSET
    """The price formatted for display (e.g. '$199.99')."""


class PriceDict(TypedDict):
    amount: float
    currency: NotRequired[str]
    formatted: NotRequired[str]
