from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Parse500Error(SdkBaseModel):
    success: Optional[bool] = UNSET
    code: Optional[str] = UNSET
    error: Optional[str] = UNSET


class Parse500ErrorDict(TypedDict):
    success: NotRequired[bool]
    code: NotRequired[str]
    error: NotRequired[str]
