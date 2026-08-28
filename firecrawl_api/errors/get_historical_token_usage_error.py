from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.team_token_usage_historical500_error1 import TeamTokenUsageHistorical500Error1

GetHistoricalTokenUsageErrorBody: TypeAlias = TeamTokenUsageHistorical500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetHistoricalTokenUsageError:
    def map(self, response: HttpResponse) -> GetHistoricalTokenUsageErrorBody:
        match response.status_code:
            case 500:
                return decode_json[TeamTokenUsageHistorical500Error1](response)
            case _:
                return RawError(response)


get_historical_token_usage_error_mapper: Final[
    ErrorMapper[GetHistoricalTokenUsageErrorBody]
] = _GetHistoricalTokenUsageError()
