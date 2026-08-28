from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.agent402_error1 import Agent402Error1
from ..models.agent429_error1 import Agent429Error1

StartAgentErrorBody: TypeAlias = Agent402Error1 | Agent429Error1 | RawError


@dataclass(frozen=True, slots=True)
class _StartAgentError:
    def map(self, response: HttpResponse) -> StartAgentErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Agent402Error1](response)
            case 429:
                return decode_json[Agent429Error1](response)
            case _:
                return RawError(response)


start_agent_error_mapper: Final[ErrorMapper[StartAgentErrorBody]] = _StartAgentError()
