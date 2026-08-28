from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type25(str, Enum):
    """Scrape the current page content, returns the url and the html."""

    SCRAPE = "scrape"

    __str__ = str.__str__


Type25OrStr: TypeAlias = Annotated[Type25 | str, open_enum_validator(Type25)]
