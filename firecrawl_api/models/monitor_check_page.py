from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .diff import Diff, DiffDict
from .enums.status3 import Status3OrStr
from .monitor_page_judgment import MonitorPageJudgment, MonitorPageJudgmentDict
from .snapshot import Snapshot, SnapshotDict


class MonitorCheckPage(SdkBaseModel):
    id: Optional[UUID] = UNSET
    target_id: Optional[str] = Field(default=UNSET, alias="targetId")
    url: Optional[str] = UNSET
    status: Optional[Status3OrStr] = UNSET
    previous_scrape_id: OptionalNullable[UUID] = Field(default=UNSET, alias="previousScrapeId")
    current_scrape_id: OptionalNullable[UUID] = Field(default=UNSET, alias="currentScrapeId")
    status_code: OptionalNullable[int] = Field(default=UNSET, alias="statusCode")
    error: OptionalNullable[str] = UNSET
    metadata: OptionalNullable[Any] = UNSET
    """Extra per-page metadata. For search monitors this includes ``searchStatus``, the finer-grained search disposition
    behind the top-level ``status``: ``alert`` (maps to ``new``), ``already_seen``, ``watching``, ``ignored`` (all map
    to ``same``), or ``skipped`` (maps to ``error``)."""

    judgment: OptionalNullable[MonitorPageJudgment] = UNSET
    diff: OptionalNullable[Diff] = UNSET
    """Inline diff artifact when the page changed. The shape depends on what the monitor's scrapeOptions.formats asked
    for. Markdown-only monitors populate both ``text`` (unified diff) and ``json`` (parseDiff AST). JSON-extraction
    monitors populate ``json`` as a per-field ``{previous, current}`` map keyed by JSON path. Mixed-mode monitors
    (``changeTracking`` with both ``json`` and ``git-diff`` modes) populate both ``text`` (markdown sidecar) and
    ``json`` (per-field diff)."""

    snapshot: OptionalNullable[Snapshot] = UNSET
    """Snapshot of the current JSON extraction at this run. Present on JSON-extraction and mixed-mode monitors; absent
    for markdown-only monitors."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")


class MonitorCheckPageDict(TypedDict):
    id: NotRequired[UUID]
    target_id: NotRequired[str]
    url: NotRequired[str]
    status: NotRequired[Status3OrStr]
    previous_scrape_id: NotRequired[UUID | None]
    current_scrape_id: NotRequired[UUID | None]
    status_code: NotRequired[int | None]
    error: NotRequired[str | None]
    metadata: NotRequired[Any | None]
    judgment: NotRequired[MonitorPageJudgment | MonitorPageJudgmentDict | None]
    diff: NotRequired[Diff | DiffDict | None]
    snapshot: NotRequired[Snapshot | SnapshotDict | None]
    created_at: NotRequired[RFC3339DateTime]
