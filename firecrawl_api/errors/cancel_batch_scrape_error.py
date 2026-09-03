from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.batch_scrape404_error1 import BatchScrape404Error1
from ..models.batch_scrape500_error1 import BatchScrape500Error1

CancelBatchScrapeErrorBody: TypeAlias = BatchScrape404Error1 | BatchScrape500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CancelBatchScrapeError:
    def map(self, response: HttpResponse) -> CancelBatchScrapeErrorBody:
        match response.status_code:
            case 404:
                return decode_json[BatchScrape404Error1](response)
            case 500:
                return decode_json[BatchScrape500Error1](response)
            case _:
                return RawError(response)


cancel_batch_scrape_error_mapper: Final[ErrorMapper[CancelBatchScrapeErrorBody]] = _CancelBatchScrapeError()
