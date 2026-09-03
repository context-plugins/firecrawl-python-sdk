from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.team_credit_usage_historical500_error1 import TeamCreditUsageHistorical500Error1

GetHistoricalCreditUsageErrorBody: TypeAlias = TeamCreditUsageHistorical500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetHistoricalCreditUsageError:
    def map(self, response: HttpResponse) -> GetHistoricalCreditUsageErrorBody:
        match response.status_code:
            case 500:
                return decode_json[TeamCreditUsageHistorical500Error1](response)
            case _:
                return RawError(response)


get_historical_credit_usage_error_mapper: Final[
    ErrorMapper[GetHistoricalCreditUsageErrorBody]
] = _GetHistoricalCreditUsageError()
