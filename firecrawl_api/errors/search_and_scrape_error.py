from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.search408_error1 import Search408Error1
from ..models.search500_error1 import Search500Error1

SearchAndScrapeErrorBody: TypeAlias = Search408Error1 | Search500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _SearchAndScrapeError:
    def map(self, response: HttpResponse) -> SearchAndScrapeErrorBody:
        match response.status_code:
            case 408:
                return decode_json[Search408Error1](response)
            case 500:
                return decode_json[Search500Error1](response)
            case _:
                return RawError(response)


search_and_scrape_error_mapper: Final[ErrorMapper[SearchAndScrapeErrorBody]] = _SearchAndScrapeError()
