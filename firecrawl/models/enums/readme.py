from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Readme(str, Enum):
    OK = "ok"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"
    SKIPPED = "skipped"

    __str__ = str.__str__


ReadmeOrStr: TypeAlias = Annotated[Readme | str, open_enum_validator(Readme)]
