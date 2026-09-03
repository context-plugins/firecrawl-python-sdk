from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Question(SdkBaseModel):
    """Ask a natural-language question about the page. Returns the answer in the response ``answer`` field."""

    type_: Literal["question"] = Field(default="question", alias="type")
    question: str
    """The question to answer about the page. Maximum 10,000 characters."""


class QuestionDict(TypedDict):
    type_: NotRequired[Literal["question"]]
    question: str
