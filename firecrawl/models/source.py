from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Source(SdkBaseModel):
    source: Optional[str] = UNSET
    indexed: Optional[bool] = UNSET


class SourceDict(TypedDict):
    source: NotRequired[str]
    indexed: NotRequired[bool]
