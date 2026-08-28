from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode3(str, Enum):
    """URL scanning mode for this request. ``normal`` checks URLs against Google Web Risk (+2 credits per URL
    scanned)."""

    OFF = "off"
    NORMAL = "normal"

    __str__ = str.__str__


Mode3OrStr: TypeAlias = Annotated[Mode3 | str, open_enum_validator(Mode3)]
