from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.skills1 import Skills1OrStr
from .enums.types1 import Types1OrStr


class SearchDeveloperRequest(SdkBaseModel):
    query: str
    k: Optional[int] = UNSET
    types: Optional[list[Types1OrStr]] = UNSET
    repos: Optional[list[str]] = UNSET
    """Repository slugs to scope the repository half of the index to. Applies to the ``issue``, ``pull_request``, and
    ``readme`` types only. Sent together with ``sources``, the two halves are combined rather than intersected. Returns
    400 when no repository type is in ``types``, reporting that ``repos`` cannot match any requested type and that you
    should add repository types or drop ``repos``."""

    sources: Optional[list[str]] = UNSET
    """Documentation source ids to scope the documentation half to, at most 20. Applies to the ``doc`` type only. Not a
    fixed enum: ids reflect the documentation sites in the index and the set grows over time. Returns 400 with ``sources
    cannot match any requested type; add doc or drop sources`` when ``doc`` is not in ``types``."""

    skills: Optional[Skills1OrStr] = UNSET
    """Set to ``only`` to limit the search to indexed agent-skill files."""

    passages: Optional[int] = UNSET
    language: Optional[str] = UNSET
    """Repository primary language, such as ``Rust``. Applies to repository results only; sending it with no ``sources``
    scope returns no ``doc`` results. See `how the repository filters scope a search
    </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__."""

    topic: Optional[str] = UNSET
    """Repository topic, such as ``async``. Applies to repository results only; sending it with no ``sources`` scope
    returns no ``doc`` results."""

    license: Optional[str] = UNSET
    """Repository license, such as ``MIT``. Applies to repository results only; sending it with no ``sources`` scope
    returns no ``doc`` results."""

    min_stars: Optional[int] = UNSET
    """Lower bound on repository stars. Applies to repository results only; sending it with no ``sources`` scope returns
    no ``doc`` results."""

    max_stars: Optional[int] = UNSET
    """Upper bound on repository stars. Applies to repository results only; sending it with no ``sources`` scope returns
    no ``doc`` results."""

    archived: Optional[bool] = UNSET
    """Include or exclude archived repositories. Applies to repository results only; sending it with no ``sources``
    scope returns no ``doc`` results."""

    fork: Optional[bool] = UNSET
    """Include or exclude forks. Applies to repository results only; sending it with no ``sources`` scope returns no
    ``doc`` results."""


class SearchDeveloperRequestDict(TypedDict):
    query: str
    k: NotRequired[int]
    types: NotRequired[list[Types1OrStr]]
    repos: NotRequired[list[str]]
    sources: NotRequired[list[str]]
    skills: NotRequired[Skills1OrStr]
    passages: NotRequired[int]
    language: NotRequired[str]
    topic: NotRequired[str]
    license: NotRequired[str]
    min_stars: NotRequired[int]
    max_stars: NotRequired[int]
    archived: NotRequired[bool]
    fork: NotRequired[bool]
