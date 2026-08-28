from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type23 import Type23OrStr


class PressAKey(SdkBaseModel):
    """Press a key on the page. See https://asawicki.info/nosense/doc/devices/keyboard/key_codes.html for key codes."""

    type_: Type23OrStr = Field(alias="type")
    """Press a key on the page"""

    key: str
    """Key to press"""


class PressAKeyDict(TypedDict):
    type_: Type23OrStr
    key: str
