from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Visibility(str, Enum):
    """The visibility of the current page/URL. 'visible' means the URL was discovered through an organic route (links or
    sitemap), 'hidden' means the URL was discovered through memory from previous crawls."""

    VISIBLE = "visible"
    HIDDEN = "hidden"

    __str__ = str.__str__


VisibilityOrStr: TypeAlias = Annotated[Visibility | str, open_enum_validator(Visibility)]
