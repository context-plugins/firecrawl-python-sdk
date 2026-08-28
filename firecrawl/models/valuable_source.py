from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ValuableSource(SdkBaseModel):
    url: str
    reason: Optional[str] = UNSET


class ValuableSourceDict(TypedDict):
    url: str
    reason: NotRequired[str]
