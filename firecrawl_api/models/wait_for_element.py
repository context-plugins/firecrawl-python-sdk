from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class WaitForElement(SdkBaseModel):
    type_: Literal["wait"] = Field(default="wait", alias="type")
    """Wait for a specific element to appear"""

    selector: str
    """CSS selector to wait for"""


class WaitForElementDict(TypedDict):
    type_: NotRequired[Literal["wait"]]
    selector: str
