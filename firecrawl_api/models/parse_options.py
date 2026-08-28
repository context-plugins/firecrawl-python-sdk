from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .audit_metadata import AuditMetadata, AuditMetadataDict
from .enums.proxy1 import Proxy1OrStr
from .parser1 import Parser1, Parser1Dict
from .unions.parse_format import ParseFormat, ParseFormatDict
from .unions.redact_pii import RedactPii, RedactPiiDict


class ParseOptions(SdkBaseModel):
    """Optional parse options sent as JSON in the multipart ``options`` field."""

    formats: Optional[list[ParseFormat]] = UNSET
    """Output formats supported for ``/parse`` uploads. Browser-rendering formats and change tracking are not
    supported."""

    only_main_content: Optional[bool] = Field(default=UNSET, alias="onlyMainContent")
    """Only return the main content of the page excluding headers, navs, footers, etc."""

    include_tags: Optional[list[str]] = Field(default=UNSET, alias="includeTags")
    """Tags to include in the output."""

    exclude_tags: Optional[list[str]] = Field(default=UNSET, alias="excludeTags")
    """Tags to exclude from the output."""

    headers: Optional[Any] = UNSET
    """Headers to send when additional network requests are required."""

    timeout: Optional[int] = UNSET
    """Timeout in milliseconds for the request. Default is 30000 (30 seconds). Maximum is 300000 (300 seconds)."""

    parsers: Optional[list[Parser1]] = UNSET
    """Controls file parser behavior when relevant (for example PDF parser mode)."""

    skip_tls_verification: Optional[bool] = Field(default=UNSET, alias="skipTlsVerification")
    """Skip TLS certificate verification when making requests."""

    remove_base64_images: Optional[bool] = Field(default=UNSET, alias="removeBase64Images")
    """Remove base64-encoded images from output and keep alt text placeholders."""

    block_ads: Optional[bool] = Field(default=UNSET, alias="blockAds")
    """Enable ad and cookie popup blocking."""

    redact_pii: Optional[RedactPii] = Field(default=UNSET, alias="redactPII")
    """Redact personally identifiable information from returned markdown. Pass ``true`` to use defaults, or an object to
    tune mode, entities, and replacement style."""

    proxy: Optional[Proxy1OrStr] = UNSET
    """Proxy mode for parse uploads. ``/parse`` supports only ``basic`` and ``auto``."""

    origin: Optional[str] = UNSET
    """Origin identifier for analytics and logging."""

    integration: OptionalNullable[str] = UNSET
    """Optional integration identifier."""

    audit_metadata: Optional[AuditMetadata] = Field(default=UNSET, alias="auditMetadata")
    """User attribution included with SIEM logging events when SIEM Logging is enabled for the organization."""

    zero_data_retention: Optional[bool] = Field(default=UNSET, alias="zeroDataRetention")
    """If true, this will enable zero data retention for this parse. To enable this feature, please contact
    help@firecrawl.dev"""


class ParseOptionsDict(TypedDict):
    formats: NotRequired[list[ParseFormat | ParseFormatDict]]
    only_main_content: NotRequired[bool]
    include_tags: NotRequired[list[str]]
    exclude_tags: NotRequired[list[str]]
    headers: NotRequired[Any]
    timeout: NotRequired[int]
    parsers: NotRequired[list[Parser1 | Parser1Dict]]
    skip_tls_verification: NotRequired[bool]
    remove_base64_images: NotRequired[bool]
    block_ads: NotRequired[bool]
    redact_pii: NotRequired[RedactPii | RedactPiiDict]
    proxy: NotRequired[Proxy1OrStr]
    origin: NotRequired[str]
    integration: NotRequired[str | None]
    audit_metadata: NotRequired[AuditMetadata | AuditMetadataDict]
    zero_data_retention: NotRequired[bool]
