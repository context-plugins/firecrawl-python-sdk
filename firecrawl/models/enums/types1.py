from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Types1(str, Enum):
    DOC = "doc"
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"
    README = "readme"

    __str__ = str.__str__


Types1OrStr: TypeAlias = Annotated[Types1 | str, open_enum_validator(Types1)]
