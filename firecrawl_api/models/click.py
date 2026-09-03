from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Click(SdkBaseModel):
    type_: Literal["click"] = Field(default="click", alias="type")
    """Click on an element"""

    selector: str
    """Query selector to find the element by"""

    all: Optional[bool] = UNSET
    """Clicks all elements matched by the selector, not just the first one. Does not throw an error if no elements match
    the selector."""


class ClickDict(TypedDict):
    type_: NotRequired[Literal["click"]]
    selector: str
    all: NotRequired[bool]
