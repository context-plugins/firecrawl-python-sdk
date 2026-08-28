from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Scrape(SdkBaseModel):
    type_: Literal["scrape"] = Field(default="scrape", alias="type")
    """Scrape the current page content, returns the url and the html."""


class ScrapeDict(TypedDict):
    type_: NotRequired[Literal["scrape"]]
