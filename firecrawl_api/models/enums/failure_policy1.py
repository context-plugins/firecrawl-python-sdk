from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FailurePolicy1(str, Enum):
    """Behavior when the classifier is unreachable: ``closed`` blocks (default), ``open`` allows."""

    OPEN = "open"
    CLOSED = "closed"

    __str__ = str.__str__


FailurePolicy1OrStr: TypeAlias = Annotated[FailurePolicy1 | str, open_enum_validator(FailurePolicy1)]
