from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.format import FormatOrStr


class GeneratePdf(SdkBaseModel):
    type_: Literal["pdf"] = Field(default="pdf", alias="type")
    """Generate a PDF of the current page. The PDF will be returned in the ``actions.pdfs`` array of the response."""

    format: Optional[FormatOrStr] = UNSET
    """The page size of the resulting PDF"""

    landscape: Optional[bool] = UNSET
    """Whether to generate the PDF in landscape orientation"""

    scale: Optional[float] = UNSET
    """The scale multiplier of the resulting PDF"""


class GeneratePdfDict(TypedDict):
    type_: NotRequired[Literal["pdf"]]
    format: NotRequired[FormatOrStr]
    landscape: NotRequired[bool]
    scale: NotRequired[float]
