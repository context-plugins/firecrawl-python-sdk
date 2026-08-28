from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Doc(str, Enum):
    OK = "ok"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"
    SKIPPED = "skipped"

    __str__ = str.__str__


DocOrStr: TypeAlias = Annotated[Doc | str, open_enum_validator(Doc)]
