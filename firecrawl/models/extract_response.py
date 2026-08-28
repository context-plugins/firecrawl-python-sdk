from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExtractResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    id: Optional[str] = UNSET
    invalid_urls: Optional[list[str | None]] = Field(default=UNSET, alias="invalidURLs")
    """If ignoreInvalidURLs is true, this is an array containing the invalid URLs that were specified in the request. If
    there were no invalid URLs, this will be an empty array. If ignoreInvalidURLs is false, this field will be
    undefined."""


class ExtractResponseDict(TypedDict):
    success: NotRequired[bool]
    id: NotRequired[str]
    invalid_urls: NotRequired[list[str | None]]
