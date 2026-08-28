from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type25 import Type25OrStr


class Scrape(SdkBaseModel):
    type_: Type25OrStr = Field(alias="type")
    """Scrape the current page content, returns the url and the html."""


class ScrapeDict(TypedDict):
    type_: Type25OrStr
