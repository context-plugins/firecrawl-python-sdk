from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type1 import Type1OrStr
from .passage import Passage, PassageDict


class DeveloperSearchResult(SdkBaseModel):
    id: Optional[str] = UNSET
    """Stable result id, such as ``issue:owner/repo#123``."""

    type_: Optional[Type1OrStr] = Field(default=UNSET, alias="type")
    """Result kind."""

    url: Optional[str] = UNSET
    title: Optional[str] = UNSET
    """Frequently absent on ``doc`` results, where the source page carries no usable title. Fall back to ``url``."""

    passages: Optional[list[Passage]] = UNSET
    """Matched passages in markdown, so tables and code blocks survive."""


class DeveloperSearchResultDict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[Type1OrStr]
    url: NotRequired[str]
    title: NotRequired[str]
    passages: NotRequired[list[Passage | PassageDict]]
