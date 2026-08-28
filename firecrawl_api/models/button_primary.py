from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ButtonPrimary(SdkBaseModel):
    """Primary button styles."""

    background: Optional[str] = UNSET
    text_color: Optional[str] = Field(default=UNSET, alias="textColor")
    border_radius: Optional[str] = Field(default=UNSET, alias="borderRadius")


class ButtonPrimaryDict(TypedDict):
    background: NotRequired[str]
    text_color: NotRequired[str]
    border_radius: NotRequired[str]
