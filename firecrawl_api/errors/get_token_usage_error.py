from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.team_token_usage404_error1 import TeamTokenUsage404Error1
from ..models.team_token_usage500_error1 import TeamTokenUsage500Error1

GetTokenUsageErrorBody: TypeAlias = TeamTokenUsage404Error1 | TeamTokenUsage500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetTokenUsageError:
    def map(self, response: HttpResponse) -> GetTokenUsageErrorBody:
        match response.status_code:
            case 404:
                return decode_json[TeamTokenUsage404Error1](response)
            case 500:
                return decode_json[TeamTokenUsage500Error1](response)
            case _:
                return RawError(response)


get_token_usage_error_mapper: Final[ErrorMapper[GetTokenUsageErrorBody]] = _GetTokenUsageError()
