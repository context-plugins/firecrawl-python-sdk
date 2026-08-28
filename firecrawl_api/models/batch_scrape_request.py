from __future__ import annotations

from typing import Any

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audit_metadata import AuditMetadata, AuditMetadataDict
from .enums.format import FormatOrStr
from .enums.proxy import ProxyOrStr
from .location import Location, LocationDict
from .parser import Parser, ParserDict
from .profile import Profile, ProfileDict
from .threat_protection_override import ThreatProtectionOverride, ThreatProtectionOverrideDict
from .unions.action import Action, ActionDict
from .unions.redact_pii import RedactPii, RedactPiiDict
from .webhook import Webhook, WebhookDict


class BatchScrapeRequest(SdkBaseModel):
    urls: list[AnyUrl]
    webhook: Optional[Webhook] = UNSET
    """A webhook specification object."""

    max_concurrency: Optional[int] = Field(default=UNSET, alias="maxConcurrency")
    """Maximum number of concurrent scrapes. This parameter allows you to set a concurrency limit for this batch scrape.
    If not specified, the batch scrape adheres to your team's concurrency limit."""

    ignore_invalid_urls: Optional[bool] = Field(default=UNSET, alias="ignoreInvalidURLs")
    """If invalid URLs are specified in the urls array, they will be ignored. Instead of them failing the entire
    request, a batch scrape using the remaining valid URLs will be created, and the invalid URLs will be returned in the
    invalidURLs field of the response."""

    formats: Optional[list[FormatOrStr]] = UNSET
    """Output formats to include in the response. You can specify one or more formats, either as strings (e.g.,
    ``'markdown'``) or as objects with additional options (e.g., ``{ type: 'json', schema: {...} }``). Some formats
    require specific options to be set. Example: ``['markdown', { type: 'json', schema: {...} }]``."""

    only_main_content: Optional[bool] = Field(default=UNSET, alias="onlyMainContent")
    """Only return the main content of the page excluding headers, navs, footers, etc. This is a deterministic
    HTML-level filter applied before markdown is generated; no LLM is involved."""

    only_clean_content: Optional[bool] = Field(default=UNSET, alias="onlyCleanContent")
    """Beta. Run an additional LLM-based pass over the generated markdown to remove residual boilerplate that
    ``onlyMainContent`` can miss (cookie banners, ad blocks, social share widgets, breadcrumbs, newsletter signups,
    comment sections, related-article lists). Headings, lists, tables, code blocks, image references, and inline links
    are preserved. Can be combined with ``onlyMainContent`` (the most common setup) or used on its own. Skipped with a
    warning when the markdown exceeds the cleaning model's output token limit (the original markdown is preserved). Not
    supported on zero-data-retention requests."""

    include_tags: Optional[list[str]] = Field(default=UNSET, alias="includeTags")
    """Tags to include in the output."""

    exclude_tags: Optional[list[str]] = Field(default=UNSET, alias="excludeTags")
    """Tags to exclude from the output."""

    max_age: Optional[int] = Field(default=UNSET, alias="maxAge")
    """Returns a cached version of the page if it is younger than this age in milliseconds. If a cached version of the
    page is older than this value, the page will be scraped. If you do not need extremely fresh data, enabling this can
    speed up your scrapes by 500%. Defaults to 2 days."""

    min_age: Optional[int] = Field(default=UNSET, alias="minAge")
    """When set, the request only checks the cache and never triggers a fresh scrape. The value is in milliseconds and
    specifies the minimum age the cached data must be. If matching cached data exists, it is returned instantly. If no
    cached data is found, a 404 with error code SCRAPE_NO_CACHED_DATA is returned. Set to 1 to accept any cached data
    regardless of age."""

    headers: Optional[Any] = UNSET
    """Headers to send with the request. Can be used to send cookies, user-agent, etc."""

    wait_for: Optional[int] = Field(default=UNSET, alias="waitFor")
    """Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load. This
    waiting time is in addition to Firecrawl's smart wait feature."""

    mobile: Optional[bool] = UNSET
    """Set to true if you want to emulate scraping from a mobile device. Useful for testing responsive pages and taking
    mobile screenshots."""

    skip_tls_verification: Optional[bool] = Field(default=UNSET, alias="skipTlsVerification")
    """Skip TLS certificate verification when making requests."""

    timeout: Optional[int] = UNSET
    """Timeout in milliseconds for the request. Minimum is 1000 (1 second). Default is 60000 (60 seconds). Maximum is
    300000 (300 seconds)."""

    parsers: Optional[list[Parser]] = UNSET
    """Controls how files are processed during scraping. When "pdf" is included (default), the PDF content is extracted
    and converted to markdown format, with billing based on the number of pages (1 credit per page). When an empty array
    is passed, the PDF file is returned in base64 encoding with a flat rate of 1 credit for the entire PDF."""

    actions: Optional[list[Action]] = UNSET
    """Actions to perform on the page before grabbing the content"""

    location: Optional[Location] = UNSET
    """Location settings for the request. When specified, this will use an appropriate proxy if available and emulate
    the corresponding language and timezone settings. Defaults to 'US' if not specified."""

    remove_base64_images: Optional[bool] = Field(default=UNSET, alias="removeBase64Images")
    """Removes all base 64 images from the markdown output, which may be overwhelmingly long. This does not affect html
    or rawHtml formats. The image's alt text remains in the output, but the URL is replaced with a placeholder."""

    block_ads: Optional[bool] = Field(default=UNSET, alias="blockAds")
    """Enables ad-blocking and cookie popup blocking."""

    proxy: Optional[ProxyOrStr] = UNSET
    """Specifies the type of proxy to use.

     - **basic**: Proxies for scraping sites with none to basic anti-bot solutions. Fast and usually works.
     - **enhanced**: Enhanced proxies for scraping sites with advanced anti-bot solutions. Slower, but more reliable on
            certain sites. Billed at the same credit cost as basic.
     - **auto**: Firecrawl will automatically retry scraping with enhanced proxies if the basic proxy fails. Enhanced
            proxies carry no credit surcharge, so either way only the regular cost is billed."""

    store_in_cache: Optional[bool] = Field(default=UNSET, alias="storeInCache")
    """If true, the page will be stored in the Firecrawl index and cache. Setting this to false is useful if your
    scraping activity may have data protection concerns. Using some parameters associated with sensitive scraping (e.g.
    actions, headers) will force this parameter to be false."""

    lockdown: Optional[bool] = UNSET
    """If true, serves the request from Firecrawl's cache only and never makes an outbound request to the target URL.
    Designed for compliance-constrained or air-gapped environments where the scrape request itself could leak sensitive
    information. On cache miss, returns a 404 with error code SCRAPE_LOCKDOWN_CACHE_MISS (the URL is never logged on
    miss). Lockdown requests are treated as zero data retention. Default maxAge is extended to 2 years so existing
    cached pages remain eligible. Billed at 5 credits on hit, 1 credit on cache miss."""

    redact_pii: Optional[RedactPii] = Field(default=UNSET, alias="redactPII")
    """Redact personally identifiable information from returned markdown. Pass ``true`` to use defaults, or an object to
    tune mode, entities, and replacement style."""

    profile: Optional[Profile] = UNSET
    """Enable persistent browser storage across scrape and interact sessions. Pass a profile when scraping to preserve
    cookies, localStorage, and session data. Sessions with the same profile name share browser state."""

    threat_protection: Optional[ThreatProtectionOverride] = Field(default=UNSET, alias="threatProtection")
    """Per-request `Threat Protection <https://docs.firecrawl.dev/features/threat-protection>`__ override. Fields you
    provide replace the corresponding fields of your organization's policy for this request only; omitted fields keep
    their organization-level values. Requires Threat Protection to be enabled for your team (enterprise feature) —
    otherwise the request is rejected with a 403. If your organization has disabled request overrides, any request that
    includes this object is rejected with a 403. If Threat Protection is enforced for your team, ``mode`` may not be set
    to ``off``."""

    audit_metadata: Optional[AuditMetadata] = Field(default=UNSET, alias="auditMetadata")
    """User attribution included with SIEM logging events when SIEM Logging is enabled for the organization."""

    zero_data_retention: Optional[bool] = Field(default=UNSET, alias="zeroDataRetention")
    """If true, this will enable zero data retention for this batch scrape. To enable this feature, please contact
    help@firecrawl.dev"""


