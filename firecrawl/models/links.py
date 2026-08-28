from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type5 import Type5OrStr


class Links(SdkBaseModel):
    type_: Type5OrStr = Field(alias="type")


class LinksDict(TypedDict):
    type_: Type5OrStr
