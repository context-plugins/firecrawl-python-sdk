from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .research_paper_signals import ResearchPaperSignals, ResearchPaperSignalsDict


class ResearchPaperResult(SdkBaseModel):
    paper_id: str = Field(alias="paperId")
    """Canonical paper id, or web:<url> for SERP-discovered display results."""

    primary_id: str = Field(alias="primaryId")
    """Preferred cite/fetch id such as arxiv:<id>, pmid:<id>, pmcid:<id>, or doi:<id>."""

    ids: Optional[dict[str, Any]] = UNSET
    """Source identifiers grouped by namespace."""

    title: str
    abstract: str
    score: float
    signals: Optional[ResearchPaperSignals] = UNSET


class ResearchPaperResultDict(TypedDict):
    paper_id: str
    primary_id: str
    ids: NotRequired[dict[str, Any]]
    title: str
    abstract: str
    score: float
    signals: NotRequired[ResearchPaperSignals | ResearchPaperSignalsDict]
