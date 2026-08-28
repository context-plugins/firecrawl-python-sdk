from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type29(str, Enum):
    SEARCH = "search"

    __str__ = str.__str__


Type29OrStr: TypeAlias = Annotated[Type29 | str, open_enum_validator(Type29)]
