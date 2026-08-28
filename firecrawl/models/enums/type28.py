from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type28(str, Enum):
    CRAWL = "crawl"

    __str__ = str.__str__


Type28OrStr: TypeAlias = Annotated[Type28 | str, open_enum_validator(Type28)]
