from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sitemap2(str, Enum):
    """Sitemap mode when mapping. If you set it to ``skip``, the sitemap won't be used to find URLs. If you set it to
    ``only``, only URLs that are in the sitemap will be returned. By default (``include``), the sitemap and other
    methods will be used together to find URLs."""

    SKIP = "skip"
    INCLUDE = "include"
    ONLY = "only"

    __str__ = str.__str__


Sitemap2OrStr: TypeAlias = Annotated[Sitemap2 | str, open_enum_validator(Sitemap2)]
