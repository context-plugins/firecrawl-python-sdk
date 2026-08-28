from __future__ import annotations

from pydantic import AnyUrl, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.language import LanguageOrStr
from .unions.description import Description, DescriptionDict
from .unions.keywords import Keywords, KeywordsDict
from .unions.title import Title, TitleDict


class Metadata1(SdkBaseModel):
    title: Optional[Title] = UNSET
    """Title extracted from the page, can be a string or array of strings"""

    description: Optional[Description] = UNSET
    """Description extracted from the page, can be a string or array of strings"""

    language: OptionalNullable[LanguageOrStr] = UNSET
    """Language extracted from the page, can be a string or array of strings"""

    source_url: Optional[AnyUrl] = Field(default=UNSET, alias="sourceURL")
    """The original URL that was requested. May differ from the page's final URL if redirects occurred."""

    url: Optional[AnyUrl] = UNSET
    """The final URL of the page after all redirects have been followed."""

    keywords: Optional[Keywords] = UNSET
    """Keywords extracted from the page, can be a string or array of strings"""

    og_locale_alternate: Optional[list[str]] = Field(default=UNSET, alias="ogLocaleAlternate")
    """Alternative locales for the page"""

    any_other_metadata: Optional[str] = Field(default=UNSET, alias="<any other metadata>")
    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """The status code of the page"""

    num_pages: Optional[int] = Field(default=UNSET, alias="numPages")
    """For PDF inputs, the number of pages parsed (capped by the parsers maxPages option)."""

    total_pages: Optional[int] = Field(default=UNSET, alias="totalPages")
    """For PDF inputs, the document's true page count before any maxPages capping. Omitted when it cannot be determined;
    a totalPages greater than numPages indicates the result was truncated."""

    error: OptionalNullable[str] = UNSET
    """The error message of the page"""

    concurrency_limited: Optional[bool] = Field(default=UNSET, alias="concurrencyLimited")
    """Whether this scrape was throttled due to team concurrency limits"""

    concurrency_queue_duration_ms: Optional[float] = Field(default=UNSET, alias="concurrencyQueueDurationMs")
    """Time in milliseconds the request waited in the concurrency queue. Only present when concurrencyLimited is
    true."""


class Metadata1Dict(TypedDict):
    title: NotRequired[Title | TitleDict]
    description: NotRequired[Description | DescriptionDict]
    language: NotRequired[LanguageOrStr | None]
    source_url: NotRequired[AnyUrl]
    url: NotRequired[AnyUrl]
    keywords: NotRequired[Keywords | KeywordsDict]
    og_locale_alternate: NotRequired[list[str]]
    any_other_metadata: NotRequired[str]
    status_code: NotRequired[int]
    num_pages: NotRequired[int]
    total_pages: NotRequired[int]
    error: NotRequired[str | None]
    concurrency_limited: NotRequired[bool]
    concurrency_queue_duration_ms: NotRequired[float]
