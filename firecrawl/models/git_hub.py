from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type43 import Type43OrStr


class GitHub(SdkBaseModel):
    type_: Type43OrStr = Field(alias="type")


class GitHubDict(TypedDict):
    type_: Type43OrStr
