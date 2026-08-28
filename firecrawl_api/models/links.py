from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Links(SdkBaseModel):
    type_: Literal["links"] = Field(default="links", alias="type")


class LinksDict(TypedDict):
    type_: NotRequired[Literal["links"]]
