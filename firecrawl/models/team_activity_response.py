from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .data7 import Data7, Data7Dict


class TeamActivityResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[list[Data7]] = UNSET
    cursor: OptionalNullable[str] = UNSET
    """Cursor to use for the next page. Null if there are no more results."""

    has_more: Optional[bool] = UNSET
    """Whether there are more results available"""


class TeamActivityResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[list[Data7 | Data7Dict]]
    cursor: NotRequired[str | None]
    has_more: NotRequired[bool]
