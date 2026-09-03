from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Endpoint2(str, Enum):
    """The endpoint used for this job"""

    SCRAPE = "scrape"
    CRAWL = "crawl"
    BATCH_SCRAPE = "batch_scrape"
    SEARCH = "search"
    EXTRACT = "extract"
    LLMSTXT = "llmstxt"
    DEEP_RESEARCH = "deep_research"
    MAP = "map"
    AGENT = "agent"
    BROWSER = "browser"
    INTERACT = "interact"

    __str__ = str.__str__


Endpoint2OrStr: TypeAlias = Annotated[Endpoint2 | str, open_enum_validator(Endpoint2)]
