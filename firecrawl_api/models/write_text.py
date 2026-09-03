from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class WriteText(SdkBaseModel):
    type_: Literal["write"] = Field(default="write", alias="type")
    """Write text into an input field, text area, or contenteditable element. Note: You must first focus the element
    using a 'click' action before writing. The text will be typed character by character to simulate keyboard input."""

    text: str
    """Text to type"""


class WriteTextDict(TypedDict):
    type_: NotRequired[Literal["write"]]
    text: str
