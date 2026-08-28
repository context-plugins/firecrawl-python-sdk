from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Audio(SdkBaseModel):
    """Extract audio (MP3) from supported video URLs, e.g. YouTube. Returns a signed GCS URL."""

    type_: Literal["audio"] = Field(default="audio", alias="type")


class AudioDict(TypedDict):
    type_: NotRequired[Literal["audio"]]
