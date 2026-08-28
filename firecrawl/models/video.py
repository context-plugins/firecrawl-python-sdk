from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type14 import Type14OrStr


class Video(SdkBaseModel):
    """Extract best-quality video from supported video URLs, e.g. YouTube. Returns a signed GCS URL."""

    type_: Type14OrStr = Field(alias="type")


class VideoDict(TypedDict):
    type_: Type14OrStr
