from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type17 import Type17OrStr


class Pdf(SdkBaseModel):
    type_: Type17OrStr = Field(alias="type")


class PdfDict(TypedDict):
    type_: Type17OrStr
