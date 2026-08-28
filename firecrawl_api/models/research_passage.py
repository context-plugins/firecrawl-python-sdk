from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResearchPassage(SdkBaseModel):
    text: str
    """In-body passage text. May include markdown tables."""

    score: float
    """Dense similarity score for the passage."""


class ResearchPassageDict(TypedDict):
    text: str
    score: float
