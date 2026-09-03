from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format(str, Enum):
    """The page size of the resulting PDF"""

    A0 = "A0"
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
    LETTER = "Letter"
    LEGAL = "Legal"
    TABLOID = "Tabloid"
    LEDGER = "Ledger"

    __str__ = str.__str__


FormatOrStr: TypeAlias = Annotated[Format | str, open_enum_validator(Format)]
