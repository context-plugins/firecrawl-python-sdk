from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.endpoint import EndpointOrStr
from .enums.rating import RatingOrStr
from .missing_content import MissingContent, MissingContentDict
from .valuable_source import ValuableSource, ValuableSourceDict


class EndpointFeedbackRequest(SdkBaseModel):
    rating: RatingOrStr
    valuable_sources: Optional[list[ValuableSource]] = Field(default=UNSET, alias="valuableSources")
    missing_content: Optional[list[MissingContent]] = Field(default=UNSET, alias="missingContent")
    query_suggestions: Optional[str] = Field(default=UNSET, alias="querySuggestions")
    origin: Optional[str] = UNSET
    integration: OptionalNullable[str] = UNSET
    endpoint: EndpointOrStr
    job_id: UUID = Field(alias="jobId")
    issues: Optional[list[str]] = UNSET
    tags: Optional[list[str]] = UNSET
    note: Optional[str] = UNSET
    url: Optional[str] = UNSET
    page_numbers: Optional[list[int]] = Field(default=UNSET, alias="pageNumbers")
    metadata: Optional[Any] = UNSET
    """Small endpoint-specific metadata object. Must be 8KB or smaller; do not include full endpoint results."""


class EndpointFeedbackRequestDict(TypedDict):
    rating: RatingOrStr
    valuable_sources: NotRequired[list[ValuableSource | ValuableSourceDict]]
    missing_content: NotRequired[list[MissingContent | MissingContentDict]]
    query_suggestions: NotRequired[str]
    origin: NotRequired[str]
    integration: NotRequired[str | None]
    endpoint: EndpointOrStr
    job_id: UUID
    issues: NotRequired[list[str]]
    tags: NotRequired[list[str]]
    note: NotRequired[str]
    url: NotRequired[str]
    page_numbers: NotRequired[list[int]]
    metadata: NotRequired[Any]
