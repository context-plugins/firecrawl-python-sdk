from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .metadata1 import Metadata1, Metadata1Dict


class Data2(SdkBaseModel):
    markdown: Optional[str] = UNSET
    html: OptionalNullable[str] = UNSET
    """HTML version of the content on page if ``includeHtml`` is true"""

    raw_html: OptionalNullable[str] = Field(default=UNSET, alias="rawHtml")
    """Raw HTML content of the page if ``includeRawHtml`` is true"""

    links: Optional[list[str]] = UNSET
    """List of links on the page if ``includeLinks`` is true"""

    screenshot: OptionalNullable[str] = UNSET
    """Screenshot of the page if ``includeScreenshot`` is true"""

    metadata: Optional[Metadata1] = UNSET


class Data2Dict(TypedDict):
    markdown: NotRequired[str]
    html: NotRequired[str | None]
    raw_html: NotRequired[str | None]
    links: NotRequired[list[str]]
    screenshot: NotRequired[str | None]
    metadata: NotRequired[Metadata1 | Metadata1Dict]
