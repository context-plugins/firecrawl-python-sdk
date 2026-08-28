from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResearchPaperSignals(SdkBaseModel):
    structural: float
    """Raw structural graph signal."""

    semantic: float
    """Semantic score from the intent search."""

    article_rank: float = Field(alias="articleRank")
    """Structural expansion article-rank score."""

    seed_overlap: int = Field(alias="seedOverlap")
    """Number of distinct seeds connected to this candidate."""


class ResearchPaperSignalsDict(TypedDict):
    structural: float
    semantic: float
    article_rank: float
    seed_overlap: int
