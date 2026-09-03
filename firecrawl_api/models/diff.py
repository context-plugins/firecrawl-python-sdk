from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Diff(SdkBaseModel):
    """Inline diff artifact when the page changed. The shape depends on what the monitor's scrapeOptions.formats asked
    for. Markdown-only monitors populate both ``text`` (unified diff) and ``json`` (parseDiff AST). JSON-extraction
    monitors populate ``json`` as a per-field ``{previous, current}`` map keyed by JSON path. Mixed-mode monitors
    (``changeTracking`` with both ``json`` and ``git-diff`` modes) populate both ``text`` (markdown sidecar) and
    ``json`` (per-field diff)."""

    text: Optional[str] = UNSET
    """Unified markdown diff. Present on markdown-only and mixed-mode monitors."""

    json_value: Optional[Any] = Field(default=UNSET, alias="json")
    """For markdown-only monitors, a parseDiff AST ``{ files: [...] }``. For JSON-extraction (and mixed-mode) monitors,
    a per-field ``{ previous, current }`` map keyed by the JSON path into the extraction (e.g. ``plans[0].price``)."""


class DiffDict(TypedDict):
    text: NotRequired[str]
    json_value: NotRequired[Any]
