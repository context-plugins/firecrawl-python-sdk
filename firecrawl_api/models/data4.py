from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sitemap1 import Sitemap1OrStr


class Data4(SdkBaseModel):
    url: Optional[str] = UNSET
    """The URL to crawl"""

    include_paths: Optional[list[str]] = Field(default=UNSET, alias="includePaths")
    """URL patterns to include"""

    exclude_paths: Optional[list[str]] = Field(default=UNSET, alias="excludePaths")
    """URL patterns to exclude"""

    max_depth: Optional[int] = Field(default=UNSET, alias="maxDepth")
    """Maximum crawl depth"""

    max_discovery_depth: Optional[int] = Field(default=UNSET, alias="maxDiscoveryDepth")
    """Maximum discovery depth"""

    crawl_entire_domain: Optional[bool] = Field(default=UNSET, alias="crawlEntireDomain")
    """Whether to crawl the entire domain"""

    allow_external_links: Optional[bool] = Field(default=UNSET, alias="allowExternalLinks")
    """Whether to allow external links"""

    allow_subdomains: Optional[bool] = Field(default=UNSET, alias="allowSubdomains")
    """Whether to allow subdomains"""

    sitemap: Optional[Sitemap1OrStr] = UNSET
    """Sitemap handling strategy"""

    ignore_query_parameters: Optional[bool] = Field(default=UNSET, alias="ignoreQueryParameters")
    """Whether to ignore query parameters"""

    ignore_robots_txt: Optional[bool] = Field(default=UNSET, alias="ignoreRobotsTxt")
    """Whether robots.txt rules are ignored"""

    robots_user_agent: Optional[str] = Field(default=UNSET, alias="robotsUserAgent")
    """Custom User-Agent string used for robots.txt evaluation"""

    deduplicate_similar_urls: Optional[bool] = Field(default=UNSET, alias="deduplicateSimilarURLs")
    """Whether to deduplicate similar URLs"""

    delay: Optional[float] = UNSET
    """Delay between requests in milliseconds"""

    limit: Optional[int] = UNSET
    """Maximum number of pages to crawl"""


class Data4Dict(TypedDict):
    url: NotRequired[str]
    include_paths: NotRequired[list[str]]
    exclude_paths: NotRequired[list[str]]
    max_depth: NotRequired[int]
    max_discovery_depth: NotRequired[int]
    crawl_entire_domain: NotRequired[bool]
    allow_external_links: NotRequired[bool]
    allow_subdomains: NotRequired[bool]
    sitemap: NotRequired[Sitemap1OrStr]
    ignore_query_parameters: NotRequired[bool]
    ignore_robots_txt: NotRequired[bool]
    robots_user_agent: NotRequired[str]
    deduplicate_similar_urls: NotRequired[bool]
    delay: NotRequired[float]
    limit: NotRequired[int]
