from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Model(str, Enum):
    """The model to use for the agent task. spark-1-mini (default) is 60% cheaper, spark-1-pro offers higher accuracy
    for complex tasks"""

    SPARK_1_MINI = "spark-1-mini"
    SPARK_1_PRO = "spark-1-pro"

    __str__ = str.__str__


ModelOrStr: TypeAlias = Annotated[Model | str, open_enum_validator(Model)]
