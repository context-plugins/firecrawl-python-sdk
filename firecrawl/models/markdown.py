from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr


class Markdown(SdkBaseModel):
    type_: Type1OrStr = Field(alias="type")


class MarkdownDict(TypedDict):
    type_: Type1OrStr
