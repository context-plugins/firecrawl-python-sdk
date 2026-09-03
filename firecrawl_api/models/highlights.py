from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Highlights(SdkBaseModel):
    """Find relevant source text from the page. Returns the selected text in the response ``highlights`` field."""

    type_: Literal["highlights"] = Field(default="highlights", alias="type")
    query: str
    """The text-selection query to run against the page. Maximum 10,000 characters."""


class HighlightsDict(TypedDict):
    type_: NotRequired[Literal["highlights"]]
    query: str
