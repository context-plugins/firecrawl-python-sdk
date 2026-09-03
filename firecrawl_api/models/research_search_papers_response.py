from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .research_paper_result import ResearchPaperResult, ResearchPaperResultDict


class ResearchSearchPapersResponse(SdkBaseModel):
    success: bool
    results: list[ResearchPaperResult]


class ResearchSearchPapersResponseDict(TypedDict):
    success: bool
    results: list[ResearchPaperResult | ResearchPaperResultDict]
