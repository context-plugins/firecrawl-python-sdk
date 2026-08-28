from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type4 import Type4OrStr


class RawHtml(SdkBaseModel):
    type_: Type4OrStr = Field(alias="type")


class RawHtmlDict(TypedDict):
    type_: Type4OrStr
