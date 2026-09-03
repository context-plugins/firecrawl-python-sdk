from __future__ import annotations

from typing import Any, Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Json(SdkBaseModel):
    type_: Literal["json"] = Field(default="json", alias="type")
    schema_value: Optional[Any] = Field(default=UNSET, alias="schema")
    """The schema to use for the JSON output. Must conform to `JSON Schema <https://json-schema.org/>`__."""

    prompt: Optional[str] = UNSET
    """The prompt to use for the JSON output"""


class JsonDict(TypedDict):
    type_: NotRequired[Literal["json"]]
    schema_value: NotRequired[Any]
    prompt: NotRequired[str]
