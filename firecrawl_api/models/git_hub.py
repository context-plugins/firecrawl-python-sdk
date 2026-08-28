from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class GitHub(SdkBaseModel):
    type_: Literal["github"] = Field(default="github", alias="type")


class GitHubDict(TypedDict):
    type_: NotRequired[Literal["github"]]
