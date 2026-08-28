from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetMonitorErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMonitorError:
    def map(self, response: HttpResponse) -> GetMonitorErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


get_monitor_error_mapper: Final[ErrorMapper[GetMonitorErrorBody]] = _GetMonitorError()
