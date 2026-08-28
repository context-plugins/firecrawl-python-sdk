from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type12 import Type12OrStr


class Menu(SdkBaseModel):
    type_: Type12OrStr = Field(alias="type")


class MenuDict(TypedDict):
    type_: Type12OrStr
