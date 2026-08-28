from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .research_paper_result import ResearchPaperResult, ResearchPaperResultDict


class ResearchSimilarPapersResponse(SdkBaseModel):
    success: bool
    results: list[ResearchPaperResult]
    pool_size: int = Field(alias="poolSize")
    truncated: bool
    note: OptionalNullable[str] = UNSET


class ResearchSimilarPapersResponseDict(TypedDict):
    success: bool
    results: list[ResearchPaperResult | ResearchPaperResultDict]
    pool_size: int
    truncated: bool
    note: NotRequired[str | None]
