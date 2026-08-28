from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .evidence import Evidence, EvidenceDict
from .usage import Usage, UsageDict


class SupportDocsSearchResponse(SdkBaseModel):
    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    answer: Optional[str] = UNSET
    """Concise answer grounded in Firecrawl documentation."""

    evidence: Optional[list[Evidence]] = UNSET
    usage: Optional[Usage] = UNSET
    duration_ms: Optional[int] = Field(default=UNSET, alias="durationMs")
    """Total docs-search execution time in milliseconds."""


class SupportDocsSearchResponseDict(TypedDict):
    request_id: NotRequired[str]
    answer: NotRequired[str]
    evidence: NotRequired[list[Evidence | EvidenceDict]]
    usage: NotRequired[Usage | UsageDict]
    duration_ms: NotRequired[int]
