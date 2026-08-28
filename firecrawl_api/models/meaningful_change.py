from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type import TypeOrStr


class MeaningfulChange(SdkBaseModel):
    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    before: OptionalNullable[str] = UNSET
    after: OptionalNullable[str] = UNSET
    reason: Optional[str] = UNSET


class MeaningfulChangeDict(TypedDict):
    type_: NotRequired[TypeOrStr]
    before: NotRequired[str | None]
    after: NotRequired[str | None]
    reason: NotRequired[str]
