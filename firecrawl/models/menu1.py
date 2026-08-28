from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .merchant import Merchant, MerchantDict
from .section import Section, SectionDict


class Menu1(SdkBaseModel):
    """Menu information extracted from the page if ``menu`` is in ``formats``. Includes the merchant, currency, and a
    list of sections, where each section carries items with description, images, price, availability, dietary tags,
    calories, and option groups."""

    is_menu: bool = Field(alias="isMenu")
    """Whether the page was identified as a menu."""

    confidence: Optional[float] = UNSET
    """A confidence score between 0 and 1 for the menu extraction."""

    merchant: Optional[Merchant] = UNSET
    """The merchant the menu belongs to."""

    currency: Optional[str] = UNSET
    """The ISO 4217 currency code for the menu (e.g. 'USD'), reported only when the page sources it."""

    sections: list[Section]
    """Menu sections (e.g. 'Appetizers', 'Entrees')."""

    source_url: OptionalNullable[str] = Field(default=UNSET, alias="sourceUrl")
    """The URL the menu was extracted from."""


class Menu1Dict(TypedDict):
    is_menu: bool
    confidence: NotRequired[float]
    merchant: NotRequired[Merchant | MerchantDict]
    currency: NotRequired[str]
    sections: list[Section | SectionDict]
    source_url: NotRequired[str | None]
