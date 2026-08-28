from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteMonitorErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteMonitorError:
    def map(self, response: HttpResponse) -> DeleteMonitorErrorBody:
        match response.status_code:
            case 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_monitor_error_mapper: Final[ErrorMapper[DeleteMonitorErrorBody]] = _DeleteMonitorError()
