from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .research_paper_metadata import ResearchPaperMetadata, ResearchPaperMetadataDict
from .research_passage import ResearchPassage, ResearchPassageDict


class ResearchReadPaperResponse(SdkBaseModel):
    success: bool
    paper: ResearchPaperMetadata
    paper_id: str = Field(alias="paperId")
    query: str
    passages: list[ResearchPassage]


class ResearchReadPaperResponseDict(TypedDict):
    success: bool
    paper: ResearchPaperMetadata | ResearchPaperMetadataDict
    paper_id: str
    query: str
    passages: list[ResearchPassage | ResearchPassageDict]
