from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sitemap import SitemapOrStr
from .scrape_options import ScrapeOptions, ScrapeOptionsDict
from .webhook1 import Webhook1, Webhook1Dict


class CrawlRequest(SdkBaseModel):
    url: str
    """The base URL to start crawling from"""

    prompt: Optional[str] = UNSET
    """A prompt to use to generate the crawler options (all the parameters below) from natural language. Explicitly set
    parameters will override the generated equivalents."""

    exclude_paths: Optional[list[str]] = Field(default=UNSET, alias="excludePaths")
    """URL pathname regex patterns that exclude matching URLs from the crawl. For example, if you set "excludePaths":
    ["blog/.*"] for the base URL firecrawl.dev, any results matching that pattern will be excluded, such as
    https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap."""

    include_paths: Optional[list[str]] = Field(default=UNSET, alias="includePaths")
    """URL pathname regex patterns that include matching URLs in the crawl. Only the paths that match the specified
    patterns will be included in the response. Note: the starting URL is also checked against these patterns — if it
    does not match, the crawl may return 0 pages. For example, if you set "includePaths": ["blog/.*"] for the base URL
    firecrawl.dev/blog, only pages under /blog/ will be included in the results, such as
    https://www.firecrawl.dev/blog/firecrawl-launch-week-1-recap."""

    max_discovery_depth: Optional[int] = Field(default=UNSET, alias="maxDiscoveryDepth")
    """Maximum depth to crawl based on discovery order. The root site and sitemapped pages has a discovery depth of 0.
    For example, if you set it to 1, and you set ``sitemap: 'skip'``, you will only crawl the entered URL and all URLs
    that are linked on that page."""

    sitemap: Optional[SitemapOrStr] = UNSET
    """Sitemap mode when crawling. If you set it to 'skip', the crawler will ignore the website sitemap and only crawl
    the entered URL and discover pages from there onwards. If you set it to 'only', the crawler will only crawl URLs
    from the sitemap (plus the start URL) and will not discover links from HTML."""

    ignore_query_parameters: Optional[bool] = Field(default=UNSET, alias="ignoreQueryParameters")
    """Do not re-scrape the same path with different (or none) query parameters"""

    regex_on_full_url: Optional[bool] = Field(default=UNSET, alias="regexOnFullURL")
    """When true, includePaths and excludePaths regex patterns are matched against the full URL (including query
    parameters) instead of just the URL pathname. Useful when you need to filter URLs based on query strings."""

    limit: Optional[int] = UNSET
    """Maximum number of pages to crawl. Default limit is 10000."""

    crawl_entire_domain: Optional[bool] = Field(default=UNSET, alias="crawlEntireDomain")
    """Allows the crawler to follow internal links to sibling or parent URLs, not just child paths.

    false: Only crawls deeper (child) URLs. → e.g. /features/feature-1 → /features/feature-1/tips ✅ → Won't follow
    /pricing or / ❌

    true: Crawls any internal links, including siblings and parents. → e.g. /features/feature-1 → /pricing, /, etc. ✅

    Use true for broader internal coverage beyond nested paths."""

    allow_external_links: Optional[bool] = Field(default=UNSET, alias="allowExternalLinks")
    """Allows the crawler to follow links to external websites. External links are followed one hop (the links found on
    those external pages are not crawled). Links pointing to an external site's homepage (a root URL with no path) are
    skipped and reported in Get Crawl Errors with the code EXTERNAL_LINK; redirects to an external homepage are skipped
    for the same reason."""

    allow_subdomains: Optional[bool] = Field(default=UNSET, alias="allowSubdomains")
    """Allows the crawler to follow links to subdomains of the main domain."""

    ignore_robots_txt: Optional[bool] = Field(default=UNSET, alias="ignoreRobotsTxt")
    """Ignore the website's robots.txt rules. Enterprise only — contact support@firecrawl.com to enable."""

    robots_user_agent: Optional[str] = Field(default=UNSET, alias="robotsUserAgent")
    """Custom User-Agent string for robots.txt evaluation. When set, robots.txt is fetched with this User-Agent and
    allow/disallow rules are matched against it instead of the default. Enterprise only — contact support@firecrawl.com
    to enable."""

    delay: Optional[float] = UNSET
    """Delay in seconds between scrapes. This helps respect website rate limits. Setting this forces concurrency to
    1."""

    max_concurrency: Optional[int] = Field(default=UNSET, alias="maxConcurrency")
    """Maximum number of concurrent scrapes. This parameter allows you to set a concurrency limit for this crawl. If not
    specified, the crawl adheres to your team's concurrency limit."""

    webhook: Optional[Webhook1] = UNSET
    """A webhook specification object."""

    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")
    zero_data_retention: Optional[bool] = Field(default=UNSET, alias="zeroDataRetention")
    """If true, this will enable zero data retention for this crawl. To enable this feature, please contact
    help@firecrawl.dev"""


class CrawlRequestDict(TypedDict):
    url: str
    prompt: NotRequired[str]
    exclude_paths: NotRequired[list[str]]
    include_paths: NotRequired[list[str]]
    max_discovery_depth: NotRequired[int]
    sitemap: NotRequired[SitemapOrStr]
    ignore_query_parameters: NotRequired[bool]
    regex_on_full_url: NotRequired[bool]
    limit: NotRequired[int]
    crawl_entire_domain: NotRequired[bool]
    allow_external_links: NotRequired[bool]
    allow_subdomains: NotRequired[bool]
    ignore_robots_txt: NotRequired[bool]
    robots_user_agent: NotRequired[str]
    delay: NotRequired[float]
    max_concurrency: NotRequired[int]
    webhook: NotRequired[Webhook1 | Webhook1Dict]
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
    zero_data_retention: NotRequired[bool]
