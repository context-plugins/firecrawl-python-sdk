from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FailurePolicy(str, Enum):
    """What to do when the classifier can't be reached: ``closed`` blocks the request, ``open`` allows it."""

    OPEN = "open"
    CLOSED = "closed"

    __str__ = str.__str__


FailurePolicyOrStr: TypeAlias = Annotated[FailurePolicy | str, open_enum_validator(FailurePolicy)]
