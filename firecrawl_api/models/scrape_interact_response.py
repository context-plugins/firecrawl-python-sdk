from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScrapeInteractResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    cdp_url: OptionalNullable[str] = Field(default=UNSET, alias="cdpUrl")
    """Raw Chrome DevTools Protocol (CDP) WebSocket URL for the browser session. Use it to connect directly with
    Playwright, Puppeteer, or any CDP client."""

    live_view_url: OptionalNullable[str] = Field(default=UNSET, alias="liveViewUrl")
    """Read-only live view URL for the browser session"""

    interactive_live_view_url: OptionalNullable[str] = Field(default=UNSET, alias="interactiveLiveViewUrl")
    """Interactive live view URL (viewers can control the browser)"""

    output: OptionalNullable[str] = UNSET
    """AI agent's final response (only present when using prompt)"""

    stdout: OptionalNullable[str] = UNSET
    """Standard output from the code execution"""

    result: OptionalNullable[str] = UNSET
    """Standard output (alias for stdout)"""

    stderr: OptionalNullable[str] = UNSET
    """Standard error output from the code execution"""

    exit_code: OptionalNullable[int] = Field(default=UNSET, alias="exitCode")
    """Exit code of the executed process"""

    killed: Optional[bool] = UNSET
    """Whether the process was killed due to timeout"""

    error: OptionalNullable[str] = UNSET
    """Error message if the code raised an exception"""


class ScrapeInteractResponseDict(TypedDict):
    success: NotRequired[bool]
    cdp_url: NotRequired[str | None]
    live_view_url: NotRequired[str | None]
    interactive_live_view_url: NotRequired[str | None]
    output: NotRequired[str | None]
    stdout: NotRequired[str | None]
    result: NotRequired[str | None]
    stderr: NotRequired[str | None]
    exit_code: NotRequired[int | None]
    killed: NotRequired[bool]
    error: NotRequired[str | None]
