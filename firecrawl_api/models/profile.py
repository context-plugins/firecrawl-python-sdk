from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Profile(SdkBaseModel):
    """Enable persistent browser storage across scrape and interact sessions. Pass a profile when scraping to preserve
    cookies, localStorage, and session data. Sessions with the same profile name share browser state."""

    name: str
    """A name for the profile. Scrapes with the same name share browser state (cookies, localStorage, sessions)."""

    save_changes: Optional[bool] = Field(default=UNSET, alias="saveChanges")
    """When true, browser state is saved back to the profile when the interact session stops. Set to false to load
    existing data without writing. Only one saving session is allowed at a time."""


class ProfileDict(TypedDict):
    name: str
    save_changes: NotRequired[bool]
