from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Research(SdkBaseModel):
    type_: Literal["research"] = Field(default="research", alias="type")


class ResearchDict(TypedDict):
    type_: NotRequired[Literal["research"]]
