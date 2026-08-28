from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type19 import Type19OrStr


class WaitForElement(SdkBaseModel):
    type_: Type19OrStr = Field(alias="type")
    """Wait for a specific element to appear"""

    selector: str
    """CSS selector to wait for"""


class WaitForElementDict(TypedDict):
    type_: Type19OrStr
    selector: str
