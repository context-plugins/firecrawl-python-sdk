from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.batch_scrape_errors402_error1 import BatchScrapeErrors402Error1
from ..models.batch_scrape_errors429_error1 import BatchScrapeErrors429Error1
from ..models.batch_scrape_errors500_error1 import BatchScrapeErrors500Error1

GetBatchScrapeErrorsErrorBody: TypeAlias = (
    BatchScrapeErrors402Error1 | BatchScrapeErrors429Error1 | BatchScrapeErrors500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _GetBatchScrapeErrorsError:
    def map(self, response: HttpResponse) -> GetBatchScrapeErrorsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[BatchScrapeErrors402Error1](response)
            case 429:
                return decode_json[BatchScrapeErrors429Error1](response)
            case 500:
                return decode_json[BatchScrapeErrors500Error1](response)
            case _:
                return RawError(response)


get_batch_scrape_errors_error_mapper: Final[ErrorMapper[GetBatchScrapeErrorsErrorBody]] = _GetBatchScrapeErrorsError()
