from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Summary(SdkBaseModel):
    type_: Literal["summary"] = Field(default="summary", alias="type")


class SummaryDict(TypedDict):
    type_: NotRequired[Literal["summary"]]
