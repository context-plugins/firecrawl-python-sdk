from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type24(str, Enum):
    """Scroll the page or a specific element"""

    SCROLL = "scroll"

    __str__ = str.__str__


Type24OrStr: TypeAlias = Annotated[Type24 | str, open_enum_validator(Type24)]
