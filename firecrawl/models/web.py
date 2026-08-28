from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type40 import Type40OrStr


class Web(SdkBaseModel):
    type_: Type40OrStr = Field(alias="type")
    tbs: Optional[str] = UNSET
    """Time-based search parameter. Supports predefined time ranges (``qdr:h``, ``qdr:d``, ``qdr:w``, ``qdr:m``,
    ``qdr:y``), custom date ranges (``cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY``), and sort by date (``sbd:1``). Values
    can be combined, e.g. ``sbd:1,qdr:w``."""

    location: Optional[str] = UNSET
    """Location parameter for search results"""


class WebDict(TypedDict):
    type_: Type40OrStr
    tbs: NotRequired[str]
    location: NotRequired[str]
