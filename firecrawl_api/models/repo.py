from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .types import Types, TypesDict


class Repo(SdkBaseModel):
    repo: Optional[str] = UNSET
    indexed: Optional[bool] = UNSET
    types: Optional[Types] = UNSET
    """Which result types are indexed for this repository: ``issue``, ``pullRequest``, and ``readme``."""


class RepoDict(TypedDict):
    repo: NotRequired[str]
    indexed: NotRequired[bool]
    types: NotRequired[Types | TypesDict]
