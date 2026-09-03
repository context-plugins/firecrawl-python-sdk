from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Types(SdkBaseModel):
    """Which result types are indexed for this repository: ``issue``, ``pullRequest``, and ``readme``."""

    issue: Optional[bool] = UNSET
    pull_request: Optional[bool] = Field(default=UNSET, alias="pullRequest")
    readme: Optional[bool] = UNSET


class TypesDict(TypedDict):
    issue: NotRequired[bool]
    pull_request: NotRequired[bool]
    readme: NotRequired[bool]
