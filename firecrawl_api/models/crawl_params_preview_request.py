from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CrawlParamsPreviewRequest(SdkBaseModel):
    url: AnyUrl
    """The URL to crawl"""

    prompt: str
    """Natural language prompt describing what you want to crawl"""


class CrawlParamsPreviewRequestDict(TypedDict):
    url: AnyUrl
    prompt: str
