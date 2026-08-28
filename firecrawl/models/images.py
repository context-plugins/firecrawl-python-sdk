from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type6 import Type6OrStr


class Images(SdkBaseModel):
    type_: Type6OrStr = Field(alias="type")


class ImagesDict(TypedDict):
    type_: Type6OrStr
