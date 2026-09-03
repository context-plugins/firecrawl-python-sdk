from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status4(str, Enum):
    """The current status of the extract job"""

    COMPLETED = "completed"
    PROCESSING = "processing"
    FAILED = "failed"
    CANCELLED = "cancelled"

    __str__ = str.__str__


Status4OrStr: TypeAlias = Annotated[Status4 | str, open_enum_validator(Status4)]
