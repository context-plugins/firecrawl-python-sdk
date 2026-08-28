from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Skills(str, Enum):
    ONLY = "only"

    __str__ = str.__str__


SkillsOrStr: TypeAlias = Annotated[Skills | str, open_enum_validator(Skills)]
