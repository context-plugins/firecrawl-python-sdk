from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .research_paper_metadata import ResearchPaperMetadata, ResearchPaperMetadataDict


class ResearchPaperMetadataResponse(SdkBaseModel):
    success: bool
    paper: ResearchPaperMetadata


class ResearchPaperMetadataResponseDict(TypedDict):
    success: bool
    paper: ResearchPaperMetadata | ResearchPaperMetadataDict
