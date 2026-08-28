from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.scrape402_error1 import Scrape402Error1
from ..models.scrape429_error1 import Scrape429Error1
from ..models.scrape500_error1 import Scrape500Error1

ScrapeAndExtractFromUrlErrorBody: TypeAlias = Scrape402Error1 | Scrape429Error1 | Scrape500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ScrapeAndExtractFromUrlError:
    def map(self, response: HttpResponse) -> ScrapeAndExtractFromUrlErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Scrape402Error1](response)
            case 429:
                return decode_json[Scrape429Error1](response)
            case 500:
                return decode_json[Scrape500Error1](response)
            case _:
                return RawError(response)


scrape_and_extract_from_url_error_mapper: Final[
    ErrorMapper[ScrapeAndExtractFromUrlErrorBody]
] = _ScrapeAndExtractFromUrlError()
