from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.rating import RatingOrStr
from .missing_content import MissingContent, MissingContentDict
from .valuable_source import ValuableSource, ValuableSourceDict


class SearchFeedbackRequest(SdkBaseModel):
    """For 'good', include valuableSources. For 'partial', include valuableSources or missingContent. For 'bad', include
    missingContent or querySuggestions."""

    rating: RatingOrStr
    valuable_sources: Optional[list[ValuableSource]] = Field(default=UNSET, alias="valuableSources")
    missing_content: Optional[list[MissingContent]] = Field(default=UNSET, alias="missingContent")
    query_suggestions: Optional[str] = Field(default=UNSET, alias="querySuggestions")
    origin: Optional[str] = UNSET
    integration: OptionalNullable[str] = UNSET


class SearchFeedbackRequestDict(TypedDict):
    rating: RatingOrStr
    valuable_sources: NotRequired[list[ValuableSource | ValuableSourceDict]]
    missing_content: NotRequired[list[MissingContent | MissingContentDict]]
    query_suggestions: NotRequired[str]
    origin: NotRequired[str]
    integration: NotRequired[str | None]
