from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class Data5(SdkBaseModel):
    remaining_credits: Optional[float] = Field(default=UNSET, alias="remainingCredits")
    """Number of credits remaining for the team"""

    plan_credits: Optional[float] = Field(default=UNSET, alias="planCredits")
    """Number of credits in the plan. This does not include coupon credits, credit packs, or auto recharge credits."""

    billing_period_start: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="billingPeriodStart")
    """Start date of the current billing period."""

    billing_period_end: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="billingPeriodEnd")
    """End date of the current billing period."""


class Data5Dict(TypedDict):
    remaining_credits: NotRequired[float]
    plan_credits: NotRequired[float]
    billing_period_start: NotRequired[RFC3339DateTime | None]
    billing_period_end: NotRequired[RFC3339DateTime | None]
