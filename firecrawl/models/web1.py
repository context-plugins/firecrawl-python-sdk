from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .metadata3 import Metadata3, Metadata3Dict


class Web1(SdkBaseModel):
    title: Optional[str] = UNSET
    """Title from search result"""

    description: Optional[str] = UNSET
    """Description from search result"""

    url: Optional[str] = UNSET
    """URL of the search result"""

    markdown: OptionalNullable[str] = UNSET
    """Markdown content if scraping was requested"""

    html: OptionalNullable[str] = UNSET
    """HTML content if requested in formats"""

    raw_html: OptionalNullable[str] = Field(default=UNSET, alias="rawHtml")
    """Raw HTML content if requested in formats"""

    links: Optional[list[str]] = UNSET
    """Links found if requested in formats"""

    screenshot: OptionalNullable[str] = UNSET
    """Screenshot URL if requested in formats. Screenshots expire after 24 hours and can no longer be downloaded."""

    audio: OptionalNullable[str] = UNSET
    """Signed URL to the extracted MP3 audio file if ``audio`` is in ``formats``. The signed URL expires after 1
    hour."""

    video: OptionalNullable[str] = UNSET
    """Signed URL to the extracted video file if ``video`` is in ``formats``. The signed URL expires after 1 hour."""

    metadata: Optional[Metadata3] = UNSET


class Web1Dict(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    url: NotRequired[str]
    markdown: NotRequired[str | None]
    html: NotRequired[str | None]
    raw_html: NotRequired[str | None]
    links: NotRequired[list[str]]
    screenshot: NotRequired[str | None]
    audio: NotRequired[str | None]
    video: NotRequired[str | None]
    metadata: NotRequired[Metadata3 | Metadata3Dict]
