from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .data8 import Data8, Data8Dict


class SearchResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    data: Optional[Data8] = UNSET
    """The search results. The arrays available will depend on the sources you specified in the request. By default, the
    ``web`` array will be returned."""

    warning: OptionalNullable[str] = UNSET
    """Warning message if any issues occurred"""

    id: Optional[str] = UNSET
    """The ID of the search job"""

    credits_used: Optional[int] = Field(default=UNSET, alias="creditsUsed")
    """The number of credits used for the search"""


class SearchResponseDict(TypedDict):
    success: NotRequired[bool]
    data: NotRequired[Data8 | Data8Dict]
    warning: NotRequired[str | None]
    id: NotRequired[str]
    credits_used: NotRequired[int]
