from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.team_credit_usage404_error1 import TeamCreditUsage404Error1
from ..models.team_credit_usage500_error1 import TeamCreditUsage500Error1

GetCreditUsageErrorBody: TypeAlias = TeamCreditUsage404Error1 | TeamCreditUsage500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetCreditUsageError:
    def map(self, response: HttpResponse) -> GetCreditUsageErrorBody:
        match response.status_code:
            case 404:
                return decode_json[TeamCreditUsage404Error1](response)
            case 500:
                return decode_json[TeamCreditUsage500Error1](response)
            case _:
                return RawError(response)


get_credit_usage_error_mapper: Final[ErrorMapper[GetCreditUsageErrorBody]] = _GetCreditUsageError()
