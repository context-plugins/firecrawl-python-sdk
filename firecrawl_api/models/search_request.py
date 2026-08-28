from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.enterprise import EnterpriseOrStr
from .scrape_options import ScrapeOptions, ScrapeOptionsDict
from .threat_protection_override import ThreatProtectionOverride, ThreatProtectionOverrideDict
from .unions.category import Category, CategoryDict
from .unions.source1 import Source1, Source1Dict


class SearchRequest(SdkBaseModel):
    query: str
    """The search query"""

    limit: Optional[int] = UNSET
    """Maximum number of results to return (per source type when using multiple sources)"""

    sources: Optional[list[Source1]] = UNSET
    """Sources to search. Will determine the arrays available in the response. Defaults to ['web']."""

    categories: Optional[list[Category]] = UNSET
    """Categories to filter results by. Defaults to [], which means results will not be filtered by any categories."""

    include_domains: Optional[list[str]] = Field(default=UNSET, alias="includeDomains")
    """Restricts search results to the specified domains. Domains should be hostnames only, without protocol or path.
    Cannot be used with excludeDomains."""

    exclude_domains: Optional[list[str]] = Field(default=UNSET, alias="excludeDomains")
    """Excludes search results from the specified domains. Domains should be hostnames only, without protocol or path.
    Cannot be used with includeDomains."""

    tbs: Optional[str] = UNSET
    """Time-based search parameter. Supports predefined time ranges (``qdr:h``, ``qdr:d``, ``qdr:w``, ``qdr:m``,
    ``qdr:y``), custom date ranges (``cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY``), and sort by date (``sbd:1``). Values
    can be combined, e.g. ``sbd:1,qdr:w``."""

    location: Optional[str] = UNSET
    """Location parameter for search results (e.g. ``San Francisco,California,United States``). For best results, set
    both this and the ``country`` parameter."""

    country: Optional[str] = UNSET
    """ISO country code for geo-targeting search results (e.g. ``US``). For best results, set both this and the
    ``location`` parameter."""

    safe: Optional[bool] = UNSET
    """When ``true``, filters explicit content from search results (SafeSearch). Omit to keep the default behavior,
    which does not apply the filter."""

    timeout: Optional[int] = UNSET
    """Timeout in milliseconds"""

    ignore_invalid_urls: Optional[bool] = Field(default=UNSET, alias="ignoreInvalidURLs")
    """Excludes URLs from the search results that are invalid for other Firecrawl endpoints. This helps reduce errors if
    you are piping data from search into other Firecrawl API endpoints."""

    highlights: Optional[bool] = UNSET
    """Generate query-relevant highlights for search results. Set to false to return provider descriptions or snippets
    without highlighting."""

    enterprise: Optional[list[EnterpriseOrStr]] = UNSET
    """Enterprise search options for Zero Data Retention (ZDR). Use ``["zdr"]`` for end-to-end ZDR (10 credits / 10
    results) or ``["anon"]`` for anonymized ZDR (2 credits / 10 results). Must be enabled for your team."""

    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")
    """Options for scraping search results"""

    threat_protection: Optional[ThreatProtectionOverride] = Field(default=UNSET, alias="threatProtection")
    """Per-request `Threat Protection <https://docs.firecrawl.dev/features/threat-protection>`__ override. Fields you
    provide replace the corresponding fields of your organization's policy for this request only; omitted fields keep
    their organization-level values. Requires Threat Protection to be enabled for your team (enterprise feature) —
    otherwise the request is rejected with a 403. If your organization has disabled request overrides, any request that
    includes this object is rejected with a 403. If Threat Protection is enforced for your team, ``mode`` may not be set
    to ``off``."""


class SearchRequestDict(TypedDict):
    query: str
    limit: NotRequired[int]
    sources: NotRequired[list[Source1 | Source1Dict]]
    categories: NotRequired[list[Category | CategoryDict]]
    include_domains: NotRequired[list[str]]
    exclude_domains: NotRequired[list[str]]
    tbs: NotRequired[str]
    location: NotRequired[str]
    country: NotRequired[str]
    safe: NotRequired[bool]
    timeout: NotRequired[int]
    ignore_invalid_urls: NotRequired[bool]
    highlights: NotRequired[bool]
    enterprise: NotRequired[list[EnterpriseOrStr]]
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
    threat_protection: NotRequired[ThreatProtectionOverride | ThreatProtectionOverrideDict]
