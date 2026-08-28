from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type28 import Type28OrStr
from .scrape_options import ScrapeOptions, ScrapeOptionsDict


class CrawlTarget(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Optional stable ID for this target. Generated if omitted."""

    type_: Type28OrStr = Field(alias="type")
    url: str
    crawl_options: Optional[Any] = Field(default=UNSET, alias="crawlOptions")
    """Crawl options such as ``limit``, ``maxDepth``, ``includePaths``, and ``excludePaths``."""

    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")


class CrawlTargetDict(TypedDict):
    id: NotRequired[UUID]
    type_: Type28OrStr
    url: str
    crawl_options: NotRequired[Any]
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
