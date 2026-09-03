from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class InteractExecuteResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
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


class InteractExecuteResponseDict(TypedDict):
    success: NotRequired[bool]
    stdout: NotRequired[str | None]
    result: NotRequired[str | None]
    stderr: NotRequired[str | None]
    exit_code: NotRequired[int | None]
    killed: NotRequired[bool]
    error: NotRequired[str | None]