class BatchScrapeRequestDict(TypedDict):
    urls: list[AnyUrl]
    webhook: NotRequired[Webhook | WebhookDict]
    max_concurrency: NotRequired[int]
    ignore_invalid_urls: NotRequired[bool]
    formats: NotRequired[list[FormatOrStr]]
    only_main_content: NotRequired[bool]
    only_clean_content: NotRequired[bool]
    include_tags: NotRequired[list[str]]
    exclude_tags: NotRequired[list[str]]
    max_age: NotRequired[int]
    min_age: NotRequired[int]
    headers: NotRequired[Any]
    wait_for: NotRequired[int]
    mobile: NotRequired[bool]
    skip_tls_verification: NotRequired[bool]
    timeout: NotRequired[int]
    parsers: NotRequired[list[Parser | ParserDict]]
    actions: NotRequired[list[Action | ActionDict]]
    location: NotRequired[Location | LocationDict]
    remove_base64_images: NotRequired[bool]
    block_ads: NotRequired[bool]
    proxy: NotRequired[ProxyOrStr]
    store_in_cache: NotRequired[bool]
    lockdown: NotRequired[bool]
    redact_pii: NotRequired[RedactPii | RedactPiiDict]
    profile: NotRequired[Profile | ProfileDict]
    threat_protection: NotRequired[ThreatProtectionOverride | ThreatProtectionOverrideDict]
    audit_metadata: NotRequired[AuditMetadata | AuditMetadataDict]
    zero_data_retention: NotRequired[bool]
