from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.confidence import ConfidenceOrStr


class SupportAskResponse(SdkBaseModel):
    answer: Optional[str] = UNSET
    """Diagnosis and recommended fix."""

    confidence: Optional[ConfidenceOrStr] = UNSET
    fix_parameters: OptionalNullable[Any] = Field(default=UNSET, alias="fixParameters")
    """Machine-readable API parameters that may fix the issue."""

    validation: OptionalNullable[Any] = UNSET
    """Validation result when the support agent tested or attempted a fix."""

    feedback: OptionalNullable[Any] = UNSET
    """Present when the support agent is blocked or needs more information."""

    duration_ms: Optional[int] = Field(default=UNSET, alias="durationMs")
    """Total support-agent execution time in milliseconds."""


class SupportAskResponseDict(TypedDict):
    answer: NotRequired[str]
    confidence: NotRequired[ConfidenceOrStr]
    fix_parameters: NotRequired[Any | None]
    validation: NotRequired[Any | None]
    feedback: NotRequired[Any | None]
    duration_ms: NotRequired[int]
