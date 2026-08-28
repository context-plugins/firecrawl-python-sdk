from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type23(str, Enum):
    """Press a key on the page"""

    PRESS = "press"

    __str__ = str.__str__


Type23OrStr: TypeAlias = Annotated[Type23 | str, open_enum_validator(Type23)]
