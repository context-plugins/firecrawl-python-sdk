from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Identifiers(SdkBaseModel):
    """Merchant-specific identifiers for the item."""

    merchant_item_id: Optional[str] = Field(default=UNSET, alias="merchantItemId")
    """The merchant's own item ID."""


class IdentifiersDict(TypedDict):
    merchant_item_id: NotRequired[str]
