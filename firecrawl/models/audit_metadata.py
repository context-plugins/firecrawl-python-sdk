from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuditMetadata(SdkBaseModel):
    """User attribution included with SIEM logging events when SIEM Logging is enabled for the organization."""

    username: str
    """The username associated with the request."""


class AuditMetadataDict(TypedDict):
    username: str
