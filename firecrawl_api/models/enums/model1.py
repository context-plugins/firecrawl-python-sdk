from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Model1(str, Enum):
    """Model preset used for the agent run"""

    SPARK_1_PRO = "spark-1-pro"
    SPARK_1_MINI = "spark-1-mini"

    __str__ = str.__str__


Model1OrStr: TypeAlias = Annotated[Model1 | str, open_enum_validator(Model1)]
