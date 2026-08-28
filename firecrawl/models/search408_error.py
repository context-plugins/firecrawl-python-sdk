from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Search408Error(SdkBaseModel):
    success: Optional[bool] = UNSET
    error: Optional[str] = UNSET


class Search408ErrorDict(TypedDict):
    success: NotRequired[bool]
    error: NotRequired[str]
