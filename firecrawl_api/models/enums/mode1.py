from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode1(str, Enum):
    """PDF parsing mode. "fast": text-based extraction only (embedded text, fastest). "auto" (default): attempts fast
    extraction first, falls back to OCR if needed. "ocr": forces OCR parsing on every page."""

    FAST = "fast"
    AUTO = "auto"
    OCR = "ocr"

    __str__ = str.__str__


Mode1OrStr: TypeAlias = Annotated[Mode1 | str, open_enum_validator(Mode1)]
