from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type7 import Type7OrStr
from .viewport import Viewport, ViewportDict


class Screenshot(SdkBaseModel):
    type_: Type7OrStr = Field(alias="type")
    full_page: Optional[bool] = Field(default=UNSET, alias="fullPage")
    """Whether to capture a full-page screenshot (ignores viewport.height) or limit to the current viewport."""

    quality: Optional[int] = UNSET
    """The quality of the screenshot, from 1 to 100. 100 is the highest quality."""

    viewport: Optional[Viewport] = UNSET


class ScreenshotDict(TypedDict):
    type_: Type7OrStr
    full_page: NotRequired[bool]
    quality: NotRequired[int]
    viewport: NotRequired[Viewport | ViewportDict]
