from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.language import LanguageOrStr


class InteractExecuteRequest(SdkBaseModel):
    code: str
    """Code to execute in the browser sandbox"""

    language: Optional[LanguageOrStr] = UNSET
    """Language of the code to execute. Use ``node`` for JavaScript or ``bash`` for agent-browser CLI commands."""

    timeout: Optional[int] = UNSET
    """Execution timeout in seconds"""


class InteractExecuteRequestDict(TypedDict):
    code: str
    language: NotRequired[LanguageOrStr]
    timeout: NotRequired[int]
