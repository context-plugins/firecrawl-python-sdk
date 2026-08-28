from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Proxy1(str, Enum):
    """Proxy mode for parse uploads. ``/parse`` supports only ``basic`` and ``auto``."""

    BASIC = "basic"
    AUTO = "auto"

    __str__ = str.__str__


Proxy1OrStr: TypeAlias = Annotated[Proxy1 | str, open_enum_validator(Proxy1)]
