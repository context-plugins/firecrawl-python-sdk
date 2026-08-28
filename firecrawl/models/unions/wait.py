from __future__ import annotations

from typing import TypeAlias

from ..wait_by_duration import WaitByDuration, WaitByDurationDict
from ..wait_for_element import WaitForElement, WaitForElementDict

Wait: TypeAlias = WaitByDuration | WaitForElement

WaitDict: TypeAlias = WaitByDurationDict | WaitForElementDict
