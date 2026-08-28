from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type20(str, Enum):
    """Take a screenshot. The links will be in the response's ``actions.screenshots`` array."""

    SCREENSHOT = "screenshot"

    __str__ = str.__str__


Type20OrStr: TypeAlias = Annotated[Type20 | str, open_enum_validator(Type20)]
