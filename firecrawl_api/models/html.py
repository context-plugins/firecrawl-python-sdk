from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Html(SdkBaseModel):
    type_: Literal["html"] = Field(default="html", alias="type")


class HtmlDict(TypedDict):
    type_: NotRequired[Literal["html"]]
