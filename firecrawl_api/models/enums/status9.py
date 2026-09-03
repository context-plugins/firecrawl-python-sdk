from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status9(str, Enum):
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    __str__ = str.__str__


Status9OrStr: TypeAlias = Annotated[Status9 | str, open_enum_validator(Status9)]
