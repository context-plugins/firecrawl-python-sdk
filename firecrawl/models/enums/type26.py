from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type26(str, Enum):
    """Execute JavaScript code on the page"""

    EXECUTE_JAVASCRIPT = "executeJavascript"

    __str__ = str.__str__


Type26OrStr: TypeAlias = Annotated[Type26 | str, open_enum_validator(Type26)]
