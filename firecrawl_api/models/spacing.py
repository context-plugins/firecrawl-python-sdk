from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Spacing(SdkBaseModel):
    """Spacing and layout information."""

    base_unit: Optional[int] = Field(default=UNSET, alias="baseUnit")
    """Base spacing unit in pixels."""

    border_radius: Optional[str] = Field(default=UNSET, alias="borderRadius")
    """Default border radius."""

    padding: Optional[Any] = UNSET
    """Padding values."""

    margins: Optional[Any] = UNSET
    """Margin values."""


class SpacingDict(TypedDict):
    base_unit: NotRequired[int]
    border_radius: NotRequired[str]
    padding: NotRequired[Any]
    margins: NotRequired[Any]
