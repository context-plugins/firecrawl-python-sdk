from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type20 import Type20OrStr
from .viewport import Viewport, ViewportDict


class Screenshot1(SdkBaseModel):
    type_: Type20OrStr = Field(alias="type")
    """Take a screenshot. The links will be in the response's ``actions.screenshots`` array."""

    full_page: Optional[bool] = Field(default=UNSET, alias="fullPage")
    """Whether to capture a full-page screenshot (ignores viewport.height) or limit to the current viewport."""

    quality: Optional[int] = UNSET
    """The quality of the screenshot, from 1 to 100. 100 is the highest quality."""

    viewport: Optional[Viewport] = UNSET


class Screenshot1Dict(TypedDict):
    type_: Type20OrStr
    full_page: NotRequired[bool]
    quality: NotRequired[int]
    viewport: NotRequired[Viewport | ViewportDict]
