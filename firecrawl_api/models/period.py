from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class Period(SdkBaseModel):
    start_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startDate")
    """Start date of the billing period"""

    end_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="endDate")
    """End date of the billing period"""

    api_key: OptionalNullable[str] = Field(default=UNSET, alias="apiKey")
    """Name of the API key used for the billing period. null if byApiKey is false (default)"""

    total_credits: Optional[int] = Field(default=UNSET, alias="totalCredits")
    """Total number of credits used in the billing period"""


class PeriodDict(TypedDict):
    start_date: NotRequired[RFC3339DateTime]
    end_date: NotRequired[RFC3339DateTime]
    api_key: NotRequired[str | None]
    total_credits: NotRequired[int]
