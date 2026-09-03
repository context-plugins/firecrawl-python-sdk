from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .variant import Variant, VariantDict


class Product1(SdkBaseModel):
    """Product information extracted from the page if ``product`` is in ``formats``. Includes title, brand, category,
    description, and variants. Pricing, availability, and images live on each variant."""

    title: str
    """The product title."""

    brand: Optional[str] = UNSET
    """The product brand or manufacturer."""

    category: Optional[str] = UNSET
    """The product category, optionally as a breadcrumb path (e.g. 'Electronics > Audio > Headphones')."""

    url: str
    """The canonical URL of the product page."""

    description: Optional[str] = UNSET
    """The product description."""

    variants: list[Variant]
    """Product variants (e.g. different colors or sizes)."""


class Product1Dict(TypedDict):
    title: str
    brand: NotRequired[str]
    category: NotRequired[str]
    url: str
    description: NotRequired[str]
    variants: list[Variant | VariantDict]
