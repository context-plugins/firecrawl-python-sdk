from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type2 import Type2OrStr


class Summary(SdkBaseModel):
    type_: Type2OrStr = Field(alias="type")


class SummaryDict(TypedDict):
    type_: Type2OrStr
