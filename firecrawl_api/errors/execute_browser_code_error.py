from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.interact_execute402_error1 import InteractExecute402Error1

ExecuteBrowserCodeErrorBody: TypeAlias = InteractExecute402Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ExecuteBrowserCodeError:
    def map(self, response: HttpResponse) -> ExecuteBrowserCodeErrorBody:
        match response.status_code:
            case 402:
                return decode_json[InteractExecute402Error1](response)
            case _:
                return RawError(response)


execute_browser_code_error_mapper: Final[ErrorMapper[ExecuteBrowserCodeErrorBody]] = _ExecuteBrowserCodeError()
