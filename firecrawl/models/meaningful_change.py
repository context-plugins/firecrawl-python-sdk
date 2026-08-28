from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type30 import Type30OrStr


class MeaningfulChange(SdkBaseModel):
    type_: Optional[Type30OrStr] = Field(default=UNSET, alias="type")
    before: OptionalNullable[str] = UNSET
    after: OptionalNullable[str] = UNSET
    reason: Optional[str] = UNSET


class MeaningfulChangeDict(TypedDict):
    type_: NotRequired[Type30OrStr]
    before: NotRequired[str | None]
    after: NotRequired[str | None]
    reason: NotRequired[str]
