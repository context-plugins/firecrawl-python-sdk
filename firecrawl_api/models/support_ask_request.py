from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportAskRequest(SdkBaseModel):
    question: str
    """Question or issue for the support agent to diagnose."""

    rationale: Optional[str] = UNSET
    """Optional context about what the end user is trying to accomplish."""


class SupportAskRequestDict(TypedDict):
    question: str
    rationale: NotRequired[str]
