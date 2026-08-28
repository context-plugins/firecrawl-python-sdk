from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Passage(SdkBaseModel):
    text: Optional[str] = UNSET


class PassageDict(TypedDict):
    text: NotRequired[str]
