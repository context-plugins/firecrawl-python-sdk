from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type42 import Type42OrStr


class News(SdkBaseModel):
    type_: Type42OrStr = Field(alias="type")


class NewsDict(TypedDict):
    type_: Type42OrStr
