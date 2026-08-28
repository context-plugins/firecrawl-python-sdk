from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Snapshot(SdkBaseModel):
    """Snapshot of the current JSON extraction at this run. Present on JSON-extraction and mixed-mode monitors; absent
    for markdown-only monitors."""

    json_value: Optional[Any] = Field(default=UNSET, alias="json")
    """The full structured JSON extracted on this run, matching the schema/prompt declared on the target's
    ``changeTracking`` format."""


class SnapshotDict(TypedDict):
    json_value: NotRequired[Any]
