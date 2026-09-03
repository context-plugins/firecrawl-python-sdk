from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .crawl import Crawl, CrawlDict


class CrawlActiveResponse(SdkBaseModel):
    success: bool
    crawls: Optional[list[Crawl]] = UNSET


class CrawlActiveResponseDict(TypedDict):
    success: bool
    crawls: NotRequired[list[Crawl | CrawlDict]]
