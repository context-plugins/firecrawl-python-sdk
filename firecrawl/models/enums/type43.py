from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type43(str, Enum):
    GITHUB = "github"

    __str__ = str.__str__


Type43OrStr: TypeAlias = Annotated[Type43 | str, open_enum_validator(Type43)]
