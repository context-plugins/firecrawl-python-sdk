from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.crawl_errors402_error1 import CrawlErrors402Error1
from ..models.crawl_errors429_error1 import CrawlErrors429Error1
from ..models.crawl_errors500_error1 import CrawlErrors500Error1

GetCrawlErrorsErrorBody: TypeAlias = CrawlErrors402Error1 | CrawlErrors429Error1 | CrawlErrors500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetCrawlErrorsError:
    def map(self, response: HttpResponse) -> GetCrawlErrorsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[CrawlErrors402Error1](response)
            case 429:
                return decode_json[CrawlErrors429Error1](response)
            case 500:
                return decode_json[CrawlErrors500Error1](response)
            case _:
                return RawError(response)


get_crawl_errors_error_mapper: Final[ErrorMapper[GetCrawlErrorsErrorBody]] = _GetCrawlErrorsError()
