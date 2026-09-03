from __future__ import annotations

from typing import Any, Literal
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scrape_options import ScrapeOptions, ScrapeOptionsDict


class CrawlTarget(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Optional stable ID for this target. Generated if omitted."""

    type_: Literal["crawl"] = Field(default="crawl", alias="type")
    url: str
    crawl_options: Optional[Any] = Field(default=UNSET, alias="crawlOptions")
    """Crawl options such as ``limit``, ``maxDepth``, ``includePaths``, and ``excludePaths``."""

    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")


class CrawlTargetDict(TypedDict):
    id: NotRequired[UUID]
    type_: NotRequired[Literal["crawl"]]
    url: str
    crawl_options: NotRequired[Any]
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
