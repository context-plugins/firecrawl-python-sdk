from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.failure_policy import FailurePolicyOrStr
from .enums.mode3 import Mode3OrStr


class ThreatProtectionOverride(SdkBaseModel):
    """Per-request `Threat Protection <https://docs.firecrawl.dev/features/threat-protection>`__ override. Fields you
    provide replace the corresponding fields of your organization's policy for this request only; omitted fields keep
    their organization-level values. Requires Threat Protection to be enabled for your team (enterprise feature) —
    otherwise the request is rejected with a 403. If your organization has disabled request overrides, any request that
    includes this object is rejected with a 403. If Threat Protection is enforced for your team, ``mode`` may not be set
    to ``off``."""

    mode: Optional[Mode3OrStr] = UNSET
    """URL scanning mode for this request. ``normal`` checks URLs against Google Web Risk (+2 credits per URL
    scanned)."""

    risk_score_threshold: Optional[int] = Field(default=UNSET, alias="riskScoreThreshold")
    """Normalized risk score (0–100) at or above which a classifier verdict blocks the URL. Lower is stricter."""

    blacklist: Optional[list[str]] = UNSET
    """Domains to always block, as plain domains (``example.com``) or wildcard globs (``*.example.com``). No protocol,
    path, or port."""

    whitelist: Optional[list[str]] = UNSET
    """Domains to always allow, as plain domains or wildcard globs. Wins over every other rule."""

    blocked_tlds: Optional[list[str]] = Field(default=UNSET, alias="blockedTlds")
    """Top-level domains to block outright, lowercase without the leading dot (e.g. ``zip``)."""

    failure_policy: Optional[FailurePolicyOrStr] = Field(default=UNSET, alias="failurePolicy")
    """What to do when the classifier can't be reached: ``closed`` blocks the request, ``open`` allows it."""


class ThreatProtectionOverrideDict(TypedDict):
    mode: NotRequired[Mode3OrStr]
    risk_score_threshold: NotRequired[int]
    blacklist: NotRequired[list[str]]
    whitelist: NotRequired[list[str]]
    blocked_tlds: NotRequired[list[str]]
    failure_policy: NotRequired[FailurePolicyOrStr]
