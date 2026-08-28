from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.direction import DirectionOrStr
from .enums.type24 import Type24OrStr


class Scroll(SdkBaseModel):
    type_: Type24OrStr = Field(alias="type")
    """Scroll the page or a specific element"""

    direction: Optional[DirectionOrStr] = UNSET
    """Direction to scroll"""

    selector: Optional[str] = UNSET
    """Query selector for the element to scroll"""


class ScrollDict(TypedDict):
    type_: Type24OrStr
    direction: NotRequired[DirectionOrStr]
    selector: NotRequired[str]
