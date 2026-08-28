from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type18 import Type18OrStr


class WaitByDuration(SdkBaseModel):
    type_: Type18OrStr = Field(alias="type")
    """Wait for a specified amount of milliseconds"""

    milliseconds: int
    """Number of milliseconds to wait"""


class WaitByDurationDict(TypedDict):
    type_: Type18OrStr
    milliseconds: int
