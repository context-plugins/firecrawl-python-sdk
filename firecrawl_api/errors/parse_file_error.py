from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.parse400_error1 import Parse400Error1
from ..models.parse402_error1 import Parse402Error1
from ..models.parse429_error1 import Parse429Error1
from ..models.parse500_error1 import Parse500Error1

ParseFileErrorBody: TypeAlias = Parse400Error1 | Parse402Error1 | Parse429Error1 | Parse500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ParseFileError:
    def map(self, response: HttpResponse) -> ParseFileErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Parse400Error1](response)
            case 402:
                return decode_json[Parse402Error1](response)
            case 429:
                return decode_json[Parse429Error1](response)
            case 500:
                return decode_json[Parse500Error1](response)
            case _:
                return RawError(response)


parse_file_error_mapper: Final[ErrorMapper[ParseFileErrorBody]] = _ParseFileError()
