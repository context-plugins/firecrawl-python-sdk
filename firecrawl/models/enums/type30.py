from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type30(str, Enum):
    ADDED = "added"
    REMOVED = "removed"
    CHANGED = "changed"

    __str__ = str.__str__


Type30OrStr: TypeAlias = Annotated[Type30 | str, open_enum_validator(Type30)]
