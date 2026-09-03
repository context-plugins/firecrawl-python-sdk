from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode4 import Mode4OrStr


class Parser1(SdkBaseModel):
    type_: Literal["pdf"] = Field(default="pdf", alias="type")
    mode: Optional[Mode4OrStr] = UNSET
    """PDF parsing mode. "fast": text-only extraction. "auto": text-first with OCR fallback. "ocr": OCR on every
    page."""

    max_pages: Optional[int] = Field(default=UNSET, alias="maxPages")
    """Maximum number of pages to parse from the PDF."""


class Parser1Dict(TypedDict):
    type_: NotRequired[Literal["pdf"]]
    mode: NotRequired[Mode4OrStr]
    max_pages: NotRequired[int]
