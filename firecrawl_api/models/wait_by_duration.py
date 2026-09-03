from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class WaitByDuration(SdkBaseModel):
    type_: Literal["wait"] = Field(default="wait", alias="type")
    """Wait for a specified amount of milliseconds"""

    milliseconds: int
    """Number of milliseconds to wait"""


class WaitByDurationDict(TypedDict):
    type_: NotRequired[Literal["wait"]]
    milliseconds: int
