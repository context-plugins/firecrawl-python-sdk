from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Agent429Error(SdkBaseModel):
    error: Optional[str] = UNSET


class Agent429ErrorDict(TypedDict):
    error: NotRequired[str]
