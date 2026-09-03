from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Trigger(str, Enum):
    SCHEDULED = "scheduled"
    MANUAL = "manual"

    __str__ = str.__str__


TriggerOrStr: TypeAlias = Annotated[Trigger | str, open_enum_validator(Trigger)]
