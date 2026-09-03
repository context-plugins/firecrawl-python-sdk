from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Profile1(SdkBaseModel):
    """Enable persistent storage across interact sessions. Data saved in one session can be loaded in a later session
    using the same name."""

    name: str
    """A name for the profile. Sessions with the same name share storage."""

    save_changes: Optional[bool] = Field(default=UNSET, alias="saveChanges")
    """When true, browser state is saved back to the profile on close. Set to false to load existing data without
    writing. Multiple non-saving sessions are allowed but only one saving session at a time."""


class Profile1Dict(TypedDict):
    name: str
    save_changes: NotRequired[bool]
