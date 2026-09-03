from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Proxy(str, Enum):
    """Specifies the type of proxy to use.

     - **basic**: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
     - **enhanced**: Enhanced proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on
            certain sites. Billed at the same credit cost as basic.
     - **auto**: Firecrawl will automatically retry scraping with enhanced proxies if the basic proxy fails. Enhanced
            proxies carry no credit surcharge, so either way only the regular cost is billed."""

    BASIC = "basic"
    ENHANCED = "enhanced"
    AUTO = "auto"

    __str__ = str.__str__


ProxyOrStr: TypeAlias = Annotated[Proxy | str, open_enum_validator(Proxy)]
