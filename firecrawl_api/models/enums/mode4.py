from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode4(str, Enum):
    """PDF parsing mode. "fast": text-only extraction. "auto": text-first with OCR fallback. "ocr": OCR on every
    page."""

    FAST = "fast"
    AUTO = "auto"
    OCR = "ocr"

    __str__ = str.__str__


Mode4OrStr: TypeAlias = Annotated[Mode4 | str, open_enum_validator(Mode4)]
