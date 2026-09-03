from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Video(SdkBaseModel):
    """Extract best-quality video from supported video URLs, e.g. YouTube. Returns a signed GCS URL."""

    type_: Literal["video"] = Field(default="video", alias="type")


class VideoDict(TypedDict):
    type_: NotRequired[Literal["video"]]
