from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type21 import Type21OrStr


class Click(SdkBaseModel):
    type_: Type21OrStr = Field(alias="type")
    """Click on an element"""

    selector: str
    """Query selector to find the element by"""

    all: Optional[bool] = UNSET
    """Clicks all elements matched by the selector, not just the first one. Does not throw an error if no elements match
    the selector."""


class ClickDict(TypedDict):
    type_: Type21OrStr
    selector: str
    all: NotRequired[bool]
