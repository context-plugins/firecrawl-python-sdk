from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Viewport(SdkBaseModel):
    width: int
    """The width of the viewport in pixels"""

    height: int
    """The height of the viewport in pixels"""


class ViewportDict(TypedDict):
    width: int
    height: int
