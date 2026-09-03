from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class CrawlErrorsResponseObj(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Errored scrape jobs and error details"""

    robots_blocked: Optional[list[str]] = Field(default=UNSET, alias="robotsBlocked")
    """List of URLs that were attempted in scraping but were blocked by robots.txt"""


class CrawlErrorsResponseObjDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    robots_blocked: NotRequired[list[str]]
