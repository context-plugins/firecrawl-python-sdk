from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SearchWindow(str, Enum):
    """Recency filter — only consider results published within this window."""

    _5M = "5m"
    _15M = "15m"
    _1H = "1h"
    _6H = "6h"
    _24H = "24h"
    _7D = "7d"

    __str__ = str.__str__


SearchWindowOrStr: TypeAlias = Annotated[SearchWindow | str, open_enum_validator(SearchWindow)]
