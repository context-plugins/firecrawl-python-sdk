from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class News(SdkBaseModel):
    type_: Literal["news"] = Field(default="news", alias="type")


class NewsDict(TypedDict):
    type_: NotRequired[Literal["news"]]
