from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links2 import Links2, Links2Dict


class MapResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    links: Optional[list[Links2]] = UNSET


class MapResponseDict(TypedDict):
    success: NotRequired[bool]
    links: NotRequired[list[Links2 | Links2Dict]]
