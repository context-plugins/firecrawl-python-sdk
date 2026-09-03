from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.scrape402_error21 import Scrape402Error21
from ..models.scrape429_error21 import Scrape429Error21
from ..models.scrape500_error21 import Scrape500Error21

GetScrapeStatusErrorBody: TypeAlias = Scrape402Error21 | Scrape429Error21 | Scrape500Error21 | RawError


@dataclass(frozen=True, slots=True)
class _GetScrapeStatusError:
    def map(self, response: HttpResponse) -> GetScrapeStatusErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Scrape402Error21](response)
            case 429:
                return decode_json[Scrape429Error21](response)
            case 500:
                return decode_json[Scrape500Error21](response)
            case _:
                return RawError(response)


get_scrape_status_error_mapper: Final[ErrorMapper[GetScrapeStatusErrorBody]] = _GetScrapeStatusError()
