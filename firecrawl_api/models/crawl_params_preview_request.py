from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CrawlParamsPreviewRequest(SdkBaseModel):
    url: str
    """The URL to crawl"""

    prompt: str
    """Natural language prompt describing what you want to crawl"""


class CrawlParamsPreviewRequestDict(TypedDict):
    url: str
    prompt: str
