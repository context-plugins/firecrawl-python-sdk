from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type7(str, Enum):
    SCREENSHOT = "screenshot"

    __str__ = str.__str__


Type7OrStr: TypeAlias = Annotated[Type7 | str, open_enum_validator(Type7)]
