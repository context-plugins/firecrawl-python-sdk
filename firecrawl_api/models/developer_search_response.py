from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .coverage import Coverage, CoverageDict
from .developer_search_result import DeveloperSearchResult, DeveloperSearchResultDict
from .repo import Repo, RepoDict
from .source import Source, SourceDict


class DeveloperSearchResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    results: Optional[list[DeveloperSearchResult]] = UNSET
    coverage: Optional[Coverage] = UNSET
    """Outcome for each result type. Check this when an expected result type is missing: ``skipped`` means your
    ``types`` value did not ask for that type, while ``degraded`` or ``unavailable`` means the gap came from the index
    or from a filter, not from the query. A repository filter is one such cause — see `how the repository filters scope
    a search </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__."""

    reranked: Optional[bool] = UNSET
    """Whether the ranked list went through the reranking stage."""

    repos: Optional[list[Repo]] = UNSET
    """Present only when ``repos`` was sent. Echoes each slug with whether it is indexed, plus a per-type breakdown
    under ``types``."""

    sources: Optional[list[Source]] = UNSET
    """Present only when ``sources`` was sent. Reports each id exactly as requested along with whether it is indexed.
    ``indexed: true`` means the source has a published generation, so documentation evidence from it may appear;
    ``indexed: false`` means nothing from that id can match, which distinguishes an id that is not in the index from a
    query that simply found nothing."""


class DeveloperSearchResponseDict(TypedDict):
    success: NotRequired[bool]
    results: NotRequired[list[DeveloperSearchResult | DeveloperSearchResultDict]]
    coverage: NotRequired[Coverage | CoverageDict]
    reranked: NotRequired[bool]
    repos: NotRequired[list[Repo | RepoDict]]
    sources: NotRequired[list[Source | SourceDict]]
