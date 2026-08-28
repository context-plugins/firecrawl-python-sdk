from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Map402Error(SdkBaseModel):
    error: Optional[str] = UNSET


class Map402ErrorDict(TypedDict):
    error: NotRequired[str]
