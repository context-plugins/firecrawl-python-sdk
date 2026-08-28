from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type18(str, Enum):
    """Wait for a specified amount of milliseconds"""

    WAIT = "wait"

    __str__ = str.__str__


Type18OrStr: TypeAlias = Annotated[Type18 | str, open_enum_validator(Type18)]
