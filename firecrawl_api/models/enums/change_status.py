from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChangeStatus(str, Enum):
    """The result of the comparison between the two page versions. 'new' means this page did not exist before, 'same'
    means content has not changed, 'changed' means content has changed, 'removed' means the page was removed."""

    NEW = "new"
    SAME = "same"
    CHANGED = "changed"
    REMOVED = "removed"

    __str__ = str.__str__


ChangeStatusOrStr: TypeAlias = Annotated[ChangeStatus | str, open_enum_validator(ChangeStatus)]
