from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class Data6(SdkBaseModel):
    remaining_tokens: Optional[float] = Field(default=UNSET, alias="remainingTokens")
    """Number of tokens remaining for the team"""

    plan_tokens: Optional[float] = Field(default=UNSET, alias="planTokens")
    """Number of tokens in the plan. This does not include coupon tokens."""

    billing_period_start: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="billingPeriodStart")
    """Start date of the current billing period."""

    billing_period_end: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="billingPeriodEnd")
    """End date of the current billing period."""


class Data6Dict(TypedDict):
    remaining_tokens: NotRequired[float]
    plan_tokens: NotRequired[float]
    billing_period_start: NotRequired[RFC3339DateTime | None]
    billing_period_end: NotRequired[RFC3339DateTime | None]
