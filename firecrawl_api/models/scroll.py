from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.direction import DirectionOrStr


class Scroll(SdkBaseModel):
    type_: Literal["scroll"] = Field(default="scroll", alias="type")
    """Scroll the page or a specific element"""

    direction: Optional[DirectionOrStr] = UNSET
    """Direction to scroll"""

    selector: Optional[str] = UNSET
    """Query selector for the element to scroll"""


class ScrollDict(TypedDict):
    type_: NotRequired[Literal["scroll"]]
    direction: NotRequired[DirectionOrStr]
    selector: NotRequired[str]
