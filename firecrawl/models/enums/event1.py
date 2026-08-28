from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Event1(str, Enum):
    COMPLETED = "completed"
    PAGE = "page"
    FAILED = "failed"
    STARTED = "started"

    __str__ = str.__str__


Event1OrStr: TypeAlias = Annotated[Event1 | str, open_enum_validator(Event1)]
