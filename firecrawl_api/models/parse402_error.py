from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Parse402Error(SdkBaseModel):
    error: Optional[str] = UNSET


class Parse402ErrorDict(TypedDict):
    error: NotRequired[str]
