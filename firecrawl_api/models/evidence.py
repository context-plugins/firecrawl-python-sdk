from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Evidence(SdkBaseModel):
    path_or_url: Optional[str] = Field(default=UNSET, alias="pathOrUrl")
    reason: Optional[str] = UNSET


class EvidenceDict(TypedDict):
    path_or_url: NotRequired[str]
    reason: NotRequired[str]
