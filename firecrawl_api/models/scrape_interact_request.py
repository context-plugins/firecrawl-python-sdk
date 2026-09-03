from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.language import LanguageOrStr


class ScrapeInteractRequest(SdkBaseModel):
    code: str
    """Code to execute in the scrape-bound browser sandbox"""

    language: Optional[LanguageOrStr] = UNSET
    """Language of the code to execute. Use ``node`` for JavaScript or ``bash`` for agent-browser CLI commands."""

    timeout: Optional[int] = UNSET
    """Execution timeout in seconds"""

    origin: Optional[str] = UNSET
    """Optional origin label used for execution telemetry"""


class ScrapeInteractRequestDict(TypedDict):
    code: str
    language: NotRequired[LanguageOrStr]
    timeout: NotRequired[int]
    origin: NotRequired[str]
