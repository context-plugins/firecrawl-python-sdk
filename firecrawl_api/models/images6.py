from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Images6(SdkBaseModel):
    title: Optional[str] = UNSET
    """Title from search result"""

    image_url: Optional[str] = Field(default=UNSET, alias="imageUrl")
    """URL of the image"""

    image_width: Optional[int] = Field(default=UNSET, alias="imageWidth")
    """Width of the image"""

    image_height: Optional[int] = Field(default=UNSET, alias="imageHeight")
    """Height of the image"""

    url: Optional[str] = UNSET
    """URL of the search result"""

    position: Optional[int] = UNSET
    """Position of the search result"""


class Images6Dict(TypedDict):
    title: NotRequired[str]
    image_url: NotRequired[str]
    image_width: NotRequired[int]
    image_height: NotRequired[int]
    url: NotRequired[str]
    position: NotRequired[int]
