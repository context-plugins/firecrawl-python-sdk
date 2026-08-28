from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.extract400_error1 import Extract400Error1
from ..models.extract500_error1 import Extract500Error1

ExtractDataErrorBody: TypeAlias = Extract400Error1 | Extract500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ExtractDataError:
    def map(self, response: HttpResponse) -> ExtractDataErrorBody:
        match response.status_code:
            case 400:
                return decode_json[Extract400Error1](response)
            case 500:
                return decode_json[Extract500Error1](response)
            case _:
                return RawError(response)


extract_data_error_mapper: Final[ErrorMapper[ExtractDataErrorBody]] = _ExtractDataError()
