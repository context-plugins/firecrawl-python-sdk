from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scrape_options import ScrapeOptions, ScrapeOptionsDict
from .threat_protection_override import ThreatProtectionOverride, ThreatProtectionOverrideDict


class ExtractRequest(SdkBaseModel):
    urls: list[str]
    prompt: Optional[str] = UNSET
    """Prompt to guide the extraction process"""

    schema_value: Optional[Any] = Field(default=UNSET, alias="schema")
    """Schema to define the structure of the extracted data. Must conform to `JSON Schema
    <https://json-schema.org/>`__."""

    enable_web_search: Optional[bool] = Field(default=UNSET, alias="enableWebSearch")
    """When true, the extraction will use web search to find additional data"""

    ignore_sitemap: Optional[bool] = Field(default=UNSET, alias="ignoreSitemap")
    """When true, sitemap.xml files will be ignored during website scanning"""

    include_subdomains: Optional[bool] = Field(default=UNSET, alias="includeSubdomains")
    """When true, subdomains of the provided URLs will also be scanned"""

    show_sources: Optional[bool] = Field(default=UNSET, alias="showSources")
    """When true, the sources used to extract the data will be included in the response as ``sources`` key"""

    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")
    ignore_invalid_urls: Optional[bool] = Field(default=UNSET, alias="ignoreInvalidURLs")
    """If invalid URLs are specified in the urls array, they will be ignored. Instead of them failing the entire
    request, an extract using the remaining valid URLs will be performed, and the invalid URLs will be returned in the
    invalidURLs field of the response."""

    threat_protection: Optional[ThreatProtectionOverride] = Field(default=UNSET, alias="threatProtection")
    """Per-request `Threat Protection <https://docs.firecrawl.dev/features/threat-protection>`__ override. Fields you
    provide replace the corresponding fields of your organization's policy for this request only; omitted fields keep
    their organization-level values. Requires Threat Protection to be enabled for your team (enterprise feature) —
    otherwise the request is rejected with a 403. If your organization has disabled request overrides, any request that
    includes this object is rejected with a 403. If Threat Protection is enforced for your team, ``mode`` may not be set
    to ``off``."""


class ExtractRequestDict(TypedDict):
    urls: list[str]
    prompt: NotRequired[str]
    schema_value: NotRequired[Any]
    enable_web_search: NotRequired[bool]
    ignore_sitemap: NotRequired[bool]
    include_subdomains: NotRequired[bool]
    show_sources: NotRequired[bool]
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
    ignore_invalid_urls: NotRequired[bool]
    threat_protection: NotRequired[ThreatProtectionOverride | ThreatProtectionOverrideDict]
