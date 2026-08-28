from __future__ import annotations

from pydantic import AnyUrl
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ValuableSource(SdkBaseModel):
    url: AnyUrl
    reason: Optional[str] = UNSET


class ValuableSourceDict(TypedDict):
    url: AnyUrl
    reason: NotRequired[str]
