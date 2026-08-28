from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.doc import DocOrStr
from .enums.issue import IssueOrStr
from .enums.pull_request import PullRequestOrStr
from .enums.readme import ReadmeOrStr


class Coverage(SdkBaseModel):
    """Outcome for each result type. Check this when an expected result type is missing: ``skipped`` means your
    ``types`` value did not ask for that type, while ``degraded`` or ``unavailable`` means the gap came from the index
    or from a filter, not from the query. A repository filter is one such cause — see `how the repository filters scope
    a search </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__."""

    doc: Optional[DocOrStr] = UNSET
    issue: Optional[IssueOrStr] = UNSET
    pull_request: Optional[PullRequestOrStr] = UNSET
    readme: Optional[ReadmeOrStr] = UNSET


class CoverageDict(TypedDict):
    doc: NotRequired[DocOrStr]
    issue: NotRequired[IssueOrStr]
    pull_request: NotRequired[PullRequestOrStr]
    readme: NotRequired[ReadmeOrStr]
