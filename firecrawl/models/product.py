from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type11 import Type11OrStr


class Product(SdkBaseModel):
    type_: Type11OrStr = Field(alias="type")


class ProductDict(TypedDict):
    type_: Type11OrStr
