from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type26 import Type26OrStr


class ExecuteJavaScript(SdkBaseModel):
    type_: Type26OrStr = Field(alias="type")
    """Execute JavaScript code on the page"""

    script: str
    """JavaScript code to execute"""


class ExecuteJavaScriptDict(TypedDict):
    type_: Type26OrStr
    script: str
