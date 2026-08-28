from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.support_proxy_error_response import SupportProxyErrorResponse

SearchSupportDocsErrorBody: TypeAlias = SupportProxyErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _SearchSupportDocsError:
    def map(self, response: HttpResponse) -> SearchSupportDocsErrorBody:
        match response.status_code:
            case 400 | 401 | 503 | 504:
                return decode_json[SupportProxyErrorResponse](response)
            case _:
                return RawError(response)


search_support_docs_error_mapper: Final[ErrorMapper[SearchSupportDocsErrorBody]] = _SearchSupportDocsError()
