from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SupportProxyErrorResponseError(SdkBaseModel):
    error: Optional[str] = UNSET
    """Support proxy or upstream error code."""


class SupportProxyErrorResponseErrorDict(TypedDict):
    error: NotRequired[str]
