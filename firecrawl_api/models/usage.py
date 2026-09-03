from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Usage(SdkBaseModel):
    input_tokens: Optional[int] = Field(default=UNSET, alias="inputTokens")
    output_tokens: Optional[int] = Field(default=UNSET, alias="outputTokens")
    total_tokens: Optional[int] = Field(default=UNSET, alias="totalTokens")


class UsageDict(TypedDict):
    input_tokens: NotRequired[int]
    output_tokens: NotRequired[int]
    total_tokens: NotRequired[int]
