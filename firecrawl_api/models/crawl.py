from __future__ import annotations

from uuid import UUID

from pydantic import AnyUrl, Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .options import Options, OptionsDict


class Crawl(SdkBaseModel):
    id: UUID
    """The unique identifier of the crawl"""

    team_id: str = Field(alias="teamId")
    """The ID of the team that owns the crawl"""

    url: AnyUrl
    """The origin URL of the crawl"""

    options: Options
    """The crawler options used for this crawl"""


class CrawlDict(TypedDict):
    id: UUID
    team_id: str
    url: AnyUrl
    options: Options | OptionsDict
