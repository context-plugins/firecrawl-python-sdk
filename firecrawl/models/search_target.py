from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.search_window import SearchWindowOrStr
from .enums.type29 import Type29OrStr


class SearchTarget(SdkBaseModel):
    """Runs web search queries on each check and alerts on new results that match the monitor's goal. Requires a
    non-empty top-level ``goal`` on the monitor unless ``judgeEnabled`` is ``false``."""

    id: Optional[UUID] = UNSET
    """Optional stable ID for this target. Generated if omitted."""

    type_: Type29OrStr = Field(alias="type")
    queries: list[str]
    """Search queries to run on each check (1-12)."""

    search_window: Optional[SearchWindowOrStr] = Field(default=UNSET, alias="searchWindow")
    """Recency filter — only consider results published within this window."""

    max_results: Optional[int] = Field(default=UNSET, alias="maxResults")
    """Total results to evaluate per check, merged and deduped across all queries (a combined cap, not per-query)."""

    include_domains: Optional[list[str]] = Field(default=UNSET, alias="includeDomains")
    """Optional. Restrict results to these domains."""

    exclude_domains: Optional[list[str]] = Field(default=UNSET, alias="excludeDomains")
    """Optional. Drop results from these domains."""


class SearchTargetDict(TypedDict):
    id: NotRequired[UUID]
    type_: Type29OrStr
    queries: list[str]
    search_window: NotRequired[SearchWindowOrStr]
    max_results: NotRequired[int]
    include_domains: NotRequired[list[str]]
    exclude_domains: NotRequired[list[str]]
