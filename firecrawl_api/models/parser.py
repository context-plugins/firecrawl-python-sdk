from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode1 import Mode1OrStr


class Parser(SdkBaseModel):
    type_: Literal["pdf"] = Field(default="pdf", alias="type")
    mode: Optional[Mode1OrStr] = UNSET
    """PDF parsing mode. "fast": text-based extraction only (embedded text, fastest). "auto" (default): attempts fast
    extraction first, falls back to OCR if needed. "ocr": forces OCR parsing on every page."""

    max_pages: Optional[int] = Field(default=UNSET, alias="maxPages")
    """Maximum number of pages to parse from the PDF. Must be a positive integer up to 10000."""


class ParserDict(TypedDict):
    type_: NotRequired[Literal["pdf"]]
    mode: NotRequired[Mode1OrStr]
    max_pages: NotRequired[int]
