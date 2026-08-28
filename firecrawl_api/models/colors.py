from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Colors(SdkBaseModel):
    """Brand colors extracted from the page."""

    primary: Optional[str] = UNSET
    """Primary brand color (hex)."""

    secondary: Optional[str] = UNSET
    """Secondary brand color (hex)."""

    accent: Optional[str] = UNSET
    """Accent color (hex)."""

    background: Optional[str] = UNSET
    """Background color (hex)."""

    text_primary: Optional[str] = Field(default=UNSET, alias="textPrimary")
    """Primary text color (hex)."""

    text_secondary: Optional[str] = Field(default=UNSET, alias="textSecondary")
    """Secondary text color (hex)."""

    link: Optional[str] = UNSET
    """Link color (hex)."""

    success: Optional[str] = UNSET
    """Success/positive color (hex)."""

    warning: Optional[str] = UNSET
    """Warning color (hex)."""

    error: Optional[str] = UNSET
    """Error/danger color (hex)."""


class ColorsDict(TypedDict):
    primary: NotRequired[str]
    secondary: NotRequired[str]
    accent: NotRequired[str]
    background: NotRequired[str]
    text_primary: NotRequired[str]
    text_secondary: NotRequired[str]
    link: NotRequired[str]
    success: NotRequired[str]
    warning: NotRequired[str]
    error: NotRequired[str]
