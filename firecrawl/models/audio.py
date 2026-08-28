from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type13 import Type13OrStr


class Audio(SdkBaseModel):
    """Extract audio (MP3) from supported video URLs, e.g. YouTube. Returns a signed GCS URL."""

    type_: Type13OrStr = Field(alias="type")


class AudioDict(TypedDict):
    type_: Type13OrStr
