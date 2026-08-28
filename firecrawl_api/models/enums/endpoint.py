from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Endpoint(str, Enum):
    SEARCH = "search"
    SCRAPE = "scrape"
    PARSE = "parse"
    MAP = "map"

    __str__ = str.__str__


EndpointOrStr: TypeAlias = Annotated[Endpoint | str, open_enum_validator(Endpoint)]
