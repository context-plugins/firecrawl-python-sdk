from __future__ import annotations

from typing import Any, Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.mode import ModeOrStr


class ChangeTracking(SdkBaseModel):
    type_: Literal["changeTracking"] = Field(default="changeTracking", alias="type")
    modes: Optional[list[ModeOrStr]] = UNSET
    """The mode to use for change tracking. 'git-diff' provides a detailed diff, and 'json' compares extracted JSON
    data."""

    schema_value: Optional[Any] = Field(default=UNSET, alias="schema")
    """Schema for JSON extraction when using 'json' mode. Defines the structure of data to extract and compare. Must
    conform to `JSON Schema <https://json-schema.org/>`__."""

    prompt: Optional[str] = UNSET
    """Prompt to use for change tracking when using 'json' mode. If not provided, the default prompt will be used."""

    tag: OptionalNullable[str] = UNSET
    """Tag to use for change tracking. Tags can separate change tracking history into separate "branches", where change
    tracking with a specific tagwill only compare to scrapes made in the same tag. If not provided, the default tag
    (null) will be used."""


class ChangeTrackingDict(TypedDict):
    type_: NotRequired[Literal["changeTracking"]]
    modes: NotRequired[list[ModeOrStr]]
    schema_value: NotRequired[Any]
    prompt: NotRequired[str]
    tag: NotRequired[str | None]
