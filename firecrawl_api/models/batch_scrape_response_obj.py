from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BatchScrapeResponseObj(SdkBaseModel):
    success: Optional[bool] = UNSET
    id: Optional[str] = UNSET
    url: Optional[AnyUrl] = UNSET
    invalid_urls: Optional[list[str | None]] = Field(default=UNSET, alias="invalidURLs")
    """If ignoreInvalidURLs is true, this is an array containing the invalid URLs that were specified in the request. If
    there were no invalid URLs, this will be an empty array. If ignoreInvalidURLs is false, this field will be
    undefined."""


class BatchScrapeResponseObjDict(TypedDict):
    success: NotRequired[bool]
    id: NotRequired[str]
    url: NotRequired[AnyUrl]
    invalid_urls: NotRequired[list[str | None]]
