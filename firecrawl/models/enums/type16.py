from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type16(str, Enum):
    HIGHLIGHTS = "highlights"

    __str__ = str.__str__


Type16OrStr: TypeAlias = Annotated[Type16 | str, open_enum_validator(Type16)]
