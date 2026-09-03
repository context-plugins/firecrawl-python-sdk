from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Menu(SdkBaseModel):
    type_: Literal["menu"] = Field(default="menu", alias="type")


class MenuDict(TypedDict):
    type_: NotRequired[Literal["menu"]]
