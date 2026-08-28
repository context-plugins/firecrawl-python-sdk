from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type40(str, Enum):
    WEB = "web"

    __str__ = str.__str__


Type40OrStr: TypeAlias = Annotated[Type40 | str, open_enum_validator(Type40)]
