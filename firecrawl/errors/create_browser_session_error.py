from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.interact402_error1 import Interact402Error1

CreateBrowserSessionErrorBody: TypeAlias = Interact402Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateBrowserSessionError:
    def map(self, response: HttpResponse) -> CreateBrowserSessionErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Interact402Error1](response)
            case _:
                return RawError(response)


create_browser_session_error_mapper: Final[ErrorMapper[CreateBrowserSessionErrorBody]] = _CreateBrowserSessionError()
