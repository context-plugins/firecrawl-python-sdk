from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class RawHtml(SdkBaseModel):
    type_: Literal["rawHtml"] = Field(default="rawHtml", alias="type")


class RawHtmlDict(TypedDict):
    type_: NotRequired[Literal["rawHtml"]]
