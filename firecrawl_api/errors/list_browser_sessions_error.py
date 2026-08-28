from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.interact402_error1 import Interact402Error1

ListBrowserSessionsErrorBody: TypeAlias = Interact402Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ListBrowserSessionsError:
    def map(self, response: HttpResponse) -> ListBrowserSessionsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Interact402Error1](response)
            case _:
                return RawError(response)


list_browser_sessions_error_mapper: Final[ErrorMapper[ListBrowserSessionsErrorBody]] = _ListBrowserSessionsError()
