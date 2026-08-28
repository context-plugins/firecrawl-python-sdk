from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.failure_policy1 import FailurePolicy1OrStr
from .enums.mode6 import Mode6OrStr


class Data9(SdkBaseModel):
    mode: Optional[Mode6OrStr] = UNSET
    """Threat protection mode. ``off`` disables checks; ``normal`` checks URLs against Google Web Risk (+2 credits per
    URL scanned)."""

    risk_score_threshold: Optional[int] = Field(default=UNSET, alias="riskScoreThreshold")
    """Normalized score (0-100) at or above which a classifier verdict is blocked. Lower is stricter."""

    blacklist: Optional[list[str]] = UNSET
    """Exact domains or globs (e.g. ``*.example.com``) always blocked, without a classifier call."""

    whitelist: Optional[list[str]] = UNSET
    """Exact domains or globs always allowed. Wins over every other rule."""

    blocked_tlds: Optional[list[str]] = Field(default=UNSET, alias="blockedTlds")
    """Top-level domains to block outright, lowercase without a leading dot."""

    failure_policy: Optional[FailurePolicy1OrStr] = Field(default=UNSET, alias="failurePolicy")
    """Behavior when the classifier is unreachable: ``closed`` blocks (default), ``open`` allows."""

    allow_request_overrides: Optional[bool] = Field(default=UNSET, alias="allowRequestOverrides")
    """Whether individual requests may pass a ``threatProtection`` object. When false, such requests are rejected with
    403."""

    configured: Optional[bool] = UNSET
    """Whether the organization has saved a policy (vs. serving defaults)."""

    updated_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")


class Data9Dict(TypedDict):
    mode: NotRequired[Mode6OrStr]
    risk_score_threshold: NotRequired[int]
    blacklist: NotRequired[list[str]]
    whitelist: NotRequired[list[str]]
    blocked_tlds: NotRequired[list[str]]
    failure_policy: NotRequired[FailurePolicy1OrStr]
    allow_request_overrides: NotRequired[bool]
    configured: NotRequired[bool]
    updated_at: NotRequired[RFC3339DateTime | None]
