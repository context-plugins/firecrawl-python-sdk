from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ExecuteJavaScript(SdkBaseModel):
    type_: Literal["executeJavascript"] = Field(default="executeJavascript", alias="type")
    """Execute JavaScript code on the page"""

    script: str
    """JavaScript code to execute"""


class ExecuteJavaScriptDict(TypedDict):
    type_: NotRequired[Literal["executeJavascript"]]
    script: str
