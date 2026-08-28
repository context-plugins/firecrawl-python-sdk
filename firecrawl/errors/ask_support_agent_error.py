from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.support_proxy_error_response import SupportProxyErrorResponse

AskSupportAgentErrorBody: TypeAlias = SupportProxyErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _AskSupportAgentError:
    def map(self, response: HttpResponse) -> AskSupportAgentErrorBody:
        match response.status_code:
            case 400 | 401 | 503 | 504:
                return decode_json[SupportProxyErrorResponse](response)
            case _:
                return RawError(response)


ask_support_agent_error_mapper: Final[ErrorMapper[AskSupportAgentErrorBody]] = _AskSupportAgentError()
