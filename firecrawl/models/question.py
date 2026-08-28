from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type15 import Type15OrStr


class Question(SdkBaseModel):
    """Ask a natural-language question about the page. Returns the answer in the response ``answer`` field."""

    type_: Type15OrStr = Field(alias="type")
    question: str
    """The question to answer about the page. Maximum 10,000 characters."""


class QuestionDict(TypedDict):
    type_: Type15OrStr
    question: str
