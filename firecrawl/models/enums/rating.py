from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Rating(str, Enum):
    GOOD = "good"
    PARTIAL = "partial"
    BAD = "bad"

    __str__ = str.__str__


RatingOrStr: TypeAlias = Annotated[Rating | str, open_enum_validator(Rating)]
