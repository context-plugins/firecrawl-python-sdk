from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type3 import Type3OrStr


class Html(SdkBaseModel):
    type_: Type3OrStr = Field(alias="type")


class HtmlDict(TypedDict):
    type_: Type3OrStr
