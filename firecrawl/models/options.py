from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scrape_options import ScrapeOptions, ScrapeOptionsDict


class Options(SdkBaseModel):
    """The crawler options used for this crawl"""

    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")


class OptionsDict(TypedDict):
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
