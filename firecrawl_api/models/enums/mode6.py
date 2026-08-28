from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode6(str, Enum):
    """Threat protection mode. ``off`` disables checks; ``normal`` checks URLs against Google Web Risk (+2 credits per
    URL scanned)."""

    OFF = "off"
    NORMAL = "normal"

    __str__ = str.__str__


Mode6OrStr: TypeAlias = Annotated[Mode6 | str, open_enum_validator(Mode6)]
