from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SupportDocsSearchRequest(SdkBaseModel):
    question: str
    """Documentation question to answer."""


class SupportDocsSearchRequestDict(TypedDict):
    question: str
