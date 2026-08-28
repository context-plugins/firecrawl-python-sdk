from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sitemap(str, Enum):
    """Sitemap mode when crawling. If you set it to 'skip', the crawler will ignore the website sitemap and only crawl
    the entered URL and discover pages from there onwards. If you set it to 'only', the crawler will only crawl URLs
    from the sitemap (plus the start URL) and will not discover links from HTML."""

    SKIP = "skip"
    INCLUDE = "include"
    ONLY = "only"

    __str__ = str.__str__


SitemapOrStr: TypeAlias = Annotated[Sitemap | str, open_enum_validator(Sitemap)]
