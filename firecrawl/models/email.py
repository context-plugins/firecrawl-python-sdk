from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Email(SdkBaseModel):
    enabled: Optional[bool] = UNSET
    recipients: Optional[list[EmailStr]] = UNSET
    include_diffs: Optional[bool] = Field(default=UNSET, alias="includeDiffs")
    """Include changed page details in email summaries."""


class EmailDict(TypedDict):
    enabled: NotRequired[bool]
    recipients: NotRequired[list[EmailStr]]
    include_diffs: NotRequired[bool]
