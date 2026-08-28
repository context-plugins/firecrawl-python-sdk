from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .images6 import Images6, Images6Dict
from .news1 import News1, News1Dict
from .web1 import Web1, Web1Dict


class Data8(SdkBaseModel):
    """The search results. The arrays available will depend on the sources you specified in the request. By default, the
    ``web`` array will be returned."""

    web: Optional[list[Web1]] = UNSET
    images: Optional[list[Images6]] = UNSET
    news: Optional[list[News1]] = UNSET


class Data8Dict(TypedDict):
    web: NotRequired[list[Web1 | Web1Dict]]
    images: NotRequired[list[Images6 | Images6Dict]]
    news: NotRequired[list[News1 | News1Dict]]
