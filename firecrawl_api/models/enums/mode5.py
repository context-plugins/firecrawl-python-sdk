from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode5(str, Enum):
    SIMILAR = "similar"
    CITERS = "citers"
    REFERENCES = "references"

    __str__ = str.__str__


Mode5OrStr: TypeAlias = Annotated[Mode5 | str, open_enum_validator(Mode5)]
