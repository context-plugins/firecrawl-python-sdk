from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Links2(SdkBaseModel):
    url: AnyUrl
    title: Optional[str] = UNSET
    """The title of the page, if available."""

    description: Optional[str] = UNSET
    """A description of the page, if available."""


class Links2Dict(TypedDict):
    url: AnyUrl
    title: NotRequired[str]
    description: NotRequired[str]
