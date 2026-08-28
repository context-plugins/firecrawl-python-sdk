from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type44 import Type44OrStr


class Research(SdkBaseModel):
    type_: Type44OrStr = Field(alias="type")


class ResearchDict(TypedDict):
    type_: Type44OrStr
