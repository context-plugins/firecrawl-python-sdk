from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .email import Email, EmailDict


class MonitorNotification(SdkBaseModel):
    email: Optional[Email] = UNSET


class MonitorNotificationDict(TypedDict):
    email: NotRequired[Email | EmailDict]
