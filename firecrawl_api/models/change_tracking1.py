from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.change_status import ChangeStatusOrStr
from .enums.visibility import VisibilityOrStr


class ChangeTracking1(SdkBaseModel):
    """Change tracking information if ``changeTracking`` is in ``formats``. Only present when the ``changeTracking``
    format is requested."""

    previous_scrape_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="previousScrapeAt")
    """The timestamp of the previous scrape that the current page is being compared against. Null if no previous scrape
    exists."""

    change_status: Optional[ChangeStatusOrStr] = Field(default=UNSET, alias="changeStatus")
    """The result of the comparison between the two page versions. 'new' means this page did not exist before, 'same'
    means content has not changed, 'changed' means content has changed, 'removed' means the page was removed."""

    visibility: Optional[VisibilityOrStr] = UNSET
    """The visibility of the current page/URL. 'visible' means the URL was discovered through an organic route (links or
    sitemap), 'hidden' means the URL was discovered through memory from previous crawls."""

    diff: OptionalNullable[str] = UNSET
    """Git-style diff of changes when using 'git-diff' mode. Only present when the mode is set to 'git-diff'."""

    json_value: OptionalNullable[Any] = Field(default=UNSET, alias="json")
    """JSON comparison results when using 'json' mode. Only present when the mode is set to 'json'. This will emit a
    list of all the keys and their values from the ``previous`` and ``current`` scrapes based on the type defined in the
    ``schema``. Example `here </features/change-tracking>`__"""


class ChangeTracking1Dict(TypedDict):
    previous_scrape_at: NotRequired[RFC3339DateTime | None]
    change_status: NotRequired[ChangeStatusOrStr]
    visibility: NotRequired[VisibilityOrStr]
    diff: NotRequired[str | None]
    json_value: NotRequired[Any | None]
