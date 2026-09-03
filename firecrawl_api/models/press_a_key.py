from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PressAKey(SdkBaseModel):
    """Press a key on the page. See https://asawicki.info/nosense/doc/devices/keyboard/key_codes.html for key codes."""

    type_: Literal["press"] = Field(default="press", alias="type")
    """Press a key on the page"""

    key: str
    """Key to press"""


class PressAKeyDict(TypedDict):
    type_: NotRequired[Literal["press"]]
    key: str
