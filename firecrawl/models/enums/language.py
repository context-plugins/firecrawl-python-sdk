from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Language(str, Enum):
    """Language of the code to execute. Use ``node`` for JavaScript or ``bash`` for agent-browser CLI commands."""

    PYTHON = "python"
    NODE = "node"
    BASH = "bash"

    __str__ = str.__str__


LanguageOrStr: TypeAlias = Annotated[Language | str, open_enum_validator(Language)]
