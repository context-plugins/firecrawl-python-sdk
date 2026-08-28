from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type17(str, Enum):
    PDF = "pdf"

    __str__ = str.__str__


Type17OrStr: TypeAlias = Annotated[Type17 | str, open_enum_validator(Type17)]
