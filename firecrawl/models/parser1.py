from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode4 import Mode4OrStr
from .enums.type17 import Type17OrStr


class Parser1(SdkBaseModel):
    type_: Type17OrStr = Field(alias="type")
    mode: Optional[Mode4OrStr] = UNSET
    """PDF parsing mode. "fast": text-only extraction. "auto": text-first with OCR fallback. "ocr": OCR on every
    page."""

    max_pages: Optional[int] = Field(default=UNSET, alias="maxPages")
    """Maximum number of pages to parse from the PDF."""


class Parser1Dict(TypedDict):
    type_: Type17OrStr
    mode: NotRequired[Mode4OrStr]
    max_pages: NotRequired[int]
