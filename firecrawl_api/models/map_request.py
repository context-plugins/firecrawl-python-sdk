from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audit_metadata import AuditMetadata, AuditMetadataDict
from .enums.sitemap2 import Sitemap2OrStr
from .location import Location, LocationDict
from .threat_protection_override import ThreatProtectionOverride, ThreatProtectionOverrideDict


class MapRequest(SdkBaseModel):
    url: AnyUrl
    """The base URL to start crawling from"""

    search: Optional[str] = UNSET
    """Specify a search query to order the results by relevance. Example: 'blog' will return URLs that contain the word
    'blog' in the URL ordered by relevance."""

    sitemap: Optional[Sitemap2OrStr] = UNSET
    """Sitemap mode when mapping. If you set it to ``skip``, the sitemap won't be used to find URLs. If you set it to
    ``only``, only URLs that are in the sitemap will be returned. By default (``include``), the sitemap and other
    methods will be used together to find URLs."""

    include_subdomains: Optional[bool] = Field(default=UNSET, alias="includeSubdomains")
    """Include subdomains of the website"""

    ignore_query_parameters: Optional[bool] = Field(default=UNSET, alias="ignoreQueryParameters")
    """Do not return URLs with query parameters"""

    ignore_cache: Optional[bool] = Field(default=UNSET, alias="ignoreCache")
    """Bypass the sitemap cache to retrieve fresh URLs. Sitemap data is cached for up to 7 days; use this parameter when
    your sitemap has been recently updated."""

    limit: Optional[int] = UNSET
    """Maximum number of links to return"""

    timeout: Optional[int] = UNSET
    """Timeout in milliseconds. There is no timeout by default."""

    location: Optional[Location] = UNSET
    """Location settings for the request. When specified, this will use an appropriate proxy if available and emulate
    the corresponding language and timezone settings. Defaults to 'US' if not specified."""

    audit_metadata: Optional[AuditMetadata] = Field(default=UNSET, alias="auditMetadata")
    """User attribution included with SIEM logging events when SIEM Logging is enabled for the organization."""

    threat_protection: Optional[ThreatProtectionOverride] = Field(default=UNSET, alias="threatProtection")
    """Per-request `Threat Protection <https://docs.firecrawl.dev/features/threat-protection>`__ override. Fields you
    provide replace the corresponding fields of your organization's policy for this request only; omitted fields keep
    their organization-level values. Requires Threat Protection to be enabled for your team (enterprise feature) —
    otherwise the request is rejected with a 403. If your organization has disabled request overrides, any request that
    includes this object is rejected with a 403. If Threat Protection is enforced for your team, ``mode`` may not be set
    to ``off``."""


class MapRequestDict(TypedDict):
    url: AnyUrl
    search: NotRequired[str]
    sitemap: NotRequired[Sitemap2OrStr]
    include_subdomains: NotRequired[bool]
    ignore_query_parameters: NotRequired[bool]
    ignore_cache: NotRequired[bool]
    limit: NotRequired[int]
    timeout: NotRequired[int]
    location: NotRequired[Location | LocationDict]
    audit_metadata: NotRequired[AuditMetadata | AuditMetadataDict]
    threat_protection: NotRequired[ThreatProtectionOverride | ThreatProtectionOverrideDict]
