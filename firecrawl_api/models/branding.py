from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Branding(SdkBaseModel):
    type_: Literal["branding"] = Field(default="branding", alias="type")


class BrandingDict(TypedDict):
    type_: NotRequired[Literal["branding"]]
