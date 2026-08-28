from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type22(str, Enum):
    """Write text into an input field, text area, or contenteditable element. Note: You must first focus the element
    using a 'click' action before writing. The text will be typed character by character to simulate keyboard input."""

    WRITE = "write"

    __str__ = str.__str__


Type22OrStr: TypeAlias = Annotated[Type22 | str, open_enum_validator(Type22)]
