from __future__ import annotations

from typing import TypeAlias

from ..redact_piioptions import RedactPiioptions, RedactPiioptionsDict

RedactPii: TypeAlias = bool | RedactPiioptions
"""Redact personally identifiable information from returned markdown. Pass ``true`` to use defaults, or an object to
tune mode, entities, and replacement style."""

RedactPiiDict: TypeAlias = bool | RedactPiioptionsDict
