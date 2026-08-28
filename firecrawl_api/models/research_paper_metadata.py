from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResearchPaperMetadata(SdkBaseModel):
    paper_id: str = Field(alias="paperId")
    """Canonical paper id."""

    ids: Optional[dict[str, Any]] = UNSET
    """Source identifiers grouped by namespace."""

    title: str
    abstract: str
    authors: Optional[str] = UNSET
    """Comma-joined author names."""

    categories: Optional[list[str]] = UNSET
    """Paper categories."""

    created_date: Optional[str] = Field(default=UNSET, alias="createdDate")
    """Original creation date string."""

    update_date: Optional[str] = Field(default=UNSET, alias="updateDate")
    """Last-updated date string."""


class ResearchPaperMetadataDict(TypedDict):
    paper_id: str
    ids: NotRequired[dict[str, Any]]
    title: str
    abstract: str
    authors: NotRequired[str]
    categories: NotRequired[list[str]]
    created_date: NotRequired[str]
    update_date: NotRequired[str]
