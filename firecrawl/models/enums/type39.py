from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type39(str, Enum):
    """Result kind."""

    DOC = "doc"
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"
    README = "readme"

    __str__ = str.__str__


Type39OrStr: TypeAlias = Annotated[Type39 | str, open_enum_validator(Type39)]
