from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type21(str, Enum):
    """Click on an element"""

    CLICK = "click"

    __str__ = str.__str__


Type21OrStr: TypeAlias = Annotated[Type21 | str, open_enum_validator(Type21)]
