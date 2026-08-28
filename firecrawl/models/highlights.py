from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type16 import Type16OrStr


class Highlights(SdkBaseModel):
    """Find relevant source text from the page. Returns the selected text in the response ``highlights`` field."""

    type_: Type16OrStr = Field(alias="type")
    query: str
    """The text-selection query to run against the page. Maximum 10,000 characters."""


class HighlightsDict(TypedDict):
    type_: Type16OrStr
    query: str
