from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.map402_error1 import Map402Error1
from ..models.map429_error1 import Map429Error1
from ..models.map500_error1 import Map500Error1

MapUrlsErrorBody: TypeAlias = Map402Error1 | Map429Error1 | Map500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _MapUrlsError:
    def map(self, response: HttpResponse) -> MapUrlsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Map402Error1](response)
            case 429:
                return decode_json[Map429Error1](response)
            case 500:
                return decode_json[Map500Error1](response)
            case _:
                return RawError(response)


map_urls_error_mapper: Final[ErrorMapper[MapUrlsErrorBody]] = _MapUrlsError()
