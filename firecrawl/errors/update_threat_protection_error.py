from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

UpdateThreatProtectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _UpdateThreatProtectionError:
    def map(self, response: HttpResponse) -> UpdateThreatProtectionErrorBody:
        match response.status_code:
            case 400 | 403:
                return RawError(response)
            case _:
                return RawError(response)


update_threat_protection_error_mapper: Final[
    ErrorMapper[UpdateThreatProtectionErrorBody]
] = _UpdateThreatProtectionError()
