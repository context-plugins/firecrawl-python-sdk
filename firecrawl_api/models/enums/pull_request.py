from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PullRequest(str, Enum):
    OK = "ok"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"
    SKIPPED = "skipped"

    __str__ = str.__str__


PullRequestOrStr: TypeAlias = Annotated[PullRequest | str, open_enum_validator(PullRequest)]
