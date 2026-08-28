from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.format import FormatOrStr
from .enums.type27 import Type27OrStr


class GeneratePdf(SdkBaseModel):
    type_: Type27OrStr = Field(alias="type")
    """Generate a PDF of the current page. The PDF will be returned in the ``actions.pdfs`` array of the response."""

    format: Optional[FormatOrStr] = UNSET
    """The page size of the resulting PDF"""

    landscape: Optional[bool] = UNSET
    """Whether to generate the PDF in landscape orientation"""

    scale: Optional[float] = UNSET
    """The scale multiplier of the resulting PDF"""


class GeneratePdfDict(TypedDict):
    type_: Type27OrStr
    format: NotRequired[FormatOrStr]
    landscape: NotRequired[bool]
    scale: NotRequired[float]
