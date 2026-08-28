from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

RunMonitorErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _RunMonitorError:
    def map(self, response: HttpResponse) -> RunMonitorErrorBody:
        match response.status_code:
            case 409:
                return RawError(response)
            case _:
                return RawError(response)


run_monitor_error_mapper: Final[ErrorMapper[RunMonitorErrorBody]] = _RunMonitorError()
