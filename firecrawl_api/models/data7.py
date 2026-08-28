from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.endpoint2 import Endpoint2OrStr


class Data7(SdkBaseModel):
    id: Optional[str] = UNSET
    """The job ID. Use this with the corresponding GET endpoint to retrieve results."""

    endpoint: Optional[Endpoint2OrStr] = UNSET
    """The endpoint used for this job"""

    api_version: Optional[str] = UNSET
    """The API version used for this request"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """When the job was created"""

    target: OptionalNullable[str] = UNSET
    """The URL or query that was submitted"""


class Data7Dict(TypedDict):
    id: NotRequired[str]
    endpoint: NotRequired[Endpoint2OrStr]
    api_version: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    target: NotRequired[str | None]
