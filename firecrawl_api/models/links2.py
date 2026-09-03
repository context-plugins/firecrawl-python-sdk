from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Links2(SdkBaseModel):
    url: str
    title: Optional[str] = UNSET
    """The title of the page, if available."""

    description: Optional[str] = UNSET
    """A description of the page, if available."""


class Links2Dict(TypedDict):
    url: str
    title: NotRequired[str]
    description: NotRequired[str]
