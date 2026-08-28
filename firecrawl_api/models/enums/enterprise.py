from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Enterprise(str, Enum):
    ANON = "anon"
    ZDR = "zdr"

    __str__ = str.__str__


EnterpriseOrStr: TypeAlias = Annotated[Enterprise | str, open_enum_validator(Enterprise)]
