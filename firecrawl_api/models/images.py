from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Images(SdkBaseModel):
    type_: Literal["images"] = Field(default="images", alias="type")


class ImagesDict(TypedDict):
    type_: NotRequired[Literal["images"]]
