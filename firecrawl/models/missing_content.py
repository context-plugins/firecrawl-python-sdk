from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MissingContent(SdkBaseModel):
    topic: str
    description: Optional[str] = UNSET


class MissingContentDict(TypedDict):
    topic: str
    description: NotRequired[str]
