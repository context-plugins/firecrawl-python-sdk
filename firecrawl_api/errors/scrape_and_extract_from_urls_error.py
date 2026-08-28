from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.batch_scrape402_error1 import BatchScrape402Error1
from ..models.batch_scrape429_error1 import BatchScrape429Error1
from ..models.batch_scrape500_error1 import BatchScrape500Error1

ScrapeAndExtractFromUrlsErrorBody: TypeAlias = (
    BatchScrape402Error1 | BatchScrape429Error1 | BatchScrape500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ScrapeAndExtractFromUrlsError:
    def map(self, response: HttpResponse) -> ScrapeAndExtractFromUrlsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[BatchScrape402Error1](response)
            case 429:
                return decode_json[BatchScrape429Error1](response)
            case 500:
                return decode_json[BatchScrape500Error1](response)
            case _:
                return RawError(response)


scrape_and_extract_from_urls_error_mapper: Final[
    ErrorMapper[ScrapeAndExtractFromUrlsErrorBody]
] = _ScrapeAndExtractFromUrlsError()
