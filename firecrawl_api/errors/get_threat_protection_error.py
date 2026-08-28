from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetThreatProtectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetThreatProtectionError:
    def map(self, response: HttpResponse) -> GetThreatProtectionErrorBody:
        match response.status_code:
            case 403:
                return RawError(response)
            case _:
                return RawError(response)


get_threat_protection_error_mapper: Final[ErrorMapper[GetThreatProtectionErrorBody]] = _GetThreatProtectionError()
