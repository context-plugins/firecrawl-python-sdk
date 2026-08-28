from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode1 import Mode1OrStr
from .enums.type17 import Type17OrStr


class Parser(SdkBaseModel):
    type_: Type17OrStr = Field(alias="type")
    mode: Optional[Mode1OrStr] = UNSET
    """PDF parsing mode. "fast": text-based extraction only (embedded text, fastest). "auto" (default): attempts fast
    extraction first, falls back to OCR if needed. "ocr": forces OCR parsing on every page."""

    max_pages: Optional[int] = Field(default=UNSET, alias="maxPages")
    """Maximum number of pages to parse from the PDF. Must be a positive integer up to 10000."""


class ParserDict(TypedDict):
    type_: Type17OrStr
    mode: NotRequired[Mode1OrStr]
    max_pages: NotRequired[int]
