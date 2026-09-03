from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status3(str, Enum):
    SAME = "same"
    NEW = "new"
    CHANGED = "changed"
    REMOVED = "removed"
    ERROR = "error"

    __str__ = str.__str__


Status3OrStr: TypeAlias = Annotated[Status3 | str, open_enum_validator(Status3)]
