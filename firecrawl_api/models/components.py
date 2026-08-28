from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .button_primary import ButtonPrimary, ButtonPrimaryDict
from .button_secondary import ButtonSecondary, ButtonSecondaryDict


class Components(SdkBaseModel):
    """UI component styles."""

    button_primary: Optional[ButtonPrimary] = Field(default=UNSET, alias="buttonPrimary")
    """Primary button styles."""

    button_secondary: Optional[ButtonSecondary] = Field(default=UNSET, alias="buttonSecondary")
    """Secondary button styles."""

    input: Optional[Any] = UNSET
    """Input field styles."""


class ComponentsDict(TypedDict):
    button_primary: NotRequired[ButtonPrimary | ButtonPrimaryDict]
    button_secondary: NotRequired[ButtonSecondary | ButtonSecondaryDict]
    input: NotRequired[Any]
