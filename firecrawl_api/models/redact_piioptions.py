from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode2 import Mode2OrStr
from .enums.redact_piientity import RedactPiientityOrStr
from .enums.replace_style import ReplaceStyleOrStr


class RedactPiioptions(SdkBaseModel):
    """Tuning options for PII redaction."""

    mode: Optional[Mode2OrStr] = UNSET
    """Redaction strategy. ``accurate`` is model-only and optimized for precision, ``aggressive`` increases recall with
    additional heuristics, and ``fast`` uses heuristics without the model call."""

    entities: Optional[list[RedactPiientityOrStr]] = UNSET
    """Restrict redaction to these entity buckets. If omitted, all supported entities are redacted."""

    replace_style: Optional[ReplaceStyleOrStr] = Field(default=UNSET, alias="replaceStyle")
    """``tag`` replaces spans with placeholders like ``<EMAIL>``, ``mask`` replaces characters with ``*``, and
    ``remove`` deletes the span text."""


class RedactPiioptionsDict(TypedDict):
    mode: NotRequired[Mode2OrStr]
    entities: NotRequired[list[RedactPiientityOrStr]]
    replace_style: NotRequired[ReplaceStyleOrStr]
