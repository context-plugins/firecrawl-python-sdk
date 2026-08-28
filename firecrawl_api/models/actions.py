from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .javascript_return import JavascriptReturn, JavascriptReturnDict
from .scrape1 import Scrape1, Scrape1Dict


class Actions(SdkBaseModel):
    """Results of the actions specified in the ``actions`` parameter. Only present if the ``actions`` parameter was
    provided in the request"""

    screenshots: Optional[list[str]] = UNSET
    """Screenshot URLs, in the same order as the screenshot actions provided."""

    scrapes: Optional[list[Scrape1]] = UNSET
    """Scrape contents, in the same order as the scrape actions provided."""

    javascript_returns: Optional[list[JavascriptReturn]] = Field(default=UNSET, alias="javascriptReturns")
    """JavaScript return values, in the same order as the executeJavascript actions provided."""

    pdfs: Optional[list[str]] = UNSET
    """PDFs generated, in the same order as the pdf actions provided."""


class ActionsDict(TypedDict):
    screenshots: NotRequired[list[str]]
    scrapes: NotRequired[list[Scrape1 | Scrape1Dict]]
    javascript_returns: NotRequired[list[JavascriptReturn | JavascriptReturnDict]]
    pdfs: NotRequired[list[str]]
