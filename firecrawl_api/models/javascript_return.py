from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class JavascriptReturn(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    value: Optional[Any] = UNSET


class JavascriptReturnDict(TypedDict):
    type_: NotRequired[str]
    value: NotRequired[Any]
