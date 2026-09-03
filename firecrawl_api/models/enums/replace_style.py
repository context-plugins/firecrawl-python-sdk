from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReplaceStyle(str, Enum):
    """``tag`` replaces spans with placeholders like ``<EMAIL>``, ``mask`` replaces characters with ``*``, and
    ``remove`` deletes the span text."""

    TAG = "tag"
    MASK = "mask"
    REMOVE = "remove"

    __str__ = str.__str__


ReplaceStyleOrStr: TypeAlias = Annotated[ReplaceStyle | str, open_enum_validator(ReplaceStyle)]
