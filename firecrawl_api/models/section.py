from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .item import Item, ItemDict


class Section(SdkBaseModel):
    id: Optional[str] = UNSET
    """The section identifier."""

    name: str
    """The section name."""

    description: OptionalNullable[str] = UNSET
    """The section description."""

    items: list[Item]
    """The items in the section."""


class SectionDict(TypedDict):
    id: NotRequired[str]
    name: str
    description: NotRequired[str | None]
    items: list[Item | ItemDict]
