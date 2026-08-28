from __future__ import annotations

from typing import TypeAlias

from ..crawl_target import CrawlTarget, CrawlTargetDict
from ..scrape_target import ScrapeTarget, ScrapeTargetDict
from ..search_target import SearchTarget, SearchTargetDict

MonitorTarget: TypeAlias = ScrapeTarget | CrawlTarget | SearchTarget

MonitorTargetDict: TypeAlias = ScrapeTargetDict | CrawlTargetDict | SearchTargetDict
