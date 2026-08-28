from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audit_metadata import AuditMetadata, AuditMetadataDict
from .enums.model import ModelOrStr
from .threat_protection_override import ThreatProtectionOverride, ThreatProtectionOverrideDict


class AgentRequest(SdkBaseModel):
    urls: Optional[list[str]] = UNSET
    """Optional list of URLs to constrain the agent to"""

    prompt: str
    """The prompt describing what data to extract"""

    schema_value: Optional[Any] = Field(default=UNSET, alias="schema")
    """Optional JSON schema to structure the extracted data"""

    max_credits: Optional[float] = Field(default=UNSET, alias="maxCredits")
    """Maximum credits to spend on this agent task. Defaults to 2500 if not set. Values above 2,500 are always billed as
    paid requests."""

    strict_constrain_to_urls: Optional[bool] = Field(default=UNSET, alias="strictConstrainToURLs")
    """If true, agent will only visit URLs provided in the urls array"""

    model: Optional[ModelOrStr] = UNSET
    """The model to use for the agent task. spark-1-mini (default) is 60% cheaper, spark-1-pro offers higher accuracy
    for complex tasks"""

    audit_metadata: Optional[AuditMetadata] = Field(default=UNSET, alias="auditMetadata")
    """User attribution included with SIEM logging events when SIEM Logging is enabled for the organization."""

    threat_protection: Optional[ThreatProtectionOverride] = Field(default=UNSET, alias="threatProtection")
    """Per-request `Threat Protection <https://docs.firecrawl.dev/features/threat-protection>`__ override. Fields you
    provide replace the corresponding fields of your organization's policy for this request only; omitted fields keep
    their organization-level values. Requires Threat Protection to be enabled for your team (enterprise feature) —
    otherwise the request is rejected with a 403. If your organization has disabled request overrides, any request that
    includes this object is rejected with a 403. If Threat Protection is enforced for your team, ``mode`` may not be set
    to ``off``."""


class AgentRequestDict(TypedDict):
    urls: NotRequired[list[str]]
    prompt: str
    schema_value: NotRequired[Any]
    max_credits: NotRequired[float]
    strict_constrain_to_urls: NotRequired[bool]
    model: NotRequired[ModelOrStr]
    audit_metadata: NotRequired[AuditMetadata | AuditMetadataDict]
    threat_protection: NotRequired[ThreatProtectionOverride | ThreatProtectionOverrideDict]
