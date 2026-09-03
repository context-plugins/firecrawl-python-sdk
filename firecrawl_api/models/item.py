from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .availability1 import Availability1, Availability1Dict
from .identifiers import Identifiers, IdentifiersDict
from .images4 import Images4, Images4Dict
from .price1 import Price1, Price1Dict


class Item(SdkBaseModel):
    id: Optional[str] = UNSET
    """The item identifier."""

    name: str
    """The item name."""

    description: OptionalNullable[str] = UNSET
    """The item description."""

    images: Optional[list[Images4]] = UNSET
    """Item images."""

    price: Optional[Price1] = UNSET
    """The price of the item."""

    availability: Optional[Availability1] = UNSET
    """The availability of the item."""

    dietary: Optional[list[str]] = UNSET
    """Dietary tags for the item (e.g. ['vegetarian'])."""

    calories: OptionalNullable[float] = UNSET
    """The item's calorie count."""

    option_groups: Optional[list[Any]] = Field(default=UNSET, alias="optionGroups")
    """Option/modifier groups for the item."""

    identifiers: Optional[Identifiers] = UNSET
    """Merchant-specific identifiers for the item."""

    url: OptionalNullable[str] = UNSET
    """The canonical URL of the item."""

    source_url: OptionalNullable[str] = Field(default=UNSET, alias="sourceUrl")
    """The URL the item was extracted from."""


class ItemDict(TypedDict):
    id: NotRequired[str]
    name: str
    description: NotRequired[str | None]
    images: NotRequired[list[Images4 | Images4Dict]]
    price: NotRequired[Price1 | Price1Dict]
    availability: NotRequired[Availability1 | Availability1Dict]
    dietary: NotRequired[list[str]]
    calories: NotRequired[float | None]
    option_groups: NotRequired[list[Any]]
    identifiers: NotRequired[Identifiers | IdentifiersDict]
    url: NotRequired[str | None]
    source_url: NotRequired[str | None]
