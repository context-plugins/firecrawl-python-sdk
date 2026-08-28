from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode2(str, Enum):
    """Redaction strategy. ``accurate`` is model-only and optimized for precision, ``aggressive`` increases recall with
    additional heuristics, and ``fast`` uses heuristics without the model call."""

    ACCURATE = "accurate"
    AGGRESSIVE = "aggressive"
    FAST = "fast"

    __str__ = str.__str__


Mode2OrStr: TypeAlias = Annotated[Mode2 | str, open_enum_validator(Mode2)]
