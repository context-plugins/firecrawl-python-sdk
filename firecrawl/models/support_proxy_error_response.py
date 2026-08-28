from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportProxyErrorResponse(SdkBaseModel):
    error: Optional[str] = UNSET
    """Support proxy or upstream error code."""


class SupportProxyErrorResponseDict(TypedDict):
    error: NotRequired[str]
