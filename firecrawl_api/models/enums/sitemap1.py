from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sitemap1(str, Enum):
    """Sitemap handling strategy"""

    SKIP = "skip"
    INCLUDE = "include"

    __str__ = str.__str__


Sitemap1OrStr: TypeAlias = Annotated[Sitemap1 | str, open_enum_validator(Sitemap1)]
