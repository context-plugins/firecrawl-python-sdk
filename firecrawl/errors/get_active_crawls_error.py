from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.crawl_active402_error1 import CrawlActive402Error1
from ..models.crawl_active429_error1 import CrawlActive429Error1
from ..models.crawl_active500_error1 import CrawlActive500Error1

GetActiveCrawlsErrorBody: TypeAlias = CrawlActive402Error1 | CrawlActive429Error1 | CrawlActive500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetActiveCrawlsError:
    def map(self, response: HttpResponse) -> GetActiveCrawlsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[CrawlActive402Error1](response)
            case 429:
                return decode_json[CrawlActive429Error1](response)
            case 500:
                return decode_json[CrawlActive500Error1](response)
            case _:
                return RawError(response)


get_active_crawls_error_mapper: Final[ErrorMapper[GetActiveCrawlsErrorBody]] = _GetActiveCrawlsError()
