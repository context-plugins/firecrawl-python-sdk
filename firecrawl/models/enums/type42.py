from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type42(str, Enum):
    NEWS = "news"

    __str__ = str.__str__


Type42OrStr: TypeAlias = Annotated[Type42 | str, open_enum_validator(Type42)]
