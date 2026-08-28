from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetMonitorCheckErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMonitorCheckError:
    def map(self, response: HttpResponse) -> GetMonitorCheckErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


get_monitor_check_error_mapper: Final[ErrorMapper[GetMonitorCheckErrorBody]] = _GetMonitorCheckError()
