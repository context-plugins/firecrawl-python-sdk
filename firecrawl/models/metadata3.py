from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Metadata3(SdkBaseModel):
    title: Optional[str] = UNSET
    description: Optional[str] = UNSET
    source_url: Optional[str] = Field(default=UNSET, alias="sourceURL")
    """The original URL that was requested. May differ from the page's final URL if redirects occurred."""

    url: Optional[str] = UNSET
    """The final URL of the page after all redirects have been followed."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    num_pages: Optional[int] = Field(default=UNSET, alias="numPages")
    """For PDF inputs, the number of pages parsed (capped by the parsers maxPages option)."""

    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    """For PDF inputs, the document's true page count before any maxPages capping. Omitted when it cannot be determined;
    a totalPages greater than numPages indicates the result was truncated."""

    error: OptionalNullable[str] = UNSET


class Metadata3Dict(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    source_url: NotRequired[str]
    url: NotRequired[str]
    status_code: NotRequired[int]
    num_pages: NotRequired[int]
    total_pages: NotRequired[int]
    error: NotRequired[str | None]
