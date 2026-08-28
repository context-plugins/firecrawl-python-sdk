from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Pdf(SdkBaseModel):
    type_: Literal["pdf"] = Field(default="pdf", alias="type")


class PdfDict(TypedDict):
    type_: NotRequired[Literal["pdf"]]
