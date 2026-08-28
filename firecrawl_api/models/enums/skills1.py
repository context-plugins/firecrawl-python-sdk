from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Skills1(str, Enum):
    """Set to ``only`` to limit the search to indexed agent-skill files."""

    ONLY = "only"

    __str__ = str.__str__


Skills1OrStr: TypeAlias = Annotated[Skills1 | str, open_enum_validator(Skills1)]
