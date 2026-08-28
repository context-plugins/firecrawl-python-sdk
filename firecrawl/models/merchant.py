from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Merchant(SdkBaseModel):
    """The merchant the menu belongs to."""

    name: str
    """The merchant name."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The merchant type (e.g. 'restaurant')."""


class MerchantDict(TypedDict):
    name: str
    type_: NotRequired[str]
