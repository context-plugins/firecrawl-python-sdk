from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Markdown(SdkBaseModel):
    type_: Literal["markdown"] = Field(default="markdown", alias="type")


class MarkdownDict(TypedDict):
    type_: NotRequired[Literal["markdown"]]
