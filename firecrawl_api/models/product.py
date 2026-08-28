from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Product(SdkBaseModel):
    type_: Literal["product"] = Field(default="product", alias="type")


class ProductDict(TypedDict):
    type_: NotRequired[Literal["product"]]
