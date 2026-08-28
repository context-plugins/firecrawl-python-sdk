from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type22 import Type22OrStr


class WriteText(SdkBaseModel):
    type_: Type22OrStr = Field(alias="type")
    """Write text into an input field, text area, or contenteditable element. Note: You must first focus the element
    using a 'click' action before writing. The text will be typed character by character to simulate keyboard input."""

    text: str
    """Text to type"""


class WriteTextDict(TypedDict):
    type_: Type22OrStr
    text: str
