from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.interact402_error1 import Interact402Error1

DeleteBrowserSessionErrorBody: TypeAlias = Interact402Error1 | RawError


@dataclass(frozen=True, slots=True)
class _DeleteBrowserSessionError:
    def map(self, response: HttpResponse) -> DeleteBrowserSessionErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Interact402Error1](response)
            case _:
                return RawError(response)


delete_browser_session_error_mapper: Final[ErrorMapper[DeleteBrowserSessionErrorBody]] = _DeleteBrowserSessionError()
