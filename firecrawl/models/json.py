from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type8 import Type8OrStr


class Json(SdkBaseModel):
    type_: Type8OrStr = Field(alias="type")
    schema_value: Optional[Any] = Field(default=UNSET, alias="schema")
    """The schema to use for the JSON output. Must conform to `JSON Schema <https://json-schema.org/>`__."""

    prompt: Optional[str] = UNSET
    """The prompt to use for the JSON output"""


class JsonDict(TypedDict):
    type_: Type8OrStr
    schema_value: NotRequired[Any]
    prompt: NotRequired[str]
