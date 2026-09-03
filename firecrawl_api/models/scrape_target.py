from __future__ import annotations

from typing import Literal
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scrape_options import ScrapeOptions, ScrapeOptionsDict


class ScrapeTarget(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Optional stable ID for this target. Generated if omitted."""

    type_: Literal["scrape"] = Field(default="scrape", alias="type")
    urls: list[str]
    scrape_options: Optional[ScrapeOptions] = Field(default=UNSET, alias="scrapeOptions")


class ScrapeTargetDict(TypedDict):
    id: NotRequired[UUID]
    type_: NotRequired[Literal["scrape"]]
    urls: list[str]
    scrape_options: NotRequired[ScrapeOptions | ScrapeOptionsDict]
