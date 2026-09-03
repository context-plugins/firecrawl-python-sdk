from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Event(str, Enum):
    MONITOR_PAGE = "monitor.page"
    MONITOR_CHECK_COMPLETED = "monitor.check.completed"

    __str__ = str.__str__


EventOrStr: TypeAlias = Annotated[Event | str, open_enum_validator(Event)]
